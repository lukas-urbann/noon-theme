"""Ports the generated VS Code themes to a Zed theme family.

Reads themes/noon-color-theme.json and themes/noon-light-color-theme.json and
writes output/zed/red-noon.json, so the Zed port always matches the VS Code
themes. Run it after build.sh (build.sh calls it for you).

Usage: python3 scripts/build_zed.py
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "output", "zed", "red-noon.json")
CLEAR = "#00000000"


def hexa(color, alpha):
    """Same color with a new 2-digit hex alpha."""
    return color[:7] + alpha


def blend(fg, bg, t):
    """Mixes fg into bg by t (0..1). Used for dim terminal colors."""
    a = [int(fg[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(bg[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(y + (x - y) * t):02x}" for x, y in zip(a, b))


def convert(vs, name, appearance):
    c = vs["colors"]
    sem = vs["semanticTokenColors"]

    def s(key):  # semantic token color (plain string)
        v = sem[key]
        return v if isinstance(v, str) else v["foreground"]

    def scope(name_):  # token rule color by its rule name in build_tokens.py
        for rule in reversed(vs["tokenColors"]):
            if rule["name"] == name_:
                return rule["settings"]["foreground"]
        raise KeyError(name_)

    text, punct, keyword = s("namespace"), s("punctuation"), s("keyword")
    control, type_, iface = s("controlKeyword"), s("class"), s("interface")
    method, variable, string = s("method"), s("variable"), s("string")
    escape, number, comment = s("stringEscapeCharacter"), s("number"), s("comment")
    preproc, attr, tag = s("macro"), s("markupAttribute"), s("markupElement")
    heading = scope("Markdown: headings")
    ghost = c["editorGhostText.foreground"]

    def status(color):
        return {"": color, ".background": hexa(color, "1f"), ".border": hexa(color, "66")}

    style = {
        "background.appearance": "opaque",
        # Window frame, bars and surfaces: same layering as VS Code.
        "background": c["titleBar.activeBackground"],
        "title_bar.background": c["titleBar.activeBackground"],
        "title_bar.inactive_background": c["titleBar.inactiveBackground"],
        "status_bar.background": c["statusBar.background"],
        "toolbar.background": c["breadcrumb.background"],
        "tab_bar.background": c["editorGroupHeader.tabsBackground"],
        "tab.active_background": c["tab.activeBackground"],
        "tab.inactive_background": c["tab.inactiveBackground"],
        "panel.background": c["sideBar.background"],
        "surface.background": c["sideBar.background"],
        "elevated_surface.background": c["editorWidget.background"],
        "drop_target.background": c["list.dropBackground"],
        # Borders
        "border": c["sideBar.border"],
        "border.variant": c["editorWidget.border"],
        "border.focused": c["focusBorder"],
        "border.selected": c["list.focusOutline"],
        "border.transparent": CLEAR,
        "border.disabled": c["editorWidget.border"],
        "pane.focused_border": CLEAR,
        "pane_group.border": c["editorGroup.border"],
        "panel.focused_border": c["list.focusOutline"],
        "panel.indent_guide": c["tree.inactiveIndentGuidesStroke"],
        "panel.indent_guide_active": c["tree.indentGuidesStroke"],
        "panel.indent_guide_hover": c["tree.indentGuidesStroke"],
        # Buttons, inputs and list rows (grey selection, like the VS Code side bar)
        "element.background": c["input.background"],
        "element.hover": c["list.hoverBackground"],
        "element.active": c["toolbar.activeBackground"],
        "element.selected": c["list.activeSelectionBackground"],
        "element.disabled": c["input.background"],
        "ghost_element.background": CLEAR,
        "ghost_element.hover": c["list.hoverBackground"],
        "ghost_element.active": c["toolbar.activeBackground"],
        "ghost_element.selected": c["list.activeSelectionBackground"],
        "ghost_element.disabled": CLEAR,
        # Text and icons
        "text": c["foreground"],
        "text.muted": c["descriptionForeground"],
        "text.placeholder": c["input.placeholderForeground"],
        "text.disabled": c["disabledForeground"],
        "text.accent": c["textLink.foreground"],
        "link_text.hover": c["textLink.activeForeground"],
        "icon": c["icon.foreground"],
        "icon.muted": c["activityBar.inactiveForeground"],
        "icon.disabled": c["disabledForeground"],
        "icon.placeholder": c["input.placeholderForeground"],
        "icon.accent": c["textLink.foreground"],
        # Scrollbars
        "scrollbar.thumb.background": c["scrollbarSlider.background"],
        "scrollbar.thumb.hover_background": c["scrollbarSlider.hoverBackground"],
        "scrollbar.thumb.border": CLEAR,
        "scrollbar.track.background": CLEAR,
        "scrollbar.track.border": CLEAR,
        # Editor
        "editor.background": c["editor.background"],
        "editor.foreground": c["editor.foreground"],
        "editor.gutter.background": c["editorGutter.background"],
        "editor.subheader.background": c["multiDiffEditor.headerBackground"],
        "editor.active_line.background": c["editor.lineHighlightBackground"],
        "editor.highlighted_line.background": c["editor.rangeHighlightBackground"],
        "editor.line_number": c["editorLineNumber.foreground"],
        "editor.active_line_number": c["editorLineNumber.activeForeground"],
        "editor.invisible": c["editorWhitespace.foreground"],
        "editor.wrap_guide": c["editorRuler.foreground"],
        "editor.active_wrap_guide": c["editorRuler.foreground"],
        "editor.indent_guide": c["editorIndentGuide.background1"],
        "editor.indent_guide_active": c["editorIndentGuide.activeBackground1"],
        "editor.document_highlight.read_background": c["editor.wordHighlightBackground"],
        "editor.document_highlight.write_background": c["editor.wordHighlightStrongBackground"],
        "editor.document_highlight.bracket_background": c["editorBracketMatch.background"],
        "search.match_background": c["editor.findMatchHighlightBackground"],
        # Terminal
        "terminal.background": c["terminal.background"],
        "terminal.ansi.background": c["terminal.background"],
        "terminal.foreground": c["terminal.foreground"],
        "terminal.bright_foreground": c["terminal.ansiBrightWhite"] if appearance == "dark" else c["editor.foreground"],
        "terminal.dim_foreground": c["descriptionForeground"],
    }
    for ansi in ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]:
        base = c[f"terminal.ansi{ansi.capitalize()}"]
        style[f"terminal.ansi.{ansi}"] = base
        style[f"terminal.ansi.bright_{ansi}"] = c[f"terminal.ansiBright{ansi.capitalize()}"]
        style[f"terminal.ansi.dim_{ansi}"] = blend(base, c["terminal.background"], 0.65)

    # Diagnostics and version control
    for key, color in {
        "error": c["editorError.foreground"], "warning": c["editorWarning.foreground"],
        "info": c["editorInfo.foreground"], "hint": c["editorHint.foreground"],
        "success": c["testing.iconPassed"],
        "created": c["gitDecoration.addedResourceForeground"],
        "modified": c["gitDecoration.modifiedResourceForeground"],
        "deleted": c["gitDecoration.deletedResourceForeground"],
        "renamed": c["gitDecoration.renamedResourceForeground"],
        "conflict": c["gitDecoration.conflictingResourceForeground"],
        "ignored": c["gitDecoration.ignoredResourceForeground"],
        "hidden": c["disabledForeground"], "unreachable": c["disabledForeground"],
        "predictive": ghost,
    }.items():
        for suffix, value in status(color).items():
            style[key + suffix] = value

    # Cursors and selections. The first entry is you; the rest are collaborators.
    selection = c["editor.selectionBackground"]
    others = [c["terminal.ansiBlue"], c["terminal.ansiGreen"], c["terminal.ansiMagenta"],
              c["terminal.ansiYellow"], c["terminal.ansiCyan"], c["terminal.ansiRed"], c["editorWarning.foreground"]]
    style["players"] = [{"cursor": c["editorCursor.foreground"], "background": c["editorCursor.foreground"], "selection": selection}] + [
        {"cursor": o, "background": o, "selection": hexa(o, "3d")} for o in others]
    style["accents"] = [c[f"editorBracketHighlight.foreground{i}"] for i in (1, 2, 3)]

    def hl(color, italic=False, bold=False):
        out = {"color": color}
        if italic:
            out["font_style"] = "italic"
        if bold:
            out["font_weight"] = 700
        return out

    style["syntax"] = {
        "attribute": hl(attr),
        "boolean": hl(keyword),
        "comment": hl(comment, italic=True),
        "comment.doc": hl(comment, italic=True),
        "constant": hl(text),
        "constant.builtin": hl(keyword),
        "constructor": hl(type_),
        "embedded": hl(text),
        "emphasis": hl(text, italic=True),
        "emphasis.strong": hl(text, bold=True),
        "enum": hl(iface),
        "function": hl(method),
        "function.builtin": hl(method),
        "hint": hl(c["editorInlayHint.foreground"]),
        "keyword": hl(keyword),
        # Grammars that tag control flow separately get the control color.
        "keyword.control": hl(control),
        "keyword.conditional": hl(control),
        "keyword.repeat": hl(control),
        "keyword.return": hl(control),
        "keyword.exception": hl(control),
        "keyword.import": hl(control),
        "keyword.coroutine": hl(control),
        "label": hl(text),
        "link_text": hl(attr),
        "link_uri": hl(string),
        "namespace": hl(text),
        "number": hl(number),
        "operator": hl(punct),
        "predictive": hl(ghost, italic=True),
        "preproc": hl(preproc),
        "primary": hl(text),
        "property": hl(text),
        "property.json_key": hl(attr),
        "punctuation": hl(punct),
        "punctuation.bracket": hl(punct),
        "punctuation.delimiter": hl(punct),
        "punctuation.list_marker": hl(keyword),
        "punctuation.special": hl(keyword),
        "selector": hl(attr),
        "string": hl(string),
        "string.escape": hl(escape),
        "string.regex": hl(string),
        "string.special": hl(escape),
        "string.special.symbol": hl(escape),
        "tag": hl(tag),
        "text.literal": hl(string),
        "title": hl(heading, bold=True),
        "type": hl(type_),
        "type.builtin": hl(keyword),
        "type.interface": hl(iface),
        "variable": hl(variable),
        "variable.parameter": hl(variable),
        "variable.member": hl(text),
        "variable.special": hl(keyword),
        "variant": hl(text),
    }
    return {"name": name, "appearance": appearance, "style": style}


def main():
    dark = json.load(open(os.path.join(ROOT, "themes", "noon-color-theme.json")))
    light = json.load(open(os.path.join(ROOT, "themes", "noon-light-color-theme.json")))
    family = {
        "$schema": "https://zed.dev/schema/themes/v0.2.0.json",
        "name": "Red Noon",
        "author": "Lukáš Urban",
        "themes": [convert(dark, "Red Noon", "dark"), convert(light, "Red Noon Light", "light")],
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        f.write(json.dumps(family, indent=2, ensure_ascii=False) + "\n")
    print("wrote", os.path.relpath(OUT, ROOT))


if __name__ == "__main__":
    main()
