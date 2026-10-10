#!/bin/bash
set -uo pipefail

if [[ "$#" -ne 3 ]]; then
  echo "Usage: $0 <matrix.xlsx> <MATRIX_SCOPE_ALIAS> <phase 0..13>" >&2
  exit 2
fi

MATRIX="$1"
NICHE="$2"
PHASE="$3"

REPO="${REPO:-$HOME/Desktop/smart-imports}"
ENGINE_DIR="${ENGINE_DIR:-$HOME/Desktop/smart-imports-engine}"
PREFLIGHT="${PREFLIGHT:-$REPO/scripts/validate-method-v2-data-fidelity.py}"

fail() { echo "ERROR: $*" >&2; exit 2; }

[[ -f "$MATRIX" ]] || fail "No encuentro matrix: $MATRIX"
[[ -f "$PREFLIGHT" ]] || fail "No encuentro preflight: $PREFLIGHT"
[[ -d "$ENGINE_DIR" ]] || fail "No encuentro Engine: $ENGINE_DIR"
[[ "$PHASE" =~ ^([0-9]|1[0-3])$ ]] || fail "Phase debe ser 0..13"

echo "============================================================"
echo "METHOD V2 CHECKPOINT"
echo "============================================================"
echo "Matrix: $MATRIX"
echo "Scope:  $NICHE"
echo "Phase:  F$PHASE"
echo

echo "1/2 — Data Fidelity Preflight"
set +e
python3 "$PREFLIGHT" "$MATRIX" --niche "$NICHE" --phase "$PHASE"
fidelity_status=$?
set -e

if [[ "$fidelity_status" -ne 0 ]]; then
  echo
  echo "CHECKPOINT: FAIL — DATA FIDELITY"
  echo "Matrix Validator no se ejecuta."
  exit "$fidelity_status"
fi

echo
echo "2/2 — Matrix Validator"
cd "$ENGINE_DIR"
if ! pnpm build; then
  echo
  echo "CHECKPOINT: FAIL — ENGINE BUILD"
  exit 2
fi

set +e
node --enable-source-maps dist/cli.js validate   "$MATRIX"   --schema full-matrix-v5   --format json
validator_status=$?
set -e

echo
if [[ "$validator_status" -eq 0 ]]; then
  echo "CHECKPOINT: PASS — DATA FIDELITY + MATRIX VALIDATOR"
else
  echo "CHECKPOINT: FAIL — MATRIX VALIDATOR"
fi

exit "$validator_status"
