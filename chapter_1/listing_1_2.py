import os
import threading
print(f"Исполняется Python-процесс с идентификатором: {os.getgid()}")

total_treads = threading.active_count()
thread_name = threading.current_thread().name

print(f"В данный момент Python исполняет {total_treads} поток(ов)")
print(f"Имя текущего потока {thread_name}")

# Исполняется Python-процесс с идентификатором: 1000
# В данный момент Python исполняет 1 поток(ов)
# Имя текущего потока MainThread
