user = {
    "name": "Jhon Doe",
    "info": {
        "basic": {
            "age": 25,
            "salary": 2500
        },
        "additional": {
            "study": "mathematics",
            "famili": "married"
        },
        "special": {
            "projects": [
                {
                    "name": "quantum computer",
                    "stage": "in progress"
                },
                {
                    "name": "laser gun",
                    "stage": "in testing"
                }
            ]
        }
    }
}


def get_data(data_dict, keys):
    data = data_dict
    for key in keys:
        data = data[key]
    return data


def get_data_rec(data_dict, keys, index=0):
    if index < len(keys):
        return get_data_rec(data_dict[keys[index]], keys, index+1)
    return data_dict


print(get_data(user, ["info", "special", "projects", 0, "name"]))
print(get_data(user, ["info", "basic", "salary"]))

print(get_data_rec(user, ["info"]))
