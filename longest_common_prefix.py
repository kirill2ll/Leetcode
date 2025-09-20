# https://leetcode.com/problems/longest-common-prefix/description/

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        first = strs[0]

        if len(strs) == 0:
            return output
        

        for i in range(len(first)):
                first_prefix = first[:i+1]
                is_common = True
                for word in strs:
                    if first_prefix != word[:i+1]:
                        is_common = False
                        break

                if is_common and (len(first_prefix) > len(output)): 
                    output = first_prefix
        
        return output
     

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["f"]))
    print(s.longestCommonPrefix(["c","acc","ccc"]))