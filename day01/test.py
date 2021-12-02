#!/usr/bin/env python
from os.path import dirname
from unittest import TestLoader, TextTestRunner
from unittest.suite import TestSuite


def main() -> None:
    loader: TestLoader = TestLoader()
    start_dir: str = dirname(__file__)
    suite: TestSuite = loader.discover(start_dir)

    runner: TextTestRunner = TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    main()
