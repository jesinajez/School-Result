#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql

connection = pymysql.connect(host="localhost", user="root", password="", database="result")
cur = connection.cursor()
q1 = """select max(sno) from marklist"""
cur.execute(q1)
r = cur.fetchone()
# print(r[0])
if r[0] != None:
    n = r[0]
else:
    n = 0
z = ""
if n < 10:
    z = "000"
elif n < 100:
    z = "00"
elif n < 1000:
    z = "0"
else:
    z = ""
regNo = "GKM"+z+str(n+1)
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

        .button1 {
            position: absolute;
            transform: translate(-50%, -50%);
            -ms-transform: translate(-50%, -50%);
            background-color: #f1f1f1;
            color: black;
            font-size: 16px;
            padding: 8px 15px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            text-align: center;
        }

        .button1:hover {
            background-color: black;
            color: white;
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
    <div class="tab">
    <form method = "post" action="#" target="_blank" enctype="multipart/form-data">
    <table border="1" cellspacing="5" bgcolor="white" width="1000">
        <caption style="color:white; font-size: 30px;"><b>Student Mark</b></caption>
        <tr>
            <th rowspan="4" style="text-align: center;">Name</th>
            <th colspan="2" height="30">Roll No</th>
            <th colspan="2" height="30">Reg No</th>
            <th colspan="2" height="30">DOB</th>
            <th rowspan="5"><img id="profileImage" src="%s" width="200" height="150" alt="Profile Photo"></th>
        </tr>""")
print("""<tr>
            <td colspan="2" height="30" style="text-align: center;"><input type="text" name="rollNo" style="width: 90px; text-align: center;"></td>
            <td colspan="2" height="30" style="text-align: center;"><input type="text" name="regNo" style="width: 90px; text-align: center;" value="%s"></td>
            <td colspan="2" height="30" style="text-align: center;"><input type="date" name="dob" style="width: 120px; text-align: center;"></td>
        </tr>
        <tr>
            <th colspan="6" height="30">Score</th>
        </tr>
        <tr>
            <th height="30">Language</th>
            <th height="30">English</th>
            <th height="30">Maths</th>
            <th height="30">Physics</th>
            <th height="30">Chemistry</th>
            <th height="30">C S</th>
        </tr>
        <tr>
            <td rowspan="2" style="text-align: center;"><input type="text" style="width: 150px; text-align: center;" name="sname"></td>
            <td height="30" style="text-align: center;"><input type="text" name="lang" style="width: 150px; text-align: center;"></td>
            <td height="30" style="text-align: center;"><input type="text" name="english" style="width: 150px; text-align: center;"></td>
            <td height="30" style="text-align: center;"><input type="text" name="maths" style="width: 150px; text-align: center;"></td>
            <td height="30" style="text-align: center;"><input type="text" name="physics" style="width: 150px; text-align: center;"></td>
            <td height="30" style="text-align: center;"><input type="text" name="chemistry" style="width: 150px; text-align: center;"></td>
            <td height="30" style="text-align: center;"><input type="text" name="cs" style="width: 150px; text-align: center;"></td>
            
        </tr>
        <tr>
            <th colspan="6" height="50">
            <input type="submit" value="Add To Table" name="sub" class="button1"></th>
            <th height="30"><input type="file" name="photo" onchange="displayImage(this);"></th>
        </tr>
    </table>
    </form>
    </div>
    <footer>
    <div class="footers">
            <span class="copyright">&copy; 2013 Friend | Design and Development. All Rights Reserved.</span>
            <span class="mailto">For mor details
                <a href="mailto:gurukulam@example.com">gurukulam@example.com</a></span>
        </div>
</footer>
<script>
    // Function to update the image source
    function displayImage(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                document.getElementById('profileImage').src = e.target.result;
            };
            reader.readAsDataURL(input.files[0]);
        }
    }
</script>
    </body>
    </html>
"""%(regNo))
import cgi, os
f = cgi.FieldStorage()
preg = f.getvalue("regNo")
pname = f.getvalue("sname")
proll = f.getvalue("rollNo")
pdob = f.getvalue("dob")
plang = f.getvalue("lang")
peng = f.getvalue("english")
pmaths = f.getvalue("maths")
pphy = f.getvalue("physics")
pche = f.getvalue("chemistry")
pcs = f.getvalue("cs")
pfile = f['photo']
psub = f.getvalue("sub")
if psub != None:
    fn = os.path.basename(pfile.filename)
    open("files/"+fn,"wb").write(pfile.file.read())
    cur.execute("""insert into marklist(RegNo, Name, RollNo, DOB, Language, English, Maths, Physics, Chemistry, CS, Profile) 
    values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
                % (preg, pname, proll, pdob, plang, peng, pmaths, pphy, pche, pcs, fn))
    connection.commit()
    print("""
        <script>
            alert("Success...!");
        </script>
    """)
