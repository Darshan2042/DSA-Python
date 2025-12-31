def find_salary(package):
    if package < 500000:
        salary = package
    elif package >= 500000 and package < 1000000:
        salary = package -(package * 5 / 100)
    elif package >= 1000000 and package < 1500000:
        salary = package -(package * 10 / 100)
    elif package >= 1500000 and package < 2000000:
        salary = package -(package * 15 / 100)
    else:
        salary = package -(package * 30 / 100)
    return salary

package = int(input("Enter Package: "))
print("Salary", find_salary(package))
