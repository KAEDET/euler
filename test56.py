def digitsum(n):
    sum_ = 0
    num_ = n
    while num_ != 0:
        sum_ += num_%10
        num_ = num_//10
    return sum_

    
if __name__ == "__main__":
    max_ = 0
    for i in range(1,100):
        for j in range(1,100):
            x = digitsum(i**j)
            if max_ < x:
                max_ = x
    print(max_)






"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""