#!/usr/bin/python

print "Content-type:text/html\r\n\r\n"
print """
<!DOCTYPE html>
<html>
<head>
	<title>Sree Vanee Silk</title>
</head>
<body>
<form action="search_chittas_background.py" method="post" style="padding: 10px">
	Select the date to search chitta : 
	<input type="date" name="date"> &nbsp;&nbsp;
	<input type="submit" value="Search">
</form>
</body>
</html>
"""
