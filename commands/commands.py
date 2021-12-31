def echo(cmd_line_params):
  return ' '.join(cmd_line_params)

def whoami(user_id):
  return f"<@{user_id}>, your Slack ID is {user_id}"
