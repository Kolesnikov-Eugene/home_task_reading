

with open('recipes.txt', 'r') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingredients = []
        for item in range(int(file.readline())):
            ingredient_dict = {}
            name, quantity, measure = file.readline().split('|')
            ingredient_dict['ingredient_name'] = name.strip()
            ingredient_dict['quantity'] = int(quantity.strip())
            ingredient_dict['measure'] = measure.strip()
            ingredients.append(ingredient_dict)
        cook_book[dish] = ingredients
        file.readline()

print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for item in cook_book[dish]:
            ingredients = {}
            name, measure, quantity = item['ingredient_name'],item['measure'], int(item['quantity']) * person_count
            shop_list[name] = ingredients
            if name not in shop_list:
                ingredients = {'measure': measure, 'quantity': quantity}
            else:
                ingredients['measure'] = measure
                ingredients['quantity'] = quantity + quantity

    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))


file_1 = '1.txt'
file_2 = '2.txt'
file_3 = '3.txt'
f1 = open(file_1, 'r')
f2 = open(file_2, 'r')
f3 = open(file_3, 'a')
files_dict = {}
files_list = [f1, f2]
for file in files_list:
    files_dict[file.name] = [len(file.readlines())]
    file.seek(0,0)
    files_dict[file.name].append(file.read())

sorted_dict = sorted(files_dict.items(), key=lambda x: x[1][0])
new_dict = dict(sorted_dict)

for name, content in new_dict.items():
    f3.write(f'{name}\n{str(content[0])}\n{content[1]}\n')

f1.close()
f2.close()
f3.close()












