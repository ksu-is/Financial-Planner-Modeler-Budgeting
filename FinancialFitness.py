
#Some code borrowed from Katie Musso.
#Some code borrowed from Tristan Endreo.
#Some code borrowed from Ammar.


currentBudget = 0
savedBudget = 0
def main():
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
    print('Hello and welcome to Financial Fitness!')
    print("Please be sure to enter your revenue first.")
    endProgram = 'no'
    totalBudget = currentBudget
    while endProgram == 'no':
        print()
        print('Menu Selections: ')
        print('1 - Add your Revenue: ')
        print('2 - Add Expenses: ')
        print('3 - Check Budget Balance: ')
        print('4 - Save Current Budget: ')
        print('5 - Exit without saving!')
        print()
        choice = int(input('Please enter your selection: '))
        if choice == 1:
            print()
            totalBudget = addRevenue(totalBudget)
        elif choice == 2:
            print()
            totalBudget = addExpense(totalBudget)
        elif choice == 3:
            print()
            print('Your balance is {0}'.format(totalBudget))
        elif choice == 4:
            print()
            userChoice = input("Are you sure you want to save? This will overwrite previously saved data: Y or N")
            if userChoice.upper() == 'Y':
                savedBudget = totalBudget
                print("Budget saved:", savedBudget)
            elif userChoice.upper() == 'N':
                print("Budget not saved.")
        elif choice == 5:
            print()
            endProgram = 'yes'
            print('Thank you for using Financial Fitness, Goodbye!')
        else:
            print('Invalid selection, please try again')



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
