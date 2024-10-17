import serial


ser = serial.Serial('COM5', 9600)

n = 0
while n >= 0:
    n = input('Введите число от 0 до 180: ')
    ser.write(bytearray(n, encoding='ascii'))
    n = int(n)

    decoded_response = ser.readline().decode('ascii')
    print("Response: ", decoded_response.strip())


ser.close()
