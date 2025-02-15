import psutil
from datetime import datetime

# getting process information
process=psutil.process_iter(['pid', 'name', 'username'])
for i in process:
    print(i.info)

process = psutil.Process(30588)  # Process with PID 1
print(process.name())  # Process name
print(process.status())  # Process status
print(process.cpu_percent(interval=1))  # CPU usage of process
print(process.memory_info())  # Memory usage

# getting system information boot time
print(psutil.boot_time())  # Boot time
boot_time = psutil.boot_time()
print(datetime.fromtimestamp(boot_time))
print(psutil.users())


# getting network information
print(psutil.net_if_addrs())
print(psutil.net_if_stats())

