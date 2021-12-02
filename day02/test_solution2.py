#!/usr/bin/env python
from typing import List
from unittest import main, TestCase

from solution2 import command_factory, prepare, solve, SubmarineAimCommand, SubmarineAimPosition


class Tests02_2(TestCase):
    def test_command_factory_invalid(self) -> None:
        with self.assertRaises(RuntimeError):
            command_factory("forward5")

    def test_command_factory_forward(self) -> None:
        command: SubmarineAimCommand = command_factory("forward 5")
        self.assertEqual(command, SubmarineAimCommand(horizontal=5))

    def test_command_factory_up(self) -> None:
        command: SubmarineAimCommand = command_factory("up 3")
        self.assertEqual(command, SubmarineAimCommand(aim=-3))

    def test_command_factory_down(self) -> None:
        command: SubmarineAimCommand = command_factory("down 8")
        self.assertEqual(command, SubmarineAimCommand(aim=+8))

    def test_command_factory_unknown(self) -> None:
        with self.assertRaises(RuntimeError):
            command_factory("unknown 8")

    def test_position_horizontal_positive(self) -> None:
        position: SubmarineAimPosition = SubmarineAimPosition(horizontal=3, aim=3, depth=3)
        command: SubmarineAimCommand = SubmarineAimCommand(horizontal=3)

        self.assertEqual(position + command, SubmarineAimPosition(horizontal=6, aim=3, depth=12))

    def test_position_horizontal_negative(self) -> None:
        position: SubmarineAimPosition = SubmarineAimPosition(horizontal=3, aim=3, depth=3)
        command: SubmarineAimCommand = SubmarineAimCommand(horizontal=-3)

        self.assertEqual(position + command, SubmarineAimPosition(horizontal=0, aim=3, depth=-6))

    def test_position_depth_positive(self) -> None:
        position: SubmarineAimPosition = SubmarineAimPosition(horizontal=3, aim=3, depth=3)
        command: SubmarineAimCommand = SubmarineAimCommand(aim=3)

        self.assertEqual(position + command, SubmarineAimPosition(horizontal=3, aim=6, depth=3))

    def test_position_depth_negative(self) -> None:
        position: SubmarineAimPosition = SubmarineAimPosition(horizontal=3, aim=3, depth=3)
        command: SubmarineAimCommand = SubmarineAimCommand(aim=-3)

        self.assertEqual(position + command, SubmarineAimPosition(horizontal=3, aim=0, depth=3))

    def test_example(self) -> None:
        example_text: str = """
        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2
        """

        example_result: int = 900

        example: List[str] = list(
            line.strip()
            for line in example_text.split("\n")
            if line.strip() != ""
        )

        result: SubmarineAimPosition = solve(prepare(example))
        self.assertEqual(result.horizontal * result.depth, example_result)


if __name__ == "__main__":
    main()
