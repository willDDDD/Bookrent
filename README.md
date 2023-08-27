# Book Rental Web Service(Textbook Rent System)


## Introduction

The project is an alternative to existing software. On the internet, there are multiple products or web services for booking renting services, but our web service is specifically for students in UIUC. To be more specific, students of UIUC may have difficulties ordering and buying books at the beginning of the semester due to a large number of orders, or need books for studying and reference in the middle of the semester. So, we decide to create an alternative to existing book renting web service to address this problem, and our goal is to create a web page for book rental service, with various features embedded in our website.

Functionality:
1. Users could have their personal account on our website, and use Netid to login.
2. Staff users could post new available textbook information on the website.
3. Users could borrow textbooks on the website with the limit of 2 textbooks in total before
any returning.
4. Users could check the number of books they already borrowed.
5. Users could look up book information on the website.



 
## Technical Architecture
![graph](./TA.png)

### Django Template(frontend): 
1. Role: Display Frontend content to clients
2. Interaction: Display HTML pages incooperated with information fetched from backend/database, and send clients' requests/changes to backend/database
3. Languages/libraries: HTML, CSS

### Django Framework(backend): 
1. Role: The Three Django Apps are the main parts of our framework. The Accounts App is responsible for user's registration, login/logout and fetch personal information like borrowed records. The Books is responsible for the function of borrowing and returning books as well as listing out available books. The Bookrent App is responsible for database connections and settings.
2. Interaction: Fetch from backend and send it to frontend. Receive from frontend and update the database.
3. Languages/libraries: Python, Django

### Database: 
1. Role: Store users' and administrator's account information and text books' information
2. Interaction: Send information to Django Framework/Frontend, and process on the Create/Read/Update/Delete requests
3. Languages/libraries: Postgre, SQL


## Installation instructions
1. Clone the repo:

    $ git clone https://github.com/willDDDD/Bookrent.git
   
2. Change directory into the web-app folder:
    
    $ cd bookrent
    
3. In the web-app directory, install django:
   
    $ pip3 install django
    
4. In the web-app directory and start the django app:
    
    $ python manage.py runserver
    
5. In your browser, go to [http://localhost/:3000](http//localhost:3000) to see the website locally.
