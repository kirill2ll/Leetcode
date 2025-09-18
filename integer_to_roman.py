# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""
        num_arr = list(str(num))
        decreased_arr = list(num_arr)

        for _ in num_arr:
            current_output = ""
            current_num = int(decreased_arr.pop(0))
            numbers_left = len(decreased_arr)

            if current_num == 0:    
                continue
            elif current_num == 4:
                current_output += "IV"
            elif current_num == 9:
                current_output += "IX"

                if numbers_left == 1:
                    current_output = "XC"
                if numbers_left == 2:
                    current_output = "CM"
                output = output + current_output
                continue
            else:
                if current_num >= 5:
                    current_output += "V"
                    current_num -= 5
                while current_num > 0:
                        current_output += "I"
                        current_num -= 1

            if numbers_left == 1:
                current_output = current_output.replace("V", "L")
                current_output = current_output.replace("I", "X")
            if numbers_left == 2:
                current_output = current_output.replace("V", "D")
                current_output = current_output.replace("I", "C")
            if numbers_left == 3:
                current_output = current_output.replace("I", "M")

            output = output + current_output

        return output


if __name__ == "__main__":
    s = Solution()
    # print(s.intToRoman(3))     # Expected "III"
    # print(s.intToRoman(58))    # Expected "LVIII"
    # print(s.intToRoman(267))    # Expected "CCLXVII"
    # print(s.intToRoman(49))    # Expected "XLIX"
    print(s.intToRoman(99))    # Expected "XCIX"
    # print(s.intToRoman(444))    # Expected "CDXLIV"
    print(s.intToRoman(999))    # Expected "CMXCIX"
    print(s.intToRoman(1994))  # Expected "MCMXCIV"