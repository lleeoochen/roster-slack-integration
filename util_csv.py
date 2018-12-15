import csv

# Get a list of student emails from roster
def get_student_emails():
    email_column_name = 'email'
    email_column_index = 0
    emails = []

    with open('roster.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for index, row in enumerate(reader):
            if index == 0:
                email_column_index = find_column(row, email_column_name)
            else:
                emails.append(row[email_column_index].strip())
    return emails

# Get a mapping of team name to a list of student emails from teams.csv
def get_team_assignments():
    assignments = {}

    with open('teams.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for index, row in enumerate(reader):
            if index != 0:
                email = row[0]
                team  = row[1]
                if team not in assignments:
                    assignments[team] = []
                assignments[team].append(email)

    return assignments

# Helper: find column index from column name
def find_column(columns, name):
    for index, column in enumerate(columns):
        if column == name:
            return index;
    return 0
