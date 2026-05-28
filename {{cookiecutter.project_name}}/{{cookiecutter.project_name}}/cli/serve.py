"""Built-in CLI commands."""

from dataclasses import dataclass

from argklass.arguments import add_arguments
from argklass.command import Command, newparser


@dataclass 
class Arguments:
    host: str = "0.0.0.0"
    port: int = 5001


class Serve(Command):
    """Start the development server."""

    name: str = "serve"

    @staticmethod
    def arguments(subparsers):
        parser = newparser(subparsers, Serve)
        add_arguments(parser, Arguments)
    
    def execute(self, args: Arguments):
        from {{cookiecutter.project_name}}.server.run import main
        import os

        os.environ["HOST"] = args.host
        os.environ["PORT"] = str(args.port)
        main()


@dataclass
class Version(Command):
    """Print the current version."""

    def execute(self, args):
        print("{{cookiecutter.version}}")


COMMANDS = [Serve]