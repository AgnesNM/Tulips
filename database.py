import psycopg2

connection = psycopg2.connect(database="tulipers",
                        host="localhost",
                        user="ladies",
                        password="Tulipsrocks23#",
                        port="5433")


cursor = connection.cursor()

insert_query = "INSERT INTO payments (national_id, paybill_no, phone_number) VALUES (%s, %s, %s)"
data = ('200800', '28594210', '+254712227589')

cursor.execute(insert_query, data)

connection.commit()

print("Data inserted successfully!")

print(cursor.fetchone())