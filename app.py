import os

import dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# move to src
import wikipedia
import sys

project_dir = os.path.dirname(__file__)
dotenv_path = os.path.join(project_dir, '.env')
dotenv.load_dotenv(dotenv_path)

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# move to src ---
def get_summary(search_term):

    try:
        if search_term!="":
            resp = wikipedia.summary(search_term) 
        else:
            resp="how about you try a little something"
    except wikipedia.exceptions.DisambiguationError as err:
        new_opts = err.options
        resp=f"ok, so actually, '{err.title}' turns out not be a great search term. i'll cut you a deal. your new search term is '{new_opts[0]}'. and you're going to learn to live with it:\n"
        resp = resp + wikipedia.summary(new_opts[0])
    except wikipedia.exceptions.PageError:
        resp="na man, that doesn't return any results. Try again brohannes gutenbro."
    return resp
# ---

# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.event("app_mention")
def mention_response(ack, payload, say):
    # say() sends a message to the channel where the event was triggered
    say(f"oh, it's you again <@{payload['user']}>")
    search_term = ' '.join(payload['text'].split()[1:])
    say(f"you want to know something about {search_term}? i'll TELL you something about {search_term}")
    say(get_summary(search_term))

@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()