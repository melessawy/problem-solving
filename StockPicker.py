# You will be given a list of stock prices for a given day and your goal 
# is to return the maximum profit that could have been made by buying a stock 
# at the given price and then selling the stock later on. For example if the 
# input is: [45, 24, 35, 31, 40, 38, 11] then your program should return 16 
# because if you bought the stock at $24 and sold it at $40, a profit of $16 
# was made and this is the largest profit that could be made. If no profit 
# could have been made, return -1.


def StockPicker(arr):
    max_profit = 0
    temp = 0
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if (arr[j]>arr[i]):
                temp = arr[j]-arr[i]
                if (temp > max_profit):
                    max_profit = temp
    return max_profit

