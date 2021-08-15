class Solution:
    def isPalindrome(self, string: str) -> bool:
        
#         strings = ""
#         for s in string:
#             if s.isalnum():
#                 strings += s.lower()
                
#         return strings==strings[::-1]
    
        strings = "".join(s.lower() for s in string if s.isalnum())
        
        return strings==strings[::-1]