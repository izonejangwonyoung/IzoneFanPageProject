#!C:\Users\ericshim\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding:utf-8 -*-

print("Content-Type: text/html")
print()
import cgi, os

files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/' + pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, wizone'

print('''
<!doctype html>
<html>
<head>
    <title>Member INFO update</title>
    <meta charset="utf-8">

</head>
<body>
<div style="text-align: center;">


    <h1>Contents Modification Page</h1><br>
    <ol>
        {listStr}
    </ol>

    <form action="process_update.py" method="post">
        <input type="hidden" name="pageId" value="{form_default_title}">
        <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
        <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
        <p><input type="submit"></p>
    </form>
    <h1><a href="index.py">CLICK </a>to return previous page</h1>

</div>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr, form_default_title=pageId, form_default_description=description))






