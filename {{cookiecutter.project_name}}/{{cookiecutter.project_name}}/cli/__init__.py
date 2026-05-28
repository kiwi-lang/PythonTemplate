"""CLI entry point using argklass for command discovery."""

from __future__ import annotations

import argparse
import sys
from contextlib import contextmanager

from argklass.argformat import HelpAction, HelpActionException
from argklass.command import ParentCommand
from argklass.parallel import shutdown
from argklass.plugin import discover_module_commands, with_cache_location


def discover_commands():
    import {{cookiecutter.project_name}}.cli
    import {{cookiecutter.project_name}}.plugins

    return discover_module_commands(
        {{cookiecutter.project_name}}.cli,
        {{cookiecutter.project_name}}.plugins,
    ).found_commands


def build_parser(commands):
    parser = argparse.ArgumentParser(
        add_help=False,
        description="{{cookiecutter.description}}",
    )
    parser.add_argument(
        "-h", "--help", action=HelpAction, help="show this help message and exit"
    )

    subparsers = parser.add_subparsers(dest="command")

    ParentCommand.dispatch = dict()
    for k, command in commands.items():
        command.arguments(subparsers)

    return parser


def main(argv=None):
    """Entry point for the command line interface."""
    import {{cookiecutter.project_name}}

    with with_cache_location({{cookiecutter.project_name}}):
        commands = discover_commands()

        try:
            parser = build_parser(commands)
            parsed_args = parser.parse_args(argv)
        except HelpActionException:
            return 0

    cmd_name = parsed_args.command
    command = commands.get(cmd_name)

    if command is None:
        print(f"Action `{cmd_name}` not implemented")
        return -1

    returncode = command.execute(parsed_args)
    return returncode if returncode is not None else 0


def main_force(argv=None):
    r = main()
    shutdown()
    sys.exit(r)


if __name__ == "__main__":
    main_force()
