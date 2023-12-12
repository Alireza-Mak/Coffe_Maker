from coffe_maker_data import resources, MENU, COINS, UNITS


# TODO 1. Create a method by name of menu to show items of coffe maker
def menu():
    message = "What would you like?( "
    count = 1
    for item in MENU:
        cost = str(MENU[item]["cost"])
        message += item.title() + " " + cost
        if count != len(MENU):
            message += "$ /"
        else:
            message += "$ ): "
        count += 1
    return message


# TODO 2. Create a method by name of auto_correcting to make ready input for number or string

def auto_correcting(message, actions_list):
    user_in = input(message)
    try:
        float(user_in)
        return user_in
    except ValueError:
        while not (user_in.lower() in actions_list):
            user_in = input(f"Wrong input. {message}")
        return user_in.lower()


# TODO 3. Create a method by name of report to report the user or admin
def report():
    for key in resources:
        unit = ""
        for item in UNITS:
            if item == key:
                unit = UNITS[item]
        print(f"{key.title()}: {resources[key]}{unit}")


# TODO 5. Create a method by name of check_resources to make sure all ingredient are enough
def check_resources(coffee):
    counter = 0
    low_ingredient = ''
    for ingredient in resources:
        if ingredient in MENU[coffee]["ingredients"]:
            if resources[ingredient] < MENU[coffee]["ingredients"][ingredient]:
                counter += 1
                low_ingredient += ingredient + " and "

    if counter != 0:
        low_ingredient = low_ingredient[0:-5]
        if counter == 1:
            print(f"Sorry there is not enough {low_ingredient}.")
        else:
            print(f"Sorry there are not enough {low_ingredient}.")
        return False
    else:
        return True


# TODO 4. Create a method by name of coffe_processor to create coffe
def coffee_processor(coffe):
    turnoff_coffe_maker = check_resources(coffe)
    if turnoff_coffe_maker:
        process_coins(coffe)
    return turnoff_coffe_maker


# TODO 6. Create a method by name of process_coins to get the user money and offer change for extra money or less money
def process_coins(coffe):
    print(f'It costs {MENU[coffe]["cost"]}$, please insert coins.')
    user_money = 0
    for currency in COINS:
        currencies = input(f"How many {currency}? ")
        while not currencies.isnumeric():
            currencies = input(f"Wrong input, how many {currency}? ")
        user_money += int(currencies) * COINS[currency]
    if MENU[coffe]["cost"] > user_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        update_resources(coffe)
        remain_money = user_money - MENU[coffe]["cost"]
        print(f"Here is ${remain_money} in change.") if remain_money != 0 else None
        print(f"Here is your {coffe} ☕️. Enjoy!")
        return True


# TODO 7. Create a method by name of update_resources to calculate all ingredients and money
def update_resources(selected_coffe):
    coffe = MENU[selected_coffe]["ingredients"]
    for item in resources:
        if item in coffe:
            resources[item] = resources[item] - coffe[item]
    coffe_cost = MENU[selected_coffe]["cost"]
    resources["money"] += coffe_cost
