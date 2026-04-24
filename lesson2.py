# Lesson 2 - Numbers and maths

budget = 120000
spent = 47500
team_size = 35
weeks_total = 12
weeks_done = 7

remaining = budget - spent
budget_per_member = budget / team_size
pct_done = (weeks_done / weeks_total) * 100

print(f"Budget remaining: ${remaining}")
print(f"Budget per team member: ${budget_per_member:.0f}")
print(f"Project is {pct_done:.1f}% complete")