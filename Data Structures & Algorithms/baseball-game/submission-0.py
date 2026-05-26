class Solution:
    def calPoints(self, operations: List[str]) -> int:

        st = []

        for op in operations:

            if op not in {'+', 'C', 'D'}:

                st.append(op)
                continue
            
            if op == '+' and len(st) >= 2:

                first = st[-1]
                second = st[-2]

                result = str(int(first) + int(second))

                st.append(result)
            
            elif op == 'C' and len(st) > 0:

                st.pop()
            
            elif op == 'D' and len(st) > 0:

                st.append(str(int(st[-1]) * 2))
            
        
        result = 0
        for c in st:
            result += int(c)
        
        return result

            
        