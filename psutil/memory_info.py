import psutil

#getting RAM information    
print(psutil.virtual_memory())

#getting swap memory information
swap = psutil.swap_memory()
print(psutil.swap_memory())
print(swap.total)
print(swap.percent)
print(swap.sin)