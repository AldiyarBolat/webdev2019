def array123(nums):
    a, b, c = 0, 0, 0
    for num in nums:
        if num == 1:
            a += 1
        elif num == 2:
            b += 1
        elif num == 3:
            c += 1

    if (a >= 1 and b >= 1 and c >= 1):
        return True
    return False