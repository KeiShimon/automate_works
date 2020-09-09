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

from datetime import datetime

import pyperclip

from utils import converter


FILE_NAME = '日次定例動作確認_テスト注文.txt'

HEAD = '【日次定例動作確認】\n'


if __name__ == '__main__':
    now = datetime.now()
    weekday = converter.convert_week_number_to_japanese_str(
        datetime.today().weekday())

    content_builder = [HEAD]

    content_builder.append(
        f'{now.month}/{now.day} ({weekday})\n'
        f'{now.hour:02}:{now.minute:02} 現在\n'
    )

    content_builder.append(
        f'  出前館(SP、PC、アプリ)\n'
        f'  dデリ\n'
        f'  LINEデリマ\n\n'
        '特に問題ありません。\n\n'
        'テスト注文、完了できました。\n'
    )

    content = "".join(content_builder)

    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        f.write(content)

    pyperclip.copy(content)
