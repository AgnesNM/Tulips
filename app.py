import os
from flask import Flask, request, Response, render_template
import psycopg2



app = Flask(__name__)

connection = psycopg2.connect(database="tulipers",
                              host="localhost",
                              user="ladies",
                              password="Tulipsrocks23#",
                              port="5433")


# home route


@app.route('/')
def index():
    return render_template('index.html')


# Creating entries into a Postgress Database
@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        # Get the paybill number, national id and phone number.
        paybill_no = request.form.get('paybill_no')
        national_id = request.form.get('national_id')
        phone_number = request.form.get('phone_number')

        # Insert the data into the database
        cur = connection.cursor()
        cur.execute(
            "INSERT INTO payments (national_id, paybill_no, phone_number) VALUES (%s, %s, %s)",
            (national_id, paybill_no, phone_number))
        connection.commit()

        return "Entry created successfully"


# create incoming messages route
@app.route('/incoming-messages', methods=['POST'])
def incoming_messages():
    data = request.get_json(force=True)
    print(f'Incoming message...\n ${data}')
    return Response(status=200)

# create delivery reports route.


@app.route('/delivery-reports', methods=['POST'])
def delivery_reports():
    data = request.get_json(force=True)
    print(f'Delivery report response...\n ${data}')
    return Response(status=200)


if __name__ == "__main__":
    # TODO: Call send message function
    # send_sms()

    app.run(debug=True, port=os.environ.get("PORT"))
