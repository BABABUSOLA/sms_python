#import package
import os
import africastalking
import json
import logging
import lib
import chardet
import schema
import requests

# # Initialize SDK
username = "sandbox" # use "sandbox" for development in the test environment
api_key = "1c17a34d9185cd34bc2d1b3a3375150cacbdd21c6b3d1e81b94eee394ddbee21" #this the present sandbox api key#

africastalking.initialize(username, api_key)

#initialize a  SMS service
sms = africastalking.SMS


def sender(event, context):
    print(event)
    print(context)
    # logging.debug(event)

    #for post man
    # data = json.loads(event['body'])

    #for post man
    recipients = []
    # data = json.loads(event['body'])
    recipients.append(data['recipients'])

    #for campaign applications
    data = event
    print(data)

    sms_message = data['message']
    phone_number = data['recipients']

    #phone number for post man
    # phone_number = recipients

    print(sms_message)
    print(phone_number)

    response = sms.send(sms_message, [phone_number])
    print(response)

    responses = {
        "statusCode": 200,
        "body": json.dumps(response)
    }
    # response = sms.send(data.message,[phone_number])
    #     print(response)
    return responses

    # sms.send(data.message, data.recipients, callback=sender)
