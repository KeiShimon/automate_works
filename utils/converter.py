#     Copyright 2020 Keiichiro Shimonishi
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.


def convert_week_number_to_japanese_str(week_number: int) -> str:
    """ Converts a week number to Japanese weekday string.

    Args:
        week_number: a week number 0 to 6, typically obtained by .weekday() method of a DateTime object.

    Returns:
        a string between '月' and '日'.

    Raises:
        ValueError: If the argument is negative or greater than 6.
    """
    if week_number == 0:
        return '月'
    elif week_number == 1:
        return '火'
    elif week_number == 2:
        return '水'
    elif week_number == 3:
        return '木'
    elif week_number == 4:
        return '金'
    elif week_number == 5:
        return '土'
    elif week_number == 6:
        return '日'
    else:
        raise ValueError
