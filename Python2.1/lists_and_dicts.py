def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "Nicolas", "lastname": "Torres"}

    super_list = [
        {"firstname": "Nicolas", "lastname": "Torres"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Mel"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "Jose", "lastname": "Garcia"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "Integer_nums": [-1, -2, 0, 1, 2], 
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)
    
    for item in super_list:
        print(item["firstname"], "-", item["lastname"])
        
    

if __name__ == "__main__":
    run()

