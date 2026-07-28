import json
import time

def Load_Expense():
    try:
        with open("expenses.json","r") as file:
            loaded_data = json.load(file)
            return loaded_data
    except FileNotFoundError:
        print("File not Found Error please create the file")

def Save_Expenses(data):
    try:
        with open("expenses.json","w") as file:
            json.dump(data,file,indent=4)
    except FileNotFoundError:
        print("File not Found Error please createh the file")
    
def Add_Expense():

    loaded_data = Load_Expense()
    id = int(input("Enter Id").strip())
    for i in range(0,len(loaded_data["expenses"])):
        if loaded_data["expenses"][i]["id"] == id:
            print("Alread Exits please Choose another id")
            return 
    date = input("Enter Date(DD/MM/YYYY): ").strip()
    while True:
            try:
                amount = int(input("Enter Amount").strip())
                break
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
    found = False
    print("To View By ID press '1'")
    print("To View all Expense press '2'")
    print("Press 3 to Exit")
    while True:
        choice = int(input("Enter your choice"))
        if choice == 1:
            id = input("Enter Id to view the Expense: ").strip()
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["id"] == id:
                    print(loaded_data["expenses"][i])
                    found = True
                    break            
            if not found:
                print(f"No Id Was Found By the {id}")
        elif choice == 2:
            for i in range(0,len(loaded_data["expenses"])):
                print(loaded_data["expenses"][i])
        elif choice == 3:
            break

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
    found = False
    for i in range(0,len(loaded_data["expenses"])):
        if loaded_data["expenses"][i]["id"] == id:
            found = True
            del loaded_data["expenses"][i]
            print(f"Successfully Deleted.")
            break
    if not found :
        print(f"No Id was found by the {id}")
    Save_Expenses(loaded_data)

def calculate_total():
    total:int = 0
    loaded_data =  Load_Expense()
    for i in range(0,len(loaded_data["expenses"])):
        total += loaded_data["expenses"][i]["amount"]

    print(total)

def Highest_Expense():
    loaded_data = Load_Expense()
    try:
        max_amount = loaded_data["expenses"][0]["amount"]
    except IndexError:
        print("Please Initial the values in Add Expense Function to make operations")
    for i in range(1,len(loaded_data["expenses"])):
        if max_amount < loaded_data["expenses"][i]["amount"]:
            max_amount = loaded_data["expenses"][i]["amount"]

    print(max_amount)

def Lowest_Expense():
    loaded_data = Load_Expense()
    try:
        min_amount = loaded_data["expenses"][0]["amount"]
    except IndexError:
        print("Please Initalized the values in Add Expense Fucntion to make operations")
    for i in range(1,len(loaded_data["expenses"])):
        if min_amount > loaded_data["expenses"][i]["amount"]:
            min_amount = loaded_data["expenses"][i]["amount"]

    print(min_amount)

def Update_Expense():
    loaded_data = Load_Expense()
    found = False
    print("1.ID")
    print("2.Date")
    print("3.Category")
    print("4.Description")
    print("5.Amount")
    print("6.Exit")

    while True:
        choice = int(input("Enter your Choice"))
        if choice ==  1:
            while True:
                try:
                    old_id = int(input("Enter your old id"))
                    break
                except ValueError as e:
                    print("Enter only Valid Numbers")

            for i in range(0,len(loaded_data['expenses'])):
                if loaded_data["expenses"][i]["id"] == old_id:
                    new_id = int(input("Enter New Id"))
                    loaded_data["expenses"][i]["id"] = new_id
                    found = True
                    print(f"Upated Successfully {old_id}->{new_id}")
                    Save_Expenses(loaded_data)
                    break
            if not found:
                print(f"No Id Was Found by the {old_id}")

        elif choice  == 3:
            old_category = input("Enter your Old Category").strip().lower()
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["category"] == old_category:
                    new_category = input("Enter new category name")
                    loaded_data["expenses"][i]["category"] = new_category
                    Save_Expenses(loaded_data)
                    print(f"Successfully Updated {old_category}->{new_category}")
                    found = True
                    break
            if not found:
                print(f"No  category  was Found by the {old_category}")

        elif choice == 4:
            old_description = input("Enter Your Old Description")
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["description"] == old_description:
                    new_description = input("Enter new Description")
                    loaded_data["expenses"][i]["description"] = new_description
                    found = True
                    Save_Expenses(loaded_data)
                    print(f"Successfully changed {old_description}->{new_description}")
                    break
            if not found:
                print(f"No Description was found by the {old_category}") 

        elif choice == 5:
            selected_id = int(input("Enter the id to change"))
            index = 0
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["id"] == selected_id:
                    index = i
                    new_amount = int(input("Enter New Amount"))
                    loaded_data["expenses"][index]["amount"] = new_amount
                    found = True
                    Save_Expenses(loaded_data)
                    print(f"Successfully Changed the amount New_Amount:{new_amount}")
                    break
            if not found:
                print(f"No Id was Found by the {selected_id}")
        elif choice == 6:
            break


def menu():
    while True:
        print("1.Add Expenses")
        print("2.View Expense")
        print("3.Search Expense")
        print("4.Delete Expense")
        print("5.Calulate Expense")
        print("6.Highest Expense")
        print("7.Lowest Expense")
        print("8.Exit")

        while True:
            try:
                choice = int(input("Enter your choice"))
                break
            except ValueError:
                print("please Enter only the integers")

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

Update_Expense()