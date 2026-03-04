"""Model implementation for Anthem x40 series receivers.

This includes MRX 540, 740, 1140 and AVM 70, 90 series receivers.
"""

from typing import Dict, List

from anthemav.models.base import BaseModel


# Audio Listening mode mapping for x40 series
ALM_NUMBER_X40 = {
    "None": 0,
    "AnthemLogic Cinema": 1,
    "AnthemLogic Music": 2,
    "Dolby Surround": 3,
    "DTS neural:X": 4,
    "DTS Virtual:X": 5,
    "All Channel Stereo": 6,
    "Mono": 7,
    "All Channel Mono": 8,
}

# Commands specific to x40 series
COMMANDS_X40 = ["PVOL", "WMAC", "EMAC", "IS1ARC", "GCFPB", "GCTXS"]

# Zone lookup table for x40 series (includes PVOL for percentage volume)
ZONELOOKUP_X40 = {
    "POW": {"description": "Zone Power", "0": "Off", "1": "On"},
    "VOL": {"description": "Zone Volume"},
    "INP": {"description": "Zone current input"},
    "MUT": {"description": "Zone mute", "0": "Unmuted", "1": "Muted"},
    "PVOL": {"description": "Zone Volume in percent"},
}

# Model-specific lookup table for x40 series
LOOKUP_X40 = {
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
        "03": "Dolby Surround",
        "04": "DTS neural:X",
        "05": "DTS Virtual:X",
        "06": "All Channel Stereo",
        "07": "Mono",
        "08": "All Channel Mono",
    },
    "Z1DYN": {
        "description": "Dolby digital dynamic range",
        "0": "Normal",
        "1": "Reduced",
        "2": "Late Night",
    },
    "Z1DIA": {"description": "Dolby digital dialog normalization (dB)"},
    "WMAC": {"description": "Wi-Fi MAC address"},
    "EMAC": {"description": "Ethernet MAC address"},
    "GCFPB": {"description": "Front Panel Brightness"},
    "GCTXS": {
        "description": "Tx status",
        "0": "Off",
        "1": "IP On",
        "2": "IP and RS232 on",
    },
}


class X40Model(BaseModel):
    """Model implementation for Anthem x40 series receivers."""

    @property
    def model_series(self) -> str:
        """Return the model series identifier."""
        return "x40"

    def get_zone_count(self, model_name: str) -> int:
        """Return the number of zones supported by x40 series.

        x40 series (MRX 540, 740, 1140, AVM 70, 90) supports 2 zones.

        Args:
            model_name: The specific model name

        Returns:
            int: 2 zones for all x40 series models
        """
        return 2

    def get_available_input_numbers(self, model_name: str) -> List[int]:
        """Return list of available input numbers.

        x40 series supports all inputs (no restrictions).

        Args:
            model_name: The specific model name

        Returns:
            List[int]: Empty list indicating all inputs are available
        """
        return []

    @property
    def commands_to_query(self) -> List[str]:
        """Return list of commands to query during initialization.

        x40 series queries: GCTXS (TX status), EMAC (Ethernet MAC), WMAC (Wi-Fi MAC)

        Returns:
            List[str]: Commands to query
        """
        return ["GCTXS", "EMAC", "WMAC"]

    @property
    def commands_to_ignore(self) -> List[str]:
        """Return list of commands to ignore for x40 series.

        x40 series should ignore x20 and MDX specific commands.

        Returns:
            List[str]: Commands to ignore
        """
        # Will be combined with MDX commands in protocol
        return ["IDN", "ECH", "SIP", "Z1ARC", "FPB", "MAC"]

    @property
    def alm_number_mapping(self) -> Dict[str, int]:
        """Return audio listening mode name to number mapping for x40 series.

        Returns:
            Dict[str, int]: Mapping of listening mode names to numbers
        """
        return ALM_NUMBER_X40

    @property
    def zone_lookup(self) -> Dict[str, Dict[str, str]]:
        """Return zone-specific lookup table for x40 series.

        Returns:
            Dict[str, Dict[str, str]]: Zone lookup table
        """
        return ZONELOOKUP_X40

    @property
    def lookup(self) -> Dict[str, Dict[str, str]]:
        """Return model-specific lookup table for x40 series.

        Returns:
            Dict[str, Dict[str, str]]: Lookup table for x40-specific commands
        """
        return LOOKUP_X40
