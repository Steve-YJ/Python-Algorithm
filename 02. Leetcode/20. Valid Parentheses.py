from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }
        
        dq = deque(s)
        entries = ["{", "[", "("]
        
        init = dq[0]
        left = dq.popleft()
        # print(f"initialize left: {left}")
        # print(f"dq: {dq}")
        for idx, elem in enumerate(dq):
            if dic[left] == elem:
                left = elem
            elif elem in entries:
                left = elem
            elif dic[init] == elem:
                return True
            else:
                return False
        return True