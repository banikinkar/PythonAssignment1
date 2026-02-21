## factorial of a number
def fact_rec(num):
    """
    computes the factorial of a given number
    :param num:
    :return:
    """
    if num == 0:
        return 1
    else:
        return num * fact_rec(num-1)

print(fact_rec(5))


