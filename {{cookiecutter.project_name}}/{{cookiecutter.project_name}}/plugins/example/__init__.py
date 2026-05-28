"""Example plugin — discovered automatically by the CLI."""

from dataclasses import dataclass

from argklass.command import Command


@dataclass
class Hello(Command):
    """Say hello (example plugin command)."""

    name: str = "world"

    def execute(self, args):
        print(f"Hello, {args.name}!")
