class LogInfo:
    def __init__(self, ip, timestamp, status, url):
        self.ip = ip
        self.timestamp = timestamp
        self.status = status
        self.url = url

    def __str__(self):
        return "ip: " + self.ip + "\ntimestamp: " + self.timestamp + "\nstatus: " + self.status + "\nurl: " + self.url


ip1 = "172.16.31.10"
timestamp1 = 'Sep 21 2025, 03:09:26'
status1 = '202'
url1 = 'https://www.facebook.com'

lg1 = LogInfo(ip1, timestamp1, status1, url1)
print(lg1)