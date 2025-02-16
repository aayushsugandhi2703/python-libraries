import psutil

#finding out disk partition
print(psutil.disk_partitions())

# finding out disk usage
print(psutil.disk_usage('/'))

#getting disk io statistics
print(psutil.disk_io_counters(perdisk=True))
print(psutil.disk_io_counters(perdisk=False))

# getting disk read write statistics
print(psutil.disk_io_counters())