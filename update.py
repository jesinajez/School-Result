#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi

connection = pymysql.connect(host="localhost", user="root", password="", database="result")
cur = connection.cursor()
print("""
    <!doctype html>
    <html>
    <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="styles.css" />
    <title>Gurukulam</title>
    <link rel="stylesheet" href="Accets/welcomeDesign.css" />
    
    <style>
    .container {
        background-color: #fefefe;
        margin: 8% auto 10% auto; /* 5% from the top, 15% from the bottom and centered */
        border: 1px solid white;
        width: 20%; /* Could be more or less, depending on screen size */
    }
    footer{
            position: absolute;
            bottom: 0;
        }

        .copyright{
            text-align: right; 
            margin:20px; 
            color:white;
        }

        .mailto{
            text-align: right; 
            margin-left:950px; 
            color:white;
        }
    </style>
    </head>
    <body>
    <header>
        <section class="nav">
            <!-- We can also insert any logo here     -->

            <!-- We can also insert any logo here     -->
            <div class="logo">
                <a href="#"><i class="fas fa-utensils"></i>Gurukulam</a>
            </div>

            <!--  checkbox to control the icon's state    -->
            <input id="menu-toggle" type="checkbox" />
            <label class="menu-button-container" for="menu-toggle">
          <div class="menu-button"></div>
        </label>
            <!--  main menu    -->
            <ul class="menu">
                <li><a href="welcome.html">Home</a></li>
                <li><a href="#speciality">About</a></li>
                <li><a href="register.py">Register</a></li>
                <li><a href="result.py">Result</a></li>
                <li><a href="#order" class="order">Menu</a></li>
            </ul>
        </section>
    </header>
    
    <div class="container">
         <form method = "post" action="#" target="_blank" enctype="multipart/form-data">
         
         
         </form>
    </div>
    
    <footer>
        <div class="footers">
            <span class="copyright">&copy; 2013 Friend | Design and Development. All Rights Reserved.</span>
            <span class="mailto">For mor details
                <a href="mailto:gurukulam@example.com">gurukulam@example.com</a></span>
        </div>
    </footer>
    </body>
    </html>
""")