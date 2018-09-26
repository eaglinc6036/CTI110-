# Write a program that converts the given numerical ratio of men and women in a class to percentages.
# 9/25/2018
# CTI-110 P2HW2 - Male Female Percentage
# Cary Eaglin

#Greet User
print("Greetings User!")
#Input number of men in the class
men = float(input("How many males are in the class? "))
#Input number of women in the class
women = float(input("How many females are in the class? "))          
#Convert into percentages
total = men + women
resultsm = float(men / total)
rm = float(resultsm * 100)
resultsw = float(women / total)
rw = float(resultsw * 100)
#Display results
print("The male percentage is",format(rm,".2f"),"%")
print("The female percentage is",format(rw,".2f"),"%")
