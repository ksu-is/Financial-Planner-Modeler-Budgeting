
#Some code borrowed from Katie Musso.
#Some code borrowed from Tristan Endreo.
#Some code borrowed from Ammar.

import pickle

currentBudget = 0

def main():
    create_login()
    print('Hello and welcome to Financial Fitness!')
    print("Please be sure to enter your revenue first.")
    print("If you have not created a profile, please create one!")
    endProgram = 'no'
    totalBudget = currentBudget
    while endProgram == 'no':
        print()
        print('Menu Selections: ')
        print('1 - Create a profile (This will overwrite your previous profile name): ')
        print('2 - Open your profile: ')
        print('3 - Add your Revenue: ')
        print('4 - Add Expenses: ')
        print('5 - Check Budget Balance: ')
        print('6 - Display Saved Budget Balance: ')
        print('7 - Save Current Budget: ')
        print('8 - Exit Financial Fitness!')
        print()
        choice = input('Please enter your selection: ')
        if choice == '1':
            print()
            
            profile_dict = {1:"", 2:""}
            profile_name = input("Please enter a profile name you would like to use:")
            profile_dict[1] = profile_name
            print(profile_dict[1])

            pickle_out = open("profile.pickle", "wb")
            pickle.dump(profile_dict, pickle_out)
            #pickle_out.close()
            #create_profile()

        elif choice == '2':
            pickle_in = open("profile.pickle", "rb")
            example_dict = pickle.load(pickle_in)
            
            print(example_dict[1], example_dict[2])
            #example_dict = pickle.load(pickle_in)
            
        elif choice == '3':
            print()
            totalBudget = addRevenue(totalBudget)
    
        elif choice == '4':
            print()
            totalBudget = addExpense(totalBudget)
            
        elif choice == '5':
            print()
            print('Your balance is {0}'.format(totalBudget))
        elif choice == '6':
            print()
            print('Saved budget balance is {0}'.format(profile_dict[2]))
            
        elif choice == '7':
            print()
            userChoice = input("Are you sure you want to save? This will overwrite previously saved data: Y or N")
            if userChoice.upper() == 'Y':
                profile_dict[2] = totalBudget
                print("Budget saved:", profile_dict[2])
                
        elif choice == '8':
            print()
            endProgram = 'yes'
            pickle_out.close()
            print('Thank you for using Financial Fitness, Goodbye!')
            
        elif choice.isalpha():
            print('Invalid selection, please try again.')
            
        elif choice > '8':
            print("Invalid selection, please try again.")

def create_login():
    username = ""
    password = ""
    if username == "":
        user_username = input("Please create a username that you would like to use to log into FinancialFitness:")
        username = user_username
        print("New username is:", username)
    if password == "":
        user_password = input("Please create a password that you would like to use to log into FinancialFitness:")
        password = user_password
        print("New password is:", password)
  
def addExpense(totalBudget):
    expense = float(input('Enter your expense amount: $'))
    timesPerMonth = int(input('How many times per month: '))
    totalExpense = expense * timesPerMonth
    if totalBudget - totalExpense >= 0:
        totalBudget = totalBudget - totalExpense
        print ('The expenses were accepted, your remaining budget is: ${0}'.format(totalBudget))
        return totalBudget
    else:
        print ('The expenses were rejected because the budget exceeded.')
        return totalBudget


def addRevenue(totalBudget):
    revenue = float(input('Enter new monthly income: $'))
    totalBudget = totalBudget + revenue
    print()
    print('Your new budget is: ${0}'.format(totalBudget))
    print()
    return totalBudget

main()
