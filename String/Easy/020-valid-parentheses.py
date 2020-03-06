def isValid(s: str) -> bool:
    # allowed_sums = [81, 184, 248]
    # stack = []
    #
    # for letter in s:
    #     if not len(stack) or ord(stack[-1]) + ord(letter) not in allowed_sums:
    #         stack.append(letter)
    #     if ord(stack[-1]) < ord(letter) and (ord(stack[-1]) + ord(letter) in allowed_sums):
    #         stack.pop()
    #
    # return stack == []

    bracket_map = {"(": ")", "[": "]", "{": "}"}
    open_par = {"(", "[", "{"}
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []

    # while "()" in s or "{}" in s or '[]' in s:
    #     s = s.replace("()", "").replace('{}', "").replace('[]', "")
    # return s == ''


string = '{}'
print(isValid(string))
