#import libraries
from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import Access_token
from twilio.jwt.access_token.grants import SyncGrant

app = Flask(__name__)
fake = Faker()
#write code here


@app.route('/')
def index():
    return render_template('index.html')


#write code here
@app.route('/token')
def generated_token():
	TWILIO_ACCOUNT_SID = "ACb926285b0fc4689a7ae79d452a11a744"
	TWILIO_SYNC_SERVICE_SID = "ISec1d5788a7471f56241f8fd6ba2e625e"
	TWILIO_API_KEY = "SKbe9766688d3a2bfc16c0169668f57458"
	TWILIO_API_SECRET = "LSyPmjuvt4RH3UvEjkUFKXxbpMGwm6EG"

	username = request.args.get('username', fake.user_name())

	token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)

	sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
	token.add_grant(sync_grant_access)
	return jsonify(identity=username, token=token.to_jwt().decode())

if __name__ == "__main__":
    app.run()

