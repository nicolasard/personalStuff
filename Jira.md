## Jira

### My own app to generate timeshields

I don't like bosses that push you to save workload at Jira. But I understand that it's important to track the cost of a project. 

At my last work we used TimeShields plugin to save workload. But at my actual work, where like in whatever big company Jira it's admin centraly and they don't want to install every plugin people ask. 

So because of this limitation in big companies to install plugins I started to play with Jira API to create a simple console application almost to see the workload in of a fixed list of tasks.

So the result it's this application [Ji.py](https://github.com/nicolasard/personalStuff/blob/master/Ji.py)

To run it just do

```sh
python ji.py <user> <password> <From> <To> <Jiras Tasks>
 ```
 
🚧🚧🚧🚧🚧🚧 This application it's under development 🚧🚧🚧🚧🚧🚧🚧

### Creating Jira links
I learned that sometimes in your organization you have to create jira stories with allways the same fields. It's great that you can create links to create a new story and pass those field's values as a get parameter.

For example: <TODO>
