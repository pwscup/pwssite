dir=$(dirname $0)

## 更新がありそうなディレクトリを, 
## ${dir}/***/scripts/make.bash として指定する
bash ${dir}/2025/scripts/make.bash
python3 ${dir}/2026/scripts/make.py
bash ${dir}/ppsd/scripts/make.bash
