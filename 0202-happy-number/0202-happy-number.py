class Solution(object):
    def isHappy(self, n):

        string = str(n)
        
        def summer(string):
            ret = 0
            for num in string:
                ret += int(num)**2
            return str(ret)
        
        mem = set()
        
        while True:
            mem.add(string)
            string = summer(string)
            if int(string) == 1:
                return True
            if string in mem:
                return False
