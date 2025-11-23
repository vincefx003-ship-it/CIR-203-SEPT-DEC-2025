import numpy as np

transactions = np.array([
    [1300, 1350, 1150, 1180, 1500, 1600],
    [1000, 1050, 1150, 1200, 1300, 1250],   
    [2000, 2100, 1950, 2200, 2050, 2150],  
    [8200, 9950, 1000, 1100, 1200, 1150]     
])

totals = transactions.sum(axis=1)

highest_branch = np.argmax(totals) + 1  

avg_monthly = transactions.mean()

reshaped = transactions.reshape(3, 8)

print("Transactions:\n", transactions)
print("Total per branch:", totals)
print("Highest branch:", highest_branch)
print("Average monthly volume:", avg_monthly)
print("Reshaped (3x8):\n", reshaped)
