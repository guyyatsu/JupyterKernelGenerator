#!/bin/python3
"""
Jupyter Notebook Custom Kernel Generator.

"""


from argparse   import ArgumentParser
from subprocess import run
from re         import match


if __name__ == "__main__":
    arguments = ArgumentParser()
    arguments.add_argument("-n", "--name", required=True,
        help=""" Accepts a string as an (assumed valid) UNIX directory file. """
    )

    arguments = arguments.parse_args()
    name = str(arguments.name)

    if match("^(/[^/ ]*)+/?$", arguments.name) is not None:
        filepath, name = arguments.name, arguments.name\
                                                  .split("/")[-1]
    else:
        filepath = arguments.name; name = filepath

    run(f"python3 -m venv {filepath}".split())
    run(f"source {filepath}/bin/activate".split())

    with open(f"{filepath}/requirements.txt", "a") as requirements:
        requirements.write("\nipykernel")

    run(f"pip install -r {filepath}/requirements.txt".split()))
    run(f"python3 -m ipykernel install --user --name={name}".split())