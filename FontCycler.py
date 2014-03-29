from collections import namedtuple
import sublime, sublime_plugin

Field = namedtuple("Field", ["name", "default"])

def cycle_font(backward=False):
    settings = sublime.load_settings("Preferences.sublime-settings")
    settings_fonts_list = settings.get("fonts_list", [])

    if not settings_fonts_list:
        return

    fonts_list = []
    for item in settings_fonts_list:
        if isinstance(item, basestring):
            item = { "font_face": item }
        if "font_face" in item:
            fonts_list.append(item)

    fonts_list_size = len(fonts_list)
    index_delta = -1 if backward else 1
    current_font_face = settings.get("font_face")
    new_index = 0
    for index in range(fonts_list_size):
        if fonts_list[index]["font_face"] == current_font_face:
            new_index = (index + index_delta) % len(fonts_list)
            break

    font_settings = fonts_list[new_index]
    fields = [
        Field("font_face", ""),
        Field("font_size", settings.get("font_size")),
        Field("line_padding_bottom", 0),
        Field("line_padding_top", 0)
    ]
    for field in fields:
        settings.set(field.name, font_settings.get(field.name, field.default))
    sublime.save_settings("Preferences.sublime-settings")

    sublime.status_message('Font Face: %s' % (font_settings["font_face"],))

class NextFontCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_font()

class PreviousFontCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_font(backward=True)
