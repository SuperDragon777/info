import os
import platform as pf

if os.name == "posix":
    print(f"Имя ОС: {os.name} (Вероятно Android, Linux, macOS, BSD, Solaris)")
elif os.name == "nt":
    print(f"Имя ОС: {os.name} (Вероятно Windows)")
elif oa.name == "java":
    print(f"Имя ОС: {os.name} (Вероятно JVM)")    
else:
    print(f"Имя ОС: {os.name}")
    
print(f"Директория: {os.getcwd()}")

try:
    info = os.uname()
    print(f"Система: {info.sysname}")
    print(f"Имя узла: {info.nodename}")
    print(f"Релиз: {info.release}")
    print(f"Версия: {info.version}")
    print(f"Архитектура: {info.machine}")
except:
    pass 

if "u0_" in os.getlogin():
    print(f"Ваш юзернейм: {os.getlogin()} (Вероятно Android)")
else:
    print(f"Ваш юзернейм: {os.getlogin()}")
    
show_environ = False

if show_environ:
    environ = dict(os.environ)
    for key, value in sorted(environ.items()):
        print(f"{key} = {value}")
        
print(f"ID процесса: {os.getpid()}")
print(f"ID родительского процесса: {os.getppid()}")

try:
    print(f"ID пользователя: {os.getuid()}")
    print(f"ID группы: {os.getgid()}")  
except:
    pass    

size = os.get_terminal_size()
print(f"Размер терминала: {size.columns} на {size.lines}")

print(f"Количество ядер: {os.cpu_count()}")

print(f"Название ОС: {pf.platform()}")
print(f"Версия ОС: {pf.release()}")
print(f"Версия ОС (подробно): {pf.version()}")
print(f"Архитектура процессора: {pf.machine()}")

if pf.processor():
    print(f"Процессор: {pf.processor()}")

print(f"Имя узла: {pf.node()}")

print(f"Реализация Python: {pf.python_implementation()}")

do_tuple = False

if do_tuple:
    print(f"Версия Python (кортеж): {pf.python_version_tuple()}")  
    
print(f"Версия Python: {pf.python_version()}")
print(f"Билд Python: {pf.python_build()}")
print(f"Компилятор Python: {pf.python_compiler()}")

architecture = pf.architecture()
print(f"Разрядность: {architecture[0]}")

if architecture[1] == "ELF":
    print(f"Линковка: {architecture[1]} (Возможно Linux, Unix)")
else:
    print(f"Линковка: {architecture[1]}")

print(f"Издание Windows: {pf.win32_edition()}")
print(f"Версия Windows: {pf.win32_ver()}")

print(f"Издание MacOS: {pf.mac_ver()}")