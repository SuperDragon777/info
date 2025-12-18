import os

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