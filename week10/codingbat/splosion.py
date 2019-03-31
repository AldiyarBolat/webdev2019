def string_splosion(str):
    n = 1
    res = ""
    for i in range(len(str)):
        res += str[:n]
        n += 1

    return res

