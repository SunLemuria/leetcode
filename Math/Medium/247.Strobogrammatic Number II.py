# 找到所有长度为 n 的中心对称数
'''
当 n=0 的时候，应该输出空字符串：“ ”。
当 n=1 的时候，也就是长度为 1 的中心对称数有：0，1，8。
当 n=2 的时候，长度为 2 的中心对称数有：11， 69，88，96。注意：00 并不是一个合法的结果。
当 n=3 的时候，只需要在长度为 1 的合法中心对称数的基础上，不断地在两边添加 11，69，88，96 就可以了。
[101, 609, 808, 906,     111, 619, 818, 916,     181, 689, 888, 986]
随着 n 不断地增长，我们只需要在长度为 n-2 的中心对称数两边添加 11，69，88，96 即可。
'''


# recursion
def findStrobogrammatic(n):
    return helper(n, n)


def helper(n, m):
    # 第一步：判断输入或者状态是否非法？
    if n < 0 or m < 0 or n > m:
        raise Exception("invalid input")
    # 第二步：判读递归是否应当结束?
    if n == 0:
        return ['']
    if n == 1:
        return ["0", "1", "8"]

    # 第三步：缩小问题规模
    l = helper(n - 2, m)

    # 第四步: 整合结果
    res = []

    for s in l:
        if n != m:  # 防止1001的情况
            res.append("0" + s + "0")
        res.append("1" + s + "1")
        res.append("6" + s + "9")
        res.append("8" + s + "8")
        res.append("9" + s + "6")

    return res


print(findStrobogrammatic(4))
