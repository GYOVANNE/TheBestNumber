from GoodNumber import GoodNumber
import os

n = GoodNumber
os.system('cls' if os.name == 'nt' else 'clear')

num = input("Please, enter a number?")

os.system('cls' if os.name == 'nt' else 'clear')

n.firstCheck(int(num))
