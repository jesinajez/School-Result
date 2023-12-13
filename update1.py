#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
connection = pymysql.connect(host="localhost", user="root", password="", database="result")
cur = connection.cursor()

import cgi
f = cgi.FieldStorage()
pid = f.getvalue("sno")
cur.execute("""select * from marklist where sno='%s' """ %(pid))
r = cur.fetchone()
print(r)
fn = 'files/' + r[11]
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
        <div class="container">
            <form method = "post" action="#" target="_blank" enctype="multipart/form-data">
                <label>Reg No</label><input type="text" name="regNo" value="%s">
                <label>Name</label><input type="text" name="sname" value="%s">
                <label>Roll No</label><input type="text" name="rollno" value="%s">
                <label>DOB</label><input type="date" name="dob" value="%s">
                <label>Language</label><input type="text" name="lang" value="%s">
                <label>English</label><input type="text" name="eng" value="%s">
                <label>Maths</label><input type="text" name="maths" value="%s">
                <label>Physics</label><input type="text" name="phy" value="%s">
                <label>Chemistry</label><input type="text" name="che" value="%s">
                <label>CS</label><input type="text" name="cs" value="%s">
                <label>Profile</label><input type="file" name="photo" value="%s">
                <input type="submit" value="update" name="sub">
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
"""%(r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10],fn))

import os
pref = f.getvalue("regNo")
pname = f.getvalue("sname")
proll = f.getvalue("rollno")
pdob = f.getvalue("dob")
plang = f.getvalue("lang")
peng = f.getvalue("eng")
pmat = f.getvalue("maths")
pphy = f.getvalue("phy")
pche = f.getvalue("che")
pcs = f.getvalue("cs")
pfile = f['photo']
psub = f.getvalue("sub")
if psub != None:
    fm = os.path.basename(pfile.filename)
    open("files/"+fn, "wb").write(pfile.file.read())
    q = ("""update marklist set RegNo='%s', Name='%s', RollNo='%s', DOB='%s', Language='%s', English='%s', 
    Maths='%s', Physics='%s', Chemistry='%s', CS='%s', Profile='%s' where sno='%s' """
         %(pref,pname,proll,pdob,plang,peng,pmat,pphy,pche,pcs,fm))
    cur.execute(q)
    connection.commit()
    print("""
        <script>
            alert("success");
        </script>
    """)