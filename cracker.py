import string, random, argparse, threading, time
from colorama import Fore, Style
chars = string.ascii_letters + string.digits
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length", help="Length Of Randomly Generated Password", required=False)
parser.add_argument("-p", "--password", help="Password To Crack", required=False)
args = parser.parse_args()
print(Fore.YELLOW + "___________________    _____  _________  ____  __._____________________ \n\_   ___ \______   \  /  _  \ \_   ___ \|    |/ _|\_   _____/\______   \ \n/    \  \/|       _/ /  /_\  \/    \  \/|      <   |    __)_  |       _/ \n\     \___|    |   \/    |    \     \___|    |  \  |        \ |    |   \ \n \______  /____|_  /\____|__  /\______  /____|__ \/_______  / |____|_  / \n        \/       \/         \/        \/        \/        \/         \/ ")
def thread():
    start = time.time()
    guess = ""
    guesses = 0
    combi = len(chars)**len(pwd)
    print(Fore.YELLOW + f"Possible Combinations: {combi}\nStarts Cracking..." + Style.RESET_ALL)
    while guess != pwd:
        guess = "".join(random.choice(chars) for i in range(len(pwd)))
        guesses += 1
    print(Fore.GREEN + f"Cracking Done\nPassword Was \"{guess}\"\nAmount Of Guesses: {guesses}\nTime: {time.time() - start} sec")
try:
    if args.password:
        pwd = args.password
        threading.Thread(target=thread).start()
    if args.length:
        length = int(args.length)
        pwd = "".join(random.choice(chars) for i in range(length))
        threading.Thread(target=thread).start()
except:
    length = int(input(Fore.YELLOW + "Enter Password Length: " + Style.RESET_ALL))
    threading.Thread(target=thread).start()
