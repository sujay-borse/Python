total_days = int(input("Enter the total number of days: "))

# Calculations
years = total_days // 365
remaining_days = total_days % 365
weeks = remaining_days // 7
remaining_days %= 7

# Output
print("Converted to Years, Weeks, and Days:")
print("Years:", years)
print("Weeks:", weeks)
print("Remaining Days:", remaining_days)