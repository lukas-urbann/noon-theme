# Noon Theme

A VS Code color theme with red accents and calm, high-contrast syntax colors. Beautiful, simple and easy on the eyes.

- **Noon Theme**: deep blue-grey backgrounds.
- **Noon Light**: dampened light greys around `#ccc`, never pure white.

## Zed

A Zed port of both themes lives in [`../zed`](../zed). It's generated from these themes, so it always matches them.

## Install from source

```bash
npx @vscode/vsce package
code --install-extension noon-theme-1.5.0.vsix
```

Then open **Preferences: Color Theme** and pick **Noon Theme** or **Noon Light**.

## Develop

Open this folder in VS Code and press `F5`. A new window opens with the theme loaded, and edits to
`themes/noon-color-theme.json` show up there right away. Run **Developer: Inspect Editor Tokens and Scopes**
to find the scope behind a token.

## Changing colors

The theme files are generated. Edit a palette at the top of a script, then run `sh scripts/build.sh` to regenerate both themes.

- UI colors: `scripts/build_colors.py` (the light palette is in its `if light:` block)
- Syntax colors: `scripts/build_tokens.py` (same layout)
