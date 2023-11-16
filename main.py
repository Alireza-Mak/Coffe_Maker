from coffe_maker_data import LIST_OF_ACTIONS
from coffe_maker_methods import auto_correcting, report, coffe_processor

turn_off = False


while not turn_off:
    user_input = auto_correcting("What would you like? (espresso/latte/cappuccino): ", LIST_OF_ACTIONS)
    if user_input == LIST_OF_ACTIONS[0]:
        turn_off = True
    elif user_input == LIST_OF_ACTIONS[4]:
        report()
    elif user_input in LIST_OF_ACTIONS:
        turn_off = not coffe_processor(user_input)





