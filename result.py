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
    <link rel="stylesheet" href="resultDisplay.css" />
    <style>
    .btn1 {
        position: absolute;
        top: 150px;
        left: 1200px;
        transform: translate(-50%, -50%);
        -ms-transform: translate(-50%, -50%);
        background-color: #f1f1f1;
        color: black;
        font-size: 16px;
        padding: 16px 30px;
        border: none;
        cursor: pointer;
        border-radius: 5px;
        text-align: center;
    }
    
    .btn1:hover {
        background-color: black;
        color: white;
    }
    
    .btn2 {
        position: absolute;
        top: 150px;
        left: 1000px;
        transform: translate(-50%, -50%);
        -ms-transform: translate(-50%, -50%);
        background-color: #f1f1f1;
        color: black;
        font-size: 16px;
        padding: 16px 30px;
        border: none;
        cursor: pointer;
        border-radius: 5px;
        text-align: center;
    }
    
    .btn2:hover {
        background-color: black;
        color: white;
    }
    
    /* Full-width input fields */
    input[type=text], input[type=date] {
        width: 180px;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        box-sizing: border-box;
    }
    
    .container {
        padding: 16px;
    }

    .modal-content {
        background-color: #fefefe;
        margin: 8% auto 10% auto; /* 5% from the top, 15% from the bottom and centered */
        border: 1px solid #212531;
        width: 20%; /* Could be more or less, depending on screen size */
    }
    
    .button1 {
        background-color: #845398;
        color: white;
        padding: 14px 20px;
        margin: 8px 10px;
        border: none;
        cursor: pointer;
        width: 40%;
    }
        
    .button1:hover {
        opacity: 0.8;
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
    
    <input type="submit" value="Individual Result" name="isub" class="btn2" onclick="toggleInputs()">
    <input type="submit" value="Overall Result" name="osub" class="btn1" onclick="window.location.href = 'overallresult.py';">
    
    <form class="modal-content" action="#" method="post">
        <div id="inputFields"  class="container" style="display:none;">
            <label><b>Register Number</b></label>
            <input type="text" placeholder="Enter Register Number" name="regNo" required><br><br>
            
            <label><b>Date of Birth &nbsp; &nbsp; &nbsp; &nbsp; </b></label>
            <input type="date" name="dob" required><br><br>
          
            <div style="display: flex; justify-content: space-between;">
                <input type="submit" value="Result" name="sub" class="button1">
                <input type="button" value="Cancel" class="button1">
            </div>
        </div>  
    </form>
     <script>
        function toggleInputs() {
            var inputFields = document.getElementById("inputFields");
            if (inputFields.style.display === "none") {
                inputFields.style.display = "block";
            } else {
                inputFields.style.display = "none";
            }
        }
    </script>
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
f = cgi.FieldStorage()
preg = f.getvalue("regNo")
pdob = f.getvalue("dob")
psub = f.getvalue("sub")
if psub != None:
    cur.execute("""select sno from marklist where RegNo='%s' and DOB='%s'""" % (preg, pdob))
    r = cur.fetchone()
    if r != None:
        print("""
            <script>
                alert("Loading...");
                location.href = "resultDisplay.py?sno=%s";
            </script>
        """ % r)
    else:
        print("""
            <script>
                alert("Incorrect entry");
            </script>
        """)
