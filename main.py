from coffe_maker_data import LIST_OF_ACTIONS
from coffe_maker_methods import auto_correcting, report, coffee_processor, menu

turn_off = False

print(f'Welcome to the coffee machine program.\nYou can turn off or report the machine by typing "off" or "report".')
while not turn_off:
    user_input = auto_correcting(menu(), LIST_OF_ACTIONS)
    # Turn off the machine
    if user_input == LIST_OF_ACTIONS[0]:
        turn_off = True
        print("Created by: Alireza Mak.")
    # Report
    elif user_input == LIST_OF_ACTIONS[4]:
        report()
    # Order coffee
    elif user_input in LIST_OF_ACTIONS:
        turn_off = not coffee_processor(user_input)





