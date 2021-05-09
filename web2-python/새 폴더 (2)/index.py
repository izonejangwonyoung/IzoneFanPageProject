#!C:\Users\ericshim\AppData\Local\Programs\Python\Python39\python.exe

#-*- coding:utf-8 -*-


print("content-type: text/html; charset=euc-kr ")

print()
import cgi
import os
import view

files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId,'r').read()
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId = 'WELCOME'
    description = 'WIZONE'
    update_link = ''
    delete_action = ''


print('''<!DOCTYPE HTML>

<html>
	<head>
		<title>Member Register Page</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
	</head>
	<body class="is-preload">

		<!-- Header -->
			<header id="header">
				<h1>Member Register Page</h1>
				<p>멤버 등록 페이지에 오신 것을 환영합니다</p>
				
				<ol>{listStr}</ol>
			</header>

		
			
		<a href="create.py">Create Member</a>
<a href="index.py">Member Register Page</a>
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
					<li>&copy; Untitled.</li><li>Helped by <strong>HTML5</strong></li><li><a href="http://127.0.0.1/index.html"> Home</li>
				</ul>
			</footer>

		<!-- Scripts -->
				<script src="assets/js/main.js"></script>

	</body>
</html>




'''.format(title=pageId, desc=description, listStr=view.getlist(),
           update_link=update_link, delete_action=delete_action))

