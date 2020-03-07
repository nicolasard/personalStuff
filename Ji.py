##########################################################################
# Jira playground - List the workinglogs for a list of jira task.
# Nicolas Ardison - https://github.com/nicolasard
##########################################################################
import json
import urllib2
import base64
import datetime

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
table_lines[]

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
line = []
for task in tasks:
    line.append(task.key)
    for worklog in task.worklogs:
        print "Date: " + worklog.date.strftime("%m/%d/%Y")
        print "Time Spend: " + str(worklog.time_spend/3600) + " hours"
        for tittle_date in table_lines[0]:
            if tittle_date == worklog.date.strftime("%m/%d/%Y")

