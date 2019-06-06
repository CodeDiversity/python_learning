print('How Many KM did you run today?')
kms = float(input())
miles = kms/1.60934
miles = round(miles,2)
print(f"Your {kms}km ride was {miles} miles")

#round (thing to round, how many dec points)