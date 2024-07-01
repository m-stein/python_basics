def test_console_input(execute_test):
    if not execute_test:
        return

    pizza_toppings = ['cheese', 'mushrooms', 'salami', 'peperoni', 'spinach', "ham"]
    pizza_order = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'cheese', 'salami'],
        'client': {
            'name': 'Bob Kelzo',
            'mobile number': '017926734647',
            'address': 'Pizzastreet 15, Berlin'
        }
    }
    for key, value in pizza_order.items():
        print(f"{key}: {value}")

    #
    # Console input
    #

    age = int(input('How old are you? '))
    if age == 1:
        unit = 'year'
    else:
        unit = 'years'
    print(f'You are {age} {unit} old')

    pizza_order['toppings'] = []
    while True:
        user_input = input('Add a topping to your pizza or enter "order": ')
        if user_input == 'order':
            break
        if user_input not in pizza_toppings:
            print(f'Sorry, we do not have "{user_input}" try another!')
            continue
        pizza_order['toppings'].append(user_input)

    print(f"Your order:\n{pizza_order}")