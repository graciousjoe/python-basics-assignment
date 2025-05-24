# display the banking option
# customer choice
# amount limit
# phone number length check
# create a while loop that repeats the options until user exits


while True:
    print("")
    intro = input("Welcome to GTB USSD Services. \nSelect an option: \n\n 1. Check balance \n 2. Transfer funds \n 3. Buy airtime \n 4. Buy data \n 5. Pay bills \n 6. Exit \n")
    customer_choice =int(intro)
    
    if customer_choice == 1:
        print("Your account balance will be sent as an SMS to you shortly.")

    elif customer_choice == 2:
        amount = int(input("Enter the desired amount:"))
        if 100 <= amount <= 100000:
            account_number = input("Input recipient's account number:")
            if len(account_number) == 10:
               print("Transfer successful")
            else:
               print("Invalid account number")
        else:
            print("Transfer limit must be within 100 and 100000")

    elif customer_choice == 3:
        recharge_choice = int(input("1. recharge for self \n2. recharge  others\n"))
        if recharge_choice == 1:
            recharge_amount = int(input("Enter the desired amount:"))
            if 100 <= recharge_amount <= 100000:
                print("Recharge of", recharge_amount, "successful!")
            else:
                print("Recharge amount must be within 100 and 100000")
        elif recharge_choice == 2:
            recipient_number = str(input("Input recipient's phone number:\n"))
            amount = int(input("Enter the desired amount:"))
            if len(recipient_number) == 11 and 100 <= amount <= 100000:
                print("Recharge of", amount, "to", recipient_number, "successful!")
            else:
                print("Invalid details")
        else:
            print("Invalid choice")
       
    elif customer_choice == 4:
        data_choice = int(input("1. data for self \n2. data  others\n"))
        if data_choice == 1:
            data_bundle = int(input("\n1. 1gb for 500 \n2. 2.5gb for 1000 \n3. 5gb for 2000\n"))
            if data_bundle == 1:
                print("You have succesfully purchased 1gb for 500")
            elif data_bundle == 2:
                print("You have succesfully purchased 2.5gb for 1000")
            elif data_bundle == 3:
                print("You have succesfully purchased 5gb for 2000")
            else:
                print("Invalid choice")
        elif data_choice == 2:
            recipient_phone_number = str(input("Input recipient's phone number\n"))
            if len(recipient_phone_number) == 11:
                data_bundle = int(input("\n1. 1gb for 500 \n2. 2.5gb for 1000 \n3. 5gb for 2000\n"))
                if data_bundle == 1:
                    print("You have succesfully purchased 1gb for 500 for", recipient_phone_number, )
                elif data_bundle == 2:
                    print("You have succesfully purchased 2.5gb for 1000 for", recipient_phone_number, )
                elif data_bundle == 3:
                    print("You have succesfully purchased 5gb for 2000 for", recipient_phone_number, )
                else:
                    print("Invalid choice")
            else:
                print("Invalid phone number")
        else:
            print("Invalid choice")
          
    elif customer_choice == 5:
        bill_type = int(input("1. Electricity bills 2. TV subscriptions\n"))
        if bill_type == 1:
            amount = int(input("Input amount to be paid:\n"))
            meter_number = input("Enter meter number:\n")
            print("Electricity bill of", amount, "paid successfully for meter number", meter_number, )
        elif bill_type == 2:
            amount = int(input("Input amount to be paid"))
            IUC_number = input("Enter IUC number")
            print("TV subscription bill of", amount, "paid successfully for IUC number", IUC_number, )
        else:
            print("Invalid choice")

    elif customer_choice == 6:
        break

    else:
        print("Invalid choice")