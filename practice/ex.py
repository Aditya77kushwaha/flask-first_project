emp_data = {
        "Adam": {
            "Skils": [
                "Python-Flask",
                "Python"
            ],
            "hours": 4
        },
        "Sam": {
            "Skils": [
                "Html",
                "Css"
            ],
            "hours": 4
        },
        "David": {
            "Skils": [
                "MySQL",
                "Flask",
                "Python"
            ],
            "hours": 8
        },
        "Rahul": {
            "Skils": [
                "MySQL",
                "Flask",
                "Python"
            ],
            "hours": 8
        }
    }

for x,y in emp_data.items():
    for key,key1 in y.items():
        if type(key1) == list:
            if "Python" in key1:
                print(x)


