user_id = int(input("please enter your_id:"))
full_name = input("please enter your full_name:")
national_number = int(input("please enter national_number:"))

fixed_salary = float(input("please enter fixed_salary:"))
number_of_days = int(input("please enter number_of_days:"))
total_salary_for_days = fixed_salary * number_of_days

overtime_hours = float(input("enter your overtime_hours:"))
overtime_pay = float(input("please enter overtime_pay:"))
u_u = overtime_hours * overtime_pay

gross_salary = total_salary_for_days + u_u
value_added = 0.5 * gross_salary

if gross_salary > 3100000:
    tax = 0.12 * gross_salary
    net_salary = (gross_salary) - (tax + value_added)
    y = "{} dar in mah {} hoghogh daryaft kardeh,shamele yaraneh nemishavad"
    print(y.format(full_name, net_salary))

elif gross_salary == 3100000:
    tax = 0.1 * gross_salary
    net_salary = (gross_salary) - (tax + value_added)
    print(net_salary)
    print("shamel nemishvad!!!!:)")
else:
    tax = 0.1 * gross_salary
    net_salary = (gross_salary) - (tax + value_added)
    print(net_salary)
    print("vam 100 melyoni ba tavajoh be mizan pardakhti shakse dade sahavad:)")

