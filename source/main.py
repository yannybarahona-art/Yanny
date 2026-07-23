# import os
def main():
    item_price = 10
    tax_rate = 0.05
    total_cost = item_price + (item_price * tax_rate)
    budget = 15
    is_budget_exceeded = total_cost > budget
    print(f"Total cost: {total_cost}")
    print(f"Is budget exceeded? {is_budget_exceeded}")

    a = 11
    b = 10
    if a > b:
        print("a is greater than b")
    else:
        print("a is not greater than b")

    difference = a - b
    print(f"Difference between a and b: {difference}")

    # estado=10
    # match estado:
    #    case 2:
    #        print("Estado is 2")
    #    case 10:
    #        print("Estado is 10")
    #    case 3:
    #        print("Estado is 3")

    p = False
    if p:
        print("p is True")
    elif not p:
        print("p is False")
    else:
        print("p is False")

    for i in range(5):
        print(f"Iteration {i}")

    structure = [1, 2, 3, 4, "five"]

    for variable in structure:
        if variable == 3:
            print("Variable is 3")
            break
        else:
            print(f"Variable: {variable}")


# p=True
# while p:
#    print("This is an infinite loop")

if __name__ == "__main__":
    main()
