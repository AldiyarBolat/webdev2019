def front_back(str):
    if len(str) <= 1:
        return str

    a = str[len(str) - 1]
    b = str[0]
    c = str[1:-1]

    return a + c + b