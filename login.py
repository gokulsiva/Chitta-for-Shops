#!/usr/bin/python

import cgi
import MySQLdb

form = cgi.FieldStorage()
password = None
if form.getvalue('password'):
    password = form.getvalue('password')

db = MySQLdb.connect('localhost', 'guest', 'guest123', 'SREEVANEE')
cursor = db.cursor()
cursor.execute('SELECT DISTINCT PASSWORD FROM PASSWORD')
result = cursor.fetchall()
check = False
if cursor.rowcount > 1:
    for row in result:
        if row[0] == password:
            check = True
elif cursor.rowcount == 1:
    if result[0][0] == password:
        check = True

if check:
    print "Content-type:text/html\r\n\r\n"
    print """
<!DOCTYPE html>
<html>
<head>
	<title>Sree Vanee Silk</title>
	<script type="text/javascript">
		function setURL(url){
    		document.getElementById('iframe').src = url;
    	}
	</script>
	<style type="text/css">
		#top {
			width: 100%;
			height: 100px;
			background-color: #6666FF;
		}
		#left {
			width: 20%;
			height: 635px;
			float: left;
			background-color: #91C2FF;
			text-align: center;
			color: #C50914;
			padding-top: 20px;
		}
		#right {
			width: 80%;
			height: 635px;
			float: left;
		}
		a{
			text-decoration: none;
			border-spacing: 10px;
		}
	</style>
</head>
<body>
<div id="top">
	<div style="align-self: center; text-align: center; color: red; padding: 10px;padding-top: 20px; font-weight: bolder;">
		<font size="20px">SREE VANEE SILK</font>
	</div>
</div>
<div id="left">
	<a href="http://localhost/SreeVanee/daily_chitta.py" target="iframe">CHITTA</a><br><br>
	<a href="http://localhost/SreeVanee/view_balance.py" target="iframe">VIEW BALANCE</a><br><br>
	<a href="http://localhost/SreeVanee/search_chitta.py" target="iframe">SEARCH CHITTA</a><br><br>
	<a href="http://localhost/SreeVanee/add_credit.py" target="iframe">ADD CREDIT TO COMPANY</a><br><br>
	<a href="http://localhost/SreeVanee/add_company.py" target="iframe">ADD COMPANY</a><br><br>
</div>
<div id="right">
	<iframe name="iframe" src="daily_chitta.py" style="width: 99.65%; height: 650px" />
</div>
</body>
</html>
    """
else:
	print 'Location:http://localhost/SreeVanee/index.html\r\n'