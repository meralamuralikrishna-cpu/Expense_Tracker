import json
import time

def Load_Expense():
    with open("expenses.json","r") as file:
        loaded_data = json.load(file)
        return loaded_data

def Save_Expenses(data):
    with open("expenses.json","w") as file:
        json.dump(data,file,indent=4)
    
def Add_Expense():

    loaded_data = Load_Expense()

    id = input("Enter Id: ").strip()
    date = input("Enter Date(DD/MM/YYYY): ").strip()

    try:
        amount = int(input("Enter Amount: ".strip()))
    except ValueError:
        print("Enter intger only")

    category = input("Enter Category: ").strip().lower()
    description = input("Enter Description: ").strip().lower()

    data = {
        "id":id,
        "date":date,
        "amount":amount,
        "category":category,
        "description":description
    }
    loaded_data["expenses"].append(data)
    Save_Expenses(loaded_data)
    """
    with open("expenses.json","w") as file:
        json.dump(loaded_data,file,indent=4)
    """
def View_Expense():
    loaded_data = Load_Expense()

    id = input("Enter Id to view the Expense: ").strip()
    for i in range(0,len(loaded_data["expenses"])):
        if loaded_data["expenses"][i]["id"] == id:
            print(loaded_data["expenses"][i])
            return            
        else:
            print(f"No Id was Found By the {id}")
            return 

def Search_Expense():
    print("1.ID")
    print("2.Date")
    print("3.Category")
    print("4.Description")
    print("5.Amount")

    search_by = int(input("Enter your choice"))
    loaded_data = Load_Expense()
    match search_by:
        case 1:
            found = False
            id = input("Enter Id")
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["id"] == id:
                    print(loaded_data["expenses"][i])
                    found = True
                    break
            if not found:
                print(f"No Id Was Found by the {id}")
        case 2:
            found = False
            date = input("Enter Date")
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["date"] == date:
                    print(loaded_data["expenses"][i])
                    found = True
                    break
            if not found:
                print(f"No date was found by the {date}")

        case 3:
            found = False
            category = input("Enter Category")
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["category"] == category:
                    print(loaded_data["expenses"][i])
                    found = True
                    break
            if not found:
                print(f"No Data was Found by the {category}")

        case 4:
            found = False
            description = input("Enter Description to search")
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["description"] == description:
                    found = True
                    print(loaded_data["expenses"][i])
                    break
            if not found:

                print(f"No Data Was Found by the {description}")

        case 5:
            found = False
            amount = int(input("Enter Amount to Search: "))
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["amount"] == amount:
                    print(loaded_data["expenses"][i])
                    found = True
                    break
            if not found:
                print(f"No Data was Found by the {amount}")


def Delete_Expense():
    loaded_data = Load_Expense()
    id = input("Enter Id to Delete: ").strip()

    for i in range(0,len(loaded_data["expenses"])):
        if loaded_data["expenses"][i]["id"] == id:
            del loaded_data["expenses"][i]
            print(f"Successfully Deleted Id:{id}")
        else:
            print(f"No Id was Found by the {id}")

    Save_Expenses(loaded_data)

def calculate_total():
    total:int = 0
    loaded_data =  Load_Expense()
    for i in range(0,len(loaded_data["expenses"])):
        total += loaded_data["expenses"][i]["amount"]

    print(total)

def Highest_Expense():
    loaded_data = Load_Expense()
    max_amount = loaded_data["expenses"][0]["amount"]
    for i in range(1,len(loaded_data["expenses"])):
        if max_amount < loaded_data["expenses"][i]["amount"]:
            max_amount = loaded_data["expenses"][i]["amount"]

    print(max_amount)

def Lowest_Expense():
    loaded_data = Load_Expense()
    min_amount = loaded_data["expenses"][0]["amount"]
    for i in range(1,len(loaded_data["expenses"])):
        if min_amount > loaded_data["expenses"][i]["amount"]:
            min_amount = loaded_data["expenses"][i]["amount"]

    print(min_amount)

def menu():
    while True:
        print("1.Add Expenses")
        print("2.View Expense")
        print("3.Search Expense")
        print("4.Delete Expense")
        print("Calulate Expense")
        print("6.Highest Expense")
        print("7.Lowest Expense")
        print("8.Exit")

        choice = int(input("Enter your choice"))

        if choice == 1:
            Add_Expense()
        elif choice == 2:
            View_Expense()
        elif choice == 3:
            Search_Expense()
        elif choice == 4:
            Delete_Expense()
        elif choice == 5:
            calculate_total()
        elif choice == 6:
            Highest_Expense()
        elif choice == 7:
            Lowest_Expense()
        elif choice == 8:
            print("Exiting.....")
            time.sleep(1)
            break

menu()