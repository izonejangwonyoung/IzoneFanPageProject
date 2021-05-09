#!C:\Users\ericshim\AppData\Local\Programs\Python\Python38\python.exe

#-*- coding:utf-8 -*-



print("content-type: text/html; charset=utf-8\n")

print()
import cgi
import os
import view

files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr +  '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId,'r').read()
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId"   value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId = 'HELLO'
    description = 'WIZ*ONE'
    update_link = ''
    delete_action = ''


print('''<!DOCTYPE HTML>

<html>
	<head>
		<title>WELCOME TO TEXT REGISTER PAGE</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<link rel="shortcut icon" href="izone.ico" />

	</head>
	<body class="is-preload">

		<!-- Header -->
			<header id="header">
				<h1>TEXT REGISTER PAGE</h1>
				<p>WELCOME TO TEXT REGISTER PAGE</p>
				<p>Because of technical problems, You can only write in English. </p>
				<h4>갤러리로 이동하려면 <a href="http://211.179.91.220/index.html">여기</a>를 눌러주세요.</h4>

				
				<ol>{listStr}</ol>
			</header>

		
			
		<a href="create.py">Create Text</a>
<a href="index.py">TEXT REGISTER PAGE</a>
{update_link}
{delete_action}

<h2>{title}</h2>
<p>{desc}</p>
<br><br><br><br><br><br>
		<!-- Footer -->
			<footer id="footer">
				<ul class="icons">

					<li><a href="https://github.com/izonejangwonyoung" class="icon brands fa-github"><span class="label">GitHub</span></a></li>

				</ul>
				<ul class="copyright">
					<li>&copy; Untitled.</li><li>Helped by <strong>HTML5</strong></li><li><a href="http://211.179.91.220/index.html"> Home</li>
				</ul>
			</footer>

		<!-- Scripts -->
				<script src="assets/js/main.js"></script>

	</body>
</html>




'''.format(title=pageId, desc=description, listStr=view.getlist(),
           update_link=update_link, delete_action=delete_action))

