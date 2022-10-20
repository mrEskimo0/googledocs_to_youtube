from utils.description import Description
from utils.youtube import Youtube
from config import google_sheet_id

desc = Description('./description_template.txt','./doc_text.txt')
desc.get_doc_text(google_sheet_id)
finished_desc = desc.make_description()

#now update youtube with desc
youtube = Youtube('./client_secret.json')
youtube.update_youtube_description(finished_desc)

