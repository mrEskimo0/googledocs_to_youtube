from utils.description import Description
from utils.youtube import Youtube
from config import google_sheet_id, description_template

desc = Description('./' + description_template,'./doc_text.txt') #doc_text.txt is the google docs download
desc.get_doc_text(google_sheet_id)
finished_desc = desc.make_description()

#now update youtube with desc
youtube = Youtube('./client_secret.json')
youtube.update_youtube_description(finished_desc)

