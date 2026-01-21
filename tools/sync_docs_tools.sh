#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
src="${repo_root}/tools/index.html"
dest_dir="${repo_root}/docs/tools"
dest="${dest_dir}/index.html"

mkdir -p "${dest_dir}"
cp "${src}" "${dest}"

echo "Synced ${src} -> ${dest}"
