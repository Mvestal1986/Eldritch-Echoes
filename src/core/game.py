"""Core game engine implementation."""

from __future__ import annotations
from src.character.create import create_investigator, list_archetypes

import time


class Game:
    """Basic game class skeleton."""

    def __init__(self) -> None:
        self.running = False

    def process_input(self) -> None:
        input_str = input("Enter command: ")
        if input_str.lower() == "exit":
            self.running = False
            print("Exiting game...")
        elif input_str.lower() == "help":
            print("Available commands: exit, help")
        elif input_str.lower() == "create character":
            name = input("Enter character name: ")
            archetype = input("Enter character archetype: ")
            self.character = create_investigator(name, archetype)
            print("Character created successfully!")
        else:
            print(f"Unknown command: {input_str}. Type 'help' for available commands.")

    def update(self) -> None:
        """Update the game state."""

    def render(self) -> None:
        """Render the current game state."""

    def run(self, frame_limit: int = 1) -> None:
        """Start the main game loop.

        Parameters
        ----------
        frame_limit:
            Number of iterations to run the loop. Keeping this small ensures
            tests execute quickly and prevents an infinite loop during early
            development.
        """

        print("Starting Eldritch Echoes...")
        self.running = True

        frames = 0
        while self.running and frames < frame_limit:
            self.process_input()
            self.update()
            self.render()

            frames += 1
            time.sleep(0.01)
