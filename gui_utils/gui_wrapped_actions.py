""" 複数の操作を関数としてまとめたアクションのパッケージ。

マウス操作（とキーボード操作）のコンビネーション。
キーボード操作しか必要としない低レベルな操作の場合、gui_wrapped_shortcuts に登録すること。

"""

import keyboard
import pyautogui

from gui_utils import gui_classes
from gui_utils import gui_constants
from time import sleep
from typing import List, Optional


def action_drag_and_drop(
        frm: gui_classes.Coordinate,
        to: gui_classes.Coordinate,
        t_milliseconds: Optional[float]
) -> None:
    """ドラッグ＆ドロップをする。

    マウスを移動させ、クリックしながら指定した場所までドラッグする。

    Args:
        frm: origin coordinate
        to: target coordinate
        t_milliseconds: how long the function should take to drag in millisecond

    Returns:
        None
    """

    if t_milliseconds is None:
        t_milliseconds = gui_constants.WaitDurations.GUI_NORMAL

    pyautogui.moveTo(frm.x, frm.y)
    sleep(gui_constants.WaitDurations.GUI_SHORTER)
    pyautogui.dragTo(to.x - frm.x, to.y - frm.y, t_milliseconds, button='left')
    sleep(gui_constants.WaitDurations.GUI_NORMAL)


def action_multiple_click(targets: List[gui_classes.ClickTarget]):
    """指定されたクリックターゲット全ての座標を一度ずつクリックする。

    Args:
        targets: a list of ClickTarget
    Returns:
        None
    """
    for target in targets:
        pyautogui.click(target.x, target.y)
        sleep(gui_constants.WaitDurations.GUI_SHORTER)


def action_multiple_select(targets: List[gui_classes.ClickTarget]):
    """複数選択可能な選択リストから、複数の選択肢をクリックする。\n
    ”ctrl キーを押しながら複数の選択肢をクリックする” アクションの実装。

    Args:
        targets: a list of ClickTarget
    Returns:
        None
    """
    keyboard.press('ctrl')
    sleep(gui_constants.WaitDurations.GUI_SHORTER)
    for target in targets:
        pyautogui.click(target.x, target.y)
        sleep(gui_constants.WaitDurations.GUI_SHORTER)
    keyboard.release('ctrl')
    sleep(gui_constants.WaitDurations.GUI_SHORTER)
