# Class Activity 1


***For this task, assume that you have been approached by a small financial
company and asked to create a program that allows the user to access two
different financial calculators: an investment calculator and a home loan
repayment calculator.*** 
-  Create a new Python file in this folder called finance_calculators.py.
-  At the top of the file include the line: import math
-  Write the code that will do the following:
<ol>
<li></li> The user should be allowed to choose which calculation they want to do.
The first output that the user sees when the program runs should look like
this :<ol>
<li>Investment</li> - to calculate the amount of interest you'll earn on your investment
<li>Bond</li> - to calculate the amount you'll have to pay on a home loan
</ol>
*Enter either 'investment' or 'bond' from the menu above to proceed:*


<li></li> How the user capitalises their selection should not affect how the
program proceeds. i.e. ‘Bond’, ‘bond’, ‘BOND’ or ‘investment’, ‘Investment’,
‘INVESTMENT’, etc., should all be recognised as valid entries. If the user
doesn’t type in a valid input, show an appropriate error message.


<li></li> If the user selects ‘investment’, do the following:
**Ask the user to input:**
<ol>
<li/>The amount of money that they are depositing.
<li/> The interest rate (as a percentage). Only the number of the interest rate should be entered — don’t worry about having to deal with the added ‘%’, e.g. The user should enter 8 and not 8%.
<li/> The number of years they plan on investing.
<li/> Then ask the user to input if they want “simple” or “compound” interest, and store this in a variable called interest. Depending on
whether or not they typed “simple” or “compound”, output the appropriate amount that they will get back after the given period,at the specified interest rate.
<ol/>

*See below for the formula to be used:*

**Interest formula:**
-  The total amount when simple interest is applied is calculated as follows: 𝐴 = 𝑃(1 + 𝑟 × 𝑡) 
-  The Python equivalent is very similar: A =P *(1 + r*t) 
-  The total amount when compound interest is applied is calculated as follows: 𝐴 = 𝑃(1 + 𝑟)𝑡 
-  The Python equivalent is slightly different: A = P * math.pow((1+r),t)


**In the formula above:**
-  ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08.
-  ‘P’ is the amount that the user deposits.
-  ‘t’ is the number of years that the money is being invested.
-  ‘A’ is the total amount once the interest has been applied.

-  Print out the answer!
-  Try entering 20 years and 8 (%) and see what the difference is depending on the type of interest rate!
</ol></ol>

<li/> If the user selects ‘bond’, do the following:
<ol>
<li>Ask the user to input:</li>
<li>The present value of the house. e.g. 100000</li>
<li>The interest rate. e.g. 7</li>
<li>The number of months they plan to take to repay the bond. e.g. 120</li>
</ol>
**Bond repayment formula:**
-  The amount that a person will have to be repaid on a home loan each month is calculated as follows: 
𝑟𝑒𝑝𝑎𝑦𝑚𝑒𝑛𝑡 =
𝑖 × 𝑃 
1− (1+𝑖)-𝑛

**The Python equivalent is slightly different:**

repayment = (i * P)/(1 - (1 + i)**(-n))

*In the formula above:*
-  ‘P’ is the present value of the house.
-  ‘i’ is the monthly interest rate, calculated by dividing the annual interest rate by 12. Remember to divide the interest entered by the user by 100 e.g. (8 / 100) before dividing by 12.
-  ‘n’ is the number of months over which the bond will be repaid
<li/> Calculate how much money the user will have to repay monthly and output the answer. 
</ol>
