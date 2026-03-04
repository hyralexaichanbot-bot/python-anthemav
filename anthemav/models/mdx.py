"""Model implementation for Anthem MDX series amplifiers.

This includes MDX-8 and MDX-16 multi-channel amplifiers.
"""

from typing import Dict, List

from anthemav.models.base import BaseModel


# MDX series does not support audio listening modes
ALM_NUMBER_MDX = {
    "None": 0,
}

# Commands specific to MDX series
COMMANDS_MDX = ["MAC"]

# Commands to ignore for MDX series (most zone-specific commands don't apply)
COMMANDS_MDX_IGNORE = [
    "IDR",
    "ICN",
    "Z1AIC",
    "Z1AIN",
    "Z1AIR",
    "Z1ALM",
    "Z1BRT",
    "Z1DIA",
    "Z1DYN",
    "Z1IRH",
    "Z1IRV",
    "Z1VIR",
]

# Zone lookup table for MDX series
ZONELOOKUP_MDX = {
    "POW": {"description": "Zone Power", "0": "Off", "1": "On"},
    "VOL": {"description": "Zone Volume"},
    "INP": {"description": "Zone current input"},
    "MUT": {"description": "Zone mute", "0": "Unmuted", "1": "Muted"},
}

# Model-specific lookup table for MDX series
LOOKUP_MDX = {
    "IDR": {"description": "Region"},
    "IDM": {"description": "Model"},
    "IDS": {"description": "Software version"},
    "IDB": {"description": "Software build date"},
    "IDH": {"description": "Hardware version"},
    "MAC": {"description": "MAC address"},
}


class MDXModel(BaseModel):
    """Model implementation for Anthem MDX series amplifiers."""

    @property
    def model_series(self) -> str:
        """Return the model series identifier."""
        return "mdx"

    def get_zone_count(self, model_name: str) -> int:
        """Return the number of zones supported by MDX series.

        MDX-16 supports 8 zones, MDX-8 supports 4 zones.

        Args:
            model_name: The specific model name (e.g., 'MDX-16', 'MDX-8')

        Returns:
            int: Number of zones (8 for MDX-16, 4 for MDX-8)
        """
        if "16" in model_name:
            return 8
        elif "8" in model_name:
            return 4
        # Default to 4 zones if model name is unclear
        return 4

    def get_available_input_numbers(self, model_name: str) -> List[int]:
        """Return list of available input numbers for MDX series.

        MDX-8 has limited input numbers: 1, 2, 3, 4, 9

        Args:
            model_name: The specific model name

        Returns:
            List[int]: List of available input numbers, or empty list for all
        """
        if "8" in model_name:
            return [1, 2, 3, 4, 9]
        return []

    @property
    def commands_to_query(self) -> List[str]:
        """Return list of commands to query during initialization.

        MDX series queries: MAC (MAC address)

        Returns:
            List[str]: Commands to query
        """
        return ["MAC"]

    @property
    def commands_to_ignore(self) -> List[str]:
        """Return list of commands to ignore for MDX series.

        MDX series ignores most zone-specific commands that don't apply
        to multi-channel amplifiers.

        Returns:
            List[str]: Commands to ignore
        """
        # Will be combined with x20/x40 commands in protocol
        return COMMANDS_MDX_IGNORE.copy()

    @property
    def alm_number_mapping(self) -> Dict[str, int]:
        """Return audio listening mode name to number mapping for MDX series.

        MDX series does not support audio listening modes.

        Returns:
            Dict[str, int]: Minimal mapping with just "None"
        """
        return ALM_NUMBER_MDX

    @property
    def zone_lookup(self) -> Dict[str, Dict[str, str]]:
        """Return zone-specific lookup table for MDX series.

        Returns:
            Dict[str, Dict[str, str]]: Zone lookup table
        """
        return ZONELOOKUP_MDX

    @property
    def lookup(self) -> Dict[str, Dict[str, str]]:
        """Return model-specific lookup table for MDX series.

        Returns:
            Dict[str, Dict[str, str]]: Lookup table for MDX-specific commands
        """
        return LOOKUP_MDX
