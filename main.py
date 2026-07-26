import json

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
    data = input("Enter Data: ").strip()

    try:
        amount = int(input("Enter Amount: ".strip()))
    except ValueError:
        print("Enter intger only")

    category = input("Enter Category: ").strip()
    description = input("Enter Description: ").strip()

    data = {
        "id":id,
        "data":data,
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


Delete_Expense()

