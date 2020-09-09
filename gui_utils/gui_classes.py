"""

Base classes for gui objects.
"""

import pyautogui

from gui_utils.keyboard_shortcuts import select_all


class Coordinate(object):
    """An immutable class for managing 2-D coordinates.
    """
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class ClickTarget(Coordinate):
    def __init__(self, x: int, y: int, name: str):
        super(ClickTarget, self).__init__(x, y)
        self.name = name

    def click(self, n: int = None):
        if n is None:
            pyautogui.click(self.x, self.y)
        else:
            pyautogui.click(self.x, self.y, n)


class ClickTargetWithOffset(ClickTarget):
    def __init__(self, x: int, y: int, name: str,
                 offset_x: int, offset_y: int):
        super(ClickTargetWithOffset, self).__init__(x, y, name)
        self.offset_x = offset_x
        self.offset_y = offset_y

    def click_with_offset(self, n: int = None):
        if n is None:
            pyautogui.click(self.x + self.offset_x,
                            self.y + self.offset_y)
        else:
            pyautogui.click(self.x + self.offset_x,
                            self.y + self.offset_y,
                            n)


class TextField(ClickTargetWithOffset):
    def __init__(self, input_str: str, x: int, y: int, name: str,
                 offset_x: int = 0, offset_y: int = 0):
        super(TextField, self).__init__(x, y, name, offset_x, offset_y)
        self.input_str = input_str

    def fill_field(self):
        self.click()
        select_all()
        pyautogui.write(self.input_str)

    def fill_field_with_offset(self):
        self.click_with_offset()
        select_all()
        pyautogui.write(self.input_str)
