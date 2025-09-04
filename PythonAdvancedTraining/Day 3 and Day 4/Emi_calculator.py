import math

principal = float(input("Enter the principal amount you have taken:"))
rate = float(input("Enter annual interest rate:"))/100/12
years = float(input("Enter the loan tenure((in years)):"))
month = years * 12

Emi = principal * rate * (math.pow((1+rate),month)/(math.pow((1+rate),month) - 1))

print(f"Your monthly emi will be Rs. {Emi:.2f}")