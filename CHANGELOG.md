# Change Log

## [1.0.1]

- Darker tab bar so open tabs stand out, with `#3b3d42` borders between tabs and under the tab bar and file path bar (dark theme).
- Title bar and status bar share one color, separate from the editor. All window borders use one color.
- Sticky scroll has a thin bar instead of a dark shadow, and the scroll shadow is gone.
- Notification popups get a softer blue border. In the light theme the selected activity bar button is clearly darker, with a red marker.
- Package ready for the Marketplace: icon, MIT license, README with an AI notice and recommended Material icon and product icon extensions.
- Zed and Visual Studio builds in `output/`.

## [1.0.0] Red Noon

- Renamed to Red Noon (themes: Red Noon, Red Noon Light) and versioning restarted at 1.0.
- Softer red accent; red hover on menus, menu bar and lists; reddish text selection.
- Git colors: green for new files, blue for modified, matching the syntax palette.
- Less blue tint in the dark theme, more contrast between surfaces in the light theme, orange errors.
- New ports: Zed and Visual Studio.

## [1.5.0]

- Ember Apricot syntax colors are 60% more vivid (OKLCH chroma). Lightness is adjusted only where needed to stay displayable and above 4.5:1 contrast. Grey roles (text, punctuation, variables, comments) are unchanged.
- The light theme gains less (about +10% to +40%), because dark colors run out of room to get more vivid.

## [1.4.0]

- New syntax palette, **Ember Apricot**, made for Noon and used by both themes. It has apricot keywords, orchid control flow, cyan types, mint interfaces and enums, cream methods, green strings, aqua escapes, violet numbers and italic grey comments.
- HTML attributes, CSS properties and JSON/YAML keys share the cyan type color.
- Every syntax color is at least 4.5:1 against the editor background in both themes. Code in a false `#if` block is the exception and stays faded on purpose.
- Side bar and icon bar selection is grey instead of red.
- The status bar matches the window frame in its normal state.
- The icon bar is a step lighter than the window frame, and the side bar uses the editor background.

## [1.3.0]

- New **Noon Light** variant: cool greys around `#ccc` instead of pure white, with the same red accent darkened to read on grey.
- Noon Light uses Visual Studio 2022 Light syntax colors. Some are darkened to keep at least 4.5:1 contrast on the grey background, and HTML attributes and CSS properties use VS's variable navy instead of pure red.
- Both palette scripts now take `--light`, and `scripts/build.sh` regenerates both themes.

## [1.2.0]

- Syntax colors now follow Visual Studio 2022 Dark, tuned so every color has at least 5:1 contrast on the editor background.
- Red no longer colors normal code. It marks only invalid code and deleted diff lines.
- Dedicated rules for C#, Razor/cshtml, HTML, XML, CSS/SCSS/Less, JavaScript/TypeScript (including JSX), JSON, YAML and Markdown.
- Semantic highlighting is on, with colors for the C# extension's token types (records, structs, interfaces, XML doc comments, regex, excluded code and more).
- The palettes now live in `scripts/build_colors.py` (UI) and `scripts/build_tokens.py` (syntax).

## [1.1.0]

- Rebuilt all UI colors from one palette, so backgrounds, borders, selections and accents match everywhere.
- Menus, dropdowns and notifications are dark now (they were light grey and pure red).
- Selections and highlights use a translucent red tint instead of solid red.
- Added colors for current VS Code UI: command center, sticky scroll, inlay hints, bracket pairs, diff and merge editors, terminal ANSI palette, testing, notebooks, SCM graph, chat and inline edits.

## [1.0.0]

- Revived the theme: the theme file is now strict JSON, the manifest has a publisher, and the extension packages with `vsce`.
- Numbers use the red constant color instead of matching comments.
- Markdown code fences are readable again (they were nearly invisible).
- Fixed an invalid markdown heading scope.

## [0.0.1]

- Initial release
