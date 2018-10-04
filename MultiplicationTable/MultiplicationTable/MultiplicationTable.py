def writeTable(number,start,end):
    for x in range(start,end+1):
        product=x*number
        print(str(number) + ' * ' + str(x) + ' = ' + str(product))
