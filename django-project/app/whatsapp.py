from twilio.rest import Client 
 
account_sid = 'ACac705688726d9eede317dec0d86f84f9' 
auth_token = '0c73fe3177bab7665d5ec5c745a6ad11' 
client = Client(account_sid, auth_token) 
 
def message(number, content):
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body=f'{content}',      
                                to=f'whatsapp:+91{number}' 
                            ) 
# message = client.messages.create( 
#                               from_='whatsapp:+14155238886',  
#                               body='Unknown vehicle numbered XXXX entered the premises',      
#                               to='whatsapp:+918850528134' 
#                           ) 
# message = client.messages.create( 
#                               from_='whatsapp:+14155238886',  
#                               body='Unknown vehicle numbered XXXX entered the premises',      
#                               to='whatsapp:+918281523382' 
#                           ) 
 
    print(message.sid)