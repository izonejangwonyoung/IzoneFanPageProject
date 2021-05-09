#!C:\Users\ericshim\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding:utf-8 -*-


print("content-type: text/html; charset=euc-kr ")

print()
import cgi
import os
import view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form['id'].value
    description = open('data/' + pageId, 'r').read()
    description = description.replace('<', '&lt;')
    description = description.replace('<', '&gt;')

    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
        <input type="hidden" name="pageId" value="{}">
        <input type="submit" value="delete">
        '''.format(pageId)

else:
    pageId = "welcome"
    description = 'hello wiz*one'
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
				<p>멤버 등록 페이지에 오신 것을 환영합니다<a href="http://html5up.net"></a></p>
				<ol>{listStr}</ol>
				<h4>갤러리로 이동하려면 <a href="http://211.179.91.220/index.html">여기</a>를 눌러주세요.</h4>

			</header>

		<!-- Signup Form -->
			
		<a href="create.py">create</a>
<a href="index.py">Member Register Page</a>
{update_link}
{delete_action}
<br><br>
<!--<h2>{title}</h2>-->
<!--<p>{desc}</p>-->

		<!-- Footer -->
			<footer id="footer">
				<ul class="icons">

					<li><a href="https://github.com/izonejangwonyoung" class="icon brands fa-github"><span class="label">GitHub</span></a></li>

				</ul>
				<ul class="copyright">
					<li>&copy; Untitled.</li><li>Helped by <strong>HTML5</strong></li>
				</ul>
			</footer>

		<!-- Scripts -->
			<script src="assets/js/main.js"></script>
<a href="create.py">create</a>
  <form action="process_create.py" method="post">
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
      <p><input type="submit"></p>
  </form>
  	<script src="assets/js/main.js"></script>
	</body>
</html>




'''.format(title=pageId, desc=description, listStr=view.getlist(),
           update_link=update_link, delete_action=delete_action))
