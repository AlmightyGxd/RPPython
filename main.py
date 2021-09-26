choice = input("Rifle or Shotgun? ")
if choice == "Rifle":
    choice2 = input("Input Type (Ex. AR, M4)")
    print(f'/me Unslings{choice2} turning safety [OFF]')
elif choice == "Shotgun":
    choice3 = input("Input Shotgun")
    print(f'/me Unslings{choice3} pumping one into the chamber')
else:
    print("Invalid input")