# Red Noon

A VS Code color theme with red accents and calm, high-contrast syntax colors. Beautiful, simple and easy on the eyes.

- **Red Noon**: deep blue-grey backgrounds.
- **Red Noon Light**: dampened light greys around `#ccc`, never pure white.

## Zed

Builds live in `output/`:

- `red-noon-1.0.0.vsix`: VS Code.
- `zed/red-noon.json`: Zed. Copy it to `~/.config/zed/themes/`.
- `visual-studio/`: Visual Studio. Import `RedNoon-Dark.vssettings` or `RedNoon-Light.vssettings` through Tools > Import and Export Settings for editor colors. `RedNoon.vstheme` holds the shell colors for the Visual Studio Color Theme Editor.

## Install from source

```bash
npx @vscode/vsce package
code --install-extension red-noon-1.0.0.vsix
```

Then open **Preferences: Color Theme** and pick **Red Noon** or **Red Noon Light**.

## Develop

Open this folder in VS Code and press `F5`. A new window opens with the theme loaded, and edits to
`themes/noon-color-theme.json` show up there right away. Run **Developer: Inspect Editor Tokens and Scopes**
to find the scope behind a token.

## Changing colors

The theme files are generated. Edit a palette at the top of a script, then run `sh scripts/build.sh` to regenerate both themes.

- UI colors: `scripts/build_colors.py` (the light palette is in its `if light:` block)
- Syntax colors: `scripts/build_tokens.py` (same layout)
