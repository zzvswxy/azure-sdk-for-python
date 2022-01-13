import platform
import json
import argparse
import urllib
import urllib.request
from subprocess import check_call, CalledProcessError
import sys
import os
import zipfile
import tarfile
import time

from packaging.version import Version
from packaging.version import InvalidVersion


MAX_INSTALLER_RETRY = 3
CURRENT_UBUNTU_VERSION = "20.04"  # full title is ubuntu-20.04
MAX_PRECACHED_VERSION = "3.10.0"

HOSTEDTOOLCACHE = os.getenv("")


def find_pypy_version(spec):
    discovered_locations = ["wat"]  # do work here

    if not discovered_installer_location:
        print(
            "Unable to locate a valid executable folder for {}. Examined folder {}".format(
                spec, HOSTEDTOOLCACHE
            )
        )
        exit(1)

    return []


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""This python script is used to discover and prepend a devops agent path with a specific pypy version. 
        It is not intended to be generic, and should not be be used in general "Use Python Version X" kind of situations."""
    )

    parser.add_argument(
        "version_spec",
        nargs="?",
        help=("The version specifier passed in to the UsePythonVersion extended task."),
    )

    args = parser.parse_args()
    max_precached_version = Version(MAX_PRECACHED_VERSION)
    try:
        version_from_spec = Version(args.version_spec)
    except InvalidVersion:
        print("Invalid Version '{}'. Exiting".format(args.version_spec))
        exit(1)

    discovered_installer_location = find_pypy_version(version_from_spec)

    print(
        "Path should be prepended with discovered location{} [{}]".format(
            ("s" if discovered_installer_location >= 2 else ""),
            ", ".join(discovered_installer_location),
        )
    )

    for path in discovered_installer_location:
        print("##vso[task.prependpath]{}".format(path))
