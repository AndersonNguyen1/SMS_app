from twilio.rest import Client
from credentials import account_sid, auth_token, my_cellphone, my_twilio

client = Client(account_sid, auth_token)

my_msg = "Anderson I love you!"

message = client.messages.create(to = my_cellphone, from_ = my_twilio, body = my_msg)