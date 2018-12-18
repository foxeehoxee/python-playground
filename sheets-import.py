"""
This will take an Excel or OpenOffice spreadsheet file and import it into your Google Drive
auto-magically via the Google Sheets API. Maintains format & layout which is rad, eh? Eh?!
"""

from __future__ import print_function

import datetime

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
# noinspection SpellCheckingInspection
from oauth2client import file as oafile, client, tools

# If modifying these scopes, delete the file 'token.json'
SCOPES = 'https://www.googleapis.com/auth/drive'

# Update report source accordingly
# REPORT_MASTER = 'data/master_report_sample.csv'
REPORT_MASTER = 'data/master_report_sample.ods'

# Gussy up these curtains a bit
timeStamp = datetime.datetime.now()
formattedTimeStamp = timeStamp.strftime("%Y-%m-%d (%A)")
formattedReportName = u'Auto-Imported Report: {0}'.format(formattedTimeStamp)


def main():
    # The file token.json stores the user's access and refresh tokens, and is
    # auto-generated when the authorization flow completes for the first time.
    store = oafile.Storage('token.json')
    tokens = store.get()
    if not tokens or tokens.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        tokens = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=tokens.authorize(Http()))

    # Call the Drive v3 API
    results = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('\nDirectory is empty...')
    else:
        print('\nExisting Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

    file_metadata = {
        'name': formattedReportName,
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    media = MediaFileUpload(REPORT_MASTER,
                            mimetype='application/vnd.oasis.opendocument.spreadsheet',
                            resumable=True)
    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()
    print('\n\nImport complete!\nImported File ID: %s' % file.get('id'))


if __name__ == '__main__':
    main()
