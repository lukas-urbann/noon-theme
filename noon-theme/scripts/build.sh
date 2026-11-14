#!/bin/sh
# Regenerates both theme files from the palettes in build_colors.py and build_tokens.py.
set -e
cd "$(dirname "$0")/.."
python3 scripts/build_colors.py themes/noon-color-theme.json
python3 scripts/build_tokens.py themes/noon-color-theme.json
python3 scripts/build_colors.py themes/noon-light-color-theme.json --light
python3 scripts/build_tokens.py themes/noon-light-color-theme.json --light
python3 scripts/build_zed.py
