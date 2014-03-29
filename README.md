FontCycler
==========

Quickly cycle between your favorite fonts in Sublime Text with the press of a key. Some research says that this makes you productive. *wink* *wink*

Installation
------------

The simplest method of installation is through Package Control, which can be found at this site: https://sublime.wbond.net/installation

Just install Package Control, and select FontCycler in the list of available packages.

Usage
-----

You can cycle through the fonts by pressing the `F10` key, and cycle backwards with `Shift+F10`.

You need to set the `fonts_list` key in the `Preferences.sublime-settings` file to a list of fonts you want to cycle within. The fonts need to be **pre-installed** on the system.

You can specify just a font name or an object with the properties `font_face`, `font_size`, `line_padding_bottom` and `line_padding_top`. `font_face` is a required property on the object.

```JSON
{
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
}
```

```JSON
{
	"fonts_list":
	[
		{
			"font_face": "Consolas",
			"font_size": 9,
			"line_padding_bottom": 1,
			"line_padding_top": 0
		},
		{
			"font_face": "Courier",
			"font_size": 12
		},
		{
			"font_face": "Menlo",
			"font_size": 10,
			"line_padding_bottom": 1,
			"line_padding_top": 0
		}
	]
}
```

Or even a mixed approach:

```JSON
{
	"fonts_list":
	[
		"Consolas",
		{
			"font_face": "Courier",
			"font_size": 12
		},
		{
			"font_face": "Menlo",
			"font_size": 10,
			"line_padding_bottom": 1,
			"line_padding_top": 0
		}
	]
}
```

Configuration
-------------

To change the keyboard shortcut for next and previous font, bind the `next_font` and `previous_font` commands respectively to the desired keys.
