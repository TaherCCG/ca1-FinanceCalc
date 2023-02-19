import math                                                     #import math library
class color:                                                    #set colors 
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'       

print(color.BOLD + color.YELLOW + color.UNDERLINE +"\n\nWelcome to the Finance Calculator" + color.END)  # print title
choice= False                      # set choice to false
while choice != True:              # while choice is fault 
    # print the choices
    print (color.BOLD + color.YELLOW + "\n\nInvestment" +color.END + " - to calculate the amount of interest you'll earn on your investment\n")
    print (color.BOLD + color.YELLOW + "Bond" +color.END + " - to calculate the amount you'll have to pay on a home loan\n")
    print (color.BOLD + color.YELLOW + "Exit" +color.END + " - to exit the Finance Calculator\n")
    #ask user for input
    userReply= input ("Please type Investment, Bond or Exit :").lower().strip()     # defines var userReply to input value of the user, makes the value lowercase and removes any whitespaces
    if userReply =="investment":                                                    # if var userReply is investment
        print (color.BOLD + color.YELLOW + color.UNDERLINE + "\n\n\nInvestment" + color.END)    # print Investment with text emphases 
        print ("\nPlease provide the details below.\n")                                         # print message
        md= float (input ("Please enter the amount you would like to deposit :"))               # define var md to input value as float
        ir= float (input ("Interest rate :"))                                                   # define var ir to input value as float
        nir=ir/100                                                                              # define var nir as a calculation of var ir/100
        ny= int (input ("Number of years you plan to invest :"))                                # define var ny to input value as integer
        choice2 = False                                                             # define choice 2 as False
        while choice2 != True:                                                      # while var choice 2 is not True
            print ("\n What type of interest do you need?")                         # print message asking user for input
            print (color.YELLOW + "\nSimple" + color.END + " - Interest is calculated on the original (principal) amount")  # print choices 
            print (color.YELLOW + "\nCompound" + color.END + " - Interest is calculated on the original amount and on the interest already accumulated on it.")
            interest = input ("\nplease type Simple or Compound :").lower().strip() # define var interest as user input value to lower case and remove whitespace 
        # simple
            if interest == "simple":                                                                        # if var interest is "simple"
                sTotal= md* (1 + nir*ny)                                                                    # define var sTotal as calculation     
                sans=float(round(sTotal,2))                                                                 # define sans to sTotal and round of to 2 decimal places
                print (color.BOLD + color.YELLOW + color.UNDERLINE + "\n\n\nSimple Interest" + color.END)   # print following messages
                print ("\nYou will Deposit £",md," for ",ny," years at interest rate of ",ir,"%")
                print ("Your total returns after ",ny," years will be £",sans)
                choice2=True                                                                                # choice2 is True
        # compound
            elif interest == "compound":                                                                    # else if var interest is compound
                total=md * math.pow((1+nir),ny)                                                             # define var total as calculation for compound    
                ans=float(round(total,2))                                                                   # define var ans as total and round of to 2 decimal places    
                print (color.BOLD + color.YELLOW + color.UNDERLINE + "\n\n\nCompound Interest" + color.END) # print following messages
                print ("\nYou will Deposit £",md," for ",ny," years at interest rate of ",ir,"%")
                print ("Your total returns after",ny," years will be £",ans)
                choice2=True                                                                                # choice2 is True   
            else:    #error message for choice 2                                                            # else if interest is not simple or compound then   
                print (color.RED + "\nError : Please choose Simple or Compound" + color.END)                # print message
       
    # bond
    elif userReply =="bond":                                                                    # else if userReply is bond
        print (color.BOLD + color.YELLOW + color.UNDERLINE + "\n\n\nBond" + color.END)          # print following message
        print ("\nPlease provide the details below.\n")                                         
        houseValue= int (input ("Please enter the House Value :"))                              # define var houseValue as user input value to integer
        interestRate= float (input ("Interest rate :"))                                         # define var interestRate as user input value to float
        noMonths= int (input ("Number of months over which the bond will be repaid :"))         # define var noMonths as user input value to integer
        monthlyRate= (interestRate/100)/12                                                      # define var monthlyRate as calculation of (interestRate/100)/12
        repayment = (monthlyRate * houseValue)/(1 - (1 + monthlyRate)**(-noMonths))             # define var repayment as calculation
        tRepayment = (round(repayment,2))                                                       # define var tRepayment as repayment and round it of to 2 decimal places
        print (color.BOLD + color.YELLOW + color.UNDERLINE + "\n\n\nLoan Calculation " + color.END) # print following messages
        print ("\nTotal loan taken is £",houseValue," for ",noMonths," months, interest rate of ",interestRate,"%")
        print ("Your total monthly repayments will be ",tRepayment," for ",noMonths," months.")
        totalRepay=(round(tRepayment*noMonths,2))                                               # define var totalRepay to calculation
        print ("the total amount repayable is :£",totalRepay)                                   # print message and totalRepay var
       
    #exit
    elif userReply =="exit":                                                                    # else if var userReply is exit then
        print("\n\n\nThank you for using the" + color.YELLOW + color.BOLD + " Finance Calculator! \n\n\n"+ color.END)   # print message
        choice=True                                                                             # choice is True
    #error message for main 
    else:                                                                                       # else 
        print (color.RED + "\n\nError - you typed : "+ color.END + userReply )                  # print following message as error
        print (color.RED + "please type from the options below "+ color.END)
