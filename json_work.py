# Вспомним формат json.

# 1. Дан словарь Python:

cities = {
    "Gotham": {
        "pos": [12.16, 30.14],
        "size": 12080040
    },
    "Smallville": {
        "pos": [32.02, 40.63],
        "size": 28003000
    }
}

# Написать функцию, которая без использования
# стандартного или стороннего модуля json
# запишет входной словарь такого формата
# в файл формата json в таком виде:

# cities.json
{
    "Gotham": {
        "pos": [12.16, 30.14],
        "size": 12080040
    },
    "Smallville": {
        "pos": [32.02, 40.63],
        "size": 28003000
    }
}



def json(cities):

	json = str(cities).replace('\'','"')

	json = json.replace('{', '{\n    ')

	json = json.replace('}}', '\n    }\n}')

	json = json.replace('}, "', '},\n    "')

	json = json.replace(', "',',\n    "')

	json = json.replace('"pos"','    "pos"')

	json = json.replace('"size"','    "size"')

	json = json.replace('},', '\n    },') 
	
	return json



string = json(cities)

print(string)

with open ('cities.json', 'w') as file:
	file.write(string)
# 2. Создадим свою замену классам,
# использванным в этом словаре (словарь, строка, список, числа..).
#
# Тогда задание такого словаря будет выглядеть следующим
# образом:
#
# cities = Cities(
#     City(name="Gotham", pos=Point(12.16, 30.14), size=Size(12080040)),
#     City(name="Smallville", pos=Point(32.02, 40.63), size=Size(28003000)),
# )
#
# Напишите эти классы.
