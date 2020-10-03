from db_connection import db

cursor = db.cursor()
query = cursor.execute("SELECT * FROM thedenton.open_minds")

participants = cursor.fetchall()
total_participant = cursor.rowcount

print('Total participant: {}'.format(total_participant))
print(participants)