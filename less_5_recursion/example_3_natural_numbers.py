def values(n, current=1):
    if current <= n:
        print(current)
        values(current=current+1, n=n)


def check_pow_2(n):
    if n == 1:
        print("YES")
    else:
        if n % 2 == 0:
            check_pow_2(n // 2)
        else:
            print("NO")

def sum_val(num, res=0):
    if not num:
        return res
    res += num % 10
    num //= 10
    return sum_val(num, res)


print(sum_val(345))
