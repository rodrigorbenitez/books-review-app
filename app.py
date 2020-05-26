import os
from flask import Flask, render_template, redirect, url_for, request, session, jsonify

from flask_sqlalchemy  import SQLAlchemy
from sqlalchemy.orm.session import sessionmaker
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dominate.tags import option
from werkzeug.exceptions import BadRequest
import requests



app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
db = SQLAlchemy(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True



# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


#global variables
member=""


#---------------------------------LOGIN-----------------------------------#
@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get('logged_in'):
        return render_template("error.html", message="you are already logged in")
    else:
     global member
     if request.method == 'POST':
         username_login = request.form.get("username_login")
         password_login = request.form.get("password_login")
         #save the query selection in a variable
         user= db.execute("SELECT * FROM members WHERE member = :member", {"member": username_login}).fetchone()
        #check first if the user exists, then if the password is correct and if is correct redirect to the index page
         if user:
            if user.password==password_login:
                #turn on the session and you are logged in
                session['logged_in'] = True
                session['name'] = username_login
                member=session['name']
                return redirect(url_for('index'))
            return render_template("error.html", message="password invalid")
         return render_template("error.html", message="Username invalid")
        


   
     return render_template("login.html")




#------------------------REGISTER-------------------------------#
@app.route("/register", methods=["GET","POST"])
def register():
    if  session.get('logged_in'):
        return render_template("error.html", message="you must logout to register a new user")
    else:
        if request.method == 'POST':
         username = request.form.get("username")
         email = request.form.get("email")
         password = request.form.get("password")
         
         count=db.execute("SELECT member FROM members WHERE member = :member", {"member": username}).rowcount
         if count==0:
             db.execute("INSERT INTO members (password, member, email) VALUES (:password, :member, :email)",{"password": password, "member": username ,"email": email})
             db.commit()
             return"<h1>New user has been created!</h1>"
         else:
             return render_template("register.html", message="The username already exists")
         
         
    
        return render_template("register.html")


#-----------------INDEX SEARCH PAGE------------------------#
@app.route("/",methods=["GET","POST"])
def index():

 if not session.get('logged_in'):  
   return redirect(url_for('login'))
 else:
     option=""
     bookSearch=""
     bookData=""
     message=""
     if request.method == 'POST':
         option = request.form.get("inlineRadioOptions")
         bookSearch = request.form.get("bookSearch")+"%"

     if option=="isbn":
         bookSearch="%"+bookSearch+"%"
         bookData=db.execute("SELECT * FROM books WHERE isbn LIKE :search ORDER BY isbn ASC;", {"option": option, "search": bookSearch}).fetchall()
         count=db.execute("SELECT * FROM books WHERE isbn LIKE :search ORDER BY isbn ASC;", {"option": option, "search": bookSearch}).rowcount
         if count==0:
             message="Sorry, not book for that search"
     elif option=="author":
         bookData=db.execute("SELECT * FROM books WHERE author LIKE :search ORDER BY author ASC;", {"option": option, "search": bookSearch.capitalize()}).fetchall()
         count=db.execute("SELECT * FROM books WHERE author LIKE :search ORDER BY author ASC;", {"option": option, "search": bookSearch.capitalize()}).rowcount
         if count==0:
             message="Sorry, not book for that search"
     elif option=="title":
         bookData=db.execute("SELECT * FROM books WHERE title LIKE :search ORDER BY title ASC;", {"option": option, "search": bookSearch.capitalize()}).fetchall()
         count=db.execute("SELECT * FROM books WHERE title LIKE :search ORDER BY title ASC;", {"option": option, "search": bookSearch.capitalize()}).rowcount
         if count==0:
             message="Sorry, not book for that search"
     return render_template("index.html",bookSearch=bookSearch, option=option, bookData=bookData, message=message)


#-------------------particular book--------------------#

@app.route("/index/<isbn>", methods=["GET","POST"])
def bookIndex(isbn):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        global member
    message="" 
    bookIndex = db.execute("SELECT * FROM books WHERE isbn = :isbn", {"isbn": isbn}).fetchone()
    key="pwh6vGSF3hghIcn5TseMsA"
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": key, "isbns": isbn})
    data=res.json()
    averageRating=data["books"][0]["average_rating"]
    rev = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": key, "isbns": isbn})
    data2=rev.json()
    reviews=data2["books"][0]["ratings_count"]
    if isbn is None:
     return render_template("error.html", message="No such book.")

    isbn_review=db.execute("SELECT id FROM books WHERE isbn = :isbn",{"isbn": bookIndex.isbn}).fetchone()
    allReviews=db.execute("SELECT members.member, reviews.review, reviews.rating, reviews.isbn_review FROM reviews INNER JOIN members ON members.id=reviews.member_id WHERE reviews.isbn_review = :isbn_review",{"isbn_review": isbn_review.id}) 
    
    if request.method == 'POST':
        rate = request.form.get("inlineRadioOptions")
        review = request.form.get("textarea")
        member_id=db.execute("SELECT id FROM members WHERE member = :member",{"member": session['name']}).fetchone()
        isbn_review=db.execute("SELECT id FROM books WHERE isbn = :isbn",{"isbn": bookIndex.isbn}).fetchone()        
        count=db.execute("SELECT * FROM reviews WHERE isbn_review= :isbn_review AND member_id= :member_id", {"isbn_review":isbn_review.id, "member_id": member_id.id}).rowcount
        if count==0:
            db.execute("INSERT INTO reviews (isbn_review, member_id, review, rating) VALUES (:isbn, :member_id, :review, :rating)",{"isbn": isbn_review.id, "member_id": member_id.id ,"review": review, "rating": rate})
            db.commit()
            isbn_review=db.execute("SELECT id FROM books WHERE isbn = :isbn",{"isbn": bookIndex.isbn}).fetchone()
            allReviews=db.execute("SELECT members.member, reviews.review, reviews.rating, reviews.isbn_review FROM reviews INNER JOIN members ON members.id=reviews.member_id WHERE reviews.isbn_review = :isbn_review",{"isbn_review": isbn_review.id})
            return render_template("book.html", bookIndex=bookIndex, averageRating=averageRating, message=message, allReviews=allReviews, reviews=reviews)
        else:
         message="sorry you can't write another review for the same book"
    return render_template("book.html", bookIndex=bookIndex, averageRating=averageRating, message=message, allReviews=allReviews, reviews=reviews)


#---------------LOGOUT---------------------#
@app.route("/logout")
def logout():

 if not session.get('logged_in'):
     return redirect(url_for('login'))
    
 else:
     #turn off the session
    session['logged_in'] = False
    session['name']=""
    return render_template("error.html", message="you are logged out")


@app.route("/api/index/<isbn>")
def book_api(isbn):

    
    bookIndex = db.execute("SELECT * FROM books WHERE isbn = :isbn", {"isbn": isbn}).fetchone()
    if bookIndex is None:
        return jsonify({"error": "Invalid isbn number"}), 422

    key="pwh6vGSF3hghIcn5TseMsA"
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": key, "isbns": isbn})
    data=res.json()
    




    return jsonify(
        {
    "title": bookIndex.title,
    "author": bookIndex.author,
    "year": bookIndex.year,
    "isbn": bookIndex.isbn,
    "review_count": data["books"][0]["reviews_count"],
    "average_score": data["books"][0]["average_rating"]

       })




if __name__ == "__main__":
    app.run(debug=True)