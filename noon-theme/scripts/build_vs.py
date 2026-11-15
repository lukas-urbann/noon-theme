"""Ports the VS Code themes to classic Visual Studio.

Reads themes/noon-color-theme.json and themes/noon-light-color-theme.json and writes to output/visual-studio/:
  RedNoon-Dark.vssettings, RedNoon-Light.vssettings  editor colors (Tools > Import and Export Settings)
  RedNoon.vstheme                                    shell colors (window, tabs, menus, status bar)

Usage: python3 scripts/build_vs.py
"""
import json, os, uuid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "output", "visual-studio")
NS = uuid.UUID("6f1c2a52-5d5e-4f43-9a37-2f0c1d6a7e11")


def rgb(h):
    return h[1:7].upper()


def bgr(h):  # Visual Studio Fonts and Colors uses 0x00BBGGRR
    h = rgb(h)
    return "0x00" + h[4:6] + h[2:4] + h[0:2]


def argb(h):
    return "FF" + rgb(h)


def load(name):
    with open(os.path.join(ROOT, "themes", name), encoding="utf8") as f:
        return json.load(f)


def sem(vs, key, default):
    v = vs["semanticTokenColors"].get(key)
    if v is None:
        return default
    return v if isinstance(v, str) else v["foreground"]


def settings(vs, name):
    c = vs["colors"]
    fg, bg = c["editor.foreground"], c["editor.background"]
    text = sem(vs, "namespace", fg)
    cls = sem(vs, "class", fg)
    iface = sem(vs, "interface", cls)
    items = [
        ("Plain Text", fg, bg),
        ("Selected Text", fg, c["editor.selectionBackground"]),
        ("Inactive Selected Text", fg, c["editor.selectionBackground"]),
        ("Line Numbers", c["editorLineNumber.foreground"], bg),
        ("Visible White Space", c["editorWhitespace.foreground"], bg),
        ("Indicator Margin", fg, c["editorGutter.background"]),
        ("Brace Matching (Highlight)", fg, c["editorBracketMatch.background"]),
        ("Comment", sem(vs, "comment", fg), bg),
        ("XML Doc Comment", sem(vs, "comment", fg), bg),
        ("Excluded Code", c["editorGhostText.foreground"], bg),
        ("Keyword", sem(vs, "keyword", fg), bg),
        ("Keyword - Control", sem(vs, "controlKeyword", fg), bg),
        ("Preprocessor Keyword", sem(vs, "macro", fg), bg),
        ("String", sem(vs, "string", fg), bg),
        ("String - Verbatim", sem(vs, "string", fg), bg),
        ("String - Escape Character", sem(vs, "stringEscapeCharacter", fg), bg),
        ("Number", sem(vs, "number", fg), bg),
        ("Operator", sem(vs, "punctuation", fg), bg),
        ("Punctuation", sem(vs, "punctuation", fg), bg),
        ("Identifier", fg, bg),
        ("Namespace Name", text, bg),
        ("Method Name", sem(vs, "method", fg), bg),
        ("Extension Method Name", sem(vs, "method", fg), bg),
        ("Parameter Name", sem(vs, "variable", fg), bg),
        ("Local Name", sem(vs, "variable", fg), bg),
        ("Field Name", text, bg),
        ("Property Name", text, bg),
        ("User Types", cls, bg),
        ("User Types (Classes)", cls, bg),
        ("User Types (Delegates)", cls, bg),
        ("User Types (Value types)", cls, bg),
        ("User Types (Type parameters)", cls, bg),
        ("User Types (Interfaces)", iface, bg),
        ("User Types (Enums)", iface, bg),
        ("XML Attribute", sem(vs, "markupAttribute", fg), bg),
        ("XML Name", sem(vs, "markupElement", fg), bg),
        ("HTML Attribute", sem(vs, "markupAttribute", fg), bg),
        ("HTML Element Name", sem(vs, "markupElement", fg), bg),
    ]
    rows = "\n".join(
        f'            <Item Name="{n}" Foreground="{bgr(f)}" Background="{bgr(b)}" BoldFont="No"/>'
        for n, f, b in items)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- {name}: editor colors. Import with Tools > Import and Export Settings. -->
<UserSettings>
  <ApplicationIdentity version="17.0"/>
  <ToolsOptions>
    <ToolsOptionsCategory name="Environment" RegisteredName="Environment"/>
  </ToolsOptions>
  <Category name="Environment_Group" RegisteredName="Environment_Group">
    <Category name="Environment_FontsAndColors" Category_GUID="{{1EDA5DD4-927A-43a7-810E-7FD247D0DA1D}}" Package_GUID="{{DA9FB551-C724-11d0-AE1F-00A0C90FFFC3}}">
      <PageName>Fonts and Colors</PageName>
      <PageData>
        <Categories>
          <Category GUID="{{A27B4E24-A735-4d1d-B8E7-9716E1E3D8E0}}" FontName="Cascadia Mono" FontSize="10" CharSet="1" FontIsDefault="No">
            <Items>
{rows}
            </Items>
          </Category>
        </Categories>
      </PageData>
    </Category>
  </Category>
</UserSettings>
"""


def theme_xml(vs, name, fallback):
    c = vs["colors"]
    pairs = {
        "EnvironmentBackground": (c["editor.background"], c["foreground"]),
        "ToolWindowBackground": (c["sideBar.background"], c["sideBar.foreground"]),
        "ToolWindowText": (None, c["sideBar.foreground"]),
        "ToolWindowBorder": (c["sideBar.border"], None),
        "PanelBorder": (c["panel.border"], None),
        "TitleBarActive": (c["titleBar.activeBackground"], c["titleBar.activeForeground"]),
        "TitleBarInactive": (c["titleBar.inactiveBackground"], c["titleBar.inactiveForeground"]),
        "CommandBarGradientBegin": (c["titleBar.activeBackground"], None),
        "CommandBarTextActive": (None, c["menubar.selectionForeground"]),
        "CommandBarMouseOverBackgroundBegin": (c["menubar.selectionBackground"], None),
        "CommandBarMenuBackgroundGradientBegin": (c["menu.background"], c["menu.foreground"]),
        "CommandBarMenuItemMouseOverBackground": (c["menu.selectionBackground"], c["menu.selectionForeground"]),
        "CommandBarMenuBorder": (c["menu.border"], None),
        "CommandBarMenuSeparator": (c["menu.separatorBackground"], None),
        "FileTabSelectedGradientTop": (c["tab.activeBackground"], c["tab.activeForeground"]),
        "FileTabInactiveGradientTop": (c["tab.inactiveBackground"], c["tab.inactiveForeground"]),
        "FileTabHotGradientTop": (c["list.hoverBackground"], c["list.hoverForeground"]),
        "StatusBarDefault": (c["statusBar.background"], c["statusBar.foreground"]),
        "StatusBarBuilding": (c["statusBar.background"], c["statusBar.foreground"]),
        "ScrollBarBackground": (c["editor.background"], None),
        "ScrollBarThumbBackground": (c["scrollbarSlider.background"], None),
        "ScrollBarThumbMouseOverBackground": (c["scrollbarSlider.hoverBackground"], None),
        "SearchBoxBackground": (c["input.background"], c["input.foreground"]),
        "ComboBoxBackground": (c["dropdown.background"], c["dropdown.foreground"]),
        "ButtonDefault": (c["button.background"], c["button.foreground"]),
        "ButtonMouseOver": (c["button.hoverBackground"], c["button.foreground"]),
        "TreeViewSelectedItemActive": (c["list.activeSelectionBackground"], c["list.activeSelectionForeground"]),
        "TreeViewMouseOver": (c["list.hoverBackground"], c["list.hoverForeground"]),
        "HyperlinkText": (None, c["textLink.foreground"]),
    }
    out = []
    for key, (b, f) in pairs.items():
        parts = []
        if b:
            parts.append(f'<Background Type="CT_RAW" Source="{argb(b)}"/>')
        if f:
            parts.append(f'<Foreground Type="CT_RAW" Source="{argb(f)}"/>')
        out.append(f'      <Color Name="{key}">{"".join(parts)}</Color>')
    guid = str(uuid.uuid5(NS, name)).upper()
    return (f'  <Theme Name="{name}" GUID="{{{guid}}}" FallbackId="{fallback}">\n'
            '    <Category Name="Environment" GUID="{624ed9c3-bdfd-41fa-96c3-7c824ea32e3d}">\n'
            + "\n".join(out) + "\n    </Category>\n  </Theme>\n")


def vstheme(dark, light):
    return ('<?xml version="1.0" encoding="utf-8"?>\n<Themes>\n'
            + theme_xml(dark, "Red Noon", "{1ded0138-47ce-435e-84ef-9ec1f439b749}")
            + theme_xml(light, "Red Noon Light", "{de3dbbcd-f642-433c-8353-8f1df4370aba}")
            + "</Themes>\n")


def main():
    dark, light = load("noon-color-theme.json"), load("noon-light-color-theme.json")
    os.makedirs(OUT, exist_ok=True)
    for fname, text in (("RedNoon-Dark.vssettings", settings(dark, "Red Noon")),
                        ("RedNoon-Light.vssettings", settings(light, "Red Noon Light")),
                        ("RedNoon.vstheme", vstheme(dark, light))):
        with open(os.path.join(OUT, fname), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("wrote", os.path.relpath(os.path.join(OUT, fname), ROOT))


if __name__ == "__main__":
    main()
