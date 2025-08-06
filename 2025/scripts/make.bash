#!/usr/bin/env bash
set -euo pipefail

# ディレクトリ定義
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
md_dir="${script_dir}/../markdown"
html_dir="${script_dir}/../html"
# 公開ルートは markdown の親（scripts 位置に依存しない）
public_dir="$(cd "$md_dir/.." && pwd)"

mkdir -p "$html_dir"

# markdown 配下の .md を収集（再帰）
rel_md_list=()
while IFS= read -r -d '' rel; do
  rel="${rel#./}"           # 先頭の ./ を除去
  rel_md_list+=("$rel")
done < <(cd "$md_dir" && find . -type f -name '*.md' -print0)

# 更新が必要なターゲットを抽出（html が無い or md が新しい）
targets=()
for rel in "${rel_md_list[@]}"; do
  base="$(basename "${rel%.md}")"
  md="$md_dir/$rel"
  html="$html_dir/${base}.html"
  if [[ ! -e "$html" || "$md" -nt "$html" ]]; then
    targets+=("$base")
  fi
done

if [[ ${#targets[@]} -eq 0 ]]; then
  echo "No markdown newer than existing HTML."
  exit 0
fi

echo "Build targets:"
for base in "${targets[@]}"; do
  echo "  ${base}.md"
done
echo "----------------------------------------"

# ビルド → 整形（tidyのエラーは無視）→ 権限 → 公開ルートへコピー
for base in "${targets[@]}"; do
  md="${md_dir}/${base}.md"
  html="${html_dir}/${base}.html"

  echo "[BUILD] ${base}.md → ${base}.html"
  "${script_dir}/pandoc.bash" "$base"

  # ① tidy が警告で非0終了しても続行する
  if ! tidy -quiet -indent -utf8 -m "$html"; then
    echo "[WARN] tidy reported issues; continuing"
  fi

  chmod 660 "$html"

  # 配置先を明示出力（配置階層の確認用）
  echo "[COPY] ${html} -> ${public_dir}/${base}.html"
  cp -p "$html" "${public_dir}/${base}.html"
done

# 画像の同期（存在する場合のみ）
if [[ -d "${md_dir}/Images" ]]; then
  rsync -rt --delete \
        --chmod=Du=rwx,Dg=rwx,Fu=rw,Fg=rw \
        "${md_dir}/Images/" "${html_dir}/Images/"
fi

echo "Done."

