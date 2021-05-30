from twilio.rest import Client 
 
account_sid = 'AC4f6cd40422527c351a3e8b22484dcac7' 
auth_token = '4b5586ce90a6e9da487feb6b23aff50c' 
client = Client(account_sid, auth_token) 
 
def message(number, content):
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body=f'{content}',     
                                to=f'whatsapp:+91{number}' 
                            ) 

# message = client.messages.create( 
#                             from_='whatsapp:+14155238886',  
#                             body='Hemlo',      
#                             to='whatsapp:+918291523382' 
#                         ) 
# message = client.messages.create( 
#                               from_='whatsapp:+',  
#                               body='Unknown vehicle numbered XXXX entered the premises',      
#                               to='whatsapp:+918850528134' 
#                           ) 
# message = client.messages.create( 
#                               from_='whatsapp:+14155238886',  
#                               body='Unknown vehicle numbered XXXX entered the premises',      
#                               to='whatsapp:+918281523382' 
#                           ) 
 
    # print(message.sid)