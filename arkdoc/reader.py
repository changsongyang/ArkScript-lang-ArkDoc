#!/usr/bin/env python3

import glob
import os.path
from typing import List, Generator

from .parser import Parser


def explore(folder: str) -> Generator[str, None, None]:
    supported_exts = ["txt", "ark", "cpp"]

    if os.path.isdir(folder):
        for ext in supported_exts:
            yield from glob.glob(f"{folder}/*.{ext}", recursive=True)
    elif os.path.isfile(folder) and os.path.splitext(folder)[1][1:] in supported_exts:
        yield folder
    else:
        raise RuntimeError(f"{folder} isn't a valid file or folder")


def parse_all_in(folder: str) -> List[Parser]:
    parsers = []
    for f in explore(folder):
        parsers.append(Parser(f))
    return parsers
