from abc import ABC, abstractmethod
from typing import Any, Iterable

class IBaseString(ABC):
    """Interface for structural string content inspections, mutations, and splits."""

    @abstractmethod
    def replace(self, old: str, new: str, count: int = -1) -> "IBaseString": 
        """
        Replaces occurrences of a substring with another substring.
        
        Parameters:
        - old (str): The target substring you want to find and replace.
        - new (str): The new string that will swap into the old substring's place.
        - count (int): Maximum replacements to perform. Defaults to -1 (replace all).
        """
        pass

    #@abstractmethod
    #def count(self, sub: str, start: int = 0, end: int = -1) -> int: 
        #"""
        #Counts the non-overlapping occurrences of a substring.
        
        #Parameters:
        #- sub (str): The substring to search for.
        #- start (int): The starting index slice to begin searching. Defaults to 0.
        #- end (int): The ending index slice boundary. Defaults to -1 (end of string).
        #"""
        #pass

    #@abstractmethod
    #def find(self, sub: str, start: int = 0, end: int = -1) -> int: 
        #"""
        #Finds the lowest index where a substring is found. Returns -1 if not found.
        
        #Parameters:
        #- sub (str): The target substring to look for.
        #- start (int): Starting index slice boundary. Defaults to 0.
        #- end (int): Ending index slice boundary. Defaults to -1.
        #"""
        #pass

    #@abstractmethod
    #def rfind(self, sub: str, start: int = 0, end: int = -1) -> int: 
        #"""
        #Finds the highest (rightmost) index where a substring is found. Returns -1 if not found.
        
        #Parameters:
        #- sub (str): The target substring to search for.
        #- start (int): Starting index slice boundary. Defaults to 0.
        #- end (int): Ending index slice boundary. Defaults to -1.
        #"""
        #pass

    #@abstractmethod
    #def index(self, sub: str, start: int = 0, end: int = -1) -> int: 
        #"""
        #Like find(), but raises a ValueError if the substring is not found.
        
        #Parameters:
        #- sub (str): The target substring to look for.
        #- start (int): Starting index slice boundary. Defaults to 0.
        #- end (int): Ending index slice boundary. Defaults to -1.
        #"""
        #pass

    #@abstractmethod
    #def rindex(self, sub: str, start: int = 0, end: int = -1) -> int: 
        #"""
        #Like rfind(), but raises a ValueError if the substring is not found.
        
        #Parameters:
        #- sub (str): The target substring to search for.
        #- start (int): Starting index slice boundary. Defaults to 0.
        #- end (int): Ending index slice boundary. Defaults to -1.
        #"""
        #pass

    #@abstractmethod
    #def split(self, sep: str = None, maxsplit: int = -1) -> list: 
        #"""
        #Splits the string into a list of substrings using a specified delimiter.
        
        #Parameters:
        #- sep (str): The delimiter string used to split on. If None, splits on any consecutive whitespace.
        #- maxsplit (int): Maximum splits to do. Defaults to -1 (unlimited splits).
        #"""
        #pass

    #@abstractmethod
    #def rsplit(self, sep: str = None, maxsplit: int = -1) -> list: 
        #"""
        #Splits the string starting from the right side using a specified delimiter.
        
        #Parameters:
        #- sep (str): The delimiter string used to split on. If None, splits on whitespace.
        #- maxsplit (int): Maximum splits to do from the right. Defaults to -1.
        #"""
        #pass

    #@abstractmethod
    #def splitlines(self, keepends: bool = False) -> list: 
        #"""
        #Splits the string at line breaks (\\n, \\r, etc.).
        
        #Parameters:
        #- keepends (bool): If True, line break characters are kept inside the resulting strings. Defaults to False.
        #"""
        #pass

    #@abstractmethod
    #def join(self, iterable: Iterable[Any]) -> "IBaseString": 
        #"""
        #Concatenates an iterable of strings using this current string as the separator.
        
        #Parameters:
        #- iterable (Iterable): A collection (list, tuple, etc.) containing elements to string together.
        #"""
        #pass

    #@abstractmethod
    #def strip(self, chars: str = None) -> "IBaseString": 
        #"""
        #Trims symbols out from both the leading and trailing edges of the string.
        
        #Parameters:
        #- chars (str): A string specifying the set of characters to strip. If None, strips whitespace.
        #"""
        #pass

    #@abstractmethod
    #def lstrip(self, chars: str = None) -> "IBaseString": 
        #"""
        #Trims symbols out from only the leading (left) edge of the string.
        
        #Parameters:
        #- chars (str): Specific characters to drop. Defaults to None (all whitespaces).
        #"""
        #pass

    #@abstractmethod
    #def rstrip(self, chars: str = None) -> "IBaseString": 
        #"""
        #Trims symbols out from only the trailing (right) edge of the string.
        
        #Parameters:
        #- chars (str): Specific characters to drop. Defaults to None (all whitespaces).
        #"""
        #pass

    #@abstractmethod
    #def startswith(self, prefix: str, start: int = 0, end: int = -1) -> bool: 
        #"""
        #Checks if the string begins with a specific prefix substring.
        
        #Parameters:
        #- prefix (str): The exact string pattern you want to match at the beginning.
        #- start (int): Index position to start the evaluation from. Defaults to 0.
        #- end (int): Index position to end the evaluation at. Defaults to -1.
        #"""
        #pass

    #@abstractmethod
    #def endswith(self, suffix: str, start: int = 0, end: int = -1) -> bool: 
        #"""
        #Checks if the string ends with a specific suffix substring.
        
        #Parameters:
        #- suffix (str): The exact string pattern you want to match at the end.
        #- start (int): Index position to start evaluation boundaries. Defaults to 0.
        #- end (int): Index position to end evaluation boundaries. Defaults to -1.
        #"""
        #pass

    #@abstractmethod
    #def removeprefix(self, prefix: str) -> "IBaseString": 
        #"""
        #Removes a prefix if it exists, otherwise returns the original string unchanged.
        
        #Parameters:
        #- prefix (str): The exact substring chunk to slice off from the front.
        #"""
        #pass

    #@abstractmethod
    #def removesuffix(self, suffix: str) -> "IBaseString": 
        #"""
        #Removes a suffix if it exists, otherwise returns the original string unchanged.
        
        #Parameters:
        #- suffix (str): The exact substring chunk to slice off from the back.
        #"""
        #pass 
        
    
