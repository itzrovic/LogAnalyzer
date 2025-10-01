import re
from collections import Counter

with open('generated_log.log') as file:
    for line in file:
        res = re.search(r"\[(.*?)]", line)
        print(res)

s = "Welcome [GFG] to [Python]"

# Extract all substrings inside brackets
res = re.findall(r"\[(.*?)\]", s)
print(res)

httpStatusP = '/^[1-5][0-9][0-9]$/'


{"ip": self.ip, "timestamp": self.timestamp, "status": self.status, "url": self.url}


def __str__(self):
    return "ip: " + self.ip + "\ntimestamp: " + self.timestamp + "\nstatus: " + self.status + "\nurl: " + self.url
