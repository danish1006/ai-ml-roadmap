# Personal Profile
name = "Danish"
age = 40
current_weight = 58.0
target_weight = 68.0
career_switch = True

# Career Info
current_role = "BFSI IT Project Manager"
target_role = "AI Systems Leader"
goal_salary = 8000000

# Output Profile
print("Name:", name)
print("Age:", age)
print("Current Role:", current_role)
print("Target Role:", target_role)

# Decision Logic (IMPORTANT)
if current_weight < target_weight:
    print("Bulking Phase Active")
else:
    print("Maintenance Phase")

# Skills
skills = ["Python", "ML", "AI"]
skills.append("Deep Learning")

# Loop
for skill in skills:
    print("Learning:", skill)

if career_switch:
    print("AI Career Rebuild in Progress")

for skill in skills:
    if skill == "Python":
        print("Core Skill:", skill)
    else:
        print("Secondary Skill:", skill)

print("----- SUMMARY -----")
print(name, "is transitioning from", current_role, "to", target_role)
