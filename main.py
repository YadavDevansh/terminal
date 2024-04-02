import json  
# python objects can store in json format  
value ={  
        "a": "1",  
        "b": "2",  
        "c": "4",  
        "d": "8"  
}  
# the json file to save the output data   
save_file = open("C:/Users/Devansh/Desktop/ai_projects/proj_2/json.json", "w")  
json.dump(value, save_file, indent = 6)  
save_file.close()  

# Python program to update
# JSON
import json

# JSON data:
x =save_file = open("C:/Users/Devansh/Desktop/ai_projects/proj_2/json.json", "r")  

# python object to be appended
y = {"pin":110096}

# parsing JSON string:
z = json.loads(x)

# appending the data
z.update(y)

# the result is a JSON string:
print(json.dumps(z))
