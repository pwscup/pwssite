
dir=$(dirname $0)

## mdファイルを引数にする
filename=$1

if [ $filename = "" ]; then
  echo "input filename"
  exit 0
fi

## .mdファイルのパスでなかったら、中断する
echo ${filename} | grep -E ".md$"

if [ $? = 0 ]; then
  echo " md file OK"
else
  echo "please input .md filepath"
  exit 0
fi

## .mdを削除する
basefilename=$(echo $filename | sed "s/.md$//")

PID=$$

# ***.md -> ***.htmlを生成する

pandoc -f markdown -t html ${dir}/../markdown/${filename} > ${dir}/${PID}.${basefilename}.html

# headとtailの間に、***.mdをhtmlに変換したものを追加する

cat $dir/../template/header.html > $dir/../${basefilename}.html
echo "<!-- contents start -->" >> $dir/../${basefilename}.html
cat $dir/${PID}.${basefilename}.html >> $dir/../${basefilename}.html
echo "<!-- contents end -->" >> $dir/../${basefilename}.html
cat $dir/../template/tail.html >> $dir/../${basefilename}.html

rm $dir/${PID}.*



