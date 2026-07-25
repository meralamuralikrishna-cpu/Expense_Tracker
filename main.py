import json

def Add_Expense():
    with open("expenses.json","r") as file:
        loaded_data = json.load(file)


    id = input("Enter Id")
    data = input("Enter Data")
    amount = input("Enter Amount")
    category = input("Enter Category")
    description = input("Enter Description")

    data = {
        "id":id,
        "data":data,
        "amount":amount,
        "category":category,
        "description":description
    }
    loaded_data["expenses"].append(data)
    with open("expenses.json","w") as file:
        json.dump(loaded_data,file,indent=4)

def View_Expense():
    with open("expenses.json","r") as file:
        loaded_data = json.load(file)
    
    id = input("Enter Id to view the Expense")
    for i in range(0,len(loaded_data["expenses"])):
        if loaded_data["expenses"][i]["id"] == id:
            print(loaded_data["expenses"][i])
            break
            
        else:
            print(f"No Id was Found By the {id}")
            
            

View_Expense()