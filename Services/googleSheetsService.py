from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from Config.sheetConfig import SERVICE_ACCOUNT_FILE, SCOPES

def get_service():
    """
    Данный метод возвращает объект класса, для работы с google sheets
    :return:
    """
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)

    return service
