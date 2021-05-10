from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        arr = [(k,v) for k,v in count.items()]
        arr.sort(key = lambda x: x[1])
        arr.reverse()
        result=''
        for k,v in arr:
            result+=''.join(k*v)
        return result
