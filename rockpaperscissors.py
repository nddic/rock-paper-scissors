import random

choices = ['R', 'P', 'S']

computer = random.choice(choices)

print('Welcome To The Rock Paper Scissors game')
print('To play rock, input "R". To play paper, input "P". To play scissors, input "S"')
print('How to play/win: Rock("R") smashes Scissors("S"), Scissors("S") cuts Paper("P"), and Paper("P") covers Rock("R")')

# 

while True:
    user_choice = input('What is your choice? ("R","P","S"): ')

    if user_choice == "R":
        if computer == "R":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print("\t\t It's a tie ")
            print("\t Do you want to continue playing? ")

            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == 'y':
                continue
            elif chance == "q":
                print(' GoodBye :) ')
                break
            else:
                print('  Invalid Choice-----Choose Again ')
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == 'y':
                    continue
                elif chance == "q":
                    print(' GoodBye :) ')
                    break

    if user_choice == "S":
        if computer == "S":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print("\t\t It's a tie ")
            print("\t Do you want to continue playing?  ")

            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == 'y':
                continue
            elif chance == "q":
                print(' GoodBye :) ')
                break
            else:
                print(' Invalid Choice-----Choose Again ')
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == 'y':
                    continue
                elif chance == "q":
                    print(' GoodBye :) ')
                    break

    if user_choice == "P":
        if computer == "P":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print("\t\t It's a tie ")
            print("\t Do you want to continue playing?  ")

            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == 'y':
                continue
            elif chance == "q":
                print(' GoodBye :) ')
                break
            else:
                print(' Invalid Choice-----Choose Again ')
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == 'y':
                    continue
                elif chance == "q":
                    print(' GoodBye :) ')
                    break



    if user_choice == "R":
        if computer == "S":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print(' You won!!! ')

            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == 'y':
                continue
            elif chance == "q":
                print(' GoodBye :) ')
                break
            else:
                print(' Invalid Choice-----Choose Again ')
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == 'y':
                    continue
                elif chance == "q":
                    print(' GoodBye :) ')
                    break

    if user_choice == "S":
        if computer == "P":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print(' You won!!! ')
            
            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == 'y':
                continue
            elif chance == "q":
                print(' GoodBye :) ')
                break
            else:
                print(' Invalid Choice-----Choose Again ')
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == 'y':
                    continue
                elif chance == "q":
                    print(' GoodBye :) ')
                    break

    if user_choice == "P":
        if computer == "R":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print(' You won!!! ')
            
            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == 'y':
                continue
            elif chance == "q":
                print(' GoodBye :) ')
                break
            else:
                print(' Invalid Choice-----Choose Again ')
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == 'y':
                    continue
                elif chance == "q":
                    print(' GoodBye :) ')
                    break



    if user_choice == "P":
        if computer == "S":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print(' You Lost ):  ')

            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == 'y':
                continue
            elif chance == "q":
                print(' GoodBye :) ')
                break
            else:
                print(' Invalid Choice-----Choose Again ')
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == 'y':
                    continue
                elif chance == "q":
                    print(' GoodBye :) ')
                    break

    if user_choice == "R":
        if computer == "P":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print(' You Lost ):  ')

            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == 'y':
                continue
            elif chance == "q":
                print(' GoodBye :) ')
                break
            else:
                print(' Invalid Choice-----Choose Again ')
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == 'y':
                    continue
                elif chance == "q":
                    print(' GoodBye :) ')
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == 'y':
                    continue
                elif chance == "q":
                    print(' GoodBye :) ')
                    break
                

    if user_choice == "S":
        if computer == "R":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print(' You Lost ): ')
            
            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == 'y':
                continue
            elif chance == "q":
                print(' GoodBye :) ')
                break
            else:
                print(' Invalid Choice-----Choose Again ')
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == 'y':
                    continue
                elif chance == "q":
                    print(' GoodBye :) ')
                    break
import random

choices = ["R", "P", "S"]

computer = random.choice(choices)

print("Welcome To The Rock Paper Scissors game")
print('To play rock, input "R". To play paper, input "P". To play scissors, input "S"')
print(
    'How to play/win: Rock("R") smashes Scissors("S"), Scissors("S") cuts Paper("P"), and Paper("P") covers Rock("R")'
)

#

while True:
    user_choice = input('What is your choice? ("R","P","S"): ')

    if user_choice == "R":
        if computer == "R":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print("\t\t It's a tie ")
            print("\t Do you want to continue playing? ")

            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == "y":
                continue
            elif chance == "q":
                print(" GoodBye :) ")
                break
            else:
                print("  Invalid Choice-----Choose Again ")
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == "y":
                    continue
                elif chance == "q":
                    print(" GoodBye :) ")
                    break

    if user_choice == "S":
        if computer == "S":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print("\t\t It's a tie ")
            print("\t Do you want to continue playing?  ")

            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == "y":
                continue
            elif chance == "q":
                print(" GoodBye :) ")
                break
            else:
                print(" Invalid Choice-----Choose Again ")
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == "y":
                    continue
                elif chance == "q":
                    print(" GoodBye :) ")
                    break

    if user_choice == "P":
        if computer == "P":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print("\t\t It's a tie ")
            print("\t Do you want to continue playing?  ")

            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == "y":
                continue
            elif chance == "q":
                print(" GoodBye :) ")
                break
            else:
                print(" Invalid Choice-----Choose Again ")
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == "y":
                    continue
                elif chance == "q":
                    print(" GoodBye :) ")
                    break

    if user_choice == "R":
        if computer == "S":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print(" You won!!! ")

            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == "y":
                continue
            elif chance == "q":
                print(" GoodBye :) ")
                break
            else:
                print(" Invalid Choice-----Choose Again ")
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == "y":
                    continue
                elif chance == "q":
                    print(" GoodBye :) ")
                    break

    if user_choice == "S":
        if computer == "P":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print(" You won!!! ")

            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == "y":
                continue
            elif chance == "q":
                print(" GoodBye :) ")
                break
            else:
                print(" Invalid Choice-----Choose Again ")
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == "y":
                    continue
                elif chance == "q":
                    print(" GoodBye :) ")
                    break

    if user_choice == "P":
        if computer == "R":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print(" You won!!! ")

            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == "y":
                continue
            elif chance == "q":
                print(" GoodBye :) ")
                break
            else:
                print(" Invalid Choice-----Choose Again ")
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == "y":
                    continue
                elif chance == "q":
                    print(" GoodBye :) ")
                    break

    if user_choice == "P":
        if computer == "S":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print(" You Lost ):  ")

            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == "y":
                continue
            elif chance == "q":
                print(" GoodBye :) ")
                break
            else:
                print(" Invalid Choice-----Choose Again ")
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == "y":
                    continue
                elif chance == "q":
                    print(" GoodBye :) ")
                    break

    if user_choice == "R":
        if computer == "P":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print(" You Lost ):  ")

            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == "y":
                continue
            elif chance == "q":
                print(" GoodBye :) ")
                break
            else:
                print(" Invalid Choice-----Choose Again ")
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == "y":
                    continue
                elif chance == "q":
                    print(" GoodBye :) ")
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == "y":
                    continue
                elif chance == "q":
                    print(" GoodBye :) ")
                    break

    if user_choice == "S":
        if computer == "R":
            print(f"Player[{user_choice}] : Computer[{computer}]")
            print(" You Lost ): ")

            chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
            if chance == "y":
                continue
            elif chance == "q":
                print(" GoodBye :) ")
                break
            else:
                print(" Invalid Choice-----Choose Again ")
                chance = input("\t\t Type 'y' to continue and 'q' to quit :  ")
                if chance == "y":
                    continue
                elif chance == "q":
                    print(" GoodBye :) ")
                    break
