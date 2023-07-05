import os
from flask import Flask, request, Response, render_template
from send_sms import send_sms

app = Flask(__name__)

# home route


@app.route('/')
def index():
    return render_template('index.html')

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
    send_sms()

    app.run(debug=True, port=os.environ.get("PORT"))
