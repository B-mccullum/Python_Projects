import random
import string

ALLOWED_DEPARTMENTS = ["Marketing", "Accounting", "FinOps"]

def generate_unique_names(num_instances, department_name):
    unique_names = []
    for _ in range(num_instances):
        # Generate random characters
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        # Create a unique name by combining the department name and random characters
        unique_name = f"{department_name}_{random_chars}"
        # Add the unique name to the list
        unique_names.append(unique_name)
    return unique_names

if __name__ == "__main__":
    # Get the number of EC2 instances
    num_instances = int(input("Enter the number of EC2 instances you want names for: "))
    # Get the department name
    department_name = input("Enter the name of your department: ")

    # Format the department name with proper capitalization
    department_name = department_name.lower().capitalize()

    if department_name in ALLOWED_DEPARTMENTS:
        # Generate unique names based on the number of instances and the department name
        names = generate_unique_names(num_instances, department_name)
        # Print the generated names
        for name in names:
            print(name)
    else:
        # Print an error message if the department name is not allowed
        print("You should not use this Name Generator. Please choose one of the allowed departments: Marketing, Accounting, or FinOps.")
