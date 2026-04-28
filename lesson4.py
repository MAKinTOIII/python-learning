# Lesson 4: Conditionals — if / elif / else
tasks_done = 12
tasks_total = 20
days_left = 3
blockers = 2

tasks_completion = (tasks_done/tasks_total)*100

if tasks_completion >= 75:
    print("On track")
elif tasks_completion >= 50:
    print("Needs attention")
else: 
    print("Critical")

if days_left < 5 and blockers > 0: 
    print("Sprint at risk!")
