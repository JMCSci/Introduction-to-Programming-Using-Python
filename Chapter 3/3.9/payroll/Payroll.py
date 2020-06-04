''' Chapter 3.9 '''

name = raw_input("Enter employee's name: ")
hoursWorked = input("Enter number of hours worked in a week: ")
hourlyPayRate = input("Enter hourly pay rate: ")
federalTaxWithholding = input("Enter federal tax withholding rate: ")
stateTaxWithholding = input("Enter state tax withholding rate: ")

grossPay = hoursWorked * hourlyPayRate
fedWithheld = grossPay  * federalTaxWithholding
stateWithheld = grossPay * stateTaxWithholding
totalDeductions  = fedWithheld + stateWithheld
netPay = grossPay - totalDeductions

print "\nEmployee Name:", name
print "Hours worked:", hoursWorked
print "Pay Rate:", hourlyPayRate
print "Gross Pay:", format(grossPay, ".2f")
print "Deductions:"
print format("Federal Withholding (" + str(federalTaxWithholding * 100) + "%):", ">30s"), format(fedWithheld, ".2f")
print format("State Withholding (" + str(stateTaxWithholding * 100) + "%):", ">27s"), format(stateWithheld, ".2f")
print format("Total Deductions:", ">19"), format(totalDeductions, ".2f")
print "Net Pay: $", format(netPay, ".2f")