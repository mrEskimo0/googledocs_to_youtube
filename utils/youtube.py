from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

class Youtube:

    def __init__(self, secretsfile):
        self.CLIENT_SECRETS_FILE = secretsfile
        self.SCOPES = ['https://www.googleapis.com/auth/youtube']
        self.API_SERVICE_NAME = 'youtube'
        self.API_VERSION = 'v3'

    def get_authenticated_service(self):
        flow = InstalledAppFlow.from_client_secrets_file(self.CLIENT_SECRETS_FILE, self.SCOPES)
        credentials = flow.run_console()
        return build(self.API_SERVICE_NAME, self.API_VERSION, credentials = credentials)

    def get_my_uploads_list(self, youtube):
        # Retrieve the contentDetails part of the channel resource for the
        # authenticated user's channel.
        channels_response = youtube.channels().list(
        mine=True,
        part='contentDetails'
        ).execute()

        for channel in channels_response['items']:
            #gets uploads playlist id
            return channel['contentDetails']['relatedPlaylists']['uploads']

        return None

    def get_latest_video(self, uploads_playlist_id, youtube):
        # get playlist by id
        playlistitems_list_request = youtube.playlistItems().list(
            playlistId=uploads_playlist_id,
            part='snippet',
            maxResults=1
        )

        playlistitems_list_response = playlistitems_list_request.execute()
        vids = playlistitems_list_response['items']
        #return first instance from response which is latest upload
        return vids[0]['snippet']['resourceId']['videoId']

    def update_youtube_description(self, description):

        youtube = self.get_authenticated_service()
        uploads_playlist_id = self.get_my_uploads_list(youtube)
        video_id = self.get_latest_video(uploads_playlist_id, youtube)

        videos_list_response = youtube.videos().list(
        id=video_id,
        part='snippet'
      ).execute()

        videos_list_snippet = videos_list_response['items'][0]['snippet']

       #set video description
        videos_list_snippet['description'] = description

        # Update the video resource by calling the videos.update() method.
        videos_update_response = youtube.videos().update(
        part='snippet',
        body=dict(
          snippet=videos_list_snippet,
          id=video_id
        )).execute()
        print('Description Successfully Updated')



