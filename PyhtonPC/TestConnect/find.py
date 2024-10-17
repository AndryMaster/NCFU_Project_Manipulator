import serial.tools.list_ports

# Получаем список доступных Serial портов
ports = list(serial.tools.list_ports.comports())

# Выводим информацию о каждом порте
for port in ports:
    print(f"Порт: {port.device}")
    print(f"Описание: {port.description}")
    print(f"Производитель: {port.manufacturer}\n")
