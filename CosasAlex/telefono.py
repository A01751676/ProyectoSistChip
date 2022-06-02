from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1e6d6b8325da4b4406edcf8cbd914d58"
# Your Auth Token from twilio.com/console
auth_token  = "dd532883b0cfa24ea4591cf66da612f6"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+525618675785", 
    from_="+12074924829",
    body="Logre mandar mensajes mss")

print(message.sid)

