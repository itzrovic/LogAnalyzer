class LogInfo:
    def __init__(self, ip, timestamp, status, url):
        self._ip = ip
        self._timestamp = timestamp
        self._status = status
        self._url = url

    def get_ip(self):
        return self._ip
    def get_timestamp(self):
        return self._timestamp
    def get_status(self):
        return self._status
    def get_url(self):
        return self._url

    def get_info(self):
        return "ip: " + self.get_ip() + "\ntimestamp: " + self.get_timestamp() + "\nstatus: " + self.get_status() + "\nurl: " + self.get_url()



ip1 = "172.16.31.10"
timestamp1 = 'Sep 21 2025, 03:09:26'
status1 = '202'
url1 = 'https://www.facebook.com'

lg1 = LogInfo(ip1, timestamp1, status1, url1)
print(lg1.get_info())