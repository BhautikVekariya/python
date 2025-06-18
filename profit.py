def isProfit(cost_price,selling_price):
       if cost_price < selling_price:
           return True
       else:
           return False
                     

print(isProfit(100, 220))


def profit_or_loss_percent(cost_price,selling_price):
      if isProfit(cost_price,selling_price):
           profit=((selling_price-cost_price)/cost_price) * 100
           return f"Profit: {profit:.2f}%"
      elif cost_price > selling_price:
           loss=((cost_price-selling_price)/cost_price) * 100
           return f"loss: {loss:.2f}%"
      else:
           return "No profit and not loss"


result = profit_or_loss_percent(1000, 1800)
print(result)        

           