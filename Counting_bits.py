class Solution:
    def countBits(self, num):
        output = []
        for i in range(0,num+1):
            output.append(list(bin(i)).count('1'))
        return output
