dir=$(dirname $0)


## templateファイルが更新されていたら、全てのmarkdownファイルをtouchする、という処理 
ls $dir/../template/*.html | while read line
do
  echo "line: "$line
  ## 拡張子なしファイル名の取得
  basefilename=$(echo $line | xargs basename | sed "s/.md$//")
  echo "basefilename: "$basefilename
  
  ## 更新か新規作成があれば、処理する
  if [ "$line" -nt "$dir/../html/${basefilename}.html" ]; then
    echo "created or updated"
    ## md -> html変換
    bash $dir/pandoc.bash $basefilename
    ## htmlファイルのインデントを整形する
    tidy -i -utf8 $dir/../html/${basefilename}.html > $dir/../html/${basefilename}.tmp.html
    
    ## ファイルをhtml配置用のフォルダに配置する
    mv $dir/../html/${basefilename}.tmp.html $dir/../html/${basefilename}.html
    
    ## 権限を制御する
    chmod 770 $dir/../html/*.html
    chmod 770 $dir/../Images

    ## 公開する
    cp $dir/../html/${basefilename}.html $dir/../${basefilename}.html
  else
    echo "up to date"
  fi
  echo "========================"
done


## markdownの更新/新規作成があれば, pandocで md -> html変換する、という処理
ls $dir/../markdown/*.md | while read line
do
  echo "line: "$line
  ## 拡張子なしファイル名の取得
  basefilename=$(echo $line | xargs basename | sed "s/.md$//")
  echo "basefilename: "$basefilename
  
  ## 更新か新規作成があれば、処理する
  if [ "$line" -nt "$dir/../html/${basefilename}.html" ]; then
    echo "created or updated"
    ## md -> html変換
    bash $dir/pandoc.bash $basefilename
    ## htmlファイルのインデントを整形する
    tidy -i -utf8 $dir/../html/${basefilename}.html > $dir/../html/${basefilename}.tmp.html
    
    ## ファイルをhtml配置用のフォルダに配置する
    mv $dir/../html/${basefilename}.tmp.html $dir/../html/${basefilename}.html
    
    ## 権限を制御する
    chmod 770 $dir/../html/*.html
    chmod 770 $dir/../Images

    ## 公開する
    cp $dir/../html/${basefilename}.html $dir/../${basefilename}.html
  else
    echo "up to date"
  fi
  echo "========================"
done

## 図のコピー
cp -r $dir/../markdown/Images $dir/../

