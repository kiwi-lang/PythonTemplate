"""Built-in CLI commands."""

from dataclasses import dataclass

from argklass.command import Command


@dataclass
class Serve(Command):
    """Start the development server."""

    host: str = "0.0.0.0"
    port: int = 5001

    def execute(self, args):
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
