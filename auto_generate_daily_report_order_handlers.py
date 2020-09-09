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


_FILE_NAME = '日次定例動作確認_オーダー管理・シェアデリ自動差配.txt'

_HEAD = '【日次定例動作確認】\n'

_BODY = ('下記の動作確認が完了し、問題ないことを確認しました。\n'
         '\n'
         '■オーダー管理アプリ\n'
         '  横型（店舗、拠点モード）\n'
         '  縦型\n'
         '  子機\n'
         '  PC拠点管理\n'
         '\n'
         '■シェアデリ自動差配\n'
         '  横型（店舗モード）\n'
         '  差配コントローラー\n'
         '  ドライバーアプリ\n'
         )


if __name__ == '__main__':
    now = datetime.now()
    weekday = converter.convert_week_number_to_japanese_str(
        datetime.today().weekday())

    head_time = (f'{now.month:02}/{now.day:02} ({weekday}) '
                 f'{now.hour:02}:{now.minute:02} 現在\n')

    content = _HEAD + head_time + _BODY

    with open(_FILE_NAME, 'w', encoding='utf-8') as f:
        f.write(content)

    pyperclip.copy(content)
