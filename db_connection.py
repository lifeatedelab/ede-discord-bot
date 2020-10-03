import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
db = mysql.connector.connect(
    host='localhost',
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASS')
)

if db.is_connected():
    print('succesfully connected to database')