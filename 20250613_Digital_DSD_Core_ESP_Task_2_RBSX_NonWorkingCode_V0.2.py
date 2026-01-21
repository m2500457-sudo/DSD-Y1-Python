
#collects and validates the Client's first name.
def get_client_first_name():
    while True:
        name = input('Please enter the clients first name: ')
        if name.isalpha() and name != "":
            print("Client first name accepted.")
            return name
        else:
            print("Please enter your name only using letters.")

#collects and validates the Client's last name.
def get_clients_last_name():
    while True:
        last_name = input("Please enter the clients last name:")
        if last_name.isalpha() and last_name != "":
            print("Client last name accepted.")
            return last_name
        else:
            print("Please enter your name only using letters.")

#collects and validates the Client_ID number.
def get_check_client_ID ():
    while True:
        clientID = input('Please enter the Client ID number: ')
        if len(clientID) == 10 :
            print('Client ID accepted')
            return clientID
        else:
            print('Client ID must be 10 characters long')
           
#collects and validates the investment amount.  ------------------------------------------------------------------------------------------------------------------------
def get_check_investment_amount ():
    while True:
        amount = float(input('Please enter the amount to be invested per year: £ '))
        if amount == float and "." in amount:
            print("Amount accepted.")
            return amount 
        else:
            print("Please enter the amount using the format 00.00")

#collects and checks types of investment.
def investment_type (investmentAmount):

    valid = False

    while valid == False:
        print('Please choose an investment type:')
        print('1. Savings plan')
        print('2. Managed stock investments')
        choice = input('Enter choice here: ')

        if choice == "1" and investmentAmount >= 20000:
            print('The amount you wish to invest is too high for the standard savings plan.')
            print('You will be shown an example for managed stock investments instead')   
            choice = 2
            return choice
        else:
            return choice
        
#add each year's investment and calculates the returns, fees and profits for the savings plan option.
def savings_plan (investmentAmount):
    maximumValue = 0
    minimumValue = 0
    feesMax = 0
    feesMin = 0

    for i in range (1,5):

        maximumValue = maximumValue + investmentAmount
        maximumValue = maximumValue + (maximumValue * 0.24)
        maximumValue = round(maximumValue, 2)


        minimumValue = minimumValue + investmentAmount
        minimumValue = minimumValue + (minimumValue * 0.12)
        minimumValue = round(minimumValue, 2)


        feesMax = feesMax + (maximumValue * 0.025)
        feesMax = round(feesMax, 2)

        feesMin = feesMin + (minimumValue * 0.025)
        feesMin = round(feesMin, 2) 

    maxProfit = maximumValue - ((investmentAmount * 5) + feesMax)
    minProfit = minimumValue - ((investmentAmount * 5) + feesMin)

    print('****************************************')
    print('********* Savings plan summary *********')
    print('Initial Investment: £ {}'.format(investmentAmount))
    print('')
    print('If the savings plan performs at the highest rate after 5 years you can expect:')
    print('Value of investment: £ {:.2f}'.format(maximumValue))
    print('Fees paid: £ {:.2f}'.format(feesMax))
    print('Profit made: £ {:.2f}'.format(maxProfit))
    print('')
    print('If the savings plan performs at the lowest rate after 5 years you can expect:')
    print('Value of investment: £ {:.2f}'.format(minimumValue))
    print('Fees paid: £ {:.2f}'.format(feesMin))
    print('Profit made: £ {:.2f}'.format(minProfit))

#calculates the returns, fees and profits for the managed stocks investment plan option.
def managed_stocks (investmentAmount):
    maximumValue = 0
    minimumValue = 0
    feesMax = 0
    feesMin = 0

    for i in range (0,5):

        maximumValue = maximumValue + investmentAmount
        maximumValue = maximumValue + (maximumValue * 0.23)
        maximumValue = round(maximumValue, 2)


        minimumValue = minimumValue + investmentAmount
        minimumValue = minimumValue + (minimumValue * 0.40)
        minimumValue = round(minimumValue, 2)


        feesMax = feesMax + (maximumValue * 0.013)
        feesMax = round(feesMax, 2)

        feesMin = feesMin + (minimumValue * 0.013) 
        feesMin = round(feesMin, 2)

    maxProfit = maximumValue - ((investmentAmount * 5) + feesMax)
    maxProfit = round(maxProfit, 2)
    minProfit = minimumValue - ((investmentAmount * 5) + feesMin)
    minProfit = round(minProfit, 2)

    print('****************************************')
    print('** Managed Stocks Investment Summary ***')
    print('Initial Investment: £ {}'.format(investmentAmount))
    print('')
    print('If the managed stocks plan performs at the highest rate after 5 years you can expect:')
    print('Value of investment: £ {}'.format(maximumValue))
    print('Fees paid: £ {}'.format(feesMax))
    print('Profit made: £ {}'.format(maxProfit))
    print('')
    print('If the managed stocks plan performs at the lowest rate after 5 years you can expect:')
    print('Value of investment: £ {}'.format(minimumValue))
    print('Fees paid: £ {}'.format(feesMin))
    print('Profit made: £ {}'.format(minProfit))


def main ():
    name = get_client_first_name()
    last_name = get_clients_last_name()
    clientID = get_check_client_ID()
    investmentAmount = get_check_investment_amount() 
    investmentTypeChoice = investment_type (investmentAmount)
    print('********** Investment summary **********')
    print('Client name:', name)
    print('Client ID:', clientID)
    if investmentTypeChoice == "1":
        savings_plan(investmentAmount)
    else:
        managed_stocks(investmentAmount)

main()

