import psutil

# number of CPU either Physical or Logical
print(psutil.cpu_count(logical=True))
print(psutil.cpu_count(logical=False))

# CPU frequency
print(psutil.cpu_freq())

#cpu usage per CPu or total
print(psutil.cpu_percent(interval=1, percpu=True))
print(psutil.cpu_percent(interval=1, percpu=False))

# getting CPu Stats
print(psutil.cpu_stats())

#getting CPU load average
print(psutil.getloadavg())

# getting CPU times
print(psutil.cpu_times(percpu=True))
print(psutil.cpu_times(percpu=False))

