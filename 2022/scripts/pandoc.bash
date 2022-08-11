
# 定数
## デフォルトの title 要素
readonly DEFAULT_TITLE="PWS"

## このファイルが置かれたフォルダ
readonly DIR=$(dirname $0)

## ファイル名を引数にする
readonly BASE_FILENAME=$1

## 一時ファイル用に、プロセス番号を使う
readonly PID=$$

## 出力先htmlファイル
readonly OUTPUT=${DIR}/../html/${BASE_FILENAME}.html

## Headers
### 日本語版
readonly HEADER1="${DIR}/../template/header.html"
readonly HEADER2="${DIR}/../template/header_afterTitle.html"
### 英語版
readonly HEADER1_E="${DIR}/../template/header_e.html"
readonly HEADER2_E="${DIR}/../template/header_afterTitle_e.html"

## コンテンツ
### htmlファイル生成元のMarkdownファイル
readonly CONTENTS_MD=${DIR}/../markdown/${BASE_FILENAME}.md
### htmlファイルの生成先
readonly CONTENTS_HTML=${DIR}/${PID}.${BASE_FILENAME}.html

## Footer
readonly FOOTER=${DIR}/../template/footer.html

# 関数
## .mdファイルの最初の "# ..." 行からtitle要素を作成
function create_title() {
  ### title文字列の抽出
  local title=$( grep -e '^# ' ${CONTENTS_MD} | head -n1 | sed -e 's;^# \(.*\)$;\1;g' )
  ### 抽出失敗時はデフォルト値を代入
  test -z "${title}" && title="${DEFAULT_TITLE}"
  ### titleタグで挟んで返す。
  echo "    <title>${title}</title>"
}



########## MAIN ##########
# ***.md -> ***.htmlを生成する
pandoc -f markdown-auto_identifiers -t html ${CONTENTS_MD} > ${CONTENTS_HTML}

# headとtailの間に、***.mdをhtmlに変換したものを追加する処理
## ヘッダの挿入
if test ${BASE_FILENAME: -2} = '_e'; then
  ### 英語版
  cat ${HEADER1_E}  > ${OUTPUT}
  create_title     >> ${OUTPUT}
  cat ${HEADER2_E} >> ${OUTPUT}
else
  ### 日本語版
  cat ${HEADER1}    > ${OUTPUT}
  create_title     >> ${OUTPUT}
  cat ${HEADER2}   >> ${OUTPUT}
fi

# コンテンツの挿入
echo "<!-- contents start -->" >> ${OUTPUT}

cat ${CONTENTS_HTML}           >> ${OUTPUT}

echo ""                        >> ${OUTPUT}

echo "<!-- contents end -->"   >> ${OUTPUT}

# フッターの挿入
cat ${FOOTER}                  >> ${OUTPUT}

# tmpファイルの削除
rm ${DIR}/${PID}.*

