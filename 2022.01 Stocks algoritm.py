# prices = (6,12,8,7,3,8,9) # 1, 2, 1, 1, 1, 4, 5
# week_days = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')

# def sum_of_lowerdays():
#     output = list()
#     for n, nprev in zip(prices[1:], prices):
#         if n >= nprev:
#             output.append(n)
#     return output

# result = sum_of_lowerdays()



def stocks_span(rates_per_day):       # algoritm for stocks lmao
    stockspan_list = []
    imaginary_box_for_days = [0]      # start from zero obviously
    stockspan_list.append(1)          # 1 for first day
    for index in range(1, len(rates_per_day)):             # taking index from rates list
      while rates_per_day[index] >= rates_per_day[imaginary_box_for_days[-1]]:          # while rate of current day bigger than previous day
        imaginary_box_for_days.pop()        # delete previous day if its lower
        if len(imaginary_box_for_days) == 0:
          break
      
      if len(imaginary_box_for_days) > 0:           
          stockspan_list.append(index - imaginary_box_for_days[-1])
      else:
          stockspan_list.append(index + 1) 
      imaginary_box_for_days.append(index)
    
    return stockspan_list



rates = [6,12,8,7,3,8,9,13] # 1, 2, 1, 1, 1, 4, 5
stockspan = stocks_span(rates)
print(stockspan)