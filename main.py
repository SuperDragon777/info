import os
import platform as pf
import sys
import datetime as dt

import subprocess

do_copyright = False
show_environ = False
do_tuple = False
path_searching_modules = False
sys_flags = False
datetime = False
more_python_info = False
py_modules = False
do_float = False
do_int_info = False
do_hash_info = False

if os.name == "posix":
    print(f"Имя ОС: {os.name} (Вероятно Android, Linux, macOS, BSD, Solaris)")
elif os.name == "nt":
    print(f"Имя ОС: {os.name} (Вероятно Windows)")
elif oa.name == "java":
    print(f"Имя ОС: {os.name} (Вероятно JVM)")    
else:
    print(f"Имя ОС: {os.name}")
    
print(f"\nРабочая директория (Модуль OS): {os.getcwd()}")
try:
    pwd = subprocess.run(["pwd"], capture_output=True, text=True).stdout.strip()
    print(f"Рабочая директория (Команда в sh): {pwd}")
except:
    pass    

print()

try:
    info = os.uname()
    print(f"Система: {info.sysname}")
    print(f"Имя узла: {info.nodename}")
    print(f"Релиз: {info.release}")
    print(f"Версия: {info.version}")
    print(f"Архитектура: {info.machine}\n")
except:
    pass 
    
print(f"Имя узла: {pf.node()}")
mac_version = pf.mac_ver()
if mac_version[0]:
    print(f"Издание MacOS: {mac_version}")

if sys.platform == "win32":
    print(f"Платформа: {sys.platform} (Вероятно Windows)")
elif sys.platform == "android":
    print(f"Платформа: {sys.platform} (Вероятно Android)")
elif sys.platform == "linux":
	print(f"Платформа: {sys.platform} (Вероятно Linux)")
else:
    print(f"Платформа: {sys.platform}")
    

if "u0_" in os.getlogin():
    print(f"Ваш юзернейм: {os.getlogin()} (Вероятно Android)")
else:
    print(f"Ваш юзернейм: {os.getlogin()}")

print()

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

print()

size = os.get_terminal_size()
print(f"Размер терминала: {size.columns} на {size.lines}")
print(f"Аргументы командной строки: {sys.argv}")
print()

if pf.processor():
    print(f"Процессор: {pf.processor()}")
print(f"Архитектура процессора: {pf.machine()}")
architecture = pf.architecture()
print(f"Разрядность: {architecture[0]}")
if architecture[1] == "ELF":
    print(f"Линковка: {architecture[1]} (Возможно Linux, Unix)")
elif architecture[1] == "WindowsPE":
    print(f"Линковка: {architecture[1]} (Возможно Windows)")
else:
    print(f"Линковка: {architecture[1]}")
    
print(f"Количество ядер: {os.cpu_count()}\n")

print(f"Название ОС: {pf.platform()}")
print(f"Версия ОС: {pf.release()}")
print(f"Версия ОС (подробно): {pf.version()}\n")


print(f"Реализация Python: {pf.python_implementation()}")

if do_tuple:
    print(f"Версия Python (кортеж): {pf.python_version_tuple()}")  
    
print(f"Версия Python: {pf.python_version()}")
print(f"Версия Python: {sys.hexversion}")

build_number, build_date = pf.python_build()
print(f"Номер сборки Python: {build_number}")
print(f"Дата сборки Python: {build_date}")
print(f"Компилятор Python: {pf.python_compiler()}")
if more_python_info:
    print(f"Версия Python: {sys.version}")
    print(f"Реализация Python: {sys.implementation}")
print(f"Версия API Python: {sys.api_version}")
if py_modules:
    print(f"Все импортированные модули: {', '.join([name for name in sys.modules.keys() if not name.startswith('_') and '.' not in name])}")
print(f"Путь к интерпретатору: {sys.executable}")
print(f"Путь к директории установки Python: {sys.prefix}")
print(f"Путь к директории установки Python (без venv): {sys.base_prefix}")
if path_searching_modules:
    print(f"Пути поиска модулей: {sys.path}")
if do_copyright:
    print(f"Копирайт: {sys.copyright}")    
print()

if os.name == "nt":
    win_info = pf.win32_ver()
    getwindowsversion = sys.getwindowsversion()
    print(f"Мажор: {getwindowsversion.major}")
    print(f"Минор: {getwindowsversion.minor}")
    print(f"Билд: {getwindowsversion.build}")
    print(f"Платформа: {getwindowsversion.platform}")
    print(f"WINVER: {sys.winver}")
    print(f"Издание Windows: {pf.win32_edition()}")
    print(f"Версия ОС: {win_info[0]}")
    print(f"Версия сборки: {win_info[1]}")
    print(f"Service Pack: {win_info[2]}")
    print(f"Тип системы: {win_info[3]}\n")
    

if sys_flags:
    for flag_name in dir(sys.flags):
        if not flag_name.startswith('_'):
            value = getattr(sys.flags, flag_name)
            print(f"{flag_name} = {value}")
            

if do_float:
    print(f"Максимальное значение float: {sys.float_info.max}")
    print(f"Минимальное положительное значение float: {sys.float_info.min}")
    print(f"Точность float (знаков после запятой): {sys.float_info.dig}")
    print(f"Эпсилон float (разница между 1.0 и следующим значением): {sys.float_info.epsilon}")    
    print()

if do_int_info:
    int_info = sys.int_info
    print(f"Бит на цифру: {int_info.bits_per_digit}")
    print(f"Размер цифры в байтах: {int_info.sizeof_digit}")
    print(f"Максимальное значение цифр при конвертации в строку: {int_info.default_max_str_digits}")
    print(f"Порог проверки: {int_info.str_digits_check_threshold}")
    print()

if do_hash_info:
    hash_info = sys.hash_info
    print(f"Алгоритм: {hash_info.algorithm}")
    print(f"Бит в хэше: {hash_info.width}")
    print(f"Бит хэш-значения: {hash_info.hash_bits}")
    print(f"Бит зерна: {hash_info.seed_bits}")
    print(f"Модуль: {hash_info.modulus}")
    print(f"Множитель мнимых: {hash_info.imag}")
    print(f"Хэш бесконечности: {hash_info.inf}")
    print(f"Хэш NaN: {hash_info.nan}\n")

print(f"Максимальный размер контейнеров: {sys.maxsize}")
print(f"Максимальное значение Unicode: {sys.maxunicode}\n")


thread_info = sys.thread_info
print(f"Реализация потоков: {thread_info.name}")
print(f"Тип блокировки: {thread_info.lock}")
print(f"Версия: {thread_info.version}")

print(f"Порядок байтов: {sys.byteorder}\n")

if datetime:
    print(f"Дата выполнения: {dt.date.today()}")
    print(f"Дата и время выполнения: {dt.datetime.now()}")
    print(f"День недели выполнения: {dt.date.today().weekday()}")
    print(f"Год выполнения: {dt.date.today().year}")
    print(f"Число выполнения: {dt.date.today().day}")
    print(f"Час выполнения: {dt.datetime.now().hour}")
    print(f"Минута выполнения: {dt.datetime.now().minute}")
    print(f"Секунда выполнения: {dt.datetime.now().second}")
    print(f"Микросекнуда выполнения: {dt.datetime.now().microsecond}\n")



sys.exit(67)
