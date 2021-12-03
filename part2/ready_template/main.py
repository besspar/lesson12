# У вас есть подготовленный шаблон. 
# Передайте в него переменные "username" , "phone", "location"

from flask import Flask, render_template
app = Flask(__name__)


variables = {
    "username": "Skypro",
    "phone": "+7 777 77 77",
    "location": "Москва"
}


@app.route('/sign-in/')
def sign_in():
    username = "NAME"
    phone = "phone"
    location = "location"
    # TODO напишите view-функцию здесь
    return render_template('/ready_template/templates/index.html', username=variables.username, phone=variables.phone, location=variables.location)


if __name__ == "__main__":
    app.run()
