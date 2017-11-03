def getData () :
    fullName = input('Enter full name: ')
    married = input('Enter marital status(Enter \'s\' for single and \'m\' for married): ')
    if married == 'm':
        children = int(input('Enter number of children under the age of 14: '))
        spouses = input('Do both spouses earn income? (\'y\' or \'n\'): ')
        if spouses == 'y':
            salary = int(input('Enter combined salary: '))
        else:
            salary = int(input('Enter your salary: ')) 
    else:
        salary = float(input('Enter your salary: '))
        children = 0
    pension = float(input('Enter your pension contibution(up to 6%): '))
    while pension > 6:
        print('pension limit is 6%')
        pension = float(input('Enter your pension contibution(up to 6%): '))
    computeTax(salary, pension, married, children)
    

def computeTax (sal, pens, mar, chld) :
    pensCont = pens/100 * sal
    if sal>0 and sal<15000:
        tax = sal*.15
    else:
        tax = 2250 + (sal - 15000)*.25
    if mar == 's':
        ppl = 1
        standardExempt = 4000
    else:
        ppl = 2 + chld
        standardExempt = 7000
    deduction = pensCont + standardExempt + ppl*1500
    taxableIncome = sal - deduction
    taxData = [pens, deduction, taxableIncome, tax]
    print (taxData)

getData()
 
