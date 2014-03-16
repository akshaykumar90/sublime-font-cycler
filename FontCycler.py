import sublime, sublime_plugin

def cycle_font(backward=False):
    s = sublime.load_settings("Preferences.sublime-settings")
    fonts_list = s.get("fonts_list", [])
    
    if not fonts_list:
        return

    try:
        index = fonts_list.index(s.get("font_face"))
        new_index = (index + (-1 if backward else 1)) % len(fonts_list)
    except ValueError:
        new_index = 0

    s.set("font_face", fonts_list[new_index])
    sublime.save_settings("Preferences.sublime-settings")

    sublime.status_message('Font Face: ' + fonts_list[new_index])

class NextFontCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_font()

class PreviousFontCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        cycle_font(backward=True)
