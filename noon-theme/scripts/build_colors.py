"""Regenerates the `colors` block of the Noon theme from one palette.

Usage:
  python3 scripts/build_colors.py themes/noon-color-theme.json
  python3 scripts/build_colors.py themes/noon-light-color-theme.json --light
"""
import json, sys

path = sys.argv[1]
light = "--light" in sys.argv

# ---- Palette (taken from the original theme, made consistent) ----
crust   = "#191c24"   # outer window: title bar, tab strip (darkest)
rail    = "#1c1f28"   # activity bar (icon strip): a step lighter than the window
mantle  = "#1c2029"   # panels / widgets base
base    = "#1f232e"   # editor, active tab and side bar
surface = "#252833"   # inactive tabs, panel
overlay = "#2c2f3f"   # inputs, hover rows, menus
raised  = "#353b4e"   # strong hover
border  = "#2c2f3f"
borderS = "#13151b"   # subtle dark separators
select  = "#4c5261"
muted   = "#787c94"
dim     = "#65737e"
fg      = "#cccccc"
fgHi    = "#dcdcdc"
white   = "#ffffff"

red     = "#f73d3d"   # the accent
redDeep = "#992929"   # status bar
redSoft = "#ee8585"
redTint = "#f73d3d33"
redFaint= "#f73d3d1a"

green   = "#6de687"
teal    = "#5ec488"
yellow  = "#e4bb63"
orange  = "#f78c6c"
cyan    = "#21e2fc"
blue    = "#82aaff"
purple  = "#c792ea"
pink    = "#ff5370"

# dark-only extras
wash    = "#ffffff"   # translucent overlays are white on dark
shadow  = "#00000066"
redHover= "#ff5a5a"
lineNo  = "#4b5063"
lineNoDim = "#3a3f50"
sb1, sb2 = "#41455a", "#575c74"
bracket = "#815f5f"
brGreen, brYellow, brBlue, brPurple, brCyan = "#9ff2b0", "#ffcb6b", "#a9c4ff", "#dbb6f2", "#89ddff"

if light:
    # "Dampened white": cool greys around #ccc, never pure #ffffff.
    crust   = "#c3c5ca"   # outer window: title bar, tab strip (darkest)
    rail    = "#cccdd2"   # activity bar (icon strip): a step lighter than the window
    mantle  = "#dcdde1"   # popups / widgets (a step lighter so they float)
    base    = "#d5d6da"   # editor, active tab and side bar
    surface = "#cbcdd2"   # inactive tabs, panel
    overlay = "#bec1c7"   # hover rows, menus selection
    raised  = "#b2b5bd"   # strong hover
    border  = "#b5b8bf"
    borderS = "#b0b3ba"
    select  = "#a9b6cb"
    muted   = "#4c505a"
    dim     = "#5a5f6a"
    fg      = "#2b2d31"
    fgHi    = "#1a1b1e"
    white   = "#ffffff"

    red     = "#b52525"   # accent, darkened so it reads on grey and carries white text
    redDeep = "#9a2222"
    redSoft = "#8f1d1d"
    redTint = "#b525252e"
    redFaint= "#b5252517"
    redHover= "#9c1f1f"

    green   = "#2b8a3e"
    teal    = "#1f7a5c"
    yellow  = "#8f6400"
    orange  = "#b4561b"
    cyan    = "#0a7f8f"
    blue    = "#2458b3"
    purple  = "#7b3fa8"
    pink    = "#c22d4b"

    wash    = "#000000"   # overlays are black on light
    shadow  = "#00000033"
    lineNo  = "#6e737d"
    lineNoDim = "#8d929c"
    sb1, sb2 = "#8f939c", "#787c86"
    bracket = "#9aa3b5"
    brGreen, brYellow, brBlue, brPurple, brCyan = "#3fa653", "#a87a00", "#3a6fd0", "#9550c4", "#1593a3"

# Cursor: white on dark; the light theme uses near-black, since white would vanish on grey.
cursor = fgHi if light else white

c = {}
def s(**kw):
    for k, v in kw.items():
        c[k.replace("__", ".")] = v

# ---- Base ----
s(focusBorder=red + "99", foreground=fg, disabledForeground=muted,
  descriptionForeground=muted, errorForeground=pink, icon__foreground=fg,
  widget__shadow=shadow, widget__border=border, selection__background=select,
  sash__hoverBorder=red, contrastBorder="#00000000",
  textLink__foreground=red, textLink__activeForeground=redSoft,
  textBlockQuote__background=mantle, textBlockQuote__border=red,
  textCodeBlock__background=crust, textPreformat__foreground=yellow,
  textPreformat__background=overlay, textSeparator__foreground=border)

# ---- Buttons / controls ----
s(button__background=red, button__foreground=white, button__hoverBackground=redHover,
  button__border="#00000000", button__separator="#ffffff55",
  button__secondaryBackground=overlay, button__secondaryForeground=fg,
  button__secondaryHoverBackground=raised,
  checkbox__background=overlay, checkbox__foreground=fgHi, checkbox__border=raised,
  checkbox__selectBackground=overlay, checkbox__selectBorder=red,
  radio__activeForeground=fgHi, radio__activeBackground=redTint, radio__activeBorder=red,
  radio__inactiveForeground=fg, radio__inactiveBorder=raised, radio__inactiveHoverBackground=overlay,
  toolbar__hoverBackground=overlay, toolbar__activeBackground=raised,
  actionBar__toggledBackground=redTint)

# ---- Dropdowns / inputs ----
s(dropdown__background=overlay, dropdown__foreground=fg, dropdown__border=raised,
  dropdown__listBackground=mantle,
  input__background=crust, input__foreground=fgHi, input__border=border,
  input__placeholderForeground=dim,
  inputOption__activeBackground=redTint, inputOption__activeBorder=red,
  inputOption__activeForeground=fgHi, inputOption__hoverBackground=raised,
  inputValidation__errorBackground=mantle, inputValidation__errorBorder=pink,
  inputValidation__warningBackground=mantle, inputValidation__warningBorder=yellow,
  inputValidation__infoBackground=mantle, inputValidation__infoBorder=blue)

# ---- Badges / progress / scrollbars ----
s(badge__background=red, badge__foreground=white,
  progressBar__background=red,
  scrollbar__shadow=shadow,
  scrollbarSlider__background=sb1 + "80", scrollbarSlider__hoverBackground=sb2 + "aa",
  scrollbarSlider__activeBackground=muted + "aa")

# ---- Lists / trees ----
s(list__activeSelectionBackground=raised, list__activeSelectionForeground=fgHi,
  list__activeSelectionIconForeground=fgHi,
  list__inactiveSelectionBackground=overlay, list__inactiveSelectionForeground=fg,
  list__hoverBackground=overlay + "aa", list__hoverForeground=fgHi,
  list__focusBackground=overlay, list__focusForeground=fgHi,
  list__focusOutline=muted + "88", list__inactiveFocusOutline=raised,
  list__dropBackground=raised + "aa", list__highlightForeground=red,
  list__focusHighlightForeground=redSoft, list__invalidItemForeground=pink,
  list__errorForeground=pink, list__warningForeground=yellow,
  list__filterMatchBackground=redTint, list__deemphasizedForeground=muted,
  listFilterWidget__background=mantle, listFilterWidget__outline=red,
  listFilterWidget__noMatchesOutline=pink,
  tree__indentGuidesStroke=raised, tree__inactiveIndentGuidesStroke=border,
  tree__tableColumnsBorder=border, tree__tableOddRowsBackground=wash + "05")

# ---- Activity bar / profiles ----
s(activityBar__background=rail, activityBar__foreground=fgHi,
  activityBar__inactiveForeground=muted, activityBar__border=borderS,
  activityBar__activeBorder=fg, activityBar__activeBackground=overlay,
  activityBar__dropBorder=fg,
  activityBarBadge__background=red, activityBarBadge__foreground=white,
  activityBarTop__foreground=fgHi, activityBarTop__inactiveForeground=muted,
  activityBarTop__activeBorder=fg, activityBarTop__dropBorder=fg,
  activityBarTop__background=base,
  profileBadge__background=red, profileBadge__foreground=white)

# ---- Side bar ----
s(sideBar__background=base, sideBar__foreground=fg, sideBar__border=borderS,
  sideBar__dropBackground=redTint,
  sideBarTitle__foreground=fg, sideBarTitle__background=base,
  sideBarSectionHeader__background=base, sideBarSectionHeader__foreground=fg,
  sideBarSectionHeader__border=border,
  sideBarActivityBarTop__border=border,
  sideBarStickyScroll__background=base, sideBarStickyScroll__shadow=shadow)

# ---- Editor groups / tabs ----
s(editorGroup__border=borderS, editorGroup__dropBackground=redTint,
  editorGroup__emptyBackground=base, editorGroup__dropIntoPromptBackground=mantle,
  editorGroup__dropIntoPromptForeground=fg,
  editorGroupHeader__tabsBackground=crust, editorGroupHeader__tabsBorder=borderS,
  editorGroupHeader__noTabsBackground=base, editorGroupHeader__border=borderS,
  tab__activeBackground=base, tab__activeForeground=fgHi,
  tab__activeBorder=base, tab__activeBorderTop=red,
  tab__unfocusedActiveBackground=base, tab__unfocusedActiveForeground=fg,
  tab__unfocusedActiveBorderTop=redDeep,
  tab__inactiveBackground=surface, tab__inactiveForeground=muted,
  tab__unfocusedInactiveForeground=dim,
  tab__hoverBackground=raised, tab__hoverForeground=fgHi,
  tab__unfocusedHoverBackground=overlay,
  tab__border=borderS, tab__lastPinnedBorder=raised,
  tab__activeModifiedBorder=yellow, tab__inactiveModifiedBorder=yellow + "88",
  tab__dragAndDropBorder=red,
  tab__selectedBackground=base, tab__selectedForeground=fgHi, tab__selectedBorderTop=red,
  editorPane__background=base, sideBySideEditor__horizontalBorder=borderS,
  sideBySideEditor__verticalBorder=borderS)

# ---- Breadcrumbs ----
s(breadcrumb__background=base, breadcrumb__foreground=muted,
  breadcrumb__focusForeground=fgHi, breadcrumb__activeSelectionForeground=red,
  breadcrumbPicker__background=mantle)

# ---- Editor ----
s(editor__background=base, editor__foreground=fgHi,
  editorLineNumber__foreground=lineNo, editorLineNumber__activeForeground=fg,
  editorLineNumber__dimmedForeground=lineNoDim,
  editorCursor__foreground=cursor, editorCursor__background=base,
  editorMultiCursor__primary__foreground=cursor, editorMultiCursor__secondary__foreground=fg,
  editor__selectionBackground=select, editor__inactiveSelectionBackground=select + "80",
  editor__selectionHighlightBackground=select + "80", editor__selectionHighlightBorder="#00000000",
  editor__wordHighlightBackground=select + "80", editor__wordHighlightStrongBackground=red + "26",
  editor__wordHighlightTextBackground=select + "60",
  editor__findMatchBackground=red + "55", editor__findMatchBorder=red,
  editor__findMatchHighlightBackground=yellow + "33", editor__findRangeHighlightBackground=wash + "0d",
  editor__hoverHighlightBackground=wash + "12",
  editor__lineHighlightBackground=wash + "08", editor__lineHighlightBorder="#00000000",
  editor__rangeHighlightBackground=wash + "0a", editor__symbolHighlightBackground=red + "26",
  editor__linkedEditingBackground=red + "1a",
  editor__foldBackground=wash + "08", editor__foldPlaceholderForeground=muted,
  editorLink__activeForeground=red,
  editorWhitespace__foreground=wash + "1a",
  editorIndentGuide__background1=wash + "0f", editorIndentGuide__activeBackground1=wash + "33",
  editorRuler__foreground=wash + "12",
  editorCodeLens__foreground=dim,
  editorBracketMatch__background=bracket + "66", editorBracketMatch__border=bracket,
  editorBracketHighlight__foreground1=yellow, editorBracketHighlight__foreground2=purple,
  editorBracketHighlight__foreground3=cyan, editorBracketHighlight__foreground4=yellow,
  editorBracketHighlight__foreground5=purple, editorBracketHighlight__foreground6=cyan,
  editorBracketHighlight__unexpectedBracket__foreground=pink,
  editorBracketPairGuide__activeBackground1=yellow + "80",
  editorBracketPairGuide__activeBackground2=purple + "80",
  editorBracketPairGuide__activeBackground3=cyan + "80",
  editorInlayHint__background=wash + "0a", editorInlayHint__foreground=dim,
  editorInlayHint__typeForeground=dim, editorInlayHint__parameterForeground=dim,
  editorGhostText__foreground=wash + "40",
  editorLightBulb__foreground=yellow, editorLightBulbAutoFix__foreground=blue,
  editorLightBulbAi__foreground=red,
  editorUnicodeHighlight__border=yellow,
  editorUnnecessaryCode__opacity="#000000aa",
  editorStickyScroll__background=base, editorStickyScroll__shadow=shadow,
  editorStickyScroll__border=borderS, editorStickyScrollHover__background=overlay,
  editorStickyScrollGutter__background=base,
  editorError__foreground=pink, editorWarning__foreground=yellow,
  editorInfo__foreground=blue, editorHint__foreground=teal)

# ---- Gutter / overview ruler / minimap ----
s(editorGutter__background=base, editorGutter__addedBackground=green,
  editorGutter__modifiedBackground=blue, editorGutter__deletedBackground=pink,
  editorGutter__foldingControlForeground=muted,
  editorOverviewRuler__border=borderS, editorOverviewRuler__background=base,
  editorOverviewRuler__findMatchForeground=red + "aa",
  editorOverviewRuler__selectionHighlightForeground=select,
  editorOverviewRuler__errorForeground=pink, editorOverviewRuler__warningForeground=yellow,
  editorOverviewRuler__infoForeground=blue,
  editorOverviewRuler__addedForeground=green + "99",
  editorOverviewRuler__modifiedForeground=blue + "99",
  editorOverviewRuler__deletedForeground=pink + "99",
  minimap__background=base, minimap__findMatchHighlight=red,
  minimap__selectionHighlight=select, minimap__errorHighlight=pink,
  minimap__warningHighlight=yellow, minimapSlider__background=sb1 + "55",
  minimapSlider__hoverBackground=sb2 + "77", minimapSlider__activeBackground=muted + "77",
  minimapGutter__addedBackground=green, minimapGutter__modifiedBackground=blue,
  minimapGutter__deletedBackground=pink)

# ---- Diff ----
s(diffEditor__insertedTextBackground=green + "22", diffEditor__removedTextBackground=pink + "26",
  diffEditor__insertedLineBackground=green + "12", diffEditor__removedLineBackground=pink + "14",
  diffEditor__diagonalFill=wash + "0f", diffEditor__border=borderS,
  diffEditor__unchangedRegionBackground=mantle, diffEditor__unchangedRegionForeground=muted,
  diffEditor__move__border=purple + "88", diffEditor__moveActive__border=purple,
  multiDiffEditor__headerBackground=surface, multiDiffEditor__background=base,
  multiDiffEditor__border=borderS)

# ---- Editor widgets (find, hover, suggest, peek) ----
s(editorWidget__background=mantle, editorWidget__foreground=fg, editorWidget__border=border,
  editorWidget__resizeBorder=red,
  editorHoverWidget__background=mantle, editorHoverWidget__foreground=fg,
  editorHoverWidget__border=border, editorHoverWidget__statusBarBackground=surface,
  editorHoverWidget__highlightForeground=red,
  editorSuggestWidget__background=mantle, editorSuggestWidget__border=border,
  editorSuggestWidget__foreground=fg, editorSuggestWidget__highlightForeground=red,
  editorSuggestWidget__focusHighlightForeground=redSoft,
  editorSuggestWidget__selectedBackground=redTint, editorSuggestWidget__selectedForeground=fgHi,
  editorSuggestWidget__selectedIconForeground=fgHi,
  editorSuggestWidgetStatus__foreground=muted,
  editorMarkerNavigation__background=mantle,
  editorMarkerNavigationError__background=pink, editorMarkerNavigationWarning__background=yellow,
  editorMarkerNavigationInfo__background=blue,
  peekView__border=red, peekViewTitle__background=surface,
  peekViewTitleLabel__foreground=fgHi, peekViewTitleDescription__foreground=muted,
  peekViewEditor__background=mantle, peekViewEditorGutter__background=mantle,
  peekViewEditor__matchHighlightBackground=red + "40",
  peekViewEditorStickyScroll__background=mantle,
  peekViewResult__background=surface, peekViewResult__fileForeground=fgHi,
  peekViewResult__lineForeground=fg, peekViewResult__matchHighlightBackground=red + "40",
  peekViewResult__selectionBackground=redTint, peekViewResult__selectionForeground=fgHi,
  editorError__background="#00000000", editorWarning__background="#00000000")

# ---- Merge conflicts ----
s(merge__currentHeaderBackground=green + "40", merge__currentContentBackground=green + "14",
  merge__incomingHeaderBackground=blue + "40", merge__incomingContentBackground=blue + "14",
  merge__commonHeaderBackground=wash + "20", merge__commonContentBackground=wash + "0a",
  mergeEditor__change__background=blue + "1a", mergeEditor__change__word__background=blue + "33",
  mergeEditor__conflict__unhandledUnfocused__border=yellow + "88",
  mergeEditor__conflict__unhandledFocused__border=yellow,
  mergeEditor__conflict__handledUnfocused__border=green + "55",
  mergeEditor__conflict__handledFocused__border=green)

# ---- Panel / terminal ----
s(panel__background=surface, panel__border=borderS, panel__dropBorder=red,
  panelTitle__activeForeground=fgHi, panelTitle__activeBorder=red,
  panelTitle__inactiveForeground=muted, panelTitle__border=borderS,
  panelTitleBadge__background=red, panelTitleBadge__foreground=white,
  panelInput__border=border, panelSection__border=borderS,
  panelSectionHeader__background=surface, panelSectionHeader__foreground=fg,
  panelStickyScroll__background=surface, panelStickyScroll__shadow=shadow,
  outputView__background=surface, outputViewStickyScroll__background=surface,
  terminal__background=surface, terminal__foreground=fgHi, terminal__border=borderS,
  terminal__selectionBackground=select + "aa", terminal__inactiveSelectionBackground=select + "66",
  terminal__findMatchBackground=red + "55", terminal__findMatchHighlightBackground=yellow + "33",
  terminalCursor__foreground=cursor, terminal__dropBackground=redTint, terminal__tab__activeBorder=red,
  terminalCommandDecoration__defaultBackground=muted,
  terminalCommandDecoration__successBackground=green,
  terminalCommandDecoration__errorBackground=pink,
  terminalOverviewRuler__cursorForeground=cursor, terminalOverviewRuler__findMatchForeground=red,
  terminalStickyScroll__background=surface, terminalStickyScrollHover__background=overlay,
  terminal__ansiBlack=(fgHi if light else crust), terminal__ansiRed=red, terminal__ansiGreen=green,
  terminal__ansiYellow=yellow, terminal__ansiBlue=blue, terminal__ansiMagenta=purple,
  terminal__ansiCyan=cyan, terminal__ansiWhite=("#8a8e97" if light else fg),
  terminal__ansiBrightBlack=muted, terminal__ansiBrightRed=redSoft,
  terminal__ansiBrightGreen=brGreen, terminal__ansiBrightYellow=brYellow,
  terminal__ansiBrightBlue=brBlue, terminal__ansiBrightMagenta=brPurple,
  terminal__ansiBrightCyan=brCyan, terminal__ansiBrightWhite=white)

# ---- Status bar ----
s(statusBar__background=crust, statusBar__foreground=fg, statusBar__border=borderS,
  statusBar__focusBorder=muted,
  statusBar__debuggingBackground=orange, statusBar__debuggingForeground=(white if light else crust),
  statusBar__debuggingBorder=borderS,
  statusBar__noFolderBackground=crust, statusBar__noFolderForeground=fg,
  statusBar__noFolderBorder=borderS,
  statusBarItem__activeBackground=wash + "33", statusBarItem__hoverBackground=wash + "1f",
  statusBarItem__hoverForeground=fgHi, statusBarItem__focusBorder=muted,
  statusBarItem__prominentBackground="#00000033", statusBarItem__prominentForeground=fgHi,
  statusBarItem__prominentHoverBackground="#00000055",
  statusBarItem__remoteBackground=overlay, statusBarItem__remoteForeground=fgHi,
  statusBarItem__remoteHoverBackground=raised,
  statusBarItem__errorBackground=pink, statusBarItem__errorForeground=white,
  statusBarItem__warningBackground=yellow, statusBarItem__warningForeground=(white if light else crust),
  statusBarItem__offlineBackground=muted, statusBarItem__offlineForeground=white,
  statusBarItem__compactHoverBackground=wash + "1f")

# ---- Title bar / command center ----
s(titleBar__activeBackground=crust, titleBar__activeForeground=fg,
  titleBar__inactiveBackground=crust, titleBar__inactiveForeground=muted,
  titleBar__border=borderS,
  commandCenter__background=surface, commandCenter__foreground=fg,
  commandCenter__activeBackground=overlay, commandCenter__activeForeground=fgHi,
  commandCenter__border=border, commandCenter__activeBorder=raised,
  commandCenter__inactiveForeground=muted, commandCenter__inactiveBorder=border,
  commandCenter__debuggingBackground=orange + "33")

# ---- Menus ----
s(menubar__selectionBackground=overlay, menubar__selectionForeground=fgHi,
  menubar__selectionBorder="#00000000",
  menu__background=mantle, menu__foreground=fg, menu__border=border,
  menu__selectionBackground=redTint, menu__selectionForeground=fgHi,
  menu__selectionBorder="#00000000", menu__separatorBackground=border)

# ---- Quick input / command palette ----
s(quickInput__background=mantle, quickInput__foreground=fg,
  quickInputTitle__background=surface,
  quickInputList__focusBackground=redTint, quickInputList__focusForeground=fgHi,
  quickInputList__focusIconForeground=fgHi,
  pickerGroup__foreground=red, pickerGroup__border=border,
  keybindingLabel__background=overlay, keybindingLabel__foreground=fgHi,
  keybindingLabel__border=raised, keybindingLabel__bottomBorder=borderS,
  keybindingTable__headerBackground=surface, keybindingTable__rowsBackground=wash + "05")

# ---- Notifications / banner ----
s(notificationCenter__border=border, notificationCenterHeader__background=surface,
  notificationCenterHeader__foreground=fg,
  notifications__background=mantle, notifications__foreground=fg,
  notifications__border=border, notificationToast__border=red + "88",
  notificationLink__foreground=red,
  notificationsErrorIcon__foreground=pink, notificationsWarningIcon__foreground=yellow,
  notificationsInfoIcon__foreground=blue,
  banner__background=redDeep, banner__foreground=white, banner__iconForeground=white)

# ---- Extensions / settings / welcome ----
s(extensionButton__background=red, extensionButton__foreground=white,
  extensionButton__hoverBackground=redHover, extensionButton__separator="#ffffff55",
  extensionButton__prominentBackground=red, extensionButton__prominentForeground=white,
  extensionButton__prominentHoverBackground=redHover,
  extensionBadge__remoteBackground=red, extensionBadge__remoteForeground=white,
  extensionIcon__starForeground=yellow, extensionIcon__verifiedForeground=blue,
  extensionIcon__preReleaseForeground=orange, extensionIcon__sponsorForeground=pink,
  settings__headerForeground=fgHi, settings__modifiedItemIndicator=red,
  settings__headerBorder=border, settings__sashBorder=border,
  settings__dropdownBackground=overlay, settings__dropdownBorder=raised,
  settings__dropdownListBorder=border,
  settings__checkboxBackground=overlay, settings__checkboxBorder=raised,
  settings__textInputBackground=crust, settings__textInputBorder=border,
  settings__numberInputBackground=crust, settings__numberInputBorder=border,
  settings__focusedRowBackground=wash + "08", settings__rowHoverBackground=wash + "05",
  settings__focusedRowBorder=red + "66",
  welcomePage__background=base, welcomePage__tileBackground=surface,
  welcomePage__tileHoverBackground=overlay, welcomePage__tileBorder=border,
  welcomePage__progress__background=overlay, welcomePage__progress__foreground=red,
  walkThrough__embeddedEditorBackground=crust,
  walkthrough__stepTitle__foreground=fgHi)

# ---- Debug ----
s(debugToolBar__background=mantle, debugToolBar__border=border,
  debugIcon__breakpointForeground=red, debugIcon__breakpointDisabledForeground=muted,
  debugIcon__breakpointUnverifiedForeground=muted,
  debugIcon__breakpointCurrentStackframeForeground=yellow,
  debugIcon__startForeground=green, debugIcon__pauseForeground=blue,
  debugIcon__stopForeground=pink, debugIcon__disconnectForeground=pink,
  debugIcon__restartForeground=green, debugIcon__stepOverForeground=blue,
  debugIcon__stepIntoForeground=blue, debugIcon__stepOutForeground=blue,
  debugIcon__continueForeground=green,
  editor__stackFrameHighlightBackground=yellow + "26",
  editor__focusedStackFrameHighlightBackground=green + "26",
  debugExceptionWidget__background=mantle, debugExceptionWidget__border=pink,
  debugTokenExpression__name=purple, debugTokenExpression__value=fg,
  debugTokenExpression__string=yellow, debugTokenExpression__boolean=cyan,
  debugTokenExpression__number=red, debugTokenExpression__error=pink,
  debugConsole__infoForeground=blue, debugConsole__warningForeground=yellow,
  debugConsole__errorForeground=pink, debugConsole__sourceForeground=fg,
  debugConsoleInputIcon__foreground=red)

# ---- Testing ----
s(testing__iconPassed=green, testing__iconFailed=pink, testing__iconErrored=pink,
  testing__iconQueued=yellow, testing__iconSkipped=muted, testing__iconUnset=muted,
  testing__runAction=green, testing__peekBorder=pink, testing__peekHeaderBackground=mantle,
  testing__message__error__lineBackground=pink + "14",
  testing__coveredBackground=green + "14", testing__uncoveredBackground=pink + "14",
  testing__coverCountBadgeBackground=overlay, testing__coverCountBadgeForeground=fg)

# ---- Git / SCM ----
s(gitDecoration__addedResourceForeground=green,
  gitDecoration__modifiedResourceForeground=blue,
  gitDecoration__deletedResourceForeground=pink,
  gitDecoration__renamedResourceForeground=teal,
  gitDecoration__untrackedResourceForeground=green,
  gitDecoration__ignoredResourceForeground=dim,
  gitDecoration__conflictingResourceForeground=orange,
  gitDecoration__stageModifiedResourceForeground=blue,
  gitDecoration__stageDeletedResourceForeground=pink,
  gitDecoration__submoduleResourceForeground=purple,
  scmGraph__foreground1=red, scmGraph__foreground2=yellow, scmGraph__foreground3=cyan,
  scmGraph__foreground4=purple, scmGraph__foreground5=green,
  scmGraph__historyItemRefColor=red, scmGraph__historyItemRemoteRefColor=purple,
  scmGraph__historyItemBaseRefColor=yellow,
  scmGraph__historyItemHoverDefaultLabelForeground=fgHi,
  scmGraph__historyItemHoverLabelForeground=(white if light else crust),
  scmGraph__historyItemHoverAdditionsForeground=green,
  scmGraph__historyItemHoverDeletionsForeground=pink)

# ---- Notebooks ----
s(notebook__editorBackground=base, notebook__cellEditorBackground=mantle,
  notebook__cellBorderColor=border, notebook__cellToolbarSeparator=border,
  notebook__focusedCellBorder=red + "88", notebook__inactiveFocusedCellBorder=raised,
  notebook__selectedCellBackground=wash + "08", notebook__selectedCellBorder=raised,
  notebook__cellHoverBackground=wash + "05", notebook__focusedEditorBorder=red + "88",
  notebook__outputContainerBackgroundColor=mantle,
  notebook__cellStatusBarItemHoverBackground=overlay,
  notebookStatusSuccessIcon__foreground=green, notebookStatusErrorIcon__foreground=pink,
  notebookStatusRunningIcon__foreground=blue, notebookScrollbarSlider__background=sb1 + "80")

# ---- Chat / AI ----
s(chat__requestBackground=mantle, chat__requestBorder=border,
  chat__avatarBackground=overlay, chat__avatarForeground=fg,
  chat__slashCommandBackground=redTint, chat__slashCommandForeground=redSoft,
  chat__editedFileForeground=blue,
  chat__linesAddedForeground=green, chat__linesRemovedForeground=pink,
  chat__requestBubbleBackground=overlay, chat__requestBubbleHoverBackground=raised,
  chat__checkpointSeparator=border,
  inlineChat__background=mantle, inlineChat__border=red + "88",
  inlineChat__foreground=fg, inlineChat__shadow=shadow,
  inlineChatInput__background=crust, inlineChatInput__border=border,
  inlineChatInput__focusBorder=red + "99", inlineChatInput__placeholderForeground=dim,
  inlineChatDiff__inserted=green + "22", inlineChatDiff__removed=pink + "26",
  inlineEdit__originalBackground=pink + "14", inlineEdit__modifiedBackground=green + "14",
  inlineEdit__originalChangedTextBackground=pink + "33",
  inlineEdit__modifiedChangedTextBackground=green + "33",
  inlineEdit__gutterIndicator__primaryBackground=red + "66",
  inlineEdit__gutterIndicator__primaryForeground=white,
  inlineEdit__gutterIndicator__primaryBorder=red,
  inlineEdit__gutterIndicator__secondaryBackground=overlay,
  inlineEdit__gutterIndicator__secondaryForeground=fg,
  inlineEdit__gutterIndicator__successfulBackground=green + "66",
  inlineEdit__gutterIndicator__background=surface)

# ---- Misc ----
s(charts__foreground=fg, charts__lines=muted, charts__red=pink, charts__blue=blue,
  charts__yellow=yellow, charts__orange=orange, charts__green=green, charts__purple=purple,
  symbolIcon__classForeground=yellow, symbolIcon__functionForeground=green,
  symbolIcon__methodForeground=blue, symbolIcon__variableForeground=fgHi,
  symbolIcon__keywordForeground=cyan, symbolIcon__constantForeground=red,
  symbolIcon__stringForeground=yellow, symbolIcon__propertyForeground=purple,
  symbolIcon__fieldForeground=purple, symbolIcon__interfaceForeground=yellow,
  symbolIcon__moduleForeground=pink, symbolIcon__enumeratorForeground=orange,
  problemsErrorIcon__foreground=pink, problemsWarningIcon__foreground=yellow,
  problemsInfoIcon__foreground=blue,
  editorOverviewRuler__currentContentForeground=green + "99",
  editorOverviewRuler__incomingContentForeground=blue + "99",
  ports__iconRunningProcessForeground=green,
  searchEditor__findMatchBackground=red + "40", searchEditor__textInputBorder=border,
  editorCommentsWidget__resolvedBorder=muted, editorCommentsWidget__unresolvedBorder=red,
  editorCommentsWidget__rangeBackground=red + "14",
  simpleFindWidget__sashBorder=border,
  interactive__activeCodeBorder=red, interactive__inactiveCodeBorder=border)

t = json.load(open(path))
t["type"] = "light" if light else "dark"
t["colors"] = c
order = ["$schema", "name", "type", "semanticHighlighting", "colors", "tokenColors", "semanticTokenColors"]
t = {**{k: t[k] for k in order if k in t}, **{k: v for k, v in t.items() if k not in order}}
open(path, "w").write(json.dumps(t, indent="\t") + "\n")
print(len(c), "colors written")
