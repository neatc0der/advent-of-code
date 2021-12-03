#!/usr/bin/env python
import glob
from types import ModuleType
from typing import Dict, List

import importlib
import pkgutil


def import_submodules(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for _, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))
    return results


def main():
    print("run all solutions")
    for year in sorted(glob.glob("y*")):
        modules: Dict[str, ModuleType] = import_submodules(year)

        run_files: List[str] = list(sorted(glob.glob("*/**/run.py", recursive=True)))
        for f in run_files:
            package: str = f.replace("/", ".")[:-3]
            print()
            print(package.rpartition(".")[0])
            modules[package].main()


if __name__ == "__main__":
    main()
