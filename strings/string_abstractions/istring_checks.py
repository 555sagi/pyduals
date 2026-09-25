from abc import ABC, abstractmethod

class IStringChecks(ABC):
    """Interface for true/false validation checks. Methods take no parameters and return a bool."""

    @abstractmethod
    def isalnum(self) -> bool: 
        """Checks if all characters are alphanumeric (letters or numbers) and string is not empty."""
        pass

    @abstractmethod
    def isalpha(self) -> bool: 
        """Checks if all characters are alphabetic letters and string is not empty."""
        pass

    @abstractmethod
    def isascii(self) -> bool: 
        """Checks if the string is empty or contains only valid ASCII characters."""
        pass

    @abstractmethod
    def isdecimal(self) -> bool: 
        """Checks if all characters are base-10 decimals (0-9)."""
        pass

    @abstractmethod
    def isdigit(self) -> bool: 
        """Checks if all characters are digits (includes superscripts/subscripts)."""
        pass

    @abstractmethod
    def isnumeric(self) -> bool: 
        """Checks if all characters are numeric (includes fractions, roman numerals, etc.)."""
        pass

    @abstractmethod
    def isidentifier(self) -> bool: 
        """Checks if the string can function as a valid Python keyword, variable, or class name."""
        pass

    @abstractmethod
    def islower(self) -> bool: 
        """Checks if all cased letters in the string are lowercase (ignores symbols/numbers)."""
        pass

    @abstractmethod
    def isupper(self) -> bool: 
        """Checks if all cased letters in the string are uppercase (ignores symbols/numbers)."""
        pass

    @abstractmethod
    def istitle(self) -> bool: 
        """Checks if the string properly follows Title Case formatting requirements."""
        pass

    @abstractmethod
    def isspace(self) -> bool: 
        """Checks if the string contains exclusively whitespace symbols (spaces, tabs, newlines)."""
        pass

    @abstractmethod
    def isprintable(self) -> bool: 
        """Checks if all characters can be rendered visually (returns False for hidden control bytes)."""
        pass
