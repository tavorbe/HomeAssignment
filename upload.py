from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from createService import creds, DRIVE

def upload_basic():

    try:

        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {'name': 'client_secret.json'}
        media = MediaFileUpload('client_secret.json',
                                mimetype='application/zip')
        # pylint: disable=maybe-no-member

        results = service.files().create(body=file_metadata, media_body=media,
                                       fields='id').execute()
        items = results.get('files', [])

    except HttpError as error:
        print(F'An error occurred: {error}')
        results = None

    #return items


if __name__ == '__main__':
    upload_basic()