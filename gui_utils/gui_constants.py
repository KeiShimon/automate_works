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

"""GUI操作に関連する定数を集めたパッケージ。

GUI操作に必要な一般定数を保管する。
サイトごとの定数など、特定の用途の定数は別で管理すること。

"""


class AppNames(object):
    INTERNET_EXPLORER = 'iexplore'


class WaitDurations(object):
    GUI_SHORTER = 0.1
    GUI_NORMAL = 0.2
    GUI_LONGER = 0.4
    GUI_LONGEST = 0.8
    WEBSITE_OPEN_SHORTER = 1
    WEBSITE_OPEN_NORMAL = 2
    WEBSITE_OPEN_LONGER = 4
    WEBSITE_OPEN_LONGEST = 8
    APP_LAUNCH_SHORTER = 1
    APP_LAUNCH_NORMAL = 2
    APP_LAUNCH_LONGER = 4
    APP_LAUNCH_LONGEST = 8

