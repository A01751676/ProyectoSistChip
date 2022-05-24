from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1e6d6b8325da4b4406edcf8cbd914d58"
# Your Auth Token from twilio.com/console
auth_token  = "4c394c3e3706169e477552143daf75bc"

client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+525618675785", 
    from_="+12074924829",
    url = "http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)