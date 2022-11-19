import random
import string

print("Made by hellonearth311")
print("This will not check the codes, only generate them.")
run = True
while run:
    number_of_codes = int(input("How many codes do you want? "))
    use_for = string.ascii_letters + string.digits

    for i in range(1, number_of_codes + 1):
        code = []
        for i in range(1, 20):
            charToAdd = random.choice(use_for)
            code.append(charToAdd)
        code = "".join(code)
        print(code)
    generateMoreCodes = input("Want to generate more codes? (Y/N) ").upper
    if generateMoreCodes == "Y":
        run = True
    else:
        run = False
