bill=float(input("Total bill? "))
tip=int(input("What percentage of tip 10, 12, 15: "))
persons=int(input("How many persons? "))
percent_tip=tip/100
bill_amount= bill*percent_tip
total_bill=bill+bill_amount
per_person=total_bill/persons
final_amount=round(per_person,2)
print(f"Each person should pay {final_amount}")