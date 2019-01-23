# Transact-SQL 用python解析器

# 動作環境
python3

# インストール
```bash
$ python -c "import site; print(site.getsitepackages()[0])"
-> C:\python3\Lib\site-packages

$ cd C:\python3\Lib\site-packages
$ git clone https://github.com/kirin123kirin/pytsql.git
```

# 使い方
## 例１：使用しているカラムリストを取得する
```Python
import pytsql
from pprint import pprint

sql = "select a,b from c;"
parser = pytsql.parse(sql)

pprint(parser.column_elem)

Out[1]: ['A', 'B']
```

## 例２：SQL構造を全部抜き出す
```Python
pprint(parser.tolist())

Out[1]: ['query_specification',
 'SELECT',
 ['select_list',
  ['select_list_elem', ['column_elem', 'A']],
  ['select_list_elem', ['column_elem', 'B']]],
 'FROM',
 ['table_sources',
  ['table_source',
   ['table_source_item_joined',
    ['table_source_item', ['table_name_with_hint', ['table_name', 'C']]]]]]]
```

## 例３：コンテキストを抜き出す
```Python
pprint(parser.lookup())

Out[1]: {'column_elem': ['A', 'B'], 'keywords': ['SELECT', 'FROM'], 'table_name': ['C']}
```

## 例４：自分でパーサを定義する
```Python
import pytsql

class Render(pytsql.ParserListener):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.context = []
        
    def enterColumn_elem(self, ctx):
        self.context.append(ctx.getText())


sql = """
insert into testdata (
SELECT a,b f
 from A as hoge 
 left join (select * from foo) as bar
 on hoge.a = bar.b 
 where a=1 and b is not null;
 )
"""

ret = pytsql.parse(sql, callback=Render)

ret.context
Out[1]: ['A', 'BF']

```

## おまけ Formatting
```Python
import pytsql

print(pytsql.parse("select a,v from A where a is not NULL;").format())

Out[1]:
SELECT a
     , v
FROM A
WHERE a IS NOT NULL;


```
## メモ
pytsql.ParserListenerはGrammarビルドで出来上がった「TSqlParserListener」をオーバライドした自作クラス
いろいろぶち込んでしまった。
ので本家のListenerと比べ__init__の引数が増えてしまった。

大元から自作したい時は
本家の[ReadMe](https://github.com/antlr/antlr4/blob/master/doc/python-target.md#how-do-i-create-and-run-a-custom-listener)参照しながら実装してほしい。

```Python
import pytsql

class KeyPrinter(pytsql.TSqlParserListener):
    def __init__(self):
        self.context = []
        
    def enterColumn_elem(self, ctx):
        self.context.append(ctx.getText())

tree = parser.startRule()
printer = KeyPrinter()
walker = pytsql.ParseTreeWalker()
walker.walk(printer, tree)

```

# 他文法に応用できるので今回pytsqlのビルド手順を備忘
## ビルド環境
|環境|バージョン等|
|:-|:-|
|OS|windows7 64bit|
|python version|3.6.5|
|jre|Java(TM) SE Runtime Environment (build 1.8.0_171-b11)|

## pythonパーサビルドで必要な環境
* antlr-4.7.2-complete.jarをダウンロードする（一回作ってしまえば必要ない）
* antlr4-python3-runtimeをインストールする

```bash
pip install antlr4-python3-runtime
```

## antlr4によるTsqlpythonパーサビルド手順
他文法応用には[antlr/grammars-v4](https://github.com/antlr/grammars-v4)から使えばいろいろ応用可能

```Shell
# ビルドディレクトリ作成
mkdir $TEMP/pytsql
cd $TEMP/pytsql

# antlr4 ダウンロード
wget https://www.antlr.org/download/antlr-4.7.2-complete.jar

# T-SQL 文法データダウンロード
wget https://raw.githubusercontent.com/antlr/grammars-v4/master/tsql/TSqlLexer.g4
wget https://raw.githubusercontent.com/antlr/grammars-v4/master/tsql/TSqlParser.g4

# runtimeインストール
pip install antlr4-python3-runtime

# Grammerビルド
java -Xmx500M -cp antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 TSqlLexer.g4
java -Xmx500M -cp antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 TSqlParser.g4

# 出来上がったparserファイル達をsite-packages下に持ってく
mklib=`python -c "import site; print(site.getsitepackages()[0])"`
mkdir $mklib/pytsql
mv TSql*.py $mklib/pytsql
touch $mklib/pytsql/__init__.py
```

Thanks: https://qiita.com/osamunmun/items/54a00e963d1a7db0cf59

Powerd by [ANTLR](http://www.antlr.org/index.html)
