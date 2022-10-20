#Google Docs to Youtube Description Updater

## Purpose

This project was designed to pull contents from a google doc and combine with a template to produce and update a youtube description.
I use this project to automate the descriptions to a podcast on youtube. Since timestamping a podcast after recording can be time-consuming,
we timestamp the episode during recording on google docs. 

##Usage

The assumption is that the Google Docs description will go in between the intro and outro of the description.
** A line of --- or *** should be used in the Google Doc to tell the program where to stop** (this also allows you to use the Doc below that line)
The format of the output description is as follows (with example timestamps):

Description Intro

1. Topic 1 
  Subtopic (0:15)
  Subtopic (4:50)

2. Topic 2
  Subtopic (20:50)
  Subtopic (25:34)

3. Topic 3 (40:15)
4. Topic 4 (50:14)

Description Outro
...

Every topic is automatically numbered, and every subtopic automatically indented. A subtopic is any line that follows a topic. Topics are determined
by new lines. So for example:

Im a Topic
Subtopic
Subtopic

Im the 2nd Topic

Im the 3rd Topic
----------------

Would turn into -->

1. Im a Topic
  Subtopic
  Subtopic

2. Im the 2nd Topic

3. Im the 3rd Topic

## Set Up

You need to set up Authentication with Google and enable both the Docs and Youtube Data APIs in the Google Developer Console Here: https://console.developers.google.com/

Download the dependencies of the project from terminal with pip:

	pip install -r requirements.txt

Insert the ID of your Google Doc and filename of descrition template into config.py

	google_sheet_id=<insert_sheet_id_here>
	description_template=<insert_filename>

Then run main.py

Google will ask you to do input a code to be re-authenticated. You can get rid of this by setting up a refresh token: https://developers.google.com/youtube/v3/guides/authentication#OAuth2_Refreshing_a_Token
