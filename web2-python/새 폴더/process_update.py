#!C:\Users\ericshim\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding:utf-8 -*-

import cgi, os

form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form['description'].value

opened_file = open('data/' + pageId, 'w')
opened_file.write(description)
opened_file.close()

os.rename('data/' + pageId, 'data/' + title)
opened_file.close()
# Redirection
print("Location: index.py?id=" + title)
print()