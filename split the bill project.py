print( "welcom to split the bill")
bill =float(input("what was the total bill? $")) 
tip = int(input("what percentage tip would you like to give?  10 or 12 or 15"))
people = input("how many people to split the bill?")
people = int(people)
tip_amount = bill* (tip / 100)
total_bill = bill + tip_amount
each_person = total_bill / people
print(f"each person should pay :{each_person} $")