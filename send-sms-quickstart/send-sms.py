import os
from azure.communication.sms import SmsClient

try:
    # Quickstart code goes here
	# Create the SmsClient object which will be used to send SMS messages
	sms_client = SmsClient.from_connection_string("endpoint=https://communications-resource2.unitedstates.communication.azure.com/;accesskey=8qRf70AaLUexh50KrQ5SWmqe2T1FWc5DDh4TRKYdf904blm2q7gfJQQJ99AJACULyCpRBuouAAAAAZCStpuW")
	
    ## Send a 1:1 SMS Message
    # calling send() with sms values
    # sms_responses = sms_client.send(
    # from_="<from-phone-number>",
    # to="<to-phone-number>",
    # message="Hello World via SMS",
    # enable_delivery_report=True, # optional property
    # tag="custom-tag") # optional property

    # Send a 1:N SMS Message
	# calling send() with sms values
	sms_responses = sms_client.send(
    from_="+18666689132",
    to=["+19546844791", "+18633322851"],
    message="Hello World via SMS Python",
    enable_delivery_report=True, # optional property
    tag="custom-tag") # optional property
except Exception as ex:
    print('Exception:')
    print(ex)
	
