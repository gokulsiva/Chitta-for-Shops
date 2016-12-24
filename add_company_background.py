#!/usr/bin/python

import cgi
import MySQLdb
import sys
import time

date = time.strftime("%d/%m/%Y")
times = time.time()
form = cgi.FieldStorage()
name = form.getvalue('company_name')
balance = form.getvalue('company_balance')

if name == None or balance == None:
	print 'Location:http://localhost/SreeVanee/add_company.py\r\n'
	sys.exit()
db = MySQLdb.connect("localhost", "guest", "guest123", "SREEVANEE")
cursor = db.cursor()
sql = "INSERT IGNORE INTO COMPANY_TABLE(NAME, BALANCE) VALUES (\"{}\",{})".format(name, int(balance))
try:
	cursor.execute(sql)
	sql_2 = "INSERT IGNORE INTO CREDIT_TABLE(DATE, NAME, CREDIT) VALUES (\"{}\",\"{}\",{}, \"{}\")".format(date, name, int(balance))
	cursor.execute(sql_2)
	db.commit()
	message = "Successfully added {} to the list".format(name)
except:
	message = "Error updating {} to the list".format(name)
finally:
	pass
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Sree Vanee Silk</title>'
print '</head>'
print '<body>'
print '<h2>{}</h2>'.format(message)
print '</body>'
print '</html>'
