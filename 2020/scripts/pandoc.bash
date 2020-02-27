
dir=$(dirname $0)

## mdファイルを引数にする
basefilename=$1

PID=$$

## ***.md -> ***.htmlを生成する

pandoc -f markdown -t html ${dir}/../markdown/${basefilename}.md > ${dir}/${PID}.${basefilename}.html

## headとtailの間に、***.mdをhtmlに変換したものを追加する

cat $dir/../template/header.html > $dir/../html/${basefilename}.html

echo "<!-- contents start -->" >> $dir/../html/${basefilename}.html

cat $dir/${PID}.${basefilename}.html >> $dir/../html/${basefilename}.html

echo "" >> $dir/../html/${basefilename}.html

echo "<!-- contents end -->" >> $dir/../html/${basefilename}.html

cat $dir/../template/footer.html >> $dir/../html/${basefilename}.html

rm $dir/${PID}.*



