import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from commands import commands

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])
app_token = os.environ["SLACK_APP_TOKEN"]

doc_bot_id = os.environ["SLACK_DOC_BOT_ID"]
teleclinic_team_id = os.environ["SLACK_TELECLINIC_ID"]

@app.event("app_mention")
def handle_app_mention_events(body, event, say):
    # print(body) # complete request body
    user_id = event["user"]
    text = event["text"]
    if body["team_id"] != teleclinic_team_id:
      say("Sorry, this functionality is only available to Teleclinic employees.")
    elif user_id == doc_bot_id:
      print("Don't talk to yourself!")
    else:
      bot_handle = f"<@{doc_bot_id}>"

      if text.startswith(bot_handle):
        cmd_line = text.removeprefix(bot_handle).split()

        # default cmd in case empty mention
        cmd = 'help'
        if len(cmd_line) > 0:
          cmd = cmd_line[0]

        if cmd in ['help','h3p','h3lp','halp','h']:
          say("I respond to the following commands:\n" +
            "`help|h`: this cmd\n" +
            "`echo`: repeat given args\n" +
            "`whoami`: user talking to me\n")
        elif cmd == "echo" and len(cmd_line) > 1:
          say(commands.echo(cmd_line[1:]))
        elif cmd == "whoami":
          say(commands.whoami(user_id))
      else:
        say("I only respond to well formatted cmds...Try `@docbot help`")

if __name__ == "__main__":
    handler = SocketModeHandler(app, app_token)
    handler.start()
