##########################################################################
# Jira playground - List the workinglogs for a list of jira task.
# Nicolas Ardison - https://github.com/nicolasard
##########################################################################
import json
import urllib2
import base64
import datetime
import sys
import locale
locale.setlocale(locale.LC_NUMERIC, "")

jiras_tasks = ['TASK-30611','STORY-10018']

tasks=[]

class Task:
    def __init__(self):
        self.worklogs = []

class Worklog:
    def __init__(self):
        pass

for task in jiras_tasks:
    jira_url = 'https://<JIRA_URL>/rest/api/latest/issue/'+task+'?expand=names,renderedFields'

    request = urllib2.Request(jira_url)
    base64string = base64.b64encode('%s:%s' % ('<USER>', '<PASSWORD>'))
    request.add_header("Authorization", "Basic %s" % base64string)
    result = urllib2.urlopen(request)

    json_data = result.read()

    loaded_json = json.loads(json_data)

    task = Task()
    task.key = loaded_json['key']
    task.summary = loaded_json['fields']['summary']
    for worklog in loaded_json['fields']['worklog']['worklogs']: 
        worklog_obj = Worklog()
        worklog_obj.time_spend = worklog['timeSpentSeconds']
        worklog_obj.date = datetime.datetime.strptime(worklog['started'], '%Y-%m-%dT%H:%M:%S.000-0500')
        worklog_obj.author = worklog['author']['name']
        task.worklogs.append(worklog_obj)
    task.worklogs.sort(key=lambda r: r.date)
    tasks.append(task)

#### Print at console the calendar
table_lines = []

# Make the table head
start_date = datetime.date(2020,3, 3)
end_date = datetime.date(2020, 3, 7)
delta = datetime.timedelta(days=1)
line = []
line.append("")
while start_date <= end_date:
    line.append(start_date.strftime("%Y/%m/%d"))
    start_date += delta
table_lines.append(line)

# Add the table values
for task in tasks:
    line = ['']*(len(table_lines[0]))
    line[0] = task.key
    for worklog in task.worklogs:
        for i in range (0, len(table_lines[0])):
            if table_lines[0][i] == worklog.date.strftime("%Y/%m/%d"):
                line[i] = str(worklog.time_spend / 3600) + ' h'
    table_lines.append(line)

def format_num(num):
    """Format a number according to given places.
    Adds commas, etc. Will truncate floats into ints!"""

    try:
        inum = int(num)
        return locale.format("%.*f", (0, inum), True)

    except (ValueError, TypeError):
        return str(num)

def get_max_width(table, index):
    """Get the maximum width of the given column index"""
    return max([len(format_num(row[index])) for row in table])

def pprint_table(out, table):
    col_paddings = []

    for i in range(len(table[0])):
        col_paddings.append(get_max_width(table, i))

    for row in table:
        # left col
        print >> out, row[0].ljust(col_paddings[0] + 1),
        # rest of the cols
        for i in range(1, len(row)):
            col = format_num(row[i]).rjust(col_paddings[i] + 2)
            print >> out, col,
        print >> out

out = sys.stdout
pprint_table(out,table_lines)



