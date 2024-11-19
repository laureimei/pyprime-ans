def Unit1_slicing3():
    s1 = "Hello"
    s2 = "World"

    middle_index = len(s1) // 2

    first_half = s1[:middle_index]
    second_half = s1[middle_index:]

    s3 = first_half + s2 + second_half

    return s3


result = Unit1_slicing3()
print(result)
