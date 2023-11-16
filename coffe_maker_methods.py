from coffe_maker_data import resources


def auto_correcting(message, actions_list):
    user_in = input(message)
    try:
        float(user_in)
        return user_in
    except ValueError:
        while not (user_in.upper() in actions_list):
            user_in = input(f"Wrong input. {message}")
        return user_in.upper()


def report():
    for key in resources:
        print(f"{key}: {resources[key]}")


# TODO 1. Create a method by name of coffe_processor to create coffe
def coffe_processor(coffe):

# TODO 2. Create a method by name of check_resources to make sure all ingredient are enough

# TODO 3. Create a method by name of process_coins to get the user money and offer change for extra money or less money
# TODO 4. Create a method by name of check_transaction to check user insert enough money to purchase
# TODO 5. Create a method by name of make_coffe to calculate all ingredients and money