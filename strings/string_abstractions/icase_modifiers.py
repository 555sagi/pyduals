from abc import ABC, abstractmethod

class ICaseModifiers(ABC):
    """Interface for casing transformations. Methods take no arguments as they modify self."""

    @abstractmethod
    def upper(self) -> "ICaseModifiers": 
        """
        Converts all alphabetic lowercase characters to uppercase.
        Takes no arguments; operates directly on the internal text data.
        """
        pass

    @abstractmethod
    def lower(self) -> "ICaseModifiers": 
        """
        Converts all alphabetic uppercase characters to lowercase.
        Takes no arguments; operates directly on the internal text data.
        """
        pass

    @abstractmethod
    def capitalize(self) -> "ICaseModifiers": 
        """
        Capitalizes only the very first character of the string and downcases the rest.
        Takes no arguments.
        """
        pass

    @abstractmethod
    def title(self) -> "ICaseModifiers": 
        """
        Converts the string into Title Case (uppercase first letter of every isolated word).
        Takes no arguments.
        """
        pass

    @abstractmethod
    def swapcase(self) -> "ICaseModifiers": 
        """
        Inverts case states: changes uppercase letters to lowercase, and lowercase to uppercase.
        Takes no arguments.
        """
        pass

    @abstractmethod
    def casefold(self) -> "ICaseModifiers": 
        """
        Aggressively removes all case distinctions for strict case-insensitive comparisons.
        Takes no arguments.
        """
        pass
