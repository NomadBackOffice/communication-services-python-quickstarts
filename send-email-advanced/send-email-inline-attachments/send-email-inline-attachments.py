import base64
from azure.communication.email import EmailClient

with open("./inline-attachment.jpg", "rb") as file:
    jpg_b64encoded = base64.b64encode(file.read())

with open("./inline-attachment.png", "rb") as file:
    png_b64encoded = base64.b64encode(file.read())

connection_string = "COMMUNICATION_STRING"
sender_address = "jeff@nomadbackoffice.com"
recipient_address = "optiontrader91@gmail.com"

POLLER_WAIT_TIME = 10

message = {
    "senderAddress": sender_address,
    "recipients":  {
        "to": [{ "address": recipient_address }]
    },
    "content": {
        "subject": "Test email from Python Sample",
        "plainText": "This is plaintext body of test email.",
        "html": "<html><h1>HTML body inline images:</h1><img src=\"cid:kittens-1\" /><img src=\"cid:kittens-2\" /></html>"
    },
    "attachments": [
        {
            "name": "inline-attachments.jpg",
            "contentId": "kittens-1",
            "contentType": "image/jpeg",
            "contentInBase64": jpg_b64encoded.decode()
        },
        {
            "name": "inline-attachments.png",
            "contentId": "kittens-2",
            "contentType": "image/png",
            "contentInBase64": png_b64encoded.decode()
        }
    ]
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
