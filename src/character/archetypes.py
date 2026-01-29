from enum import Enum, auto
from dataclasses import dataclass
from typing import Dict
from .skills import SkillType

class ArchetypeType(Enum):
    DETECTIVE = auto()
    PROFESSOR = auto()
    JOURNALIST = auto()
    DOCTOR = auto()
    OCCULTIST = auto()

@dataclass
class ArchetypeData:
    name: str
    description: str
    starting_sanity_mod: int
    starting_health_mod: int
    skill_bonuses: Dict[SkillType, int]

ARCHETYPE_DEFINITIONS = {
    ArchetypeType.DETECTIVE: ArchetypeData(
        name="Detective",
        description="A shrewd investigator used to digging up the truth.",
        starting_sanity_mod=0,
        starting_health_mod=10,
        skill_bonuses={
            SkillType.INVESTIGATION: 20,
            SkillType.INTIMIDATION: 10,
            SkillType.PSYCHOLOGY: 10
        }
    ),
    ArchetypeType.PROFESSOR: ArchetypeData(
        name="Professor",
        description="An academic with knowledge of ancient history and obscure texts.",
        starting_sanity_mod=10,
        starting_health_mod=-5,
        skill_bonuses={
            SkillType.ARCHAEOLOGY: 20,
            SkillType.HISTORY: 20,
            SkillType.OCCULT: 10
        }
    ),
    ArchetypeType.JOURNALIST: ArchetypeData(
        name="Journalist",
        description="A reporter who knows how to get people to talk.",
        starting_sanity_mod=0,
        starting_health_mod=0,
        skill_bonuses={
            SkillType.PERSUASION: 20,
            SkillType.PSYCHOLOGY: 10,
            SkillType.INVESTIGATION: 10
        }
    ),
    ArchetypeType.DOCTOR: ArchetypeData(
        name="Doctor",
        description="A medical professional sworn to save lives.",
        starting_sanity_mod=5,
        starting_health_mod=0,
        skill_bonuses={
            SkillType.MEDICINE: 30,
            SkillType.PSYCHOLOGY: 10
        }
    ),
     ArchetypeType.OCCULTIST: ArchetypeData(
        name="Occultist",
        description="One who dabbles in the forbidden arts.",
        starting_sanity_mod=-10,
        starting_health_mod=-5,
        skill_bonuses={
            SkillType.OCCULT: 30,
            SkillType.HISTORY: 10
        }
    ),
}

def get_archetype_data(archetype: ArchetypeType) -> ArchetypeData:
    return ARCHETYPE_DEFINITIONS.get(archetype)
