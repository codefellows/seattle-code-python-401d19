"""
Calculator:
Your job is refactor this code to use a single calculate function
E.g. add, subtract,multiply, and divide.
Pass in lambda function.
"""


# def calculate_branching(a, b, operator):
#     result = ""
#     if operator == "+":
#         result = a + b
#     elif operator == "%":
#         result = a % b
#     elif operator == "**":
#
#
#     return f"Given {a} and {b} the result of your operation is {result}"

def calculate(a, b, operator_fn):
    """
    Description of what calculate does
    Arguments:
      a (int or float)
      b (int or float)
      operator_fn (function)
    Return:
      String
    """
    result = operator_fn(a, b)
    return f"Given {a} and {b} the result of your operation is {result}"


if __name__ == "__main__":
    assert calculate(5, 10, lambda x, y: x + y) == "Given 5 and 10 the result of your operation is 15"
    assert calculate(5, 10, lambda x, y: x - y) == "Given 5 and 10 the result of your operation is -5"
    assert calculate(5, 10, lambda x, y: x * y) == "Given 5 and 10 the result of your operation is 50"
    assert calculate(5, 10, lambda x, y: x / y) == "Given 5 and 10 the result of your operation is 0.5"
    assert calculate(5, 10, lambda x, y: x % y) == "Given 5 and 10 the result of your operation is 5"


    def something_longer(x, y):
        return "some long code"


    assert calculate(5, 10, something_longer) == "Given 5 and 10 the result of your operation is some long code"

    print("TESTS PASSED")

    # wierd_but_possible = lambda arg1, arg2: "some expression value"
    # return_value = wierd_but_possible("apple","banana")
    # print(return_value)
