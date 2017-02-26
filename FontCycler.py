# -*- coding: utf-8 -*-
from collections import namedtuple

import sublime
import sublime_plugin

Field = namedtuple('Field', ['name', 'default'])

ANY_FONT_SIZE = -1


def cycle_font(backward=False):
    settings = sublime.load_settings('Preferences.sublime-settings')
    settings_fonts_list = settings.get('fonts_list', [])

    if not settings_fonts_list:
        return

    fonts_list = []
    position_by_key = {}
    for pos, item in enumerate(settings_fonts_list):
        try:
            if isinstance(item, basestring):
                item = {
                    'font_face': item,
                }
        except:
            if isinstance(item, str):
                item = {
                    'font_face': item,
                }
                
        if 'font_face' in item:
            fonts_list.append(item)
            key = (item['font_face'], item.get('font_size', ANY_FONT_SIZE))
            key_any = (item['font_face'], ANY_FONT_SIZE)
            position_by_key[key_any] = position_by_key[key] = pos

    delta = -1 if backward else 1
    current_font_face = settings.get('font_face')
    current_font_size = settings.get('font_size')
    cur_pos = position_by_key.get(
        (current_font_face, current_font_size)
    ) or position_by_key.get(
        (current_font_face, ANY_FONT_SIZE)
    )
    new_pos = (cur_pos + delta) % len(fonts_list) if cur_pos is not None else 0

    font_settings = fonts_list[new_pos]
    fields = [
        Field('font_face', ''),
        Field('font_size', settings.get('font_size')),
        Field('line_padding_bottom', settings.get('line_padding_bottom')),
        Field('line_padding_top', settings.get('line_padding_top'))
    ]
    for field in fields:
        settings.set(field.name, font_settings.get(field.name, field.default))
    sublime.save_settings('Preferences.sublime-settings')

    sublime.status_message('Font Face: %s' % (font_settings['font_face'],))


class NextFontCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_font()


class PreviousFontCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_font(backward=True)
