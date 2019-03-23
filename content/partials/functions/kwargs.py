def describe_object(item, **kwargs):
    print(f"item: {item}")
    # for x in kwargs would only return the dictionary's keys
    # the items function returns both the keys and values
    for key, value in kwargs.items():
        print(f"{key}: {value}")


describe_object(item="apple", size=5, cost=1, color="red")
