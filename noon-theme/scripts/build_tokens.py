"""Regenerates `tokenColors` and `semanticTokenColors` of the Noon theme.

Palette: "Ember Apricot" at +60% vibrance (OKLCH chroma), made for Noon. Warm apricot keywords, cyan types,
green strings, violet numbers and quiet italic grey comments. Red is kept only
for invalid code and git deletions, never for normal code. Every color keeps
at least 4.5:1 contrast on its theme's editor background.

Usage:
  python3 scripts/build_tokens.py themes/noon-color-theme.json
  python3 scripts/build_tokens.py themes/noon-light-color-theme.json --light
"""
import json, sys

light = "--light" in sys.argv

# ---- Ember Apricot +60%: dark ----
text       = "#dedad4"   # plain text, fields, properties, namespaces
punct      = "#a8a29b"   # operators, punctuation
keyword    = "#fe9f5a"   # keywords, built-in types
control    = "#fe78dd"   # if / return / await / using ...
typeName   = "#02dafa"   # classes, records, delegates
iface      = "#20e8a2"   # interfaces, enums, type parameters
struct     = "#20e8a2"   # structs, record structs
method     = "#f5db92"
variable   = "#cfd3dc"   # locals, parameters
attr       = "#02dafa"   # HTML attributes, CSS properties, JSON/YAML keys
string     = "#8ee21c"
escape     = "#02fede"
number     = "#9b6fff"
comment    = "#848b99"   # shown in italics
docTag     = "#a0a7b4"   # XML doc comment tags
preproc    = "#a8a29b"
excluded   = "#7a7f8c"   # #if false code: intentionally faded
tagPunct   = "#a8a29b"   # HTML < >
attrValue  = "#8ee21c"   # HTML attribute values, CSS keyword values
selector   = "#02dafa"   # CSS selectors
invalid    = "#ff5370"   # errors only
inserted   = "#6de687"
deleted    = "#ff5370"
changed    = "#82aaff"
heading    = "#fe9f5a"
razor      = "#fe9f5a"   # Razor @ transitions and directives
markupTag  = "#fe9f5a"   # HTML/XML element names

if light:
    # ---- Ember Apricot +60%: light ----
    text       = "#22201d"
    punct      = "#4f4a44"
    keyword    = "#914902"
    control    = "#ad018f"
    typeName   = "#016477"
    iface      = "#036b40"
    struct     = "#036b40"
    method     = "#745902"
    variable   = "#2f3440"
    attr       = "#016477"
    string     = "#376700"
    escape     = "#016857"
    number     = "#6d01f9"
    comment    = "#565b67"
    docTag     = "#4a4f5a"
    preproc    = "#4f4a44"
    excluded   = "#6c717b"   # intentionally faded
    tagPunct   = "#4f4a44"
    attrValue  = "#376700"
    selector   = "#016477"
    invalid    = "#b02a2a"
    inserted   = "#216a30"
    deleted    = "#af2844"
    changed    = "#2458b3"
    heading    = "#914902"
    razor      = "#914902"
    markupTag  = "#914902"

BACKGROUND = "#d5d6da" if light else "#1f232e"

def _lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]

def contrast(a, b=BACKGROUND):
    x, y = sorted([_lum(a), _lum(b)])
    return (y + 0.05) / (x + 0.05)

def ensure_contrast(h, minimum=4.5):
    """Darkens (light) or lightens (dark) a color, keeping its hue, until it is readable."""
    target = (0, 0, 0) if light else (255, 255, 255)
    rgb = [int(h[i:i + 2], 16) for i in (1, 3, 5)]
    out = h
    for step in range(101):
        if contrast(out) >= minimum:
            return out
        t = step / 100
        out = "#" + "".join(f"{round(v + (g - v) * t):02x}" for v, g in zip(rgb, target))
    return out

adjusted = {}
for _name in ["text", "punct", "keyword", "control", "typeName", "iface", "struct", "method", "variable",
              "string", "escape", "number", "comment", "docTag", "preproc", "tagPunct", "attrValue",
              "selector", "markupTag", "attr", "invalid", "inserted", "deleted", "changed", "heading", "razor"]:
    _old = globals()[_name]
    _new = ensure_contrast(_old)
    if _new != _old:
        adjusted[_name] = (_old, _new)
        globals()[_name] = _new

rules = []
def r(name, scopes, fg=None, style=None):
    s = {}
    if fg: s["foreground"] = fg
    if style is not None: s["fontStyle"] = style
    rules.append({"name": name, "scope": scopes, "settings": s})

# ---- General (every language) ----
r("Plain text", ["source", "text", "meta.embedded", "variable.other", "variable.other.readwrite", "meta.definition.variable.name"], text)
r("Comments", ["comment", "punctuation.definition.comment"], comment, "italic")
r("Strings", ["string", "string.quoted", "string.template", "punctuation.definition.string"], string)
r("String escapes", ["constant.character.escape", "constant.character.entity", "constant.other.placeholder", "constant.character.format.placeholder"], escape)
r("Numbers", ["constant.numeric", "keyword.other.unit"], number)
r("Language constants", ["constant.language", "constant.language.boolean", "constant.language.null", "constant.language.undefined"], keyword)
r("Other constants", ["constant.other", "variable.other.constant", "variable.other.enummember", "support.constant"], text)
r("Keywords", ["keyword", "keyword.other", "keyword.operator.new", "keyword.operator.expression", "keyword.operator.logical.python",
   "storage", "storage.type", "storage.modifier", "keyword.type", "support.type.primitive", "support.type.builtin",
   "variable.language", "variable.language.this", "variable.language.super"], keyword)
r("Control keywords", ["keyword.control", "keyword.control.flow", "keyword.control.conditional", "keyword.control.loop",
   "keyword.control.import", "keyword.control.export", "keyword.control.from", "keyword.control.trycatch",
   "keyword.control.switch", "keyword.operator.expression.await", "keyword.control.anchor.regexp"], control)
r("Operators and punctuation", ["keyword.operator", "punctuation", "meta.brace", "punctuation.accessor",
   "punctuation.separator", "punctuation.terminator", "meta.delimiter"], punct)
r("Types and classes", ["entity.name.type", "entity.name.class", "entity.other.inherited-class", "support.class",
   "support.type", "entity.name.type.class", "entity.name.type.delegate", "entity.name.type.record"], typeName)
r("Interfaces, enums, type parameters", ["entity.name.type.interface", "entity.name.type.enum",
   "entity.name.type.type-parameter", "entity.name.type.parameter"], iface)
r("Structs", ["entity.name.type.struct", "entity.name.type.record.struct"], struct)
r("Functions and methods", ["entity.name.function", "support.function", "meta.function-call.generic", "variable.function",
   "entity.name.method", "meta.function-call entity.name.function"], method)
r("Parameters and locals", ["variable.parameter", "entity.name.variable.local", "entity.name.variable.parameter",
   "meta.parameter", "variable.other.local"], variable)
r("Properties and fields", ["variable.other.property", "variable.other.object.property", "entity.name.variable.field",
   "entity.name.variable.property", "support.variable.property", "meta.object-literal.key"], text)
r("Namespaces", ["entity.name.namespace", "entity.name.type.namespace", "entity.name.scope-resolution", "entity.name.module"], text)
r("Labels", ["entity.name.label"], text)
r("Decorators and attributes", ["meta.decorator", "punctuation.decorator", "entity.name.function.decorator"], typeName)
r("Regex", ["string.regexp"], string)
r("Regex groups and classes", ["string.regexp punctuation.definition.group", "string.regexp constant.other.character-class",
   "string.regexp keyword.operator.quantifier", "constant.other.character-class.regexp"], escape)
r("Invalid", ["invalid", "invalid.illegal", "invalid.deprecated"], invalid)
r("Links", ["*url*", "*link*", "*uri*"], None, "underline")

# ---- C# ----
r("C#: built-in types", ["keyword.type.cs", "keyword.type.string.cs", "keyword.type.int.cs", "storage.type.cs"], keyword)
r("C#: modifiers and declarations", ["storage.modifier.cs", "keyword.other.class.cs", "keyword.other.struct.cs",
   "keyword.other.interface.cs", "keyword.other.enum.cs", "keyword.other.record.cs", "keyword.other.namespace.cs",
   "keyword.other.using.cs", "keyword.operator.new.cs", "keyword.other.var.cs", "keyword.other.get.cs",
   "keyword.other.set.cs", "keyword.other.init.cs"], keyword)
r("C#: control flow", ["keyword.control.cs", "keyword.control.flow.cs", "keyword.control.conditional.cs",
   "keyword.control.loop.cs", "keyword.control.try.cs", "keyword.control.switch.cs", "keyword.operator.await.cs",
   "keyword.control.context.cs", "keyword.operator.expression.query.cs"], control)
r("C#: classes", ["entity.name.type.class.cs", "entity.name.type.delegate.cs", "entity.name.type.record.cs", "entity.name.type.cs"], typeName)
r("C#: interfaces and enums", ["entity.name.type.interface.cs", "entity.name.type.enum.cs", "entity.name.type.type-parameter.cs"], iface)
r("C#: structs", ["entity.name.type.struct.cs"], struct)
r("C#: namespaces", ["entity.name.type.namespace.cs", "entity.name.namespace.cs"], text)
r("C#: methods", ["entity.name.function.cs"], method)
r("C#: locals and parameters", ["entity.name.variable.local.cs", "entity.name.variable.parameter.cs",
   "variable.parameter.cs", "entity.name.variable.tuple-element.cs"], variable)
r("C#: fields, properties, events", ["entity.name.variable.field.cs", "entity.name.variable.property.cs",
   "entity.name.variable.event.cs", "variable.other.object.property.cs", "variable.other.object.cs",
   "entity.name.variable.enum-member.cs"], text)
r("C#: attributes", ["entity.name.type.attribute.cs", "meta.attribute.cs entity.name.type"], typeName)
r("C#: preprocessor", ["meta.preprocessor.cs", "keyword.preprocessor.cs", "entity.name.variable.preprocessor.symbol.cs",
   "punctuation.separator.hash.cs"], preproc)
r("C#: verbatim and interpolated strings", ["string.quoted.double.verbatim.cs", "string.quoted.double.cs",
   "punctuation.definition.interpolation.begin.cs", "punctuation.definition.interpolation.end.cs"], string)
r("C#: interpolation content", ["meta.interpolation.cs"], text)
r("C#: XML doc comment text", ["comment.block.documentation.cs", "comment.block.documentation"], comment)
r("C#: XML doc comment tags", ["comment.block.documentation.cs entity.name.tag", "comment.block.documentation.cs punctuation.definition.tag",
   "comment.block.documentation.cs entity.other.attribute-name", "comment.block.documentation.cs punctuation.separator",
   "comment.block.documentation.cs string", "comment.block.documentation.cs punctuation.definition.string"], docTag)

# ---- Razor / cshtml ----
r("Razor: transitions and directives", ["keyword.control.razor.transition", "keyword.control.cshtml.transition",
   "keyword.control.razor.directive", "keyword.control.cshtml.directive", "keyword.control.razor.directive.attribute"], razor)
r("Razor: components and tag helpers", ["entity.name.class.element.component", "entity.name.class.element.taghelper"], struct)
r("Razor: component attributes", ["entity.name.class.attribute.component", "entity.name.class.attribute.taghelper"], attr)
r("Razor: comments", ["comment.block.razor", "meta.comment.razor", "keyword.control.razor.comment.star"], comment)

# ---- HTML / XML / JSX ----
r("Markup: tag names", ["entity.name.tag", "meta.tag.sgml", "entity.name.tag.html", "entity.name.tag.xml", "meta.tag.sgml.doctype"], markupTag)
r("Markup: components (JSX, Vue, Svelte)", ["support.class.component", "entity.name.tag.component", "entity.name.tag.tsx support.class.component"], typeName)
r("Markup: tag delimiters", ["punctuation.definition.tag", "punctuation.definition.tag.begin", "punctuation.definition.tag.end",
   "punctuation.definition.tag.html", "punctuation.definition.tag.xml"], tagPunct)
r("Markup: attribute names", ["entity.other.attribute-name", "entity.other.attribute-name.html",
   "entity.other.attribute-name.localname.xml", "entity.other.attribute-name.jsx"], attr)
r("Markup: attribute values", ["string.quoted.double.html", "string.quoted.single.html", "string.unquoted.html",
   "meta.attribute string.quoted", "string.quoted.double.xml", "string.quoted.single.xml",
   "punctuation.definition.string.begin.html", "punctuation.definition.string.end.html"], attrValue)
r("Markup: entities", ["constant.character.entity.html", "constant.character.entity.named", "punctuation.definition.entity.html"], escape)
r("Markup: equals", ["punctuation.separator.key-value.html", "punctuation.separator.key-value.xml"], tagPunct)
r("Markup: embedded script braces", ["punctuation.section.embedded", "punctuation.section.embedded.begin", "punctuation.section.embedded.end"], keyword)
r("Markup: XML processing instructions", ["meta.tag.preprocessor.xml", "entity.name.tag.preprocessor"], preproc)

# ---- CSS / SCSS / Less ----
r("CSS: selectors", ["entity.name.tag.css", "entity.name.tag.scss", "entity.name.tag.less", "entity.other.attribute-name.class.css",
   "entity.other.attribute-name.id.css", "entity.other.attribute-name.class", "entity.other.attribute-name.id",
   "entity.other.attribute-name.pseudo-class", "entity.other.attribute-name.pseudo-element", "meta.selector",
   "entity.other.keyframe-offset", "entity.other.attribute-name.parent-selector"], selector)
r("CSS: property names", ["support.type.property-name", "support.type.property-name.css", "support.type.vendored.property-name",
   "meta.property-name", "support.type.custom-property"], attr)
r("CSS: property values", ["support.constant.property-value", "meta.property-value", "support.constant.font-name",
   "support.constant.color", "constant.other.color.rgb-value", "support.constant.vendored.property-value"], attrValue)
r("CSS: numbers and units", ["constant.numeric.css", "keyword.other.unit.css", "constant.numeric.scss", "keyword.other.unit.scss"], number)
r("CSS: functions", ["support.function.misc.css", "support.function.transform.css", "support.function.gradient.css",
   "support.function.calc.css", "support.function.var.css", "support.function.url.css", "support.function.misc.scss"], method)
r("CSS: at-rules", ["keyword.control.at-rule", "keyword.control.at-rule.media", "keyword.control.at-rule.import",
   "punctuation.definition.keyword.css", "support.constant.media"], keyword)
r("CSS: !important", ["keyword.other.important.css", "keyword.other.default.scss"], keyword)
r("SCSS: variables", ["variable.scss", "variable.other.less", "variable.css", "variable.argument.css"], variable)

# ---- JavaScript / TypeScript ----
r("JS/TS: declarations", ["storage.type.function", "storage.type.class", "storage.type.interface", "storage.type.type",
   "storage.type.enum", "storage.type.namespace", "storage.modifier.async", "storage.type.const", "storage.type.let",
   "storage.type.var", "keyword.operator.typeof", "keyword.operator.instanceof", "keyword.operator.new",
   "keyword.operator.expression.of", "keyword.operator.expression.in", "keyword.operator.expression.keyof"], keyword)
r("JS/TS: arrow", ["storage.type.function.arrow"], keyword)
r("JS/TS: control flow", ["keyword.control.flow.js", "keyword.control.flow.ts", "keyword.control.conditional.js",
   "keyword.control.conditional.ts", "keyword.control.loop.js", "keyword.control.loop.ts", "keyword.control.import.js",
   "keyword.control.import.ts", "keyword.control.export.js", "keyword.control.export.ts", "keyword.control.from.js",
   "keyword.control.from.ts", "keyword.control.trycatch.js", "keyword.control.trycatch.ts", "keyword.control.as"], control)
r("JS/TS: types", ["entity.name.type.ts", "entity.name.type.tsx", "entity.name.type.alias", "support.type.primitive.ts",
   "entity.name.type.module"], typeName)
r("JS/TS: built-in types", ["support.type.primitive", "support.type.builtin.ts"], keyword)
r("JS/TS: interfaces", ["entity.name.type.interface.ts", "entity.name.type.interface.tsx"], iface)
r("JS/TS: enums", ["entity.name.type.enum.ts", "entity.name.type.enum.tsx"], iface)
r("JS/TS: type parameters", ["entity.name.type.parameter.ts", "entity.name.type.parameter.tsx"], iface)
r("JS/TS: template expressions", ["punctuation.definition.template-expression.begin", "punctuation.definition.template-expression.end"], keyword)
r("JS/TS: template content", ["meta.template.expression"], text)
r("JS/TS: object keys", ["meta.object-literal.key", "meta.object.member", "variable.other.property.ts", "variable.other.property.js"], text)
r("JS/TS: built-ins", ["support.variable.dom", "support.class.builtin", "support.variable.object", "support.class.console", "support.class.promise"], typeName)

# ---- JSON / YAML ----
r("JSON: keys", ["support.type.property-name.json", "meta.structure.dictionary.json support.type.property-name.json"], attr)
r("JSON: strings", ["string.quoted.double.json", "meta.structure.dictionary.value.json string.quoted.double.json"], string)
r("JSON: constants", ["constant.language.json"], keyword)
r("YAML: keys", ["entity.name.tag.yaml"], attr)
r("YAML: anchors", ["entity.name.type.anchor.yaml", "variable.other.alias.yaml"], typeName)

# ---- Markdown ----
r("Markdown: headings", ["markup.heading", "markup.heading entity.name", "markup.heading punctuation.definition.heading", "entity.name.section.markdown"], heading, "bold")
r("Markdown: bold", ["markup.bold"], text, "bold")
r("Markdown: italic", ["markup.italic"], text, "italic")
r("Markdown: bold italic", ["markup.bold markup.italic", "markup.italic markup.bold"], text, "bold italic")
r("Markdown: strikethrough", ["markup.strikethrough"], None, "strikethrough")
r("Markdown: inline code", ["markup.inline.raw", "markup.inline.raw.string.markdown"], string)
r("Markdown: code fences", ["punctuation.definition.markdown", "markup.fenced_code.block.markdown punctuation.definition", "fenced_code.block.language"], tagPunct)
r("Markdown: links", ["markup.underline.link", "string.other.link.title.markdown", "string.other.link.description.markdown"], variable)
r("Markdown: link URLs", ["markup.underline.link.markdown", "markup.underline.link.image.markdown"], string)
r("Markdown: quotes", ["markup.quote"], comment, "italic")
r("Markdown: list markers", ["punctuation.definition.list.begin.markdown", "beginning.punctuation.definition.list.markdown"], keyword)
r("Markdown: separators", ["meta.separator.markdown"], tagPunct)

# ---- Diffs (red here means "deleted", same as git) ----
r("Diff: inserted", ["markup.inserted", "meta.diff.header.to-file", "punctuation.definition.inserted"], inserted)
r("Diff: deleted", ["markup.deleted", "meta.diff.header.from-file", "punctuation.definition.deleted"], deleted)
r("Diff: changed", ["markup.changed", "punctuation.definition.changed"], changed)
r("Diff: headers", ["meta.diff.range", "meta.diff.header"], keyword)

# ---- Semantic tokens: Roslyn (C#), TypeScript, CSS, HTML ----
semantic = {
    "namespace": text, "class": typeName, "recordClass": typeName, "delegate": typeName,
    "struct": struct, "recordStruct": struct,
    "interface": iface, "enum": iface, "typeParameter": iface,
    "type": typeName, "type.defaultLibrary": typeName,
    "enumMember": text, "event": text, "property": text, "field": text, "constant": text,
    "method": method, "function": method, "extensionMethod": method, "member": method,
    "parameter": variable, "variable": variable, "local": variable,
    "variable.readonly": variable, "variable.defaultLibrary": typeName,
    "keyword": keyword, "controlKeyword": control, "modifier": keyword,
    "operator": punct, "operatorOverloaded": method, "punctuation": punct,
    "string": string, "stringVerbatim": string, "stringEscapeCharacter": escape,
    "number": number, "comment": comment, "regexp": string,
    "macro": preproc, "preprocessorText": preproc, "excludedCode": excluded, "label": text,
    "xmlDocCommentText": comment, "xmlDocCommentName": docTag, "xmlDocCommentDelimiter": docTag,
    "xmlDocCommentAttributeName": docTag, "xmlDocCommentAttributeQuotes": docTag,
    "xmlDocCommentAttributeValue": docTag, "xmlDocCommentComment": comment, "xmlDocCommentCDataSection": comment,
    "xmlDocCommentEntityReference": docTag,
    "regexComment": comment, "regexText": string, "regexCharacterClass": escape, "regexAnchor": control,
    "regexQuantifier": escape, "regexGrouping": escape, "regexAlternation": escape,
    "regexSelfEscapedCharacter": escape, "regexOtherEscape": escape,
    "jsonComment": comment, "jsonNumber": number, "jsonString": string, "jsonKeyword": keyword,
    "jsonPropertyName": attr, "jsonPunctuation": punct, "jsonOperator": punct,
    "razorTransition": razor, "razorDirective": razor, "razorDirectiveAttribute": razor,
    "razorComponentElement": struct, "razorTagHelperElement": struct,
    "razorComponentAttribute": attr, "razorTagHelperAttribute": attr, "razorComment": comment,
    "markupElement": markupTag, "markupAttribute": attr, "markupAttributeValue": attrValue,
    "markupAttributeQuote": attrValue, "markupTagDelimiter": tagPunct, "markupOperator": tagPunct,
    "markupComment": comment, "markupCommentPunctuation": comment,
    "*.deprecated": {"strikethrough": True},
}

# Comments are italic in semantic highlighting too.
semantic = {k: ({"foreground": v, "italic": True} if v == comment and k != "*.deprecated" else v) for k, v in semantic.items()}

path = sys.argv[1]
t = json.load(open(path))
t["semanticHighlighting"] = True
t["tokenColors"] = rules
t["semanticTokenColors"] = semantic
order = ["$schema", "name", "type", "semanticHighlighting", "colors", "tokenColors", "semanticTokenColors"]
t = {k: t[k] for k in order if k in t}
open(path, "w").write(json.dumps(t, indent="\t") + "\n")
print(len(rules), "token rules,", len(semantic), "semantic token colors")
for k, (o, n) in adjusted.items():
    print(f"  contrast fix: {k} {o} -> {n} ({contrast(n):.1f}:1)")
