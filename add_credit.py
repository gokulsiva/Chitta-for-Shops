#!/usr/bin/python

import MySQLdb


db = MySQLdb.connect("localhost", "guest", "guest123", "SREEVANEE")
cursor = db.cursor()
cursor.execute("SELECT DISTINCT NAME FROM COMPANY_TABLE ORDER BY NAME ASC")
if cursor.rowcount > 1:
    result = cursor.fetchall()
    result_set = []
    for row in result:
        result_set.append(row[0])
else:
    result = cursor.fetchone()
    result_set = [result[0]]

cursor.close()
db.close()
print "Content-type:text/html\r\n\r\n"
print """
<!DOCTYPE html>
<html>
<head>
	<title>Sree Vanee Silk</title>
	<script type="text/javascript">

	function ValidateForm(form) {
		if (form.company_name.selectedIndex == 0 ){
			alert("Please select a company");
		}
		else
		{
			form.submit()
		}
	
	}
	</script>
</head>
<body>
<form action="add_credit_back.py" method="post" style="padding: 10px; font-size: 20px">
	<b>Select the company to add : </b>
	<select name="company_name">
		<option disabled selected value="none"> -- select an option -- </option>
"""
for opt in result_set:
    print "                        <option value=\"{}\">{}</option>".format(opt, opt)		
print """		
	</select><br><br>
	<b>Enter credit amount &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: </b>
	<input type="text" name="credit_amount">
	<br><br>
	<input type="button" value="Add Credit" onclick="ValidateForm(this.form)">
</form>
</body>
</html>
"""