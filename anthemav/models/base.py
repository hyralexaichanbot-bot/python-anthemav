"""Base model interface for Anthem AV receivers."""

from abc import ABC, abstractmethod
from typing import Dict, List, Set


class BaseModel(ABC):
    """Base interface for all Anthem receiver models.

    This abstract class defines the contract that all model implementations
    must follow. Each model encapsulates model-specific configuration including
    command sets, zone configuration, and audio listening mode mappings.
    """

    @property
    @abstractmethod
    def model_series(self) -> str:
        """Return the model series identifier.

        Returns:
            str: Model series identifier (e.g., 'x20', 'x40', 'mdx')
        """
        pass

    @abstractmethod
    def get_zone_count(self, model_name: str) -> int:
        """Return the number of zones supported by this model.

        Args:
            model_name: The specific model name (e.g., 'MRX 520', 'MDX-8')

        Returns:
            int: Number of zones supported
        """
        pass

    @abstractmethod
    def get_available_input_numbers(self, model_name: str) -> List[int]:
        """Return list of available input numbers.

        Args:
            model_name: The specific model name

        Returns:
            List[int]: List of available input numbers, or empty list for all inputs
        """
        pass

    @property
    @abstractmethod
    def commands_to_query(self) -> List[str]:
        """Return list of commands to query during initialization.

        Returns:
            List[str]: Commands to query on device initialization
        """
        pass

    @property
    @abstractmethod
    def commands_to_ignore(self) -> List[str]:
        """Return list of commands to ignore for this model.

        Returns:
            List[str]: Commands that should not be sent to this model
        """
        pass

    @property
    @abstractmethod
    def alm_number_mapping(self) -> Dict[str, int]:
        """Return audio listening mode name to number mapping.

        Returns:
            Dict[str, int]: Mapping of listening mode names to numbers
        """
        pass

    @property
    def alm_restricted_models(self) -> List[str]:
        """Return list of model names with restricted listening modes.

        Returns:
            List[str]: Model names that have restricted listening mode lists
        """
        return []

    @property
    def alm_restricted(self) -> List[str]:
        """Return list of restricted listening mode values.

        Returns:
            List[str]: Restricted listening mode values
        """
        return []

    @property
    def zone_lookup(self) -> Dict[str, Dict[str, str]]:
        """Return zone-specific lookup table.

        Returns:
            Dict[str, Dict[str, str]]: Zone lookup table
        """
        return {}

    @property
    def lookup(self) -> Dict[str, Dict[str, str]]:
        """Return model-specific lookup table.

        Returns:
            Dict[str, Dict[str, str]]: Lookup table for model-specific commands
        """
        return {}
