# Project 1

<h1>Web Programming with Python and JavaScript</h1>
<h1> demo here https://project1-book-review-rodrigo.herokuapp.com/

Project 1
This is the second project in the Edx course CS50 Web Programming with Python and Javascript.
Overview
<h3>Registration</h3>
<ul>
<li>http://127.0.0.1:5000/register</li>
<li>register.html, error.html
</li></ul>
<h3>Login</h3>
<ul>
<li>http://127.0.0.1:5000/login</li>
<li>login.html, error.html</li></ul>
 
<h3>Index</h3>
<ul>
<li>http://127.0.0.1:5000/</li>
<li>Index.html</li></ul>
<h3>Logout</h3>
<ul>
<li>http://127.0.0.1:5000/logout</li>
<li>logout.html, error.html</li>
 </ul>
<h3>Books</h3>
   <ul>
<li>http://127.0.0.1:5000/index/<isbn></li>
<li>example</li>
<li>book.html</li>
     </ul>
<h3>API Acces</h3>
  <ul>
<li>http://127.0.0.1:5000/api/index/<isbn></li>
<li>Example: http://127.0.0.1:5000/api/index/1481420763</li>
 </ul>
<h3>Description
When you open the page shows the register template if you are not logged in. The navbar is always showed, and if you want to log out, the page shows you the log in template.
When you log in, redirects automatically to the index page, where you can search the books by ISBN, title or author.  If the user typed in only part of a title, ISBN, or author name, the search page should find matches for those as well.
There is an error massage if your search does not match. And when the search appears there is a link in each ISBN number that redirects to the ISBN’S page.
In each particular book page, there is information from the database in Heroku, and some information from the goodreads API.
On the book page, users can submit a review: consisting of a rating on a scale of 1 to 5, as well as a text component to the review where the user can write their opinion about a book. Users can not submit multiple reviews for the same book.
PostgreSQL
In the same directory there is a Python file called import.py separate from your web application, that took the books and imported them into my PostgreSQL database. 
