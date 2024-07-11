class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        popped_ptr = 0
        stack = []
        
        for i in pushed:
            stack.append(i)
            while stack and popped_ptr < len(popped) and stack[-1] == popped[popped_ptr]:
                stack.pop()
                popped_ptr += 1
                
        return popped_ptr == len(popped)