#Super Simple Calculator With Integers

print("   _____      _            _       _             ")
print("  / ____|    | |          | |     | |            ")
print(" | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ ")
print(" | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|")
print(" | |___| (_| | | (__| |_| | | (_| | || (_) | |   ")
print("  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   ")

print("")

print("[1] Addition")
print("[2] Subtraction")
print("[3] Multiplication")
print("[4] Divsion")

userOption = int(input("Enter an option: "))

if userOption == 1:
    print("You chose addition!\n")
    valueOne = int(input("Enter One Number: \n"))
    valueTwo = int(input("Enter Another Number: \n"))
    finalRes = valueOne + valueTwo
    print(f"Your final result is: {finalRes}")
elif userOption == 2:
    print("You chose subtraction!\n")
    valueOne = int(input("Enter One Number: \n"))
    valueTwo = int(input("Enter Another Number: \n"))
    finalRes = valueOne - valueTwo
    print(f"Your final result is: {finalRes}")
elif userOption == 3:
    print("You chose multiplication!\n")
    valueOne = int(input("Enter One Number: \n"))
    valueTwo = int(input("Enter Another Number: \n"))
    finalRes = valueOne * valueTwo
    print(f"Your final result is: {finalRes}")
elif userOption == 4:
    print("You chose division!\n")
    valueOne = int(input("Enter One Number: \n"))
    valueTwo = int(input("Enter Another Number: \n"))
    finalRes = valueOne / valueTwo
    print(f"Your final result is: {finalRes}")