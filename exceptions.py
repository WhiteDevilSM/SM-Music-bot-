#
#
# This file is part of < https://github.com/901980/SM-Music-bot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/901980/SM-Music-bot/blob/master/LICENSE >
#
# All rights reserved.


class AssistantErr(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)
