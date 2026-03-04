"""Model implementation for Anthem x20 series receivers."""

from typing import Dict, List

from anthemav.models.base import BaseModel

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

COMMANDS_X20 = ["IDN", "ECH", "SIP", "Z1ARC", "FPB"]
ALM_RESTRICTED = ["00", "01", "02", "03", "04", "05", "06", "07"]
ALM_RESTRICTED_MODEL = ["MRX 520"]

ZONELOOKUP_X20 = {
    "POW": {"description": "Zone Power", "0": "Off", "1": "On"},
    "VOL": {"description": "Zone Volume"},
    "INP": {"description": "Zone current input"},
    "MUT": {"description": "Zone mute", "0": "Unmuted", "1": "Muted"},
}

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
        return "x20"

    def get_zone_count(self, model_name: str) -> int:
        return 2

    def get_available_input_numbers(self, model_name: str) -> List[int]:
        return []

    @property
    def commands_to_query(self) -> List[str]:
        return ["ECH", "IDN"]

    @property
    def commands_to_ignore(self) -> List[str]:
        return ["PVOL", "WMAC", "EMAC", "IS1ARC", "GCFPB", "GCTXS", "MAC"]

    @property
    def alm_number_mapping(self) -> Dict[str, int]:
        return ALM_NUMBER_X20

    @property
    def alm_restricted(self) -> List[str]:
        return ALM_RESTRICTED

    @property
    def alm_restricted_models(self) -> List[str]:
        return ALM_RESTRICTED_MODEL

    @property
    def zone_lookup(self) -> Dict[str, Dict[str, str]]:
        return ZONELOOKUP_X20

    @property
    def lookup(self) -> Dict[str, Dict[str, str]]:
        return LOOKUP_X20
