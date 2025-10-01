import re
from collections import Counter
import LogInfo

ipList = []
dateTimeList = []
httpStatusP = ' [1-5][0-9][0-9] ' # pattern for finding http statuscode
statusList = []

with open('generated_log.log') as file:
    for line in file:
        ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line) # finds pattern with 3 numbers between dots
        # ipList.append(ip.group())
        dateTime = re.findall(r'\[(.*?)]', line) # finds content between [] columns
        # dateTimeList.append(dateTime)
        status = re.findall(httpStatusP, line)
        # statusList.append(status)
        url = re.findall(httpStatusP, line)
        print(url)

print(dateTimeList)
print(statusList)
print(len(statusList))

ipCount = dict(Counter(ipList))
if {k:v for (k,v) in dict.items(ipCount) if v > 1}:
    print(ipCount)
else:
    print('no redundant ip found')
