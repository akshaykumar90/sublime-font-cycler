import sublime, sublime_plugin

def cycle_font(backward=False):
    settings = sublime.load_settings("Preferences.sublime-settings")
    settings_fonts_list = settings.get("fonts_list", [])
    if not settings_fonts_list:
        return
    fonts_list_size = len(settings_fonts_list)
    index_delta = -1 if backward else 1

    fonts_list = []
    for index in range(0, fonts_list_size):
        item = settings_fonts_list[index]
        if isinstance(item, str):
            item = { "font_face": item }
        fonts_list.append(item)

    try:
        current_font_face = settings.get("font_face")
        new_index = 0
        for index in range(0, fonts_list_size):
            if fonts_list[index]["font_face"] == current_font_face:
                new_index = (index + index_delta) % len(fonts_list)
                break
    except ValueError:
        new_index = 0

    font_settings = fonts_list[new_index]
    fields = [
        "font_face",
        "font_size",
        "line_padding_bottom",
        "line_padding_top"
    ]
    for field in fields:
        settings.set(field, font_settings[field])
    sublime.save_settings("Preferences.sublime-settings")
    sublime.status_message('Font Face: %s (%d)' %
        (font_settings["font_face"], font_settings["font_size"]))

class NextFontCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_font()

class PreviousFontCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_font(backward=True)
