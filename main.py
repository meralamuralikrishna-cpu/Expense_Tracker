import json

def Add_Expense():
    with open("expenses.json","r") as file:
        loaded_data = json.load(file)


    id = input("Enter Id: ").strip()
    data = input("Enter Data: ").strip()
    amount = input("Enter Amount: ".strip())
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
    with open("expenses.json","w") as file:
        json.dump(loaded_data,file,indent=4)

def View_Expense():
    with open("expenses.json","r") as file:
        loaded_data = json.load(file)
    
    id = input("Enter Id to view the Expense: ").strip()
    for i in range(0,len(loaded_data["expenses"])):
        if loaded_data["expenses"][i]["id"] == id:
            print(loaded_data["expenses"][i])
            break
            
        else:
            print(f"No Id was Found By the {id}")
            break

def Delete_Expense():
    id = input("Enter Id to Delete: ").strip()
    with open("expenses.json","r") as file:
        loaded_data = json.load(file)

    for i in range(0,len(loaded_data["expenses"])):
        if loaded_data["expenses"][i]["id"] == id:
            del loaded_data["expenses"][i]
            print(f"Successfully Deleted Id:{id}")
            break
        else:
            print(f"No Id was Found by the {id}")
            break

    with open("expenses.json",'w') as file:
        json.dump(loaded_data,file,indent=4)

Delete_Expense()






            
            

