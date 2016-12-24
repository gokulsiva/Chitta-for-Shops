#!/usr/bin/python
import cgi
import MySQLdb

form = cgi.FieldStorage()
name = form.getvalue('name')

db = MySQLdb.connect("localhost", "guest", "guest123", "SREEVANEE")
cursor = db.cursor()

sql = "SELECT DISTINCT * FROM CREDIT_TABLE WHERE NAME = '{}'".format(name)
cursor.execute(sql)
credit_result = []
if cursor.rowcount > 1:
    credit_result = cursor.fetchall()
else:
    result = cursor.fetchone()
    credit_result.append(result)

sql = "SELECT DISTINCT * FROM CHITTA_TABLE WHERE DESCRIPTION = '{}' AND CREDIT = ''".format(name)
cursor.execute(sql)
debit_result = []
if cursor.rowcount > 1:
    debit_result = cursor.fetchall()
else:
    result = cursor.fetchone()
    debit_result.append(result)

print "Content-type:text/html\r\n\r\n"
print """
<!DOCTYPE html>
<html>
<head>
	<title>Sree Vanee Silk</title>
	<style type="text/css">
		table, th, tr, td {
			border: 1px solid black;
			border-collapse: collapse;
			text-align: center;
			padding: 5px;
		}
	</style>
</head>
<body>
<div style="width: 100%; height: 10%; font-size: 25px; font-weight: bold; color: red; text-align: center;">
	NAME OF COMPANY
</div>
<div style="font-weight: bold; font-size: 20px">
	Credit list:<br>
</div>
<br>
<table style="width: 80%; margin-left: 10%; margin-right: 10%">
	<tr>
		<th>DATE</th>
		<th>NAME</th>
		<th>CREDIT</th>
	</tr> """
for row in credit_result:
	print """
	<tr>
		<td>{}</td>
		<td>{}</td>
		<td>{}</td>
	</tr> """.format(row[0], row[1], row[2])
print """
</table>
<br><br>
<div style="font-weight: bold; font-size: 20px">
	Debit list:<br>
</div>
<br>
<table style="width: 100%">
	<tr>
		<th>DATE</th>
		<th>NAME</th>
		<th>DEBIT</th>
		<th>PAYMENT</th>
	</tr>"""
for row in debit_result:
	print """
	<tr>
		<td>{}</td>
		<td>{}</td>
		<td>{}</td>
		<td>{}</td>
	</tr>
	""".format(row[0], row[1], row[3], row[4])
print """
</table>
</body>
</html>
"""
cursor.close()
db.close()