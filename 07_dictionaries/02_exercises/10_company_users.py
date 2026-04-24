cmd = input()
employees_by_company = {}

while not cmd == 'End':
    company, employee = [el for el in cmd.split(" -> ")]
    if company not in employees_by_company:
        employees_by_company[company] = []
    if employee not in employees_by_company[company]:
        employees_by_company[company].append(employee)
    cmd = input()

for company in employees_by_company:
    print(f"{company}")
    for employee in employees_by_company[company]:
        print(f"-- {employee}")


'''
TASK:
Write a program that keeps the information about companies and their employees. 
You will be receiving company names and an employees' id until you receive the command "End" command. Add each employee 
to the given company. Keep in mind that a company cannot have two employees with the same id.
Print the company name and each employee's id in the following format:
"{company_name}
-- {id1}
-- {id2}
…
-- {idN}"
'''