#!/usr/bin/python

import cgi
import MySQLdb
import time

date = time.strftime("%d/%m/%Y")
times = time.time() 
form = cgi.FieldStorage()
name = form.getvalue('company_name')
credit = form.getvalue('credit_amount')
db = MySQLdb.connect("localhost", "guest", "guest123", "SREEVANEE")
cursor = db.cursor()
select_sql = "SELECT DISTINCT BALANCE FROM COMPANY_TABLE WHERE NAME = \"{}\"".format(name)
cursor.execute(select_sql)
result = cursor.fetchone()
balance = result[0]
update_sql = "UPDATE COMPANY_TABLE SET NAME = \"{}\", BALANCE = {} WHERE NAME = \"{}\"".format(name, int(balance)+int(credit), name)
cursor.execute(update_sql)
insert_sql = "INSERT IGNORE INTO CREDIT_TABLE(DATE, NAME, CREDIT) VALUES (\"{}\",\"{}\",{},\"{}\")".format(date, name, int(credit))
cursor.execute(insert_sql)
db.commit()

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Sree Vanee Silk</title>'
print '</head>'
print '<body>'
print '<h2>Credit added to {}</h2>'.format(name)
print '</body>'
print '</html>'
