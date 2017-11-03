gross = 20000
expense = 35000
year = 1
data = []
import csv
header = ['Year', 'Profit/Loss']
netLoss = ['Net Loss', '']
data.append(header)
profits = ['Net Profit', '']
data.append(netLoss)
changes = 0

def computeProfit (gross, expense, year, changes):
    while year < 21:
        netProfit = gross - expense
        gross = gross * 1.1
        expense = expense * 1.04
        if changes > 0:
            textyear = '*' + str(year)
            changes = changes - 1
        else:
            textyear = str(year)
        newData = [str(textyear), int(netProfit)]
        data.append(newData)
        newProfit = gross - expense
        if netProfit < 0 and newProfit> 0:
            data.append(profits)
            changes = changes + 1
        year = year + 1
    writeData(data)

    
def writeData (data):
    with open('a_vogel_wk6_lab5_B.csv', 'w') as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(data)
        for rows in data:
            print('{:10} {:11}'.format(*rows))

        
computeProfit(gross, expense, year, changes)
