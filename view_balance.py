#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect("localhost", "guest", "guest123", "SREEVANEE")
cursor = db.cursor()
sql = "SELECT DISTINCT * FROM COMPANY_TABLE ORDER BY NAME"
cursor.execute(sql)
company_result = []
if cursor.rowcount > 1:
    company_result = cursor.fetchall()
else:
    result = cursor.fetchone()
    company_result.append(result)

print "Content-type:text/html\r\n\r\n"
print """
<!DOCTYPE html>
<html>
<head>
	<title>Sree Vanee Silk</title>
	<style type="text/css">
		table, th, tr{
			border: 1px solid black;
			border-collapse: collapse;
			text-align: center;
			padding: 5px;
		}
		tr:hover {
  background-color: #a8abaf;
}
	</style>
	<script type="text/javascript">
function DoNav(url)
{
   document.location.href = url;
}
</script>

</head>
<body>
<h2 style="width: 100%; text-align: center;">Balance Details<h2>
<table style="width: 80%; margin-left: 10%; margin-right: 10%">
<tr style="background:powderblue;">
	<th style="width: 60%">Company Name</th>
	<th style="width: 40%">Balance</th>
</tr>"""
for row in company_result:
    print """
    <tr onclick="DoNav('http://localhost/SreeVanee/view_balance_detail.py?name={}')">
        <th>{}</th>
        <th>{}</th>
    </tr>""".format(row[0], row[0], row[1])

print """</table>
</body>
</html>
"""
