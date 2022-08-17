from __future__ import print_function

from googleapiclient import discovery
from httplib2 import Http
from googleapiclient.errors import HttpError
from oauth2client import file, client, tools
from googleapiclient.http import MediaFileUpload


SCOPES = 'https://www.googleapis.com/auth/drive'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

files = DRIVE.files().list().execute().get('files', [])
for f in files:
    print(f['name'], f['mimeType'])

file_metadata = {'name': 'client_secret.json'}
media = MediaFileUpload('client_secret.json', mimetype='application/zip')
DRIVE.files().create(body=file_metadata, media_body=media, fields='id').execute()