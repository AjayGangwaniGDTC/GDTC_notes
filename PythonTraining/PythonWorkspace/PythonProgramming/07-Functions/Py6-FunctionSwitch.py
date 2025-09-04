from sympy.strategies.core import switch


def say_hello():
    return 'Hello!'

def say_goodbye():
    return 'Goodbye!'

def say_thank_you():
    return 'Thank You!'

def default_messsage():
    return 'Invalid Choice'

choice = int(input('Select an option(1: Hello, 2: Goodbye, 3: ThankYou): '))
match choice:
    case 1:
        print(say_hello())
    case 2:
        print(say_goodbye())
    case 3:
        print(say_thank_you())
    case default:
        print(default_messsage())