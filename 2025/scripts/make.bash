#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
md_dir="${script_dir}/../markdown"
html_dir="${script_dir}/../html"
public_dir="${script_dir}/.."

# 1) pull 前のコミット ID を退避
before="$(git -C "$md_dir" rev-parse HEAD)"

# 2) git pull（fast‑forward だけにしたい場合は --ff-only を付ける）
git -C "$md_dir" pull --ff-only

# 3) pull 後のコミット ID
after="$(git -C "$md_dir" rev-parse HEAD)"

# 4) 差分に含まれる Markdown を取得
mapfile -t changed_md < <(
  git -C "$md_dir" diff --name-only "${before}" "${after}" -- '*.md'
)

if [[ ${#changed_md[@]} -eq 0 ]]; then
  echo "No markdown files changed by the latest pull."
  exit 0
fi

echo "Changed markdown files:"
printf '  %s\n' "${changed_md[@]}"
echo "----------------------------------------"

# 5) 差分ファイルだけビルド
for rel in "${changed_md[@]}"; do
  md="${md_dir}/${rel}"
  base="$(basename "${md%.md}")"
  html="${html_dir}/${base}.html"

  echo "[BUILD] ${base}.md → ${base}.html"
  "${script_dir}/pandoc.bash" "$base"
  tidy -quiet -indent -utf8 -m "$html"
  chmod 660 "$html"
  cp -p "$html" "${public_dir}/${base}.html"
done

# 6) 画像の差分コピー（Markdown 側で Images/ 配下を使っている想定）
rsync -rt --delete \
      --chmod=Du=rwx,Dg=rwx,Fu=rw,Fg=rw \
      "${md_dir}/Images/" "${html_dir}/Images/"

echo "Done."

