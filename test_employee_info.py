import employee_info as employee

def test_get_employees_by_age_range():
    test_lower=23
    test_upper=31
    test_array=[
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
                {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}
                ]
    test_result=employee.get_employees_by_age_range(test_lower,test_upper)
    assert (test_result==test_array)

def test_calculate_average_salary():
    test_avg=60166.667
    test_result=round(employee.calculate_average_salary(),3)
    assert (test_result==test_avg)

def test_get_employee_by_dept():
    test_dept='Engineering'
    test_array=[
        {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    test_result=employee.get_employees_by_dept(test_dept)
    assert (test_result==test_array)
