from colorama import Fore, Style

def e(msg):
    print(Fore.RED, f'========== {msg} ==========', Style.RESET_ALL)

def w(msg):
    print(Fore.YELLOW, f'========== {msg} ==========', Style.RESET_ALL)

def s(msg):
    print(Fore.GREEN, f'========== {msg} ==========', Style.RESET_ALL)