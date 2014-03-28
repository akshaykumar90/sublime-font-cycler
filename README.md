FontCycler
==========

Quickly cycle between your favorite fonts in Sublime Text with the press of a key. Some research says that this makes you productive. *wink* *wink*

Usage
-----

You can cycle through the fonts by pressing the `F10` key, and cycle backwards with `Shift+F10`.

You need to set the `fonts_list` key in the `Preferences.sublime-settings` file to a list of fonts you want to cycle within. The fonts need to be **pre-installed** on the system.

You can specify just a font name or an object with the properties `font_face`, `font_size`, `line_padding_bottom`, `line_padding_top` and `font_options` (a list). Any of those is optional, so only existing properties will be set.

```JSON
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

```JSON
"fonts_list":
[
	{
		"font_face": "Consolas",
		"font_size": 9,
		"line_padding_bottom": 1,
		"line_padding_top": 0,
		"font_options":
		[
			"rgb_antialias"
		]
	},
	{
		"font_face": "Courier",
		"font_size": 12,
		"font_options":
		[
			"no_antialias"
		]
	},
	{
		"font_face": "Menlo",
		"font_size": 10,
		"line_padding_bottom": 1,
		"line_padding_top": 0
	}
]
```

Or even a mixed approach:

```JSON
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
```

Configuration
-------------

To change the keyboard shortcut for next and previous font, bind the `next_font` and `previous_font` commands respectively to the desired keys.
