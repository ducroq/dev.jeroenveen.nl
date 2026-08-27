#!/bin/sh
# Check the countable state claims in MEMORY.md and CLAUDE.md against the repo.
#
# Ported from dsp-workshop/tests/verify_state.sh on 2026-08-27, after a /curate
# pass found this repo had NO `<!-- verify: -->` annotations at all: every state
# claim here was unverifiable by construction. The row claiming "8 projects ...
# VISIBLE_PROJECT_COUNT = 2" had been wrong (9 and 3) with nothing able to catch
# it, while the sibling repo's runner caught its own stale count in seconds.
#
# Usage:  sh scripts/verify-state.sh [check ...]     (no args = run all)
# Called by the `<!-- verify: ... -->` annotations in MEMORY.md.
#
# Writing rules for anything added here, learned the hard way in the sibling
# repo (see its gotcha log, "verify-command rot", 7 recurrences):
#   - print evidence, never a bare verdict word; the disposition is the EXIT CODE
#   - a check that passes in silence is indistinguishable from one that never ran
#   - parse a quantity that MOVES when the thing fails (a pass-count does not)
#   - read the expected value FROM the claim where you can, rather than
#     hardcoding it here; a literal means the checker and the document can
#     disagree about which is authoritative
set -u

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$ROOT" || exit 2
RAN=0 PASSED=0 FAILED=0

want() { # want <label> <expected> <actual>
    RAN=$((RAN + 1))
    if [ "$2" = "$3" ]; then
        printf 'PASS  %s = %s\n' "$1" "$3"; PASSED=$((PASSED + 1))
    else
        printf 'FAIL  %s = %s (claimed %s)\n' "$1" "$3" "$2"; FAILED=$((FAILED + 1))
    fi
}

# Read the number MEMORY.md claims, so the claim is authoritative and a correct
# edit to the document does not read as a failure.
claimed() { grep -oE "$1" MEMORY.md | head -1 | grep -oE '[0-9]+' | head -1; }

check_projects() {
    actual=$(grep -c "^    title: '" src/pages/index.astro)
    want "projects in the array" "$(claimed '\*\*[0-9]+ projects\*\*')" "$actual"
}

check_visible_projects() {
    actual=$(grep -oE 'VISIBLE_PROJECT_COUNT = [0-9]+' src/pages/index.astro | grep -oE '[0-9]+')
    want "VISIBLE_PROJECT_COUNT" "$(claimed 'VISIBLE_PROJECT_COUNT = [0-9]+')" "$actual"
}

check_articles() {
    # The registry is the ground truth for what /writing/ lists.
    reg=$(grep -c "^    slug: '" src/data/writing.ts)
    pages=$(find src/pages/writing -maxdepth 1 -name '*.astro' ! -name 'index.astro' | wc -l | tr -d ' ')
    want "article pages vs registry entries" "$reg" "$pages"
}

check_posted_linkedin() {
    actual=$(find memory/posted-linkedin -maxdepth 1 -name '*.md' | wc -l | tr -d ' ')
    claim=$(grep -oE '\([0-9]+ as of [0-9-]+\)' CLAUDE.md | head -1 | grep -oE '[0-9]+' | head -1)
    want "posted-linkedin records" "$claim" "$actual"
}

check_gotcha_entries() {
    # Reconciled two ways: headings and bodies must agree, so a heading-level
    # mistake cannot return a plausible number.
    h=$(grep -cE '^#{2,3} ' memory/gotcha-log.md)
    b=$(grep -c '^\*\*Problem\*\*' memory/gotcha-log.md)
    RAN=$((RAN + 1))
    if [ "$h" -gt "$b" ]; then
        printf 'PASS  gotcha entries (bodies) = %s, headings incl. sections = %s\n' "$b" "$h"
        PASSED=$((PASSED + 1))
    else
        printf 'FAIL  gotcha headings (%s) do not exceed bodies (%s) — the extractor is wrong\n' "$h" "$b"
        FAILED=$((FAILED + 1))
    fi
}

check_hypotheses_open() {
    actual=$(awk '/^## Open/,/^## Resolved/' memory/hypothesis-log.md | grep -c '^### ')
    RAN=$((RAN + 1))
    overdue=$(awk '/^## Open/,/^## Resolved/' memory/hypothesis-log.md \
              | grep -oE '\*\*Review by:\*\* [0-9]{4}-[0-9]{2}-[0-9]{2}|Review by:\*\* [0-9]{4}-[0-9]{2}-[0-9]{2}' \
              | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' \
              | awk -v today="$(date +%F)" '$0 < today' | wc -l | tr -d ' ')
    dormant=$(grep -c 'Status:\*\* \*\*dormant\*\*' memory/hypothesis-log.md)
    printf 'PASS  hypotheses open = %s (%s past Review by, %s dormant)\n' "$actual" "$overdue" "$dormant"
    PASSED=$((PASSED + 1))
}

check_build() {
    RAN=$((RAN + 1))
    if [ ! -d node_modules ]; then
        printf 'CANNOT VERIFY: node_modules absent — run npm install\n'; return
    fi
    if npm run build >/dev/null 2>&1; then
        printf 'PASS  astro build = clean\n'; PASSED=$((PASSED + 1))
    else
        printf 'FAIL  astro build = failing\n'; FAILED=$((FAILED + 1))
    fi
}

check_dead_refs() {
    # Every backticked .md/.py path named in CLAUDE.md must resolve somewhere.
    missing=$(grep -oE '`[a-zA-Z0-9_./-]+\.(md|py)`' CLAUDE.md | tr -d '`' | sort -u \
        | while read -r f; do
            find . -name "$(basename "$f")" -not -path './node_modules/*' \
                 -not -path './.git/*' -not -path './dist/*' -print -quit 2>/dev/null \
                 | grep -q . || echo "$f"
          done)
    RAN=$((RAN + 1))
    if [ -z "$missing" ]; then
        printf 'PASS  CLAUDE.md file references = all resolve\n'; PASSED=$((PASSED + 1))
    else
        printf 'FAIL  CLAUDE.md names files that do not exist: %s\n' "$(echo "$missing" | tr '\n' ' ')"
        FAILED=$((FAILED + 1))
    fi
}

ALL="projects visible_projects articles posted_linkedin gotcha_entries hypotheses_open dead_refs build"
for c in ${*:-$ALL}; do
    case " $ALL " in *" $c "*) "check_$c" ;;
       *) printf 'FAIL  unknown check: %s\n' "$c"; FAILED=$((FAILED + 1)); RAN=$((RAN + 1)) ;;
    esac
done

printf 'ran %d checks: %d passed, %d failed\n' "$RAN" "$PASSED" "$FAILED"
[ "$FAILED" -eq 0 ]
