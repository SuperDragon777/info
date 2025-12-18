import os
import platform as pf
import sys

copyright = False
show_environ = False
do_tuple = False
path_searching_modules = False

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

if do_tuple:
    print(f"Версия Python (кортеж): {pf.python_version_tuple()}")  
    
print(f"Версия Python: {pf.python_version()}")

build_number, build_date = pf.python_build()
print(f"Номер сборки Python: {build_number}")
print(f"Дата сборки Python: {build_date}")

print(f"Компилятор Python: {pf.python_compiler()}")

architecture = pf.architecture()
print(f"Разрядность: {architecture[0]}")

if architecture[1] == "ELF":
    print(f"Линковка: {architecture[1]} (Возможно Linux, Unix)")
else:
    print(f"Линковка: {architecture[1]}")

if os.name == "nt":
    win_info = pf.win32_ver()
    print(f"Издание Windows: {pf.win32_edition()}")
    print(f"Версия ОС: {win_info[0]}")
    print(f"Версия сборки: {win_info[1]}")
    print(f"Service Pack: {win_info[2]}")
    print(f"Тип системы: {win_info[3]}")

mac_version = pf.mac_ver()
if mac_version[0]:
    print(f"Издание MacOS: {mac_version}")

if sys.platform == "win32":
    print(f"Платформа: {sys.platform} (Вероятно Windows)")
else:
    print(f"Платформа: {sys.platform}")

print(f"Версия Python: {sys.version}")
print(f"Реализация Python: {sys.implementation}")
print(f"Версия API Python: {sys.api_version}")

if copyright:
    print(f"Копирайт: {sys.copyright}")

print(f"Версия Python: {sys.hexversion}")

if path_searching_modules:
    print(f"Пути поиска модулей: {sys.path}")

print(f"Все импортированные модули: {', '.join([name for name in sys.modules.keys() if not name.startswith('_') and '.' not in name])}")
print(f"Путь к интерпретатору: {sys.executable}")
print(f"Путь к директории установки Python: {sys.prefix}")
print(f"Путь к директории установки Python (без venv): {sys.base_prefix}")
print(f"Аргументы командной строки: {sys.argv}")