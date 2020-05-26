def file_to_cb(file_input):
    with open(file_input, encoding='utf8') as f:
        cook_book = {}
        for line in f:
            dish = line[:-1]
            ing_counter = f.readline().strip()
            list_of_ingridient = []
            for i in range(int(ing_counter)):
                dish_ing = dict.fromkeys(['ingredient_name', 'quantity', 'measure']) # - временный словарь с ингридиетом
                ingridient = f.readline().strip().split(' | ') # - вот так перемещаемся по файлу
                for item in ingridient:
                    dish_ing['ingredient_name'] = ingridient[0]
                    dish_ing['quantity'] = ingridient[1]
                    dish_ing['measure'] = ingridient[2]
                list_of_ingridient.append(dish_ing)
                dish_dict = {dish: list_of_ingridient}
                cook_book.update(dish_dict)
            f.readline()

    return(cook_book)

##print(file_to_cb('recipes.txt'))

def cb_switch_on():
    a = file_to_cb('recipes.txt')
    menu = []
    for key in a:
        menu.append(key)
        
    print(f'В нашем меню имеются следующие блюда:\n{menu}')
    dish_count = input(f'Количество блюд которые можно выбрать равняется {len(menu)}\n\
Напишите число от 1 до {len(menu)} сколько блюд вы выбираете -> ')

    dishes = []
    for dish in range(int(dish_count)):
        dish_input = input('Укажите какое блюдо вы хотите выбрать: ')
        dish_input_list = []
        dish_input_list.append(dish_input[:])
        dishes.append(dish_input_list.pop())

    for dish in dishes[:]:
        if dish.islower():
            dish_cap = dish.capitalize()
            dishes.remove(dish)
            dishes.append(dish_cap)

    print(f'Заказаны следующие блюда: {dishes}')
    return dishes

dishes = cb_switch_on()
person_counter = int(input('Укажите сколько на сколько персон подавать блюда: '))

def get_shop_list_by_dishes(dishes, person_counter):

    a = file_to_cb('recipes.txt')
    
    dish_order_ing = []   
    for dish in dishes:
        for key, value in a.items():
            if dish == key:
                value_copy = value.copy()
                for ing in value:
                    dish_order_ing.append(value_copy.pop())

    for ingredient in dish_order_ing:
        ingredient['quantity'] = int(ingredient['quantity'])

    ing_quantity = 0

    for ingredient in dish_order_ing:
        if dish_order_ing.count(ingredient) >  1:
            ing_quantity += ingredient['quantity']

    new_do_ing = {}

    for ingredient in dish_order_ing:
            ing_copy = ingredient.copy()
            key = ing_copy.pop('ingredient_name')
            value = ing_copy
            if key not in new_do_ing:
                new_do_ing[key] = value
            elif key in new_do_ing:
                for key1, value1 in new_do_ing.items():
                    if key1 == ingredient['ingredient_name']:
                        value1['quantity'] = ing_quantity

    for key, value in new_do_ing.items():
        if person_counter:
            value['quantity'] = value['quantity'] * int(person_counter)
            
    print(f'Для приготовления выбранных блюд на {person_counter} гостей нужно\n\
следующее количество ингредиентов:\n{new_do_ing}')

get_shop_list_by_dishes(dishes, person_counter)