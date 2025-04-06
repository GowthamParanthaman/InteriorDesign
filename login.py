#!C:\Python\python.exe
import cgi
import mysql.connector
print("content-type:text/html\n")
print("<html>")
print("<body>")
form=cgi.FieldStorage()
Username=form.getvalue("Username")
Mobile=form.getvalue("Mobile")
Email=form.getvalue("Email")
Area=form.getvalue("Area")
print("<h1>",Username,"</h1>")
print("<h1>",Mobile,"</h1>")
print("<h1>",Email,"</h1>")
print("<h1>",Area,"</h1>")
DB=mysql.connnector.connect(
    host="localhost",
    user="root",
    password="",
    database="client_information"
)
mycursor=DB.cursor()
values=(Username,Mobile,Email,Area)
sql="INSERT INTO client_address (Username,Mobile,Email,Area) VALUES (%s,%s,%s,%s)"
mycursor.execute(sql,values)
DB.commit()
print("</body>")
print("</html>")