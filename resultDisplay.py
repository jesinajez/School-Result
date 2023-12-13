#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi
f = cgi.FieldStorage()
pid = f.getvalue("sno")
# print(pid)

connection = pymysql.connect(host="localhost", user="root", password="", database="result")
cur = connection.cursor()
q = """select * from marklist where sno=%s""" % pid
cur.execute(q)
r = cur.fetchall()
for i in r:
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
        </head>
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
    
        td {
            text-align: center;
            font-size: 15px;
        }
        </style>
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
        <div class="tab">
        <table border="1" cellspacing="5" bgcolor="white" width="1000">
            <caption style="color:white; font-size: 30px;"><b>Marks</b></caption>
                <tr>
                    <th rowspan="4">Name: %s</th>
                    <th colspan="2" height="30">Roll No: %s</th>
                    <th colspan="2" height="30">Reg No: %s</th>
                    <th colspan="2" height="30">DOB: %s</th>
                </tr>
                <tr>
                    <th colspan="6" height="30">Score</th>
                </tr>
                <tr>
                    <th height="30">Language: %s</th>
                    <th height="30">English: %s</th>
                    <th height="30">Maths: %s</th>
                    <th height="30">Physics: %s</th>
                    <th height="30">Chemistry: %s</th>
                    <th height="30">C S: %s</th>
                <tr>
        """% (i[2], i[3], i[1], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
    print("""
        </table> 
        </div>   
    """)

student_data = []
for i in r:
    total = i[5] + i[6] + i[7] + i[8] + i[9] + i[10]
    avg = total / 6

    # Append the total and average to the student_data list
    student_data.append((i[2], total, avg))

# Print the second table with total and average
print("""
    <br><br>
    <div class="tab1">
    <table border="1" cellspacing="5" bgcolor="white"
           height="100" width="500" cellpadding="5">
        <caption style="color:white; font-size: 30px;"><b>Result</b></caption>
        <tr>
            <th width="180">Name</th>
            <th>Total</th>
            <th>Average</th> 
            <th>Pass Or Fail</th> 
        </tr>
""")

# Print the total and average for each student
for data in student_data:
    name, total, avg = data
    pass_or_fail = "Pass" if avg >= 70 else "Fail"
    color="green" if pass_or_fail == "Pass" else "red"
    print(f"<tr><td>{name}</td><td>{total}</td><td>{avg:.2f}</td><td style='color:{color}'>{pass_or_fail}</td></tr>")

print("""
    </table>
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




