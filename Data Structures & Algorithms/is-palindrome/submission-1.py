class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        midway = len(s) // 2
        first = s[:midway].lower()
        second = s[midway:].lower()

        if len(first) > len(second):
            first = first[:-1] 
        if len(first) < len(second):
            second = second[1:]
        second = second[::-1]


        if first == second:
            return True
        else:
            return False
