import random
import string

ALLOWED_DEPARTMENTS = ["Marketing", "Accounting", "FinOps"]

def generate_unique_names(num_instances, department_name):
    unique_names = []
    for _ in range(num_instances):
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        unique_name = f"{department_name}_{random_chars}"
        unique_names.append(unique_name)
    return unique_names

if __name__ == "__main__":
    num_instances = int(input("Enter the number of EC2 instances you want names for: "))
    department_name = input("Enter the name of your department: ")

    department_name = department_name.lower().capitalize()

    if department_name in ALLOWED_DEPARTMENTS:
        names = generate_unique_names(num_instances, department_name)
        for name in names:
            print(name)
    else:
        print("You should not use this Name Generator. Please choose one of the allowed departments: Marketing, Accounting, or FinOps.")
        ## AWS Cloud 9 to repo##