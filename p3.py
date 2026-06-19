class solution:
    def isValid(s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack.pop() != mapping[ch]:
                    return False

        return len(stack) == 0