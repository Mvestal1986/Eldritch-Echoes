
import random
from typing import Optional
from .archetypes import ArchetypeType, get_archetype_data, ArchetypeData
from .skills import SkillSheet, SkillType

class character:
    def __init__(self, name: str, archetype: ArchetypeType = ArchetypeType.DETECTIVE, level: int = 1):
        self.name = name
        self.level = level
        self.experience = 0
        self.backstory = ""
        self.archetype = archetype
        
        # Initialize stats based on archetype
        archetype_data = get_archetype_data(archetype)
        self.base_health = 100 + archetype_data.starting_health_mod
        self.base_sanity = 100 + archetype_data.starting_sanity_mod
        
        # Apply level scaling
        self.health = self.base_health + (level - 1) * 20
        self.sanity = self.base_sanity + (level - 1) * 10
        
        # Initialize skills
        self.skills = SkillSheet()
        for skill, bonus in archetype_data.skill_bonuses.items():
            self.skills.improve_skill(skill, bonus)
            
        print(f"Character {self.name} ({archetype_data.name}) created at level {self.level}.")

    def set_name(self, name: str):
        self.name = name
        print(f"Character's name has been set to {self.name}.")

    def set_level(self, level: int):
        self.level = level
        # Recalculate max stats based on new level
        max_health = self.base_health + (level - 1) * 20
        max_sanity = self.base_sanity + (level - 1) * 10
        
        # Adjust current values proportionally or reset them? For now, let's reset to max like original code implied but maybe safely
        self.health = max_health
        self.sanity = max_sanity
        print(f"{self.name} is now at level {self.level} with {self.health} health and {self.sanity} sanity.")

    def get_info(self):
        archetype_name = get_archetype_data(self.archetype).name
        return {
            "name": self.name,
            "archetype": archetype_name,
            "level": self.level,
            "health": self.health,
            "sanity": self.sanity,
            "experience": self.experience,
            "backstory": self.backstory,
            "skills": self.skills.skills
        }    

    def set_backstory(self, backstory: str):
        self.backstory = backstory
        print(f"{self.name}'s backstory has been set.")

    def level_up(self):
        self.level += 1
        # Increase max stats
        self.health += 20
        self.sanity += 10
        print(f"{self.name} has leveled up to level {self.level}!")

    def take_damage(self, amount: int):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
            self.health = 0

    def heal(self, amount: int):
        self.health += amount
        print(f"{self.name} has healed for {amount} health points.")

    def lose_sanity(self, amount: int):
        self.sanity -= amount
        if self.sanity <= 0:
            print(f"{self.name} has lost all sanity!")
            self.sanity = 0
    
    def regain_sanity(self, amount: int):
        self.sanity += amount
        print(f"{self.name} has regained {amount} sanity points.")

    def gain_experience(self, amount: int):
        self.experience += amount
        print(f"{self.name} has gained {amount} experience points.")
        if self.experience >= 100:
            self.level_up()
            self.experience -= 100

    def roll_skill(self, skill: SkillType) -> bool:
        skill_level = self.skills.get_skill_level(skill)
        roll = random.randint(1, 100)
        print(f"Rolling {skill.name}... Rolled: {roll} vs Skill: {skill_level}")
        return roll <= skill_level
