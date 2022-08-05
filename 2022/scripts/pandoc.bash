
## このファイルが置かれたフォルダ
dir=$(dirname $0)

## ファイル名を引数にする
basefilename=$1

## 一時ファイル用に、プロセス番号を使う
PID=$$

## ***.md -> ***.htmlを生成する

pandoc -f markdown-auto_identifiers -t html ${dir}/../markdown/${basefilename}.md > ${dir}/${PID}.${basefilename}.html

## headとtailの間に、***.mdをhtmlに変換したものを追加する処理

## ヘッダの挿入
### _eで終わるファイルのヘッダは英語版に
if test ${basefilename: -2} = '_e'; then
  if test ${basefilename:0:3} = 'cup'; then
    ## cup_e用のヘッダ
    cat $dir/../template/header_cup_e.html > $dir/../html/${basefilename}.html
  else
    ## PWS_e用のヘッダ
    cat $dir/../template/header_e.html > $dir/../html/${basefilename}.html
  fi
else
  if test ${basefilename:0:3} = 'cup'; then
    ## cup用のヘッダ
    cat $dir/../template/header_cup.html > $dir/../html/${basefilename}.html
  else
    ## PWS用のヘッダ
    cat $dir/../template/header.html > $dir/../html/${basefilename}.html
  fi
fi

## コンテンツの挿入
echo "<!-- contents start -->" >> $dir/../html/${basefilename}.html

cat $dir/${PID}.${basefilename}.html >> $dir/../html/${basefilename}.html

echo "" >> $dir/../html/${basefilename}.html

echo "<!-- contents end -->" >> $dir/../html/${basefilename}.html

## フッターの挿入
cat $dir/../template/footer.html >> $dir/../html/${basefilename}.html

## tmpファイルの削除
rm $dir/${PID}.*



