locations = [
    "Москва",
    "Санкт-Петербург",
    "Новосибирск",
    "Екатеринбург",
    "Казань",
    "Нижний Новгород",
    "Челябинск",
    "Самара",
    "Омск",
    "Ростов-на-Дону",
    "Уфа",
    "Красноярск",
    "Воронеж",
    "Пермь",
    "Волгоград",
    "Краснодар",
    "Волгоград",
    "Саратов",
    "Тюмень",
    "Тольятти",
    "Ижевск",
]

search = input("Here:")

templ = []
search_for = ""

for item in locations:
    if item.lower().startswith(search.lower()):
        print(item)
        templ.append(item)

search_for = ", ".join(templ)

print(search_for)
print(type(search_for))