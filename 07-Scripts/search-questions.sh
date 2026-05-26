#!/bin/sh
# search-questions.sh — search the question bank corpus.
#
# Usage:
#   ./search-questions.sh QUERY [--bank by-phase-step|by-clarification-need|by-emotional-state|meta-questions]
#                              [--state grief|overwhelm|fear|anger|shame|paralysis|elation|numbness]
#                              [--limit N]
#                              [--help]
#
# Examples:
#   ./search-questions.sh "stuck"
#   ./search-questions.sh "permission" --bank meta-questions
#   ./search-questions.sh "carry" --state grief --limit 5
#
# Exit codes:
#   0 = matches found
#   1 = no matches
#   2 = usage error
#   3 = corpus not locatable

set -eu

usage() {
    sed -n '2,15p' "$0" | sed 's/^# \{0,1\}//'
}

# Locate corpus root by walking up from script location until AI-BOOTSTRAP.md is found.
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
QUERY=""
BANK=""
STATE=""
LIMIT=""

while [ $# -gt 0 ]; do
    case "$1" in
        --help|-h)
            usage
            exit 0
            ;;
        --bank)
            shift
            [ $# -gt 0 ] || { echo "ERROR: --bank requires a value" >&2; exit 2; }
            BANK="$1"
            ;;
        --state)
            shift
            [ $# -gt 0 ] || { echo "ERROR: --state requires a value" >&2; exit 2; }
            STATE="$1"
            ;;
        --limit)
            shift
            [ $# -gt 0 ] || { echo "ERROR: --limit requires a value" >&2; exit 2; }
            LIMIT="$1"
            ;;
        --)
            shift
            ;;
        -*)
            echo "ERROR: unknown option '$1'" >&2
            exit 2
            ;;
        *)
            if [ -z "$QUERY" ]; then
                QUERY="$1"
            else
                echo "ERROR: unexpected positional argument '$1'" >&2
                exit 2
            fi
            ;;
    esac
    shift
done

if [ -z "$QUERY" ]; then
    echo "ERROR: missing required query argument" >&2
    usage >&2
    exit 2
fi

ROOT="$(find_root)" || { echo "ERROR: SOLVE eX root not found" >&2; exit 3; }
QB_DIR="$ROOT/03-Question-Banks"

if [ ! -d "$QB_DIR" ]; then
    echo "ERROR: question bank directory missing: $QB_DIR" >&2
    exit 3
fi

# Determine search scope
SEARCH_PATH="$QB_DIR"
if [ -n "$STATE" ]; then
    SEARCH_PATH="$QB_DIR/by-emotional-state/${STATE}.md"
    if [ ! -f "$SEARCH_PATH" ]; then
        echo "ERROR: state file not found: $SEARCH_PATH" >&2
        exit 3
    fi
elif [ -n "$BANK" ]; then
    SEARCH_PATH="$QB_DIR/$BANK"
    if [ ! -d "$SEARCH_PATH" ] && [ ! -f "${SEARCH_PATH}.md" ]; then
        echo "ERROR: bank not found: $SEARCH_PATH" >&2
        exit 3
    fi
fi

# Run grep — line-numbered, case-insensitive, recursive, with filename
# Only match lines starting with '- ' (question lines, per bank convention)
if [ -d "$SEARCH_PATH" ]; then
    RESULTS="$(grep -rn -i -E "^- .*${QUERY}" "$SEARCH_PATH" 2>/dev/null || true)"
else
    RESULTS="$(grep -n -i -E "^- .*${QUERY}" "$SEARCH_PATH" 2>/dev/null || true)"
fi

if [ -z "$RESULTS" ]; then
    echo "No matches for '$QUERY' in ${SEARCH_PATH#$ROOT/}"
    exit 1
fi

# Apply limit if set
if [ -n "$LIMIT" ]; then
    echo "$RESULTS" | head -n "$LIMIT"
else
    echo "$RESULTS"
fi

exit 0
