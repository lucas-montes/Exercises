class Solution:
    def romanToInt(self, s: str) -> int:
        letter_int_map = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        num_letters = len(s)
        total = 0
        skip_next = False
        for index, letter in enumerate(s):
            if skip_next:
                skip_next = False
                continue
            value = letter_int_map[letter]
            next_index = index + 1
            if next_index != num_letters:
                next_letter = s[next_index]
                if letter == "I":
                    if next_letter == "V":
                        value = 4
                        skip_next = True
                    elif next_letter == "X":
                        value = 9
                        skip_next = True
                elif letter == "X" :
                    if next_letter == "L":
                        value = 40
                        skip_next = True
                    elif next_letter == "C":
                        value = 90
                        skip_next = True
                elif letter == "C":
                    if next_letter == "D":
                        value = 400
                        skip_next = True
                    elif next_letter == "M":
                        value = 900
                        skip_next = True
            total += value
        return total




# Runtime 36ms memory 13.9 MB