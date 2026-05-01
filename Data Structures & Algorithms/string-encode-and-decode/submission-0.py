class Solution:

    def encode(self, strs: List[str]) -> str:
        ss = ""

        for s in strs:
            ss += str(len(s)) + "#" + s # ex: 5#hello5#world

        return ss

    def decode(self, s: str) -> List[str]:
        output = [] # need a list of decoded strings
        i = 0
        
        while i < len(s):
            j = s.index('#', i) # find index of first # starting at i
            length = int(s[i:j]) # parse digits from i to # (exclusive)
            word = s[j+1 : j+1+length] # grab word after j
            output.append(word)
            i = j + 1 + length # move pointer to next digit

        return output

