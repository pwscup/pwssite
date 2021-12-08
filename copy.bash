## 新年度ディレクトリ作成用スクリプト
dir=$(dirname $0)

## 年度を入力
input=$1


## 数字かどうかチェック
if expr "$input" : "[0-9]*$" >&/dev/null;then
  echo "" >& /dev/null else
else 
  echo "$input is not a number. Please input number"
  exit 1
fi

## 存在チェック
if [ -e ${dir}/${input} ]; then
  echo "$input directory already exists."
  exit 1
fi


## ディレクトリ構造のコピー
rsync -avz --include "*/" --exclude "*" ${dir}/2020/ ${dir}/${input}/

## 共通ファイルのコピー
cp ${dir}/2020/style.css ${dir}/${input}/
cp ${dir}/2020/template/* ${dir}/${input}/template/
cp ${dir}/2020/scripts/* ${dir}/${input}/scripts/
cp ${dir}/2020/markdown/index.md ${dir}/${input}/markdown/

## make.bashに新年度分を追加
## echo "bash ${dir}/${input}/scripts/make.bash" >> ${dir}/make.bash
## TODO: ${dir}は展開せずに、${input}は展開して、make.bashに追記したい

## ビルド
echo " -- test -- "
bash ${dir}/make.bash
