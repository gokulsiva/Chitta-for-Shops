#!/usr/bin/python
import cgi
import MySQLdb

credit = 0
debit = 0
form = cgi.FieldStorage()
un_date = form.getvalue('date')
dd = un_date[8:10]
mm = un_date[5:7]
yyyy = un_date[0:4]
date = "{}/{}/{}".format(dd, mm, yyyy)

db = MySQLdb.connect("localhost", "guest", "guest123", "SREEVANEE")
cursor = db.cursor()
chitta = []
cursor.execute("SELECT DISTINCT * FROM CHITTA_TABLE WHERE DATE = '{}'".format(date))
if cursor.rowcount > 1:
    chitta = cursor.fetchall()
else:
    result = cursor.fetchone()
    chitta.append(result)

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Sree Vanee Silk</title>'
print """
	<style type="text/css">
		table, tr, th, td {
			border: 1px solid black;
			border-collapse: collapse;
			text-align: center;
			padding: 5px;
		}
	</style>
	<script type="text/javascript">
	var result = function() {
		var button_text = document.getElementById('result_button');
		var div = document.getElementById('result');
    	if (div.style.display !== 'none') {
        div.style.display = 'none';
        result_button.value = 'Show Calculations'
    	}
    	else {
        div.style.display = 'block';
        result_button.value = 'Hide Calculations'
    	}
		};

	</script>
	"""
print '</head>'
print '<body>'
print """
<form action="search_chittas_background.py" method="post" style="padding: 10px">
	Select the date to search chitta : 
	<input type="date" name="date"> &nbsp;&nbsp;
	<input type="submit" value="Search">
</form><br><br><br>
<b>Search result : </b><br><br>"""
print """
<table style="width: 100%">
<tr>
	<th>DATE</th>
	<th>DESCRIPTION</th>
	<th>CREDIT</th>
	<th>DEBIT</th>
	<th>PAYMENT</th>
</tr>
"""
for row in chitta:
	if row[2] != '':
		credit += int(row[2])
	if row[3] != '':
		debit += int(row[3])
	print """
<tr>
	<td>{}</td>
	<td>{}</td>
	<td>{}</td>
	<td>{}</td>
	<td>{}</td>
</tr>
	""".format(row[0], row[1], row[2], row[3], row[4])

print """
</table><br><br>
	<input type="button" id="result_button" value="Show Calculations" onclick="result()"><br><br>
	<div id="result" style="display:none">
		Total Credit amount : {}<br>
		Total Debit amount &nbsp;: {}<br>
		Tally amount &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: {}<br>
	</div>""".format(credit, debit, credit-debit)
print '</body>'
print '</html>'
