# My Solution
# class Solution:
#     def isPalindrome(self, string: str) -> bool:  
#         strings = "".join(s.lower() for s in string if s.isalnum()) 
#         return strings==strings[::-1]
    
    
# Python Interview - Using Stack
import collections

class Solution:
    def isPalindrome(self, string: str) -> bool:
        strings: Deque = collections.deque()
        # strings = []
        
        for char in string:
            if char.isalnum():
                strings.append(char.lower())
        
        while len(strings)>1:
            if strings.popleft() != strings.pop():
                return False
            
        return True
    
    
# Using Deque
import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # using deque data structure
        strs: Deque = collections.deque()
            
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
            
        return True
