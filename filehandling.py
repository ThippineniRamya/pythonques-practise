
import csv

# Step 1: Read the input CSV file
with open("emp.csv", "r", newline="") as file:
    reader = csv.reader(file)

    # Step 2: Read and store the header
    header = next(reader)

    # Step 3: Store all employee records
    employees = []

    for row in reader:
        # Step 4: Check the joining year
        year = row[3][:4]

        if year == "2024":
            # Step 5: Convert salary to float
            salary = float(row[2])

            # Apply 20% increment
            salary = salary + (salary * 0.20)

            # Update the salary in the row
            row[2] = str(salary)

        employees.append(row)

# Step 6: Write the updated records to a new CSV file
with open("updated_employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(header)

    # Write all employee records
    writer.writerows(employees)

print("Employee salaries updated successfully!")
