import os
from util_csv import get_student_emails, get_team_assignments
from slackclient import SlackClient

# Slack client initialization
SLACK_TOKEN = os.environ['SLACK_TOKEN']
CHANNEL_NAME_LIMIT = 21
sc = SlackClient(SLACK_TOKEN)

# Main
def main():
    option = input('Please select your option:\n1) Invite all students to #General\n2) Invite students to team channel\n')

    # Invite all students to workspace
    if option == 1:
        emails = get_student_emails()
        invite_to_workspace(emails)

    # Invite all students to team channels
    elif option == 2:
        assignments = get_team_assignments()
        for team, emails in assignments.items():
            team = team[0:CHANNEL_NAME_LIMIT].lower() # Process channel name

            channel = get_channel_id(team)
            if channel == None:
                channel = create_channel(team)
            invite_to_channel(channel, emails)

    # Invalid Selection
    else:
        print 'Invalid Option'


def create_channel(name):
    res = sc.api_call('channels.create', name=name)
    return res['channel']['id'] if res['ok'] else None

def invite_to_workspace(emails):
    for email in emails:
        sc.api_call('users.admin.invite', email=email)

def invite_to_channel(channel, emails):
    for email in emails:
        user = get_user_id(email)
        sc.api_call('channels.invite', user=user, channel=channel)

def get_user_id(email):
    res = sc.api_call('users.lookupByEmail', email=email)
    return res['user']['id'] if res['ok'] else None

def get_channel_id(name):
    res = sc.api_call('channels.list')
    for channel in res['channels']:
        if channel['name'] == name:
            return channel['id']
    return None

if __name__== '__main__':
    main()
