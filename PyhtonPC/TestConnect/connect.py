import serial

# Открываем Serial порт
ser = serial.Serial('COM5', 9600)

# Отправляем строку "Hello, Arduino!" на Arduino, предварительно преобразовав ее в байты
# ser.write(b'Hello, Arduino!')

# Читаем ответ от Arduino через Serial порт
response = ser.readline()

# Декодируем ответ из байтов в строку с использованием UTF-8
decoded_response = response.decode('ascii')

# Закрываем порт
ser.close()
print(decoded_response)
