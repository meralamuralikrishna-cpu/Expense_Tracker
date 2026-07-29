import json
import time
from datetime import datetime

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
    id = int(input("Enter Id: ").strip())
    for i in range(0,len(loaded_data["expenses"])):
        if loaded_data["expenses"][i]["id"] == id:
            print("Alread Exits please Choose another id")
            return 
    date_str = input("Enter Date(DD/MM/YYYY): ").strip()
    date_obj = datetime.strptime(date_str,"%d/%m/%Y")
    while True:
            try:
                amount = int(input("Enter Amount: ").strip())
                break
            except ValueError:
                print("Enter intger only")

    category = input("Enter Category: ").strip().lower()
    description = input("Enter Description: ").strip().lower()

    data = {
        "id":id,
        "date":date_obj.strftime("%d/%m/%Y"),
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
        choice = int(input("Enter your choice: "))
        if choice == 1:
            id = int(input("Enter Id to view the Expense: ").strip())
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

    search_by = int(input("Enter your choice: "))
    loaded_data = Load_Expense()
    match search_by:
        case 1:
            found = False
            id = int(input("Enter Id: "))
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["id"] == id:
                    print(loaded_data["expenses"][i])
                    found = True
                    break
            if not found:
                print(f"No Id Was Found by the {id}")
        case 2:
            found = False
            date = input("Enter Date: ")
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["date"] == date:
                    print(loaded_data["expenses"][i])
                    found = True
                    break
            if not found:
                print(f"No date was found by the {date}")

        case 3:
            found = False
            category = input("Enter Category: ")
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["category"] == category:
                    print(loaded_data["expenses"][i])
                    found = True
                    break
            if not found:
                print(f"No Data was Found by the {category}")

        case 4:
            found = False
            description = input("Enter Description to search: ")
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
    id = int(input("Enter Id to Delete: ").strip())
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
    total  = 0
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
        return
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
        return
    for i in range(1,len(loaded_data["expenses"])):
        if min_amount > loaded_data["expenses"][i]["amount"]:
            min_amount = loaded_data["expenses"][i]["amount"]

    print(min_amount)

def Update_Expense():
    global selected_id
    loaded_data = Load_Expense()
    found = False
    print("1.ID")
    print("2.Date")
    print("3.Category")
    print("4.Description")
    print("5.Amount")
    print("6.Exit")

    while True:
        choice = int(input("Enter your Choice: "))
        if choice ==  1:
            while True:
                try:
                    old_id = int(input("Enter your old id: "))
                    break
                except ValueError as e:
                    print("Enter only Valid Numbers")

            for i in range(0,len(loaded_data['expenses'])):
                if loaded_data["expenses"][i]["id"] == old_id:
                    new_id = int(input("Enter New Id: "))
                    loaded_data["expenses"][i]["id"] = new_id
                    found = True
                    print(f"Upated Successfully {old_id}->{new_id}")
                    Save_Expenses(loaded_data)
                    break
            if not found:
                print(f"No Id Was Found by the {old_id}")

        elif choice == 2:
            selected_id = int(input("Enter Id to update: "))
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["id"] == selected_id:
                    new_date = input("Enter New Date(DD/MM/YYYY):").strip()
                    new_date_obj = datetime.strptime(new_date,"%d/%m/%Y")
                    loaded_data["expenses"][i]["date"] = new_date_obj.strftime("%d/%m/%Y")
                    Save_Expenses(loaded_data)
                    found = True
                    print(f"Successfully Updated the Date to {new_date}")
                    break
            if not found:
                print(f"No Id was Found by the {selected_id}")

        elif choice  == 3:
            selected_id = int(input("Enter Id to update: "))
            index = 0
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["id"] ==  selected_id:
                    new_category = input("Enter your new Category: ")
                    loaded_data["expenses"][i]["category"] = new_category
                    found = True
                    Save_Expenses(loaded_data)
                    print(f"successfully Updated the category at ID:{selected_id}")
                    break
            if not found:
                print(f"No Id was Found by the {selected_id}")


        elif choice == 4:
            selected_id = int(input("Enter Id to Update: "))
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["id"] == selected_id:
                    new_description = input("Enter new Description: ")
                    loaded_data["expenses"][i]["description"] = new_description
                    found = True
                    Save_Expenses(loaded_data)
                    print(f"Successfully Updated the description at Id:{selected_id}")
                    break
            if not found:
                print(f"No Description was found by the {selected_id}") 

        elif choice == 5:
            selected_id = int(input("Enter the id to change: "))
            index = 0
            for i in range(0,len(loaded_data["expenses"])):
                if loaded_data["expenses"][i]["id"] == selected_id:
                    new_amount = int(input("Enter New Amount: "))
                    loaded_data["expenses"][i]["amount"] = new_amount
                    found = True
                    Save_Expenses(loaded_data)
                    print(f"Successfully Changed the amount New_Amount:{new_amount}")
                    break
            if not found:
                print(f"No Id was Found by the {selected_id}")

        elif choice == 6:
            break


def category_summary():
    loaded_data = Load_Expense()
    category = input("Enter Category: ").strip().lower()
    found = False
    total = 0
    for i in range(0,len(loaded_data["expenses"])):
        if category == loaded_data["expenses"][i]["category"]:
            total += loaded_data["expenses"][i]["amount"]
            found = True

    if found == True:
        print(f"Category Summary of {category} = {total}")

    if not found:
        print(f"No Category was Found {category} in data")

def Average_Expense():
    loaded_data = Load_Expense()
    average = []
    count = 0
    for i in range(0,len(loaded_data["expenses"])):
        average.append(loaded_data["expenses"][i]["amount"])
    try:
        average = sum(average) / len(average)
    except ZeroDivisionError:
        print("Values must be Initialzed before operations")
        return

    
    print(average)
    

def menu():
    while True:
        print("1.Add Expenses")
        print("2.View Expense")
        print("3.Search Expense")
        print("4.Delete Expense")
        print("5.Update Expense")
        print("6.Calculate Expense")
        print("7.category Expense")
        print("8.Highest Expense")
        print("9.Lowest Expense")
        print("10.Average Expense")
        print("11.Exit")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("please Enter only the integers")
                return

        if choice == 1:
            Add_Expense()
        elif choice == 2:
            View_Expense()
        elif choice == 3:
            Search_Expense()
        elif choice == 4:
            Delete_Expense()
        elif choice == 5:
            Update_Expense()
        elif choice == 6:
            calculate_total()
        elif choice == 7:
            category_summary()
        elif choice == 8:
            Highest_Expense()
        elif choice == 9:
            Lowest_Expense()
        elif choice == 10:
            Average_Expense()
        elif choice == 11:
            print("Exiting.....")
            time.sleep(1)
            break
        else:
            print("Invalid Choice!")

menu()