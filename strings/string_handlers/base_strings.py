from strings.string_abstractions.ibase_strings import IBaseString


class BaseStrings(IBaseString):

    def __init__(self, string: str):
        self.given_string = string

    def replace(self, old: str, new: str, count: int = -1) -> str:
        
        # CASE_ZERO: Edge case protection against an empty 'old' and new string (prevents infinite loop)
        if old == "":
            raise ValueError("replace() argument, 'old' cannot be an empty string")
        
        if new == "":
            raise ValueError("replace() argument, 'new' cannot be an empty string")
        
        
        # CASE_ONE: What if the substring, old not exist in given String
        if old not in self.given_string:
            return self.given_string

        # CASE2:What if the substring, old exist in given string
        new_str = ""
        start = 0
        end = len(old)
        given_string_len = len(self.given_string)
        count_utilization = 0

        while start < given_string_len:
            if self.given_string[start : start + end] == old and (
                count == -1 or count > count_utilization
            ):
                new_str += new
                start += end
                count_utilization += 1
            else:
                new_str += self.given_string[start]
                start += 1

        return new_str

    def find(self, sub:str , start:int = 0 , end:int = -1 ):

        # Case Zero: The Substrig not exists , The Provided String
        if sub not in self.given_string:
            return -1
        # Case One: What if The argument Sub is Empty String
        if len(sub) == 0:
            raise ValueError("The Sub-String can not be Empty")

