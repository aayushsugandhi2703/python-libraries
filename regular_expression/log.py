import re
log = '93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"'

#regular expression to finout ip
pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ip =re.search(pattern , log)
print(ip.group())

#regular expression to find out timestamp
pattern = r'\[(?P<timestamp>.*?)\]'
timestamp = re.search(pattern, log)
print(timestamp.group())


pattern = r'\"(?P<method>\w+)\s+(?P<url>.*?)\s+(?P<HTTP>HTTP/\d\.\d)\"'
request = re.search(pattern, log)
print(request.group('method'))
print(request.group('url'))
print(request.group('HTTP'))
print(request.groupdict())

#regular expression to find out referrer
pattern = r'\".\"'
referrer = re.search(pattern, log)
print(referrer.group())