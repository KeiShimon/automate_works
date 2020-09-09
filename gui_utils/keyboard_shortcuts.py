
import clipboard
import keyboard
import pyautogui

from time import sleep

from gui_utils.gui_constants import WaitDurations


def _launch_application_via_win_plus_r(app_name) -> None:
    _press_wait_release_wait('windows+r', WaitDurations.GUI_SHORTER)
    select_all()
    pyautogui.write(app_name)
    _press_wait_release_wait('enter', WaitDurations.GUI_SHORTER)
    sleep(WaitDurations.WEBSITE_OPEN_NORMAL)


def _press_wait_release_wait(key_stroke, wait_sec: float) -> None:
    keyboard.press(key_stroke)
    sleep(wait_sec)
    keyboard.release(key_stroke)
    sleep(wait_sec)


def _select_address_bar() -> None:
    _press_wait_release_wait('ctrl+l', WaitDurations.GUI_SHORTER)


def copy() -> str:
    """Copies the selected via ctrl+c.\n

    Stores selected into the clipboard and returns the content.

    Returns:
        The text in the clipboard as string.
    """

    sleep(WaitDurations.GUI_SHORTER)
    _press_wait_release_wait('ctrl+c',
                             WaitDurations.GUI_LONGER)

    # pyautogui does not work for copying (unknown reason)
    # pyautogui.hotkey('ctrl', 'c')

    return clipboard.paste()


def cut() -> None:
    _press_wait_release_wait('ctrl+x', WaitDurations.GUI_SHORTER)


def erase_all() -> None:
    select_all()
    keyboard.send('del')


def get_current_url() -> str:
    _select_address_bar()
    return copy()


def move_to_page(url) -> None:
    _select_address_bar()
    pyautogui.write(url)
    keyboard.send('enter')


def paste() -> str:
    """Pastes whatever in the clipboard via ctrl+v.\n

    Returns:
        The content in the clipboard as string.
    """

    _press_wait_release_wait('ctrl+v', WaitDurations.GUI_LONGER)
    return clipboard.paste()


def select_all() -> None:
    _press_wait_release_wait('ctrl+a', WaitDurations.GUI_SHORTER)


if __name__ == "__main__":
    _launch_application_via_win_plus_r('iexplore')
