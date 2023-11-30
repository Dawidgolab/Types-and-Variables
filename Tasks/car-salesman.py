while True:
    cars = int(input("Choose the cars: 1 - Audi , 2 - BMW , 3 - Mercedes, 4 - exit: "))

    delivery = 1500
    vat = 23 #Percent
    registrationFee = 3 #Percent
    dealerPreparationFee = 390

    if cars == 1:
        print("You have selected Audi!!!")
        audiPrice = float(input("Enter basic Audi's price: "))
        audiVat = (audiPrice * vat) / 100
        audiregistrationFee = (audiPrice * registrationFee) / 100
        while True:
            print("Do you want home delivery? ")
            options = input("Yes or No? (y/n):")
            if options == 'y':
                totalPrizeAudi = audiPrice + audiVat + audiregistrationFee + delivery + dealerPreparationFee
                print(f"Total prise of Audi : {totalPrizeAudi.__round__(2)}")
                break
            elif options == 'n':
                totalPrizeAudi = audiPrice + audiVat + audiregistrationFee + dealerPreparationFee
                print(f"Total prise of Audi : {totalPrizeAudi.__round__(2)}")
                break
            else:
                print("Wrong options , try again!!!")
                continue
        break

    elif cars == 2:
        print("You have selected BMW!!!")
        bmwPrice = float(input("Enter basic BMW's price: "))
        bmwVat = (bmwPrice * vat) / 100
        bmwRegistrationFee = (bmwPrice * registrationFee) / 100
        while True:
            print("Do you want home delivery? ")
            options = input("Yes or No? (y/n):")
            if options == 'y':
                totalPrizeBmw = bmwPrice + bmwVat + bmwRegistrationFee + delivery + dealerPreparationFee
                print(f"Total prise of Bmw : {totalPrizeBmw.__round__(2)}")
                break
            elif options == 'n':
                totalPrizeBmw = bmwPrice + bmwVat + bmwRegistrationFee + dealerPreparationFee
                print(f"Total prise of BMW : {totalPrizeBmw.__round__(2)}")
                break

            else:
                print("Wrong options , try again!!!")
                continue
        break

    elif cars == 3:
        print("You have selected Mercedes!!!")
        mercedesPrice = float(input("Enter basic Mercedes's price: "))
        mercedesVat = (mercedesPrice * vat) / 100
        mercedesRegistrationFee = (mercedesPrice * registrationFee) / 100
        while True:
            print("Do you want home delivery? ")
            options = input("Yes or No? (y/n):")
            if options == 'y':
                totalPrizeMercedes = mercedesPrice + mercedesVat + mercedesRegistrationFee + delivery + dealerPreparationFee
                print(f"Total prise of Mercedes : {totalPrizeMercedes.__round__(2)}")
                break
            elif options == 'n':
                totalPrizeMercedes = mercedesPrice + mercedesVat + mercedesRegistrationFee + dealerPreparationFee
                print(f"Total prise of Mercedes : {totalPrizeMercedes.__round__(2)}")
                break
            else:
                print("Wrong options , try again!!!")
                continue
        break

    elif cars == 4:
        print("Good bye!!")
        break

    else:
        print("Wrong options!!! Try again!!!")
        continue