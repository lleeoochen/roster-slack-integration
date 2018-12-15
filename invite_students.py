import os
from util_csv import get_student_emails, get_team_assignments
from slackclient import SlackClient

SLACK_TOKEN = os.environ['SLACK_TOKEN']
sc = SlackClient(SLACK_TOKEN)

def main():
    option = input('Please select your option:\n1) Invite all students to #General\n2) Invite students to team channel\n')
    
    if option == 1:
        emails = get_student_emails()
        invite_to_workspace(emails, 'general')

    elif option == 2:
        assignments = get_team_assignments()
        for team, emails in assignments.items():
            channel = create_channel(team)
            invite_to_channel(emails, channel)
    else:
        print 'Invalid Option'


def create_channel(name):
    res = sc.api_call('channels.create', name=name)
    return res['channel']['id'] if res['ok'] else None

def invite_to_workspace(emails, channel):
    for email in emails:
        res = sc.api_call('users.admin.invite', email=email, channel=channel)

def invite_to_channel(emails, channel):
    for email in emails:
        user = get_user_id(email)
        res = sc.api_call('channels.invite', user=user, channel=channel)

def get_user_id(email):
    res = sc.api_call('users.lookupByEmail', email=email)
    return res['user']['id'] if res['ok'] else None

if __name__== '__main__':
    main()
