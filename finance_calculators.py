import math                                                     #import math library
class color:                                                    #set colors 
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'       

print(color.BOLD + color.YELLOW + color.UNDERLINE +"\n\nWelcome to the Finance Calculator" + color.END)  # print title
choice= False                      # set choice to false
while choice != True:              #while choice is fault 
    # print the choices
    print (color.BOLD + color.YELLOW + "\n\nInvestment" +color.END + " - to calculate the amount of interest you'll earn on your investment\n")
    print (color.BOLD + color.YELLOW + "Bond" +color.END + " - to calculate the amount you'll have to pay on a home loan\n")
    print (color.BOLD + color.YELLOW + "Exit" +color.END + " - to exit the Finance Calculator\n")
    #ask user for input
    userReply= input ("Please type Investment, Bond or Exit :").lower().strip()     #makes the input to lowercase
    if userReply =="investment":
        print (color.BOLD + color.YELLOW + color.UNDERLINE + "\n\n\nInvestment" + color.END)
        print ("\nPlease provide the details below.\n")
        md= float (input ("Please enter the amount you would like to deposit :"))
        ir= float (input ("Interst rate :"))
        nir=ir/100
        ny= int (input ("Number of years you plan to invest :"))
        choice2 = False                                                            #choice 2 for simple or compound
        while choice2 != True:                                                 
            print ("\n What type of interest do you need?")                        #ask user for input
            print (color.YELLOW + "\nSimple" + color.END + " - Interest is calculated on the original (principal) amount")
            print (color.YELLOW + "\nCompound" + color.END + " - Interest is calculated on the original amount and on the interest already accumulated on it.")
            interest = input ("\nplease type Simple or Compound :").lower().strip()
        # simple
            if interest == "simple"
                stotal= md* (1 + nir*ny)
                sans=float(round(stotal,2))
                print (color.BOLD + color.YELLOW + color.UNDERLINE + "\n\n\nSimple Interest" + color.END)
                print ("\nYou will Deposit £",md," for ",ny," years at interest rate of ",ir,"%")
                print ("Your total returns after ",ny," years will be £",sans)
                choice2=True
        # compound
            elif interest == "compound":
                total=md * math.pow((1+nir),ny)
                ans=float(round(total,2))
                print (color.BOLD + color.YELLOW + color.UNDERLINE + "\n\n\nCompound Interest" + color.END)
                print ("\nYou will Deposit £",md," for ",ny," years at interest rate of ",ir,"%")
                print ("Your total returns after",ny," years will be £",ans)
                choice2=True
            else:    #error message for choice 2
                print (color.RED + "\nError : Please choose Simple or Compound" + color.END)
       
    # bond
    elif userReply =="bond":
        print (color.BOLD + color.YELLOW + color.UNDERLINE + "\n\n\nBond" + color.END)
        print ("\nPlease provide the details below.\n")
        houseValue= int (input ("Please enter the House Value :"))
        interestRate= float (input ("Interest rate :"))
        noMonths= int (input ("Number of months over which the bond will be repaid :"))
        monthlyRate= (interestRate/100)/12
        repayment = (monthlyRate * houseValue)/(1 - (1 + monthlyRate)**(-noMonths))
        trepayment = (round(repayment,2))
        print (color.BOLD + color.YELLOW + color.UNDERLINE + "\n\n\nLoan Calculation " + color.END)
        print ("\nTotal loan taken is £",houseValue," for ",noMonths," months, interest rate of ",interestRate,"%")
        print ("Your total monthly repayments will be ",trepayment," for ",noMonths," months.")
        totalRepay=(round(trepayment*noMonths,2))
        print ("the total amount repayble is :£",totalRepay)
       
    #exit
    elif userReply =="exit":
        print("\n\n\nThank you for using the" + color.YELLOW + color.BOLD + " Finance Calculator! \n\n\n"+ color.END)
        choice=True
    #error message for main 
    else:
        print (color.RED + "\n\nError - you typed : "+ color.END + userReply )
        print (color.RED + "please type from the options below "+ color.END)
