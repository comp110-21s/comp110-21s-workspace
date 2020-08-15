"""Python module to create a zip file of a Python file or directory for grading.

Usage:

    python -m tools.submission [directory or file]

You should run this from within the root directory of a Python project. It will add
file(s) within the directory, or a given file, and ignore any paths ignored by the
directory's .gitignore file.
"""

import glob
import os
import re
import sys
from typing import Set
from zipfile import ZipFile
from .helpers import date_prefix

__author__ = "Kris Jordan <kris@cs.unc.edu>"


def main() -> None:
    """Entry point of script. Expects to be run as CLI program."""
    target = parse_args()
    targetted = expand_globs(".", target, {"**"}) if os.path.isdir(target) else expand_file(".", target)
    ignored = expand_globs(".", ".", readlines(".gitignore"))
    filtered = targetted.difference(ignored)
    create_zip(date_prefix("submission.zip"), filtered)


def parse_args() -> str:
    """Ensure correct command-line arguments are provided.

    Returns:
        Path of directory or file being bundled.
    """
    if len(sys.argv) < 2:
        print("Usage: python -m submission [directory or .py file]")
        sys.exit(1)
    return sys.argv[1]


def readlines(path: str) -> Set[str]:
    """Read the lines of a plaintext file into a set."""
    if not os.path.exists(path):
        return set()
    else:
        strip_comments_re = re.compile("#.+$")
        with open(path) as file:
            entries = set()
            for line in file.read().splitlines():
                line = strip_comments_re.sub("", line).strip()
                if line != "":
                    entries.add(line)
            return entries


def expand_globs(root: str, target: str, paths: Set[str]) -> Set[str]:
    """Produce a set of glob results relative to a path."""
    entries: Set[str] = set()
    abs_root: str = os.path.realpath(root)
    abs_target: str = os.path.realpath(os.path.join(abs_root, target))
    for path in paths:
        globbed_files = glob.glob(os.path.join(abs_target, path), recursive=True)
        for file in globbed_files:
            file_path = file.replace(f"{abs_root}{os.path.sep}", "")
            entries.add(file_path)
    return entries


def expand_file(root: str, target: str) -> Set[str]:
    """Produce a set of a single file for single-script submissions, normalized to relative path."""
    abs_root: str = os.path.realpath(root)
    abs_target: str = os.path.realpath(os.path.join(abs_root, target))
    rel_path: str = abs_target.replace(f"{abs_root}{os.path.sep}", "")
    return {rel_path}


def filter_prefixes(source: Set[str], filters: Set[str]) -> Set[str]:
    """Remove any who start with a path in filters set."""
    result: Set[str] = set()
    for path in source:
        not_filtered = True
        for prefix in filters:
            if path.startswith(prefix):
                not_filtered = False
                break
        if not_filtered:
            result.add(path)
    return result


def create_zip(zip_path: str, files: Set[str]) -> None:
    """Zip up all files in a set at zip_path.

    Args:
        zip_path: The path to the zip file to create.
        files: The set of files to add to the zip file created.

    Returns:
        None
    """
    with ZipFile(zip_path, 'w') as zip:
        for file in files:
            zip.write(file)


if __name__ == "__main__":
    main()
