try:
    print("Please enter yesterday's oil price")
    yesterday_price = float(input())
except:
    print('input isnt valid')
    exit()
try:    
    print("Please enter today's oil price")
    today_price = float(input())
except:
    print('input isnt valid')
    exit()
try:
    percent_change = (today_price - yesterday_price) / yesterday_price * 100.0
    print("The price has changed by "+str(percent_change)+"%")
except ZeroDivisionError:
    print("Unable to compute percent change due to zero value for yesterday's price")
