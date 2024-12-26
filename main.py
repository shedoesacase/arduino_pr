from flask import Flask, jsonify, render_template
import serial, serial.tools.list_ports



#Поиск порта, связанного с ардуино
list_ports = list(serial.tools.list_ports.comports())
ports = []
ser_port = None
print('Список доступных устройств:')


for current_port in list_ports:
    print(current_port.device)
    print(current_port.description)
    print(current_port.manufacturer)
    ports.append((current_port.device, current_port.description, current_port.manufacturer))


for current_port in ports:
    if 'Arduino' in current_port[1]:
        ser_port = current_port[0]


#Проверка на доступность порта
if ser_port is None:
    print('Отсутствуют порты Arduino')
else:
    print(f'Выбран порт {ser_port}')
    try:
        ser = serial.Serial(ser_port, 9600)
    except serial.serialutil.SerialException:
        print('Выбранный порт занят другой программой')
    else:
        print('Всё хорошо')


#Считывание данных с ардуино
def get_a():
    data = ser.readline().decode("UTF-8").strip().split()
    if len(data)<2:
        return ["0","0"]
    return data


#Создание приложения фласк
app = Flask(__name__)


#Создание главной страницы
@app.route('/')
def index():
    return render_template('index.html')

#получение данных
@app.route('/data', methods=['POST'])
def get_data():
    data = get_a()
    response_data = {
        "LM75A": data[0],
        "DHT22": data[1]
    }
    return jsonify(response_data)

#Запуск сервера
if __name__ == '__main__':
    app.run()
