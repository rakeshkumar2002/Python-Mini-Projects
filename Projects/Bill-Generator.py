"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

totalNumberOfPeople = int(input("how many people are in the group."))
i=0
person = []
print("Tell me your names")
for i in range(0,totalNumberOfPeople):
    person.append(input())

pendingMoney = int(input("Each person owes:"))

print("Final output:")
for name in person:
    print(f"  {name} owes ₹{pendingMoney}")
