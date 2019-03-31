def sum67(nums):
    b = True
    sum = 0

    for n in nums:
        if n == 6:
            b = False

        if b == True:
            sum += n
            continue

        if n == 7:
            b = True

    return sum