def read_recipes(file_name):
    cook_book = {}

    with open('cook_book.txt', encoding='UTF-8') as file:
        while True:
            dish_name = file.readline().strip()

            if not dish_name:
               break

            ingredient_count = int(file.readline().strip())

            ingredients = []



            for _ in range(ingredient_count):
                ingredient_info = file.readline().strip().split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                ingredients.append(ingredient)

            cook_book[dish_name] = ingredients

    return cook_book


file_name = 'cook_book.txt'
cook_book = read_recipes(file_name)
list_cook_book = list(cook_book)
def get_shop_list_by_dishes(dishes, person_count):
    dict_cook = {}
    for cook in dishes:
        for ingredient in cook_book[cook]:
            name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            dict_cook[name] = {'measure': measure, 'quantity': quantity}
    return dict_cook




print(get_shop_list_by_dishes(list_cook_book, 2))