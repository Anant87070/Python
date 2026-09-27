#Expense Tracker Project

expensesList = [] #list of expenses in form of dictionary
print("Welcome to Expense tracker  ")

while True:
    print("===MENU===")
    print("1.Add Expense")
    print("2.View All Expenses")
    print("3.View Total Khrcha")
    print("4.Exit")

    choice= int(input("Plese Enter your choice :"))
    if(choice==1):
        date= input("Enter dete(dd\mm\yy):")
        category= input("Enter the category (food,shopping,travel etc):")
        description= input("Enter detial of category:")
        amount= float(input("Enter the amount:"))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        expensesList.append(expense)
        print("\nExpense is added succesfully")

#2. VIEW ALL EXPENSES
    elif(choice == 2):
        if(len(expensesList)==0):
            print("No Expenses Added")
        else:
            print("===Your all Expense===")
            count= 1
            for eachKharcha in expensesList:
                print(f"Khrcha Number {count}->{eachKharcha["date"]},{eachKharcha["category"]},{eachKharcha["description"]},{eachKharcha["amount"]}")
                count= count+1

#3. View Total Spending
    elif(choice == 3 ):
        total= 0
        for eachKharcha in expensesList:
            total = total + eachKharcha["amount"]
        print("\n TOTAL KHRCHA =", total)

#4. EXIT
    elif(choice == 4):
        print("Dhanyawad you are using my system")
        break
    else:
        print("INVALID CHOICE. TRY AGAIN")