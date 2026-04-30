# Write a script that:

# Creates a list of 5 team members on the project
# Prints the total team count
# Prints the first and last person on the list
# Adds a new team member
# Loops through the updated list printing each as "Team member: [name]"

team = ["Jack", "Sara", "Tony", "Lola", "Clara"]
team_count = len(team)

print(team_count)
print(f"First: {team[0]}")
print(f"Last: {team[-1]}")
team.append("Tom")

for member in team: 
    print(f"Total team members: {member}")


