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


function f() {
    var number_of_emp = 0, number_of_skills = 0;
    for (x in emp_data) {
        number_of_emp++;
    }
    // for (x in emp_data) {
    //     console.log(x);
    //     //number_of_skills += x.Skils.length;
    // }
    let items = Object.values(emp_data);
    console.log(items);
    items.map(value => {
        number_of_skills += value.Skils.length;
    });
    console.log(number_of_emp);
    console.log(number_of_skills);
    // console.log(typeof (x));

}