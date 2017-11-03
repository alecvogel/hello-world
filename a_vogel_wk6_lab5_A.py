mexicoPop = int(1.21 * 10**8)
USPop = int(3.15 * 10**8)
years = 0
data = []
header = ['Year', 'Mexico Pop.', 'US Pop.']
data.append(header)
initial = [years, mexicoPop, USPop]
data.append(initial)

def computePop (mexicoPop, USPop, years):
    while USPop > mexicoPop:
        mexicoPop = mexicoPop * 1.0101
        USPop = USPop * .9985
        years = years + 1
        newData = [years, int(mexicoPop), int(USPop)]
        data.append(newData)
    for rows in data:
        print('{:5} {:10} {:10}'.format(*rows))
    print('It took ', years, ' years')

computePop(mexicoPop, USPop, years)
