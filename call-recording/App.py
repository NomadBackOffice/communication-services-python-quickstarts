import os

client_id = os.getenv('AZURE_CLIENT_ID')
tenant_id = os.getenv('AZURE_TENANT_ID')
client_secret = os.getenv('AZURE_CLIENT_SECRET')
connection_string = os.getenv('COMMUNICATION_STRING')
callback_url = os.getenv('CALLBACK_URL')


from Logger import Logger
from Controller.RecordingsController import RecordingsController

class App():

    def __init__():
        Logger.log_message(Logger.INFORMATION,"Starting call-recording App... ")

if __name__ == "__main__":
    RecordingsController()
