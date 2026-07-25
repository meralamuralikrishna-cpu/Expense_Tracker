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

