from typing import List, Dict
from .character import character
from .archetypes import ArchetypeType, get_archetype_data, ARCHETYPE_DEFINITIONS

def list_archetypes() -> Dict[str, str]:
    """Returns a dictionary of archetype names and their descriptions."""
    return {
        chartype.name: data.description 
        for chartype, data in ARCHETYPE_DEFINITIONS.items()
    }

def create_investigator(name: str, archetype_name: str) -> character:
    """
    Creates a new investigator character.
    Raises ValueError if archetype_name is invalid.
    """
    try:
        archetype = ArchetypeType[archetype_name.upper()]
    except KeyError:
        valid_types = ", ".join([a.name for a in ArchetypeType])
        raise ValueError(f"Invalid archetype '{archetype_name}'. Valid types are: {valid_types}")
    
    return character(name, archetype)
