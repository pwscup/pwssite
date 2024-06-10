dir=$(dirname $0)

## 更新がありそうなディレクトリを, 
## ${dir}/***/scripts/make.bash として指定する
bash ${dir}/2023/scripts/make.bash
bash ${dir}/2024/scripts/make.bash
bash ${dir}/ppsd/scripts/make.bash
