class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def back_track(oc,cc,curr):
            
            if oc==cc==n:
                result.append(''.join(curr))
                
            if oc<n:
                curr.append('(')
                back_track(oc+1,cc,curr)
                curr.pop()
                
            if cc<oc:
                curr.append(')')
                back_track(oc,cc+1,curr)
                curr.pop()
                
                
        back_track(0,0,[])   
        
        return result
        
                            
                
        
                            
                