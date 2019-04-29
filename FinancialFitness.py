
#Some code borrowed from Ivaylo Spasov.
import pickle

currentBudget = 0
   
def main():
    print('Hello and welcome to your budget calculator!')
    print("Please be sure to enter your revenue first.")
    print("If you have not created a profile, please create one!")
    endProgram = 'no'
    totalBudget = currentBudget
    profile_name = ""
    profile_dict = {1:"", 2:""}
    while endProgram == 'no':
        print()
        print("Profile: " + profile_name)
        print('Menu Selections: ')
        print('1 - Create a profile: ')
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

            pickle_out = open(profile_name + ".pickle", "wb")
            pickle.dump(profile_dict, pickle_out)
            pickle_out.close()
            #pickle_out.close()
            #create_profile()
            
        elif choice == '2':
            profile_load = input("Please enter the name of the profile you would like to open:")
            profile_name = profile_load
            try:
                
                pickle_in = open(profile_load + ".pickle", "rb")
                example_dict = pickle.load(pickle_in)
                pickle_in.close()

                print(example_dict)
            
                print(example_dict[1])
                print(example_dict[2])
            except:
                print("That profile does not exist. Please create a profile with that name.")
                #return 0
            
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
            print("Profile", profile_dict)
            print("Profile name", profile_name)
            print('Saved budget balance is {0}'.format(profile_dict[2]))
            
        elif choice == '7':
            print()
            if not profile_name:
                profile_name = input("Please enter a profile name you would like to save to:")
            userChoice = input("Are you sure you want to save " + profile_name + "? This will overwrite previously saved data: Y or N")
            if userChoice.upper() == 'Y':
                pickle_out7 = open(profile_name + ".pickle", "wb")
                profile_dict[1] = profile_name
                profile_dict[2] = totalBudget
                pickle.dump(profile_dict, pickle_out7)
                pickle_out7.close()
                
                print("Budget saved:", profile_dict[2])
                
        elif choice == '8':
            print()
            endProgram = 'yes'
            print('Thank you for using Financial Fitness, Goodbye!')
            
        elif choice.isalpha():
            print('Invalid selection, please try again.')
            
        elif choice > '8':
            print("Invalid selection, please try again.")
            
def create_profile():
    profile_dict = {1:"", 2:"0"}

    profile_name = input("Please enter a profile name you would like to use:")
    profile_dict[1] = profile_name
    print(profile_dict[1])
    
    pickle_out = open("profile.pickle", "wb")
    pickle.dump(profile_dict, pickle_out)
    del pickle_out
    #if profileName == "":
        #user_profileName = input("Please create a profile name that you would like to use for your FinancialFitness profile: ")
        #profileName = user_profileName
        #print("New profile name is:", profileName)
    
def login():
    login = 'no'
    while login == 'no':
        if username != "":
            login_username = input("Please enter your username:")
            if login_username == username:
                print("Correct username entered.")
                print()
                if password != "":
                    login_password = input("Please enter your password:")
                    if login_password == password:
                        print("Correct username entered.")
                        login = 'yes'
            else:
                print("Incorrect username entered.")
            
        
            

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
