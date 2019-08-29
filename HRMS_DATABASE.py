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
        find_result = collection.find_one({"Employee_Code" : query})
        pprint.pprint(find_result)
        input("press any Enter key to continue: ")
        input_val = prompt_helper()

