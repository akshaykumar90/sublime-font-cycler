FontCycler
==========
---
Quickly cycle between your favorite fonts in Sublime Text with the press of a key. Some research says that this makes you productive. *wink* *wink*

Usage
-----
---

You can cycle through the fonts by pressing the `F9` key, and cycle backwards with `Shift+F9`.

You need to set the `fonts_list` key in the `Preferences.sublime-settings` file to a list of fonts you want to cycle within. The fonts need to be **pre-installed** on the system.

```
"fonts_list":
	[
		"Andale Mono",
		"Consolas",
		"Courier",
		"Courier New",
		"Envy Code R",
		"Inconsolata",
		"Lucida Console",
		"Menlo",
		"Meslo LG S",
		"Meslo LG M",
		"Meslo LG L",
		"Monaco",
		"ProFontX",
		"Source Code Pro",
		"Ubuntu Mono"
	]
```

Configuration
-------------
---
To change the keyboard shortcut for next and previous font, bind the `next_font` and `previous_font` commands respectively to the desired keys.
