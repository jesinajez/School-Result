#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi
f = cgi.FieldStorage()
pid = f.getvalue("sno")
# print(pid)

connection = pymysql.connect(host="localhost", user="root", password="", database="result")
cur = connection.cursor()
a = """ select * from marklist"""
cur.execute(a)
# f = cur.fetchone()
# print(f[1])
f = cur.fetchall()
print("""
        <!DOCTYPE html>
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
        td{
            text-align: center;
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
        <div class="resultTable">
        <table border="1" cellspacing="5" bgcolor="white" width="1300">
            <caption style="color:white; font-size: 30px;"><b>School Result</b></caption>
                <tr>
                    <th height="30">Reg No</th>
                    <th height="30">Name</th>
                    <th height="30">Roll No</th>
                    <th height="30">DOB</th>
                    <th height="30">Language</th>
                    <th height="30">English</th>
                    <th height="30">Maths</th>
                    <th height="30">Physics</th>
                    <th height="30">Chemistry</th>
                    <th height="30">C S</th>
                    <th height="30">Profile</th>
                    <th height="30">Update</th>
                </tr>
        """)
for r in f:
    print("""
                <tr>
                    <td height="30">%s</td>
                    <td height="30">%s</td>
                    <td height="30">%s</td>
                    <td height="30">%s</td>
                    <td height="30">%s</td>
                    <td height="30">%s</td>
                    <td height="30">%s</td>
                    <td height="30">%s</td>
                    <td height="30">%s</td>
                    <td height="30">%s</td>
                    <td height="30">%s</td>
                    <th height="30"><a href="update1.py?sno=%s">Update</a></th>
                </tr>
        """ % (r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10],r[11],r[0]))
print("""
    </table>
    <footer>
        <div class="footers">
            <span class="copyright">&copy; 2013 Friend | Design and Development. All Rights Reserved.</span>
            <span class="mailto">For mor details
                <a href="mailto:gurukulam@example.com">gurukulam@example.com</a></span>
        </div>
    </footer>
   </body>
</html
""")
