# Lesson 6: Dictionaries



"""   Write a script that:

Creates a dictionary for the TEST project with at least 6 fields — name, status, budget, spent, team_size, on_track
Prints the project name and status using direct access dict["key"]
Updates the status to "Delayed"
Adds a new field risk with value "High"
Prints a full project summary by looping through all key-value pairs
Bonus: calculate and print budget remaining using values from the dictionary — budget - spent

"""

project = {
    "name": "Sierra", 
    "status": "In Progress", 
    "budget": 100000, 
    "spent": 20000, 
    "team_size": 3, 
    "on_track": True    
}, 

print(project["name"])
print(project["status"])

project["status"] = "Delayed"