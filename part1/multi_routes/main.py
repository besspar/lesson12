# В данном задании вам необходимо 
# создать фласк приложение, с четырьмя html-страницами.
# У Вас имеется список с 5 числовыми значениями
# Вам необходимо при переходе на страницу по адресу:
#
# 1. 127.0.0.1:5000/all/
#    отобразить все значения списка через пробел
#
# 2. 127.0.0.1:5000/max/
#    отобразить максимальное значение списка
#
# 3. 127.0.0.1:5000/min/
#    отобразить минимальное значение списка
#
# 4. 127.0.0.1:5000/avg/
#    рассчитать и отобразить среднее значение списка
#
from flask import Flask
app = Flask(__name__)# TODO инициализируйте фласк-приложение здесь

expenses = [1240, 60, 230, 20, 310]

# TODO напишите view-функции здесь
@app.route("/")
def main_page():
    return "Главная страница"

@app.route("/all/")
def all_page():
    temp = ''
    temp_full = ''
    count = len(expenses)
    for element in expenses:
        temp = str(element)
        temp_full += temp
        count -= 1
        if count > 0:
            temp_full += ' '
    return temp_full

@app.route("/max/")
def maximax():
    return str(max(expenses))

@app.route("/min/")
def minmax():
    return str(min(expenses))

@app.route("/avg/")
def avr_page():
    summary = sum(expenses)
    avr = summary/len(expenses)
    return str(int(avr))

if __name__ == "__main__":
    app.run()