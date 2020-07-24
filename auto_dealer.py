class Car:

    """
    Car Class takes in the make and year of vehicles and creates an inventory list
    make: This will provide the list of cars the dealer carries
    year: The dealer carries car of each make from year 2005 to 2018

    """

    ## Defining the make of the car the dealer carries in his inventory
    make = [
            "bmw", "mercedes", "nissan", "toyota",
            "honda", "volkswagen", "ford"
            ]
    ## Defining the car year the dealer carries in his inventory
    year = [
            2005, 2006, 2007,
            2008, 2009, 2010,
            2011, 2012, 2013,
            2014, 2015, 2016,
            2017, 2018
            ]

    def __init__(self, make, year):
        """ initializing the class car"""
        self.make = make
        self.year = year
        ## declaring variable position for next function
        self.position = 0

    def get_make(self):
        """ returns make of the car"""
        return self.make

    def get_year(self):
        """ returns year of the car"""
        return self.year

    def __iter__(self):
        """ getting an iterator for year using iter function"""
        return self.year

    def __next__(self):
        """ iterating through year using next function"""
        ## position was declared in the init class
        ## if the index of position is less than the length of list year - stop iteration
        if self.position >= len(self.year):
            raise StopIteration
        ## else return index and increment position
        n = self.year[self.position]
        self.position += 1
        return n

    def __str__(self):
        """ returns make and year of each car in a list format"""
        return [make, year]

    def __repr__(self):
        """ returns make and year of each car in a list format"""
        return [make, year]

#######################################################################################
#######################################################################################
        
class PriceCalculator:

    """
    PriceCalculator class calculates the sale price of each car.
    We have the base price specified for each model.
    The price decreases based on the age and mileage on the car.
    This class takes in the budget and mileage input from the user and make and year from class Car

    """

    ## declaring class variabe that will include the cars that satisfies the criteria provided by the user
    vehicle_selection = []

    def __init__(self, budget, mileage = 0, make = Car.make, year = Car.year):
        """ initializing the PriceSelection"""
        self.make = make
        self.year = year
        self.mileage = mileage
        self.budget = budget
        ## declaring variable position for next function
        self.position = 0
        ## declaring inventory to capture the stock of the dealer
        self.inventory = []

    def get_inventory(self):
        """ Calculate the stock the dealer. Each car will be unique in its make and year"""
        ## create a list of inventory for every car
        [self.inventory.append([m,y]) for y in Car.year for m in make]
        return self.inventory

    def __len__(self):
        """ function to calculate the length of list of inventory"""
        return len(self.inventory)

    def sale_price(self):
        """ calulate the sales price for each car in stock
            The sale price applies the year and mileage adjustment to the base price
        """
        ## This dictonary consists the base price for each make
        ## key: make
        ## value: base price
        base_price = {
                "bmw": 50000, "mercedes": 60000, "nissan": 40000, "toyota": 25000,
                "honda": 22000, "volkswagen": 20000, "ford": 15000
                }
        ## for each vehicle in inventory,calulate the sales price using the formula
        for vehicle in self.get_inventory():
            sale_price = (base_price[vehicle[0]]
                        * (1-self.year_discount(vehicle[1]))
                        * (1+self.mileage_discount(self.mileage)))
            
            ## Add the vehicle to the selection list only if the sale price is less than budget
            lower = int(self.budget * 0.85)
            upper = self.budget + 1
            if sale_price in range(lower, upper):
                self.vehicle_selection.append([vehicle[0], vehicle[1], int(sale_price)])
        
        ## return the vehicles out of which the customer can select the car he likes
        return self.vehicle_selection

    def __iter__(self):
        """ getting an iterator for year using iter function"""
        return self.year

    def __next__(self):
        """ iterating through year using next function"""
        ## position was declared in the init class
        ## if the index of position is less than the length of list year - stop iteration
        if self.position >= len(self.year):
            raise StopIteration
        ## else return index and increment position
        n = self.year[self.position]
        self.position += 1
        return n

    def year_discount(self,year):
        """ calculates the age discount to be applied to base price"""
        ## Declaring current year
        current_year = datetime.now().year
        ## calculate the age of the car
        year_adjustment = (current_year - year)
        ## return the discount that needs to be applied
        return (year_adjustment*2/100)

    def mileage_discount(self,mileage):
        """ calculates the mileage discount to be applied to base price """
        ## return the mileage adjustment based on the range of miles
        if self.mileage == 0:
            return 1
        elif self.mileage in range(1,10001):
            return -0.1
        elif self.mileage in range(10001,20001):
            return -0.2
        elif self.mileage in range(20001,30001):
            return -0.3
        elif self.mileage in range(30001,40001):
            return -0.4
        elif self.mileage in range(40001,50001):
            return -0.5
        elif self.mileage in range(50001,60001):
            return -0.6
        elif self.mileage in range(60001,70001):
            return -0.7
        elif self.mileage in range(70001,80001):
            return -0.8
        elif self.mileage in range(80001,90001):
            return -0.9
        elif self.mileage in range(90001,100001):
            return -0.11
        elif self.mileage in range(100001,110001):
            return -0.12
        elif self.mileage in range(110001,120001):
            return -0.13
        else:
            return -0.14

    def __str__(self):
        """ returns the vehicle selection upon request """
        ## if dealer does not have any vehicles that satisfies the customer criteria
        ## return appropriate message
        if len(self.vehicle_selection) == 0:
            print("No cars match your criteria")
        ## else return the selection criteria
        else:
            return self.vehicle_selection

#######################################################################################
#######################################################################################


class Autoloan:
    
    """
    This class calculates the rate of interest and the monthly payment amount for the auto loan
    input variables:
        - income, credit score, down payment, term and loan amount
    Calulations:
        - rate of interest and monthly payment over the loan term
    """
    
    ## declare the base rate of the auto finance
    base_rate = 4.5

    def __init__(self, income, credit_score, down_payment, term, asset_amount):
        """ initialize the auto loan object """
        self.income = int(income)
        self.credit_score = int(credit_score)
        self.down_payment = int(down_payment)
        ## multiple the term by 12 to get a monthly rate
        self.term = int(term) * 12
        self.asset_amount = int(asset_amount)

    def total_payment(self):
        """ Returns the loan amount of the customer """
        total_owed = self.asset_amount - self.down_payment
        return total_owed

    def down_payment_adjustment(self):
        """ returns the rate adjustment for the down payment. Higher the down payment, higher is the discount"""
        ## if down payment is 0, no adjusment to base rate
        if self.down_payment == 0:
            return 0
        ## adjustment rate is calculated based on the down payment to asset amount ratio
        elif self.down_payment/self.asset_amount > 0 and self.down_payment/self.asset_amount <= 0.1:
            return -0.1
        elif self.down_payment/self.asset_amount > 0.1 and self.down_payment/self.asset_amount <= 0.2:
            return -0.2
        else:
            return -0.3

    def income_adjustment(self):
        """ returns the rate adjustment for buyer's income. Lower the loan to income ratio, higher is the discount """
        ## calculate the loan to income ratio
        loan_to_income = self.total_payment()/self.income
        ## adjustments based on loan to income ratio
        if  loan_to_income > 1:
            return 0
        elif loan_to_income > 0.8:
            return 0.01
        elif loan_to_income > 0.4:
            return 0.03
        elif loan_to_income > 0.2:
            return 0.05
        else:
            return 0.07

    def credit_score_adjustment(self):
        """ returns the rate adjustment for credit core. Lower the credit score, risk is added to the rate """
        ## No risk added for good scores 
        if self.credit_score >= 700:
            return 0
        ## risk adjustment is the score is below acceptable
        elif self.credit_score in range (650, 700):
            return 0.2
        elif self.credit_score in range (600, 650):
            return 0.3
        elif self.credit_score in range (500, 600):
            return 0.5
        elif self.credit_score < 500:
            return 0.7

    def interest_rate(self):
        """ interest rate calculation.
            Base rate + Adjustments
        """
        ## formula for rate calulation
        rate = (Autoloan.base_rate
                + self.down_payment_adjustment()
                + self.income_adjustment()
                + self.credit_score_adjustment())
        return round(rate,2)

    def monthly_payment(self):
        """ Calculate the monthly payment based on the loan amount, term and rate """
        ## Break down the formula and then calculate the monthly payment
        numerator = ((self.interest_rate()/1200)
                    * self.total_payment())
        
        denominator = (1 
                       - ((1 
                           + (self.interest_rate()/1200))
                           **(-self.term)))
        
        monthly_payment = (numerator / denominator)
        return "{:.2f}".format(monthly_payment)
    
#######################################################################################
#######################################################################################

class ErrorValidation:
    
    """ Error Validation for input variables"""
   
    def __init__(self):
        pass
        self.error_flag = True
    
    def reset_flag():
        ErrorValidation.error_flag = True
    
    def not_number(self):
        if type(self) != float or type(self) != int:
            print("Input should be a number")
        else:
            ErrorValidation.error_flag = False

    def is_positive_int(self):
        if int(self) <= 0:
            print("Input should be a positive number")
        else:
            ErrorValidation.error_flag = False
           
    def is_negative(self):
        if int(self) < 0:
            print("Input is a negative number")
        else:
            ErrorValidation.error_flag = False
            
    def is_zero(self):
        if int(self) == 0:
            print("Input should not be equal to zero")
        else:
            ErrorValidation.error_flag = False
                       
    def valid_credit_score(self):
        if int(self) < 0 or int(self) > 850:
            print("Credit score should be between 0 and 850")
        else:
            ErrorValidation.error_flag = False
            
    def valid_mileage(self):
        if int(self) < 0 or int(self) > 120000:
            print("Sorry, we only carry cars with mileage between 0 and 120000")        
        else:
            ErrorValidation.error_flag = False
    
#######################################################################################
#######################################################################################


print("Welcome to our store!")
print("We simplify purchasing cars. We ask you for your requirements and match it to cars in our store.")
print("We can also help you with autoloan. Each online auto loan approval is 100% personalized to you.\n")
print("="*70)
print("Let's get started with some information.")

## Car and Year inventory for error checks
make = Car.make
year = [
        2005, 2006, 2007, 2008, 2009, 2010, 2011,
        2012, 2013, 2014, 2015, 2016, 2017, 2018
        ]

## input for price calculation

## budget input
ErrorValidation.reset_flag()
while ErrorValidation.error_flag == True:
    budget_input = int(input("What is your budget? Enter a positive integer: "))
    ## budget input validation
    ErrorValidation.is_positive_int(budget_input)

## mileage input
ErrorValidation.reset_flag()
while ErrorValidation.error_flag == True:
    mileage_input = int(input("Enter an approximate mileage between 0 and 120000: "))
    ## mileage input validation
    ErrorValidation.valid_mileage(mileage_input)

## call class PriceCalulator in order to get the cars that match our criteria
## initialize a Price calculator object
car_options = PriceCalculator(int(budget_input), int(mileage_input))
## get car options
criteria_match = PriceCalculator.sale_price(car_options)
print("-"*70)

## if car options are not returned, respond appropriately
if len(criteria_match) == 0:
    print("\nNo cars match your criteria")
## if car options are returned, provide the list of options
else:
    print("\nThe below cars match your criteria:\n")
    ## sort the options based on year and price
    criteria_match = sorted(criteria_match, key=lambda x:(-x[2], -x[1]))
    ## print the sorted list for the customer to choose from 
    for c in criteria_match:
        for member in c:
            print(str(member).rjust(10), end = " ")
        print("")
    selection_flag = True

## if there are selections ask the customer to purchase a car
if len(criteria_match) > 0:
    while selection_flag == True:
        print("-"*70)
        car_selection = input("Which car would you like?\nEnter the make, year and price from our selection. For example: toyota 2009 14000\nSeperate the input with a space: ")
        ## create a list of the selection
        list_selection = car_selection.split(" ")
        list_selection[0] = list_selection[0].lower()
        list_selection[1] = int(list_selection[1])
        list_selection[2] = int(list_selection[2])
        ## ask the customer to make his selection
        ## if selection is not in selction criteria, print message
        if list_selection in criteria_match:
            ## if the selection is valid, print a message
            print("="*70)
            print("\nCongratulations! We hope you enjoy your new car!\n")
            print("="*70)
            selection_flag = False
        else:
            print("Select an option from the list")
    ## get purchase price
    purchase_price = list_selection[2]

#######################################################################################
#######################################################################################

    ## ask the customer if he wants the loan
    ## Keep asking till the customer provides a valid input  
    while True:
        loan = input("Would you like an auto loan? Type ""yes"" or ""no"": ")
        if loan.lower() not in ["yes", "no"]:
            print("Invalid selection. Try again")
        ## if the customer wants to borrow, ask for borrower information
        elif loan.lower() == "yes":
            print("Great! We need some more information to provide you a rate")
            print("-"*70)
            
            ErrorValidation.reset_flag()
            while ErrorValidation.error_flag == True:
                ## ask for the borrower's income and error check
                income = int(input("What is your annual income? "))
                ErrorValidation.is_positive_int(income)
            
            ErrorValidation.reset_flag()
            while ErrorValidation.error_flag == True:
                ## ask for credit score and error check
                credit_score = int(input("Enter your credit score between 0 and 850? "))
                ErrorValidation.valid_credit_score(credit_score)

            ErrorValidation.reset_flag()
            while ErrorValidation.error_flag == True:
                ## ask for downpayment and error check
                down_payment = int(input("Enter the amount of down payment: "))
                ErrorValidation.is_negative(down_payment)            
            
            ErrorValidation.reset_flag()
            while ErrorValidation.error_flag == True:
                ## ask for downpayment and error check
                term = int(input("Enter the term of the loan in years: "))
                ErrorValidation.is_positive_int(term)    

            ## Calculate and print the financing information
            financing = Autoloan(income, credit_score, down_payment, term, purchase_price)
            rate = Autoloan.interest_rate(financing)
            payment = Autoloan.monthly_payment(financing)
            print("-"*70)
            print("\nYour monthly payment at a rate of",rate,"percent is USD",payment)
            break
        else:
            break
print("\nThank you for choosing us! We look forward to continuing our relationship with you in the future.")
