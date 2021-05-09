#!C:\Users\ericshim\AppData\Local\Programs\Python\Python39\python.exe

import cgi, os

form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('data/' + pageId)

# Redirection
print("Location: index.py")
print()