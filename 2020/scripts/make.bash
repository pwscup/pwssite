dir=$(dirname $0)


## markdownの更新/新規作成があれば, pandocする
ls $dir/../markdown/*.md | while read line
do
  echo "line: "$line
  basefilename=$(echo $line | xargs basename | sed "s/.md$//")
  echo "basefilename: "$basefilename

  if [ "$line" -nt "$dir/../html/${basefilename}.html" ]; then
    echo "created or updated"
    bash $dir/pandoc.bash $basefilename
    tidy -i -utf8 $dir/../html/${basefilename}.html > $dir/../html/${basefilename}.tmp.html

    ## mv $dir/../html/${basefilename}.tmp.html $dir/../html/${basefilename}.html
    mv $dir/../html/${basefilename}.tmp.html $dir/../html/${basefilename}.html

    ## 公開する
    cp $dir/../html/${basefilename}.html $dir/../${basefilename}.html
  fi
done

