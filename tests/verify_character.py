import sys
import os

# Add src to path so we can import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from character.create import create_investigator, list_archetypes
from character.skills import SkillType

def verify_creation():
    print("Available Archetypes:")
    for name, desc in list_archetypes().items():
        print(f"- {name}: {desc}")
    
    print("\nCreating a Detective named 'Sherlock'...")
    sherlock = create_investigator("Sherlock", "DETECTIVE")
    
    info = sherlock.get_info()
    print("\nCharacter Info:")
    for key, value in info.items():
        if key == 'skills':
            print("Skills (showing non-default > 20):")
            for skill, level in value.items():
                if level > 20:
                    print(f"  - {skill.name}: {level}")
        else:
            print(f"{key}: {value}")
            
    # Verify Detective bonuses
    # Detective gets +10 Health (110 total)
    assert info['health'] == 110, f"Expected 110 health, got {info['health']}"
    # Detective gets +20 Investigation (40 total)
    inv_level = sherlock.skills.get_skill_level(SkillType.INVESTIGATION)
    assert inv_level == 40, f"Expected 40 Investigation, got {inv_level}"
    
    print("\nVerification Successful!")

if __name__ == "__main__":
    verify_creation()
