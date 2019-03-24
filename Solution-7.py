# The number to calculate the square root of:
sqroot = float (input("Please enter a positive number: "))
estimate = 6.0

while abs((estimate *estimate) - sqroot) > 0.1:
    estimate -=((estimate * estimate) - sqroot) / (2* estimate)

ans = str(round(estimate, 1))

print (f"The square root of {sqroot} is approx. {ans}.")