# Figuring out the profits from a business' total sales
# 9/22/2018
# CTI-110 P2T1 - Sales Prediction
# Cary Eaglin

#Greet user
print("Greetings Associate")
#ask user for amount of sales
sales = int(input("Enter whole dollar amount of total anual sales made? "))
#calculate sales profit
percent = (sales * 0.23)
#show projected profit
print("The projected profits are $",format(percent, ",.2f"))
#conclude sales pediction
print("This concludes our profit prediction. We exist to serve.")
