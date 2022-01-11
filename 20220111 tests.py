prices = (6,10,8,5,2,8,9,8,3,4,12,14,2,19,1,20)
days = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')

def sum_of_lowerdays():
    output = list()
    for n, nprev in zip(prices[1:], prices):
        if n >= nprev:
            output.append(n)
    return output

result = sum_of_lowerdays()
print(result)