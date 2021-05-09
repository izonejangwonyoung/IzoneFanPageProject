#!C:\Users\ericshim\AppData\Local\Programs\Python\Python39\python.exe

import cgi
form = cgi.FieldStorage()

title = form['title'].value
description = form['description'].value


opened_file=open('data/'+title,'w')

opened_file.write(description)
opened_file.close()

#redirection
print("location: index.py?id="+title)
print()
