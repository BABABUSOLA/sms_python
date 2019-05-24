#import package
import africastalking
import json
import logging
import chardet from lib
import chardet
# import decimal

import requests

# # Initialize SDK
username = "sandbox" # use "sandbox" for development in the test environment
api_key = "1c17a34d9185cd34bc2d1b3a3375150cacbdd21c6b3d1e81b94eee394ddbee21" #this the present sandbox api key#

africastalking.initialize(username, api_key)

#initialize a  SMS service
sms = africastalking.SMS

#use the service sycronously
# response = sms.send("Hello, This testing the sms sender!", "+2348066109631")
# print(response)



# # This is a workaround for: http://bugs.python.org/issue16535
# class DecimalEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, decimal.Decimal):
#             return int(obj)
#         return super(DecimalEncoder, self).default(obj)

# def checkTelco(number):
# 	prefix = number[0:6]
# 	telco_name = ''
# 	mtn_prefix = ['234703','234706','234803','234806','234813','234814','234816','234903','234906','234810']
# 	glo_prefix = ['234705','234805','234807','234811','234815','234905']
# 	etisalat_prefix = ['234809','234817','234818','234908','234909']
# 	airtel_prefix = ['234701','234708','234802','234808','234812','234902','234907']

# 	print("starting check")
# 	print(prefix)

# 	if (prefix in mtn_prefix):
# 		telco_name = 'mtn'
# 	elif (prefix in glo_prefix):
# 		telco_name = 'glo'
# 	elif (prefix in etisalat_prefix):
# 		telco_name = 'etisalat'
# 	elif (prefix in airtel_prefix):
# 		telco_name = 'airtel'
# 	else:
# 		telco_name = ''

# 	return telco_name


# def send(number,message):
#     console.log(number)
# 	phone_number = "234"+number[1:]
# 	telco_name = checkTelco(phone_number)
# 	if (telco_name == 'airtel'):
# 	    PARAMS = {
# 	        'username': "sponge",
# 	        'password': "sponge",
# 	        'smsc': 'Airtel_RECEIVE1',
# 	        'to': phone_number,
# 	        'from': '55332',
# 	        'text': message
# 	        }
# 	    req = requests.get("http://5.101.174.139:13035/cgi-bin/sendsms",params = PARAMS)
# 	    print(req)
# 	elif (telco_name == 'glo' or telco_name == 'mtn' or telco_name == "etisalat"):
# 	    # Initialize a service e.g. SMS
# 	    sms = africastalking.SMS

# 	    # Use the service synchronously
# 	    phone_number = "+"+phone_number
# 	    senderID = "Jk2019"
# 	    try:
# 	        print("sending sms.....",sms,phone_number)
# 	        response = sms.send(message, [phone_number],senderID)
# 	        print(response)
# 	    except Exception as e:
# 	        print ('Encountered an error while sending: {0}'.format(str(e)))
# 	else:
# 	    pass   
# def sender(event, context):
#     # logging.debug(event)
#     data = json.loads(event['body'])
#     print(data)

#     response = {
#         "statusCode": 200,
#         "body": json.dumps(data)
#     }
#     return response

def sender(error, response):
    if error is not None:
        raise error
    print(response)

sms.send("Hello Message!", ["+2348066109631"], callback=sender)
