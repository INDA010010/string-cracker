import string, time, argparse, random
from colorama import *
from itertools import chain, product

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length", help="Length Of Randomly Generated Password", required=False)
parser.add_argument("-p", "--password", help="Password To Crack", required=False)
args = parser.parse_args()

print(Fore.YELLOW + "___________________    _____  _________  ____  __._____________________ \n\_   ___ \______   \  /  _  \ \_   ___ \|    |/ _|\_   _____/\______   \ \n/    \  \/|       _/ /  /_\  \/    \  \/|      <   |    __)_  |       _/ \n\     \___|    |   \/    |    \     \___|    |  \  |        \ |    |   \ \n \______  /____|_  /\____|__  /\______  /____|__ \/_______  / |____|_  / \n        \/       \/         \/        \/        \/        \/         \/ ")

def crack(passwd):
    results = (''.join(candidate) for candidate in chain.from_iterable(product(string.printable, repeat=i) for i in range(1, len(passwd) + 1)))
    guesses = 0
    start = time.time()
    for result in results:
        guesses += 1
        if result == passwd:
            end = time.time()
            if len(result) < 5:
                print(f"{'*'*8}\n!CRACKED!\nPassword: \"{result}\"\nGuesses: {guesses}\nTime: {round(end - start)} sec\nGusses Per Second: {round(guesses / (end - start))}\n*** NOTE: If This Is A Real Password That You, Or Someone You Know Uses. Then You Should Change It ;) ***\n{'*'*8}")
            else:
                print(f"{'*'*8}\n!CRACKED!\nPassword: \"{result}\"\nGuesses: {guesses}\nTime: {round(end - start)} sec\nGusses Per Second: {round(guesses / (end - start))}\n{'*'*8}")
            break

if args.password and not args.length:
	crack(args.password)
elif args.length and not args.password:
	crack(''.join(random.choice(string.printable) for i in range(int(args.length))))
elif not args.length and not args.password:
	passwd = input("Enter Password To Bruteforce: ")
	crack(passwd)
else:
	print("Please Don't Use Both '-p' And '-l' At Once.")
