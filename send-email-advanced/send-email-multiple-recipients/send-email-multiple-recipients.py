from azure.communication.email import EmailClient

connection_string = "endpoint=https://communications-resource2.unitedstates.communication.azure.com/;accesskey=8qRf70AaLUexh50KrQ5SWmqe2T1FWc5DDh4TRKYdf904blm2q7gfJQQJ99AJACULyCpRBuouAAAAAZCStpuW"
sender_address = "jeff@nomdbackoffice.com"
recipient_address = "optiontrader91@gmail.com"
replyto_address = "jeff@nomadbackoffice.com"

POLLER_WAIT_TIME = 10

message = {
    "senderAddress": sender_address,
    "recipients":  {
        "to": [{ "address": recipient_address }, { "address": recipient_address }],
        "cc": [{ "address": recipient_address }],
        "bcc": [{ "address": recipient_address }]
    },
    "content": {
        "subject": "Test email from Python Sample",
        "plainText": "This is plaintext body of test email.",
        "html": "<html><h1>This is the html body of test email.</h1></html>",
    },
    "replyTo": [{ "address": replyto_address }]
}

try:
    client = EmailClient.from_connection_string(connection_string)

    poller = client.begin_send(message);

    time_elapsed = 0
    while not poller.done():
        print("Email send poller status: " + poller.status())

        poller.wait(POLLER_WAIT_TIME)
        time_elapsed += POLLER_WAIT_TIME

        if time_elapsed > 18 * POLLER_WAIT_TIME:
            raise RuntimeError("Polling timed out.")

    if poller.result()["status"] == "Succeeded":
        print(f"Successfully sent the email (operation id: {poller.result()['id']})")
    else:
        raise RuntimeError(str(poller.result()["error"]))
    
except Exception as ex:
    print(ex)
