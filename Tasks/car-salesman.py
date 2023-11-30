def totalPrice(price):
    delivery = 1500
    vat = 23 #Percent
    registrationFee = 3 #Percent
    dealerPreparationFee = 390

    while True:
        Vat = (price * vat) / 100
        registrationFeeCalc = (price * registrationFee) / 100
        print("Do you want home delivery? ")
        options = input("Yes or No? (y/n):")
        if options == 'y':
            totalPrize = price + Vat + registrationFeeCalc + delivery + dealerPreparationFee
            print(f"Total prise : {totalPrize.__round__(2)}")
            break
        elif options == 'n':
            totalPrize = price + Vat + registrationFeeCalc + dealerPreparationFee
            print(f"Total prise: {totalPrize.__round__(2)}")
            break
        else:
            print("Wrong options , try again!!!")
            continue


while True:
    cars = int(input("Choose the cars: 1 - Audi , 2 - BMW , 3 - Mercedes, 4 - exit: "))

    if cars == 1:
        print("You have selected Audi!!!")
        carPrice = float(input("Enter basic car's price: "))
        totalPrice(carPrice)
        break

    elif cars == 2:
        print("You have selected BMW!!!")
        carPrice = float(input("Enter basic car's price: "))
        totalPrice(carPrice)
        break

    elif cars == 3:
        print("You have selected Mercedes!!!")
        carPrice = float(input("Enter basic car's price: "))
        totalPrice(carPrice)
        break

    elif cars == 4:
        print("Good bye!!")
        break

    else:
        print("Wrong options!!! Try again!!!")
        continue