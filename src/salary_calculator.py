"""Salary Calculator."""

sales = int(input("Enter total sales:"))
target_sales = 100000
if sales >= target_sales:
    basic = 4000
    hra = basic / 10
    da = basic * (11 / 10)
    cns = 500
    bonus = 500
    incentive = sales * (4 / 100)
else:
    basic = 400
    hra = basic / 20
    da = basic * (11 / 10)
    cns = 500
    bonus = 1000
    incentive = sales * (10 / 100)
print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("Bonus:", bonus)
print("Incentive:", incentive)
print("Total Salary:", basic + hra + da + bonus + incentive)
