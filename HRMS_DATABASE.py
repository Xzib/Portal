from pymongo import MongoClient
from prompt_helper import prompt_helper
import pprint


connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)

collection = client.HRMS["user_info"]

temp_val = {"First_Name" : "",
            "Last_Name" : "",
            "Email_id" : "",
            "Contact" : "",
            "Employee_Code" : "",
            "Address" : ""}
 
input_val = prompt_helper()
while input_val != 'q':
    key_dic = [*temp_val]
    if input_val == "i":
        for k in key_dic:
            v = input(f"Enter {k} : ")
            temp_val[k] = v
        collection.insert_one(temp_val)
        input_val = prompt_helper()
    elif input_val == "f":
        query = input("Enter Employee code: ")
        find_record = collection.find_one({"Employee_Code" : query})
        pprint.pprint(find_record)
        input("press Enter key to continue: ")
        input_val = prompt_helper()
    elif input_val == "d":
        query = input("Enter Employee code: ")
        find_record = collection.find_one({"Employee_Code" : query})
        if find_record == None:    
            print("\n\nEmployee Code does not exist")
        else:
            pprint.pprint(find_record)
            check = input("\n\nAre you sure you want to delete the Employee [y/n]: ").lower()
            if check == 'y':
                delete_record = collection.delete_one({"Employee_Code" : query})
                find_record = collection.find_one({"Employee_Code" : query})
                if find_record == None:
                    print(f"\n\n Succesfully deleted Employee_Code: {query} ")
        
        input("\n\npress Enter key to continue: ")
        input_val = prompt_helper()

