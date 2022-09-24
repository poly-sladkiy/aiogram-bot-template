from typing import Optional

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class WordFilterGenerator(BoundFilter):
    filer_name = None

    def __init__(self, text: Optional[str] | Optional[list[str]] = None):
        if text is None:
            raise ValueError('Filter text must be str or list[str]')
        if isinstance(text, str):
            self.filer_name = text.lower()
        elif isinstance(text, list):
            lowered_text = list(map(lambda x: x.lower(), text))
            self.filer_name = lowered_text
        else:
            raise ValueError('Filter text must be str or list[str]')

        super(WordFilterGenerator, self).__init__()

    async def check(self, message: types.Message) -> bool:

        text = message.text.lower()

        if isinstance(self.filer_name, str):
            return text == self.filer_name
        elif isinstance(self.filer_name, list):
            return text in self.filer_name
