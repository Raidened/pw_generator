from string import ascii_letters, digits
from random import choice

number = input("De quel longueur votre mot de passe doit-il être ? (Entrez un chiffre) : ")

generated = ''.join([choice(ascii_letters + digits) for i in range(int(number))])

print(generated)


