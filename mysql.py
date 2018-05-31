__author__ = 'electop.yoo@samsung.com'

import sys
import datetime
import mysql.connector
from mysql.connector import errorcode

user = 'user'
password = ''
host = ''
database = ''
config = {}

args = sys.argv[0:]
optionLen = len(args)

def init():

  global user, password, host, database, config

  if (len(args) <= 1):
    print('[ERR] There is no option')
    return False

  for i in range(optionLen-1):
    data = str(args[i+1])
    if args[i].upper() == '-U':		# -U : user name of MySQL (e.g.: root)
      user = data
    elif args[i].upper() == '-P':	# -P : password of username
      password = data
    elif args[i].upper() == '-H':	# -H : host of MySQL (e.g.: 127.0.0.1)
      host = data
    elif args[i].upper() == '-D':	# -D : database name (e.g.: wp_aitest)
      database = data

  if (user == '') or (password == '') or (host == '') or (database == ''):
    print('[ERR] Please input all required data like user, password, host and database name.')
    return False
  else:
    config = {
    'user': user,
    'password': password,
    'host': host,
    'database': database,
    'raise_on_warnings': True,
    }
  return True

if init():
  try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Querying data using Connector/Python

    time_start = datetime.date(2018, 5, 8)
    time_end = datetime.date(2018, 5, 9)
    query = ("SELECT target_url, department_name, knox_id, full_name, employee_number, user_information, time FROM wp_misspelling WHERE id BETWEEN 11 AND 12 AND time BETWEEN %s AND %s")
    cursor.execute(query, (time_start, time_end))
    for (target_url, department_name, knox_id, full_name, employee_number, user_information, time) in cursor:
      print("{}, {}, {}, {}, {}, {} was posted on {:%d %b %Y}".format(target_url, department_name, knox_id, full_name, employee_number, user_information, time))
    cursor.close()
    print('[OK] Connection success')

  # Exceoption for connection

  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print('[ERR] Something is wrong with your user name or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print('[ERR] Database does not exist')
    else:
      print('[ERR]', err)
  else:
    cnx.close()
else:
  print("[ERR] Connection failure")
