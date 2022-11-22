# The initial

import jenkins

server = jenkins.Jenkins('http://172.16.16.20:8080', username='admin', password='admin')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

jobs = server.get_jobs()
print(jobs)
for i in jobs:
    print(i['name']," ",i['url'])
    configuration=server.get_job_config(i['name'])
    print(configuration)