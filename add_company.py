#!/usr/bin/python

print "Content-type:text/html\r\n\r\n"
print """
<!DOCTYPE html>
<html>
<head>
	<title>Sree Vanee Silk</title>
</head>
<body>
<form action="add_company_background.py" method="post" style="padding: 10px">
	Enter company name &nbsp;: <input type="text" name="company_name"><br><br>
	Enter balance amount : <input type="text" name="company_balance"><br><br>
	<input type="submit" value="Add Company">
</form>
</body>
</html>
"""