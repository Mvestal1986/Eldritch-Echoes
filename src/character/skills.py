from enum import Enum, auto
from dataclasses import dataclass, field
from typing import Dict, Any

class SkillType(Enum):
    INVESTIGATION = auto()
    OCCULT = auto()
    PSYCHOLOGY = auto()
    MEDICINE = auto()
    STEALTH = auto()
    ATHLETICS = auto()
    ARCHAEOLOGY = auto()
    HISTORY = auto()
    INTIMIDATION = auto()
    PERSUASION = auto()

@dataclass
class SkillSheet:
    skills: Dict[SkillType, int] = field(default_factory=lambda: {skill: 20 for skill in SkillType})

    def get_skill_level(self, skill: SkillType) -> int:
        return self.skills.get(skill, 0)
    
    def set_skill_level(self, skill: SkillType, level: int):
        self.skills[skill] = max(0, min(99, level))

    def improve_skill(self, skill: SkillType, amount: int):
        current = self.get_skill_level(skill)
        self.set_skill_level(skill, current + amount)
