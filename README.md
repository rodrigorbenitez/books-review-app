# Project 1

<h1>Web Programming with Python and JavaScript</h1>
<h1> demo here https://project1-book-review-rodrigo.herokuapp.com/

# Project 1

Course name: Web Programming with Python and JavaScript <br>
Course no: CS50W <br> 
Note: I made this project to accomplish project1 portion of HarvardX CS50W course <br>

## Live preview link <a href = 'https://project1-book-review-rodrigo.herokuapp.com/' > https://project1-book-review-rodrigo.herokuapp.com/ </a>
## Youtube: <a href = 'https://youtu.be/qyX7lfKpFhs'> https://youtu.be/qyX7lfKpFhs </a>

# `App name:` Book's corner'

``Breif description:`` This is a simple book review app made with flask. To use this website features you have to login first. Anyone can register in this website. After registration and logged into the website people can search for books, view reviews on particular book and can submit his own review.

## Built With

* [Javascript] (https://www.javascript.com/) - High-level, interpreted programming language
* [Jquery] (https://jquery.com/) -JavaScript library
* [Bootstrap] (https://getbootstrap.com/) - Front-end framework
* [HTML] (https://www.html.com/) - Standard markup language
* [CSS] (https://css.com) - Style sheet language
* [Python] (https://www.python.org/) - Interpreted, high-level, general-purpose programming language.
* [Flask] (https://flask.palletsprojects.com/) - Flask is a micro web framework written in Python.
* [PostgreSQL] (https://www.postgresql.org/) - PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance.


Book API used:
goodreads.com (Thank you for free api)

Server used:
heroku.com (Thank you for free web service)

### Running:

1. Clone this repositiory  or Download Source files
2. Run ```pip install -r requirements.txt``` in your terminal/CMD window to make sure that all of the necessary Python packages (Flask and SQLAlchemy, for instance) are installed.
3. Set an environmental variable to connect with database.
    <br> Varialbe name must be: ``"DATABASE_URL"``
    <br> Varialbe value will be: ``"...your database uri ..."``,  example: ``postgres://username:password@hostname/database`` 
4. Run ```python imports.py``` to create user,books and reveiws table in database and to insert 5000 books data from books.csv
5. Run ```python app.py``` to run the app
6. Done

## Features:

**Login:**  Users, once registered, are able to log in to the website with their username and password.

**Registration:** Users are able to register for the website, providing a username and password.

**Logout:** Users can log out from the website by clicking on the logout button.

**Search:**  Once a user has logged in, they are taken to a page where they can search for a book. Users are able to type in the ISBN number of a book, the title of a book, or the author of a book. After performing the search, the website display a list of possible matching results, or a message if there were no matches. If the user typed in only part of a title, ISBN, or author name, the search page find matches for those as well!

**Book page:** By clicking a book title from  the search result users can view information about that book. Statical information will come from goodread.com api and reviews data will come from my website database.

**Api:** https://project1-book-review-rodrigo.herokuapp.com/api/index/ISBN  Replace the ISBN with the real book's isbn number to get a book information in json format . It is not necessary to be logged in to use API endpoint.


## Acknowledgments

* HARVARDX Web Programming with Python and JavaScript