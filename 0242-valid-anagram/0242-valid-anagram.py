class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_table = {}
        
        if len(s) != len(t):
            return False
        
        s_sorted, t_sorted = ''.join(sorted(s)), ''.join(sorted(t))
        
        if s_sorted == t_sorted:
            return True
        else:
            return False
        
#         for letter in s:
#             if letter in count_table:
#                 count_table[letter] += 1
#             else:
#                 count_table[letter] = 0
        
        
            
            