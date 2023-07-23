class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        input_list = list(s)
        to_reverse = []
        for i, val in enumerate(input_list):
            if val.lower() in vowels:
                input_list[i] = ""
                to_reverse.append(val)
        for i, val in enumerate(input_list):
            if val == "":
                input_list[i] = to_reverse.pop()
        return "".join(input_list)
