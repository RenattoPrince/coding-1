import os
import random
import time
#core stuff stats
wage_Monthly = 5000
Monthly_tax = 500
Health = 1000
Entertainment = 1000
respect = 100
Angry_respect = 50
#The remaining credits

#stuff that the player has to spend each month
tv_subcription = 20
Football_club = 50
Football_traning = 10
car_fuel_payment = 10
internet = 25
food = 80
gym = 50
takeaway_food = 120

#questions
Monthly_tax = str(input("Do you want a to pay tax this month?"))
if Monthly_tax == "yes" or "YES" or "Yes" or "Yeah" or "yeah":
    remaining_money = Monthly_tax - wage_Monthly
elif Monthly_tax == "no" or "NO" or "No":
    remaining_respect = respect - Angry_respect

    