
dir=$(dirname $0)

## mdファイルを引数にする
basefilename=$1

PID=$$

## ***.md -> ***.htmlを生成する

pandoc -f markdown-auto_identifiers -t html ${dir}/../markdown/${basefilename}.md > ${dir}/${PID}.${basefilename}.html

## headとtailの間に、***.mdをhtmlに変換したものを追加する

## _eで終わるファイルのヘッダは英語版に
if test ${basefilename: -2} = '_e'; then
  cat $dir/../template/header_e.html > $dir/../html/${basefilename}.html
else
  cat $dir/../template/header.html > $dir/../html/${basefilename}.html
fi

echo "<!-- contents start -->" >> $dir/../html/${basefilename}.html

cat $dir/${PID}.${basefilename}.html >> $dir/../html/${basefilename}.html

echo "" >> $dir/../html/${basefilename}.html

echo "<!-- contents end -->" >> $dir/../html/${basefilename}.html

cat $dir/../template/footer.html >> $dir/../html/${basefilename}.html

rm $dir/${PID}.*



