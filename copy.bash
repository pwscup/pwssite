## 新年度ディレクトリ作成用スクリプト
dir=$(dirname $0)

## 年度を入力
input=$1


## 入力が数字かどうかチェック
if expr "$input" : "[0-9]*$" >&/dev/null;then
  echo "" >& /dev/null else
else 
  echo "$input is not a number. Please input number"
  exit 1
fi

## 入力年度フォルダの存在チェック
if [ -e ${dir}/${input} ]; then
  echo "$input directory already exists."
  exit 1
fi


## ディレクトリ構造をコピー
rsync -avz --include "*/" --exclude "*" ${dir}/2022/ ${dir}/${input}/

## 共通ファイルのコピー+作成
cp ${dir}/2022/style.css ${dir}/${input}/
cp ${dir}/2022/template/* ${dir}/${input}/template/
cp ${dir}/2022/scripts/* ${dir}/${input}/scripts/
cp ${dir}/2022/markdown/index.md ${dir}/${input}/markdown/

## make.bashに新年度分を追加
## echo "bash ${dir}/${input}/scripts/make.bash" >> ${dir}/make.bash
## TODO: ${dir}は展開せずに、${input}は展開して、make.bashに追記したい

## TODO: template/headerを最新化して、cup${input}.htmlを参照するようにする
## TODO: PWS****.htmlと、cup**.htmlへのリンクを最新化する

## htmlの生成処理.bashが上手く動くどうかのテスト
echo " -- test -- "
bash ${dir}/make.bash
