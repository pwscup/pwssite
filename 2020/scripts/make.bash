dir=$(dirname $0)


## markdownの更新/新規作成があれば, pandocする
ls $dir/../markdown/*.md | while read line
do
  echo "line: "$line
  basefilename=$(echo $line | xargs basename | sed "s/.md$//")
  echo "basefilename: "$basefilename

  if [ "$line" -nt "$dir/../html/${basefilename}.html" ]; then
    echo "新規作成/更新ある"
    bash $dir/pandoc.bash $basefilename
  fi
done

