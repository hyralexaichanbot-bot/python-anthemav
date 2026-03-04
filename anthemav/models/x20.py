"""Model implementation for Anthem x20 series receivers.

This includes MRX 520, 720, 1120 and AVM 60 series receivers.
"""

from typing import Dict, List

from anthemav.models.base import BaseModel


# Audio Listening mode mapping for x20 series
ALM_NUMBER_X20 = {
    "None": 0,
    "AnthemLogic Cinema": 1,
    "AnthemLogic Music": 2,
    "PLII Movie": 3,
    "PLII Music": 4,
    "Neo Cinema": 5,
    "Neo Music": 6,
    "All Channel": 7,
    "All Channel Mono": 8,
    "Mono": 9,
    "Mono-Academy": 10,
    "Mono (L)": 11,
    "Mono (R)": 12,
    "High Blend": 13,
    "Dolby Surround": 14,
}

# Commands specific to x20 series (not used by x20, used to ignore on other models)
COMMANDS_X20 = ["IDN", "ECH", "SIP", "Z1ARC", "FPB"]

# x20 series has restricted listening modes for some models
ALM_RESTRICTED = ["00", "01", "02", "03", "04", "05", "06", "07"]
ALM_RESTRICTED_MODEL = ["MRX 520"]

# Zone lookup table for x20 series
ZONELOOKUP_X20 = {
    "POW": {"description": "Zone Power", "0": "Off", "1": "On"},
    "VOL": {"description": "Zone Volume"},
    "INP": {"description": "Zone current input"},
    "MUT": {"description": "Zone mute", "0": "Unmuted", "1": "Muted"},
}

# Model-specific lookup table for x20 series
LOOKUP_X20 = {
    "IDR": {"description": "Region"},
    "IDM": {"description": "Model"},
    "IDS": {"description": "Software version"},
    "IDB": {"description": "Software build date"},
    "IDH": {"description": "Hardware version"},
    "ICN": {"description": "Active input count"},
    "Z1VIR": {
        "description": "Video input resolution",
        "0": "No video",
        "1": "Other",
        "2": "1080p60",
        "3": "1080p50",
        "4": "1080p24",
        "5": "1080i60",
        "6": "1080i50",
        "7": "720p60",
        "8": "720p50",
        "9": "576p50",
        "10": "576i50",
        "11": "480p60",
        "12": "480i60",
        "13": "3D",
        "14": "4K",
        "15": "4k50",
        "16": "4k24",
    },
    "Z1IRH": {"description": "Active horizontal video resolution (pixels)"},
    "Z1IRV": {"description": "Active vertical video resolution (pixels)"},
    "Z1AIC": {
        "description": "Audio input channels",
        "0": "No audio",
        "1": "Other",
        "2": "Mono (center channel)",
        "3": "2 channel",
        "4": "5.1 channel",
        "5": "6.1 channel",
        "6": "7.1 channel",
        "7": "Atmos",
    },
    "Z1AIF": {
        "description": "Audio input format",
        "0": "No audio",
        "1": "Analog",
        "2": "PCM",
        "3": "Dolby",
        "4": "DSD",
        "5": "DTS",
        "6": "Atmos",
    },
    "Z1BRT": {"description": "Audio input bitrate (kbps)"},
    "Z1SRT": {"description": "Audio input sampling rate (hKz)"},
    "Z1AIN": {"description": "Audio input name"},
    "Z1AIR": {"description": "Audio input rate name"},
    "Z1ALM": {
        "description": "Audio listening mode",
        "00": "None",
        "01": "AnthemLogic Cinema",
        "02": "AnthemLogic Music",
        "03": "PLII Movie",
        "04": "PLII Music",
        "05": "Neo Cinema",
        "06": "Neo Music",
        "07": "All Channel",
        "08": "All Channel Mono",
        "09": "Mono",
        "10": "Mono-Academy",
        "11": "Mono (L)",
        "12": "Mono (R)",
        "13": "High Blend",
        "14": "Dolby Surround",
        "15": "Neo Cinema",
        "16": "Neo Music",
    },
    "Z1DYN": {
        "description": "Dolby digital dynamic range",
        "0": "Normal",
        "1": "Reduced",
        "2": "Late Night",
    },
    "Z1DIA": {"description": "Dolby digital dialog normalization (dB)"},
    "IDN": {"description": "MAC address"},
    "ECH": {"description": "Tx status", "0": "Off", "1": "On"},
    "SIP": {"description": "Standby IP control", "0": "Off", "1": "On"},
    "Z1ARC": {"description": "Zone 1 ARC", "0": "Off", "1": "On"},
    "FPB": {
        "description": "Front Panel Brightness",
        "0": "Off",
        "1": "Low",
        "2": "Medium",
        "3": "High",
    },
}


class X20Model(BaseModel):
    """Model implementation for Anthem x20 series receivers."""

    @property
    def model_series(self) -> str:
        """Return the model series identifier."""
        return "x20"

    def get_zone_count(self, model_name: str) -> int:
        """Return the number of zones supported by x20 series.

        x20 series (MRX 520, 720, 1120, AVM 60) supports 2 zones.

        Args:
            model_name: The specific model name

        Returns:
            int: 2 zones for all x20 series models
        """
        return 2

    def get_available_input_numbers(self, model_name: str) -> List[int]:
        """Return list of available input numbers.

        x20 series supports all inputs (no restrictions).

        Args:
            model_name: The specific model name

        Returns:
            List[int]: Empty list indicating all inputs are available
        """
        return []

    @property
    def commands_to_query(self) -> List[str]:
        """Return list of commands to query during initialization.

        x20 series queries: ECH1 (enable TX), IDN (MAC address)

        Returns:
            List[str]: Commands to query
        """
        return ["ECH", "IDN"]

    @property
    def commands_to_ignore(self) -> List[str]:
        """Return list of commands to ignore for x20 series.

        x20 series should ignore x40 and MDX specific commands.

        Returns:
            List[str]: Commands to ignore
        """
        # Will be combined with MDX commands in protocol
        return ["PVOL", "WMAC", "EMAC", "IS1ARC", "GCFPB", "GCTXS", "MAC"]

    @property
    def alm_number_mapping(self) -> Dict[str, int]:
        """Return audio listening mode name to number mapping for x20 series.

        Returns:
            Dict[str, int]: Mapping of listening mode names to numbers
        """
        return ALM_NUMBER_X20

    @property
    def alm_restricted(self) -> List[str]:
        """Return list of restricted listening mode values for x20 series.

        Some x20 models (e.g., MRX 520) have restricted listening mode lists.

        Returns:
            List[str]: Restricted listening mode values
        """
        return ALM_RESTRICTED

    @property
    def alm_restricted_models(self) -> List[str]:
        """Return list of x20 model names with restricted listening modes.

        Returns:
            List[str]: Model names with restricted listening modes
        """
        return ALM_RESTRICTED_MODEL

    @property
    def zone_lookup(self) -> Dict[str, Dict[str, str]]:
        """Return zone-specific lookup table for x20 series.

        Returns:
            Dict[str, Dict[str, str]]: Zone lookup table
        """
        return ZONELOOKUP_X20

    @property
    def lookup(self) -> Dict[str, Dict[str, str]]:
        """Return model-specific lookup table for x20 series.

        Returns:
            Dict[str, Dict[str, str]]: Lookup table for x20-specific commands
        """
        return LOOKUP_X20
