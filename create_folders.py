import os
from datetime import datetime, timedelta

# Define the start and end dates
start_date = datetime(2022, 3, 1)
end_date = datetime(2023, 2, 28)

# Create the directory if it doesn't exist
path = "H:/My Drive/1. GME/Salaries/2023/Payslips"
os.makedirs(path, exist_ok=True)

# Generate and create folders for each month
current_date = start_date

counter = -1
while current_date <= end_date:
    counter += 1
    month_name = current_date.strftime("%B")
    folder_name = f"{counter}. {month_name} {current_date.year}"
    os.makedirs(os.path.join(path, folder_name), exist_ok=True)
    if current_date.month == 2:  # Adjust for February
        current_date = datetime(current_date.year, 3, 1)
    else:
        current_date += timedelta(days=30)  # Approximate month duration

print("Financial year folders have been created.")

