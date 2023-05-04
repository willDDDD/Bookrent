CS222 projects--Book Rental Web Service(Textbook Rent System)


Introduction of presentation:

Our project is an alternative to existing software. On the internet, there are multiple products or web services for booking renting services, but our web service is specifically for students in UIUC. To be more specific, students of UIUC may have difficulties ordering and buying books at the beginning of the semester due to a large number of orders, or need books for studying and reference in the middle of the semester. So, we decide to create an alternative to existing book renting web service to address this problem, and our goal is to create a web page for book rental service, with various features embedded in our website.

Features:
   1. User Login in 
   2. Book rental
   3. Designed home page
   4. User account
   5. Book information
   6. Administers account

Technical Architecture:
   1. Front-end: html
   2. Back-end: Mysql, python
   3. Platform: Django
 
###
![graph](./TA.png)

Problem 1:
When we uploaded the background image candidate locally and tries to apply the change, it failed with the reason of incorrect path. The solution is that we instead inspected the page where the image was located on and copies the image's url into our code which worked successfully. the solution is much easier as long as the image is still up on the internet.


## Installation instructions
1. Clone the repo:

    $ git clone https://github.com/CS222-UIUC/course-project-team-51.git
   
2. Change directory into the web-app folder:
    
    $ cd bookrent
    
3. In the web-app directory, install django:
   
    $ pip3 install django
    
4. In the web-app directory and start the django app:
    
    $ python manage.py runserver
    
5. In your browser, go to [http://localhost/:3000](http//localhost:3000) to see the website locally.

## Group members and their roles
Members: Haoran Wang, Chen Yang,  Zelong Liang, Xiuhao Ding <br>
<br>
Roles: <br>
   Front-end: Chen Yang, Zelong Liang, Haoran Wang <br>
   Back-end: Xiuhao Ding 



