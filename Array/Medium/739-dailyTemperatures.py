def dailyTemperatures(T):
    N = len(T)
    stack = []
    ans = [0] * N
    for i in range(N):
        while stack and T[i] > T[stack[-1]]:
            ans[stack.pop()] = i - stack[-1]
        stack.append(i)
    return ans


T = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(T))
