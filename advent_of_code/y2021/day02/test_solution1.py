#!/usr/bin/env python
from typing import List
from unittest import main, TestCase

from .solution1 import command_factory, prepare, solve, SubmarineCommand, SubmarinePosition


class Tests2021_02_1(TestCase):
    def test_command_factory_invalid_input_raises_error(self) -> None:
        with self.assertRaises(AssertionError):
            command_factory(8)

    def test_command_factory_too_few_parameters_raises_error(self) -> None:
        with self.assertRaises(AssertionError):
            command_factory("forward5")

    def test_command_factory_too_many_parameters_raises_error(self) -> None:
        with self.assertRaises(AssertionError):
            command_factory("forward 1 2")

    def test_command_factory_invalid_parameter_raises_error(self) -> None:
        with self.assertRaises(AssertionError):
            command_factory("forward a")

    def test_command_factory_unknown_raises_error(self) -> None:
        with self.assertRaises(AssertionError):
            command_factory("unknown 8")

    def test_command_factory_forward(self) -> None:
        command: SubmarineCommand = command_factory("forward 5")
        self.assertEqual(command, SubmarineCommand(horizontal=5))

    def test_command_factory_up(self) -> None:
        command: SubmarineCommand = command_factory("up 3")
        self.assertEqual(command, SubmarineCommand(depth=-3))

    def test_command_factory_down(self) -> None:
        command: SubmarineCommand = command_factory("down 8")
        self.assertEqual(command, SubmarineCommand(depth=8))

    def test_prepare_invalid_input_raises_error(self) -> None:
        with self.assertRaises(AssertionError):
            prepare("hello")

    def test_prepare(self) -> None:
        commands: SubmarineCommand = prepare(["forward 5", "up 3", "down 8"])
        self.assertEqual(commands, [
            SubmarineCommand(horizontal=5),
            SubmarineCommand(depth=-3),
            SubmarineCommand(depth=8),
        ])

    def test_solve_invalid_input_raises_error(self) -> None:
        with self.assertRaises(AssertionError):
            solve("hello")

    def test_solve_invalid_command_raises_error(self) -> None:
        with self.assertRaises(AssertionError):
            solve(["hello"])

    def test_position_horizontal_positive(self) -> None:
        position: SubmarinePosition = SubmarinePosition(horizontal=1, depth=1)
        command: SubmarineCommand = SubmarineCommand(horizontal=1)

        self.assertEqual(position + command, SubmarinePosition(horizontal=2, depth=1))

    def test_position_horizontal_negative(self) -> None:
        position: SubmarinePosition = SubmarinePosition(horizontal=1, depth=1)
        command: SubmarineCommand = SubmarineCommand(horizontal=-1)

        self.assertEqual(position + command, SubmarinePosition(horizontal=0, depth=1))

    def test_position_depth_positive(self) -> None:
        position: SubmarinePosition = SubmarinePosition(horizontal=1, depth=1)
        command: SubmarineCommand = SubmarineCommand(depth=1)

        self.assertEqual(position + command, SubmarinePosition(horizontal=1, depth=2))

    def test_position_depth_negative(self) -> None:
        position: SubmarinePosition = SubmarinePosition(horizontal=1, depth=1)
        command: SubmarineCommand = SubmarineCommand(depth=-1)

        self.assertEqual(position + command, SubmarinePosition(horizontal=1, depth=0))

    def test_example(self) -> None:
        example_text: str = """
        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2
        """

        example_result: int = 150

        example: List[str] = list(
            line.strip()
            for line in example_text.split("\n")
            if line.strip() != ""
        )

        result: SubmarinePosition = solve(prepare(example))
        self.assertEqual(result.horizontal * result.depth, example_result)


if __name__ == "__main__":
    main()
