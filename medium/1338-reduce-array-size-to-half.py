# Time complexity (N + NlogN + N) --> O(NlogN)
# TODO Put some dank comments

from typing import List, Dict # to calm the linters

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        unique_dict_to_frequency: Dict[int, int] = {}
        
        for i in range(len(arr)):
            num = arr[i]
            if num not in unique_dict_to_frequency:
                unique_dict_to_frequency[num] = 1
            else:
                unique_dict_to_frequency[num] += 1
        
        half = len(arr) / 2
        currLength = len(arr)
        
        sortedValues = sorted(unique_dict_to_frequency.values(), reverse=True)
        
        i = 0
        while currLength > half:
            currLength -= sortedValues[i]
            i += 1
            if currLength <= half:
                break
                
        return i