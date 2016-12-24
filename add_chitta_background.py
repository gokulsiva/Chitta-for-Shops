#!/usr/bin/python

import cgi
import time
import MySQLdb

db = MySQLdb.connect("localhost", "guest", "guest123", "SREEVANEE")
cursor = db.cursor()
date = time.strftime("%d/%m/%Y")
times = time.time()
form = cgi.FieldStorage()
types = form.getvalue('type')
if types == 'credit':
    details = form.getvalue('credit_description')
    amount = form.getvalue('credit_amount')
    sql = "INSERT IGNORE INTO CHITTA_TABLE (DATE, DESCRIPTION, CREDIT, DEBIT, PAYMENT) VALUES (\"{}\",\"{}\",\"{}\",\"\", \"\", \"{}\")".format(date, details, amount)
if types == 'debit':
    subtype = form.getvalue('debit_radio')
    if subtype == 'own':
        details = form.getvalue('debit_own')
        amount = form.getvalue('debited_amount')
    if subtype == 'company':
        details = form.getvalue('dropdown')
        amount = form.getvalue('debited_amount')
        select_sql = "SELECT DISTINCT BALANCE FROM COMPANY_TABLE WHERE NAME = \"{}\"".format(details)
        cursor.execute(select_sql)
        result = cursor.fetchone()
        balance = result[0]
        update_sql = "UPDATE COMPANY_TABLE SET NAME = \"{}\", BALANCE = {} WHERE NAME = \"{}\"".format(details, int(balance)-int(amount), details)
        cursor.execute(update_sql)
    payment = form.getvalue('payment')
    if payment == 'cash':
        payment_desc = 'CASH'
    else:
        payment_desc = "Cheque : "+form.getvalue('cheque_detail')
    sql = "INSERT IGNORE INTO CHITTA_TABLE (DATE, DESCRIPTION, CREDIT, DEBIT, PAYMENT) VALUES (\"{}\",\"{}\",\"\",\"{}\",\"{}\", \"{}\")".format(date, details, amount, payment_desc)

cursor.execute(sql)
db.commit()
cursor.close()
db.close()


print 'Location:http://localhost/SreeVanee/daily_chitta.py\r\n'
