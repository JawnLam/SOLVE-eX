#!/bin/sh
# list-tools-by-facet.sh — list tool entries matching a single facet value.
#
# Usage:
#   ./list-tools-by-facet.sh FACET VALUE [--help]
#
# FACET is the YAML frontmatter key (without leading colon).
# VALUE is the exact value to match.
#
# Examples:
#   ./list-tools-by-facet.sh tt_Form "Matrix"
#   ./list-tools-by-facet.sh tt_Clarifies "Destination"
#   ./list-tools-by-facet.sh tt_SOLVE_eX_Phase "5"
#
# Exit codes:
#   0 = matches found
#   1 = no matches
#   2 = usage error
#   3 = corpus not locatable
#
# This script is a thin wrapper for quick CLI scanning. For complex
# multi-facet queries, use find-tools.py instead.

set -eu

usage() {
    sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'
}

find_root() {
    dir="$(cd "$(dirname "$0")" && pwd)"
    i=0
    while [ "$i" -lt 20 ]; do
        if [ -f "$dir/AI-BOOTSTRAP.md" ]; then
            printf '%s\n' "$dir"
            return 0
        fi
        parent="$(dirname "$dir")"
        if [ "$parent" = "$dir" ]; then
            return 1
        fi
        dir="$parent"
        i=$((i + 1))
    done
    return 1
}

# Parse args
if [ $# -eq 0 ]; then
    usage >&2
    exit 2
fi

case "$1" in
    --help|-h)
        usage
        exit 0
        ;;
esac

if [ $# -lt 2 ]; then
    echo "ERROR: usage: $0 FACET VALUE" >&2
    exit 2
fi

FACET="$1"
VALUE="$2"

ROOT="$(find_root)" || { echo "ERROR: SOLVE eX root not found" >&2; exit 3; }
TOOLS_DIR="$ROOT/01-Tools/Tool Entries"

if [ ! -d "$TOOLS_DIR" ]; then
    echo "ERROR: tool entries directory missing: $TOOLS_DIR" >&2
    exit 3
fi

# Match either of:
#   <FACET>: <VALUE>           (inline scalar)
#   <FACET>: "<VALUE>"
#   <FACET>: '<VALUE>'
#   <FACET>:                   (list form)
#     - <VALUE>
#     - "<VALUE>"
# Tool-entry corpus uses the list form for most multi-value facets
# (tt_Form, tt_Operation, tt_Clarifies, etc.). We use awk to track which
# YAML key is currently being read, so list items are scoped to the right
# parent key.

COUNT=0
for FILE in "$TOOLS_DIR"/*.md; do
    [ -f "$FILE" ] || continue
    if awk -v facet="$FACET" -v value="$VALUE" '
        BEGIN { in_fm = 0; current_key = ""; found = 0 }
        /^---$/ {
            if (in_fm == 0) { in_fm = 1; next }
            else { exit }
        }
        in_fm == 0 { next }

        # Match an inline scalar: KEY: VALUE
        match($0, "^" facet ":[ \t]*[\"'\''`]?" value "[\"'\''`]?[ \t]*$") {
            found = 1; exit
        }

        # Track current top-level key (lines that start with `<key>:` at column 0)
        /^[A-Za-z_][A-Za-z0-9_]*:/ {
            split($0, parts, ":")
            current_key = parts[1]
            next
        }

        # Match list-item form when scoped to the right parent key
        current_key == facet && match($0, "^[ \t]*-[ \t]+[\"'\''`]?" value "[\"'\''`]?[ \t]*$") {
            found = 1; exit
        }

        END { exit (found == 1 ? 0 : 1) }
    ' "$FILE" 2>/dev/null; then
        BASENAME="${FILE##*/}"
        echo "${BASENAME%.md}"
        COUNT=$((COUNT + 1))
    fi
done

if [ "$COUNT" -eq 0 ]; then
    echo "No tools matched ${FACET}=${VALUE}" >&2
    exit 1
fi

echo "" >&2
echo "Total: $COUNT tool(s)" >&2
exit 0
