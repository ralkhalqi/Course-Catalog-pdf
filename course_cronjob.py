from crontab import CronTab
from datetime import datetime
import os

# Perform cronjob
cron = CronTab(user=True)
cwd = os.getcwd()
job = cron.new(command='python3' + cwd + '/document_transfer.py' )
job.day.every(1)
cron.write()

# Log the last time job was done. 
output = open('access.txt', 'w') 
output.write('\nCourse Catalog last downloaded on ' + str(datetime.now()))
output.close()