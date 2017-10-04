from flask import Flask
from twilio.rest import Client

client = Client()

app = Flask(__name__)

to = "+13234924416"
from_ = "+17867892968"
message_body = "Hello from Haseeb ur Rahman CS643 Fall 2017"

@app.route("/")
def hello():

    message = client.messages.create(
            to=to,
            from_=from_,
            body=message_body
            )

    return "Message ID: {} sent to {} from {}".format(message.sid, to, from_)

app.run(host='0.0.0.0', port=80)
