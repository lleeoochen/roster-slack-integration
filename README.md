# Course Slack Integration

### Setup App
- Create an app on [Slack API Apps](https://api.slack.com/apps)
	1. Give an app name and select the Slack workspace of your course.
	2. Go to **OAuth & Permissions** and scroll down to **Scopes** section.
	3. Add the following permissions:
		- admin
		- channels:write
		- users:read
		- users:read.email
	4. Save permissions. Then, scroll back up and ...
	5. Right click on **Install App to Workspace** button and **Copy the link address**.
	6. Paste link onto a new browser tab and add `&scope=admin+client` after the URL.
	7. Enter and authorize permissions.
	5. Copy **OAuth Access Token**
- Set up token environment variable:
	1. Open terminal and paste the access token to `~/.bashrc` or `~/.bash_profile`:
		`export SLACK_TOKEN=[Access Token Without the brackets]`
	2. Take bash file to effect: `source ~/.bashrc` or `source ~/.bash_profile`

### Run App
- Put roster and teams data to `roster.csv` and `teams.csv`
- Execute python script `python invite_students.py`
	- Option 1: invite all students to the workspace (from `roster.csv`)
	- Option 2: invite students to each team channel (from `teams.csv`)
