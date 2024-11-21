# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
"""Output Decorator - Library for decorating strings in CLI apps """
import shutil


class StringDecorator:
    @classmethod
    def term_width(cls):
        return shutil.get_terminal_size()[0]

    @classmethod
    def string_decorate(cls, text='', symbol='*', print_flag=True):
        if text:
            result_string = f' {text} '.center(cls.term_width(), symbol)
        else:
            result_string = ''.center(cls.term_width(), symbol)

        if print_flag:
            print(result_string)
        else:
            return result_string

    @classmethod
    def framed_decorate(cls, text='', top_symbol='-', bottom_symbol='-'):
        text_len = len(text)
        top = top_symbol * text_len
        bottom = bottom_symbol * text_len
        return f'{top}\n{text}\n{bottom}'


print(StringDecorator.framed_decorate('Hello World!', '*'))
