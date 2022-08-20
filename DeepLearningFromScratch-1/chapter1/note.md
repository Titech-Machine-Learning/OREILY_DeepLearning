# Python 入門

## 1.3 Python インタプリタ

```shell
python --version
```

で Python のバージョンを確認できます。
macOS の場合は、通常 intel chip では python2.x が M1 chip では python3.x がデフォルトでインストールされていますが、これは System 用(macOS 側が利用する)なのでこの Python バージョンを変更することは推奨されていません。`sudo`コマンドを用いると system 用の python バージョンを変更できますが、これは行うべきではありません。

最も簡単な方法は homebrew を導入した後に `brew instal python3`を行うことですが、欠点としては `brew update`で python3 のバージョンが変更されてしまうことや、必ずしも最新の Python が homebrew によって導入される保証がないことがあります。自分で version を管理したい or 特定の Python のバージョンでコーディングを行いたい場合は pyenv を利用すること推奨します。 また、導入方法によっては `python`ではなく `python3`が python3.x を呼び出すコマンドになっていることがあります。

以下では python -> python3 に読み替えて作業を行う方がよいかもしれません。

優先されている Python の path を確認するには `which python3`とすることで確認できます。

### Python の基礎

#### 演算子

算術計算は他のプログラミング言語と同様に、 `+, -, *, / ,%`の演算子によって行えます。  
ただし、C/C++/Ruby などプログラミング言語と決定的に異なる挙動がある演算子が 2 つあります。

1. `/` 演算子  
   C/C++ では、整数(int, long, long long)同士の除算は整数になり、切り捨てが行われますが、Python では int / int -> float となります。また、Python は動的型付け言語であるため、意図せぬ型変換(正確には型変換ではない)が起こることがあり、注意が必要です。また、メモリ制約が厳しい場合は浮動小数演算を意図せぬ形で行うことになり、余計なメモリを消費しかねない事態が起こり得ます。

2. `**`演算子  
   C/C++には存在しない(デフォルト GCC/Clang では存在しない)演算子であり、累乗を計算します。pow 関数は繰り返し自乗法を用いる内部実装であるので計算量は$O(log(N))$ですが、 `**`演算子がどうなのかは裏付けが取れていません。

詳しくは以下

> / (除算: division) および // (切り捨て除算: floor division) は、引数同士の商を与えます。数値引数はまず共通の型に変換されます。整数の除算結果は浮動小数点になりますが、整数の切り捨て除算結果は整数になります; この場合、結果は数学的な除算に 'floor' 関数 を適用したものになります。ゼロによる除算を行うと ZeroDivisionError 例外を送出します

[二項演算子 binary operator 公式ドキュメント](https://docs.python.org/ja/3/reference/expressions.html?highlight=%E6%BC%94%E7%AE%97%E5%AD%90#binary-arithmetic-operations)

#### データ型

Python のデータ型には代表的なもので以下のようなものがあります。

- int : 整数
- str : 文字列
- float : 浮動小数点数
- bool : 真偽値
- list : リスト
- tuple : タプル
- dict : 辞書
- set : 集合
- None : None

実は組み込みデータ型にはこれ以外にも多くの型があり、詳しくは以下のリンクを参照ください

[データ型 公式ドキュメント](https://docs.python.org/ja/3/library/datatypes.html)

型情報を取得するには

```python
type(x)
```

により、変数 x の型情報を取得できます。

#### dict

辞書は、キーと値のペアを格納するためのデータ型です。
しかし、C++の map とは異なる挙動もあります。

特に重要なのは、存在しない key にアクセスした際の挙動です。
(計算量は赤黒木、または平衡二分木の改良型のデータ構造を採用しているので、ほとんど差はありません。詳細は自分で調べてください)

default dict [公式ドキュメント](https://docs.python.org/ja/3.10/library/collections.html#defaultdict-objects)

> 1 つ目の引数は default_factory 属性の初期値です。デフォルトは None です。残りの引数はキーワード引数も含め、 dict のコンストラクタに与えられた場合と同様に扱われます。

> defaultdict オブジェクトは標準の dict に加えて、以下のメソッドを実装しています:

> `__missing__(key)`  
> もし default_factory 属性が `None` であれば、このメソッドは `KeyError` 例外を、 `key` を引数として発生させます。

> もし `default_factory` 属性が `None` でない場合、このメソッドは引数なしで呼び出され、与えらえた key に対応するデフォルト値を提供します。この値は、辞書内に key に対応して登録され、最後に返されます。

> もし default_factory の呼出が例外を発生させた場合には、変更せずそのまま例外を投げます。

> このメソッドは dict クラスの `__getitem__()` メソッドで、キーが存在しなかった場合によびだされます。値を返すか例外を発生させるのどちらにしても、 `__getitem__()` からもそのまま値が返るか例外が発生します。

> なお、 `__missing__()` は `__getitem__()` 以外のいかなる演算に対しても呼び出され ません 。よって `get()` は、普通の辞書と同様に、 `default_factory` を使うのではなくデフォルトとして None を返します。

Python の dict の挙動は以下の通り

```python
    mapping: dict[str, int] = {}
    mapping["key1"] = 1
    mapping["key2"] = 2

    print(mapping["key1"]) # 1
    print(mapping["key3"]) # KeyError 'key3'

    print(mapping["key2"]) # 2
    print(mapping.get("key3")) # None
```

default dict の挙動は以下

```python
    mapping: defaultdict[str, int] = defaultdict(int)
    mapping["key1"] = 1
    mapping["key2"] = 2

    print(mapping["key1"]) # 1
    print(mapping["key3"]) # 0
```
これは C++ の `map<string, int>`と同じ挙動。
このように、キーが存在しない場合には、デフォルト値を返す。

Qittaの記事だが、以下に詳しくまとまっている。
[python defalut dictについて](https://qiita.com/xza/items/72a1b07fcf64d1f4bdb7)

これら以外の Python の基礎文法に関しては説明を行わない。

自信のないものは、[Python早見帳](https://chokkan.github.io/python/index.html)を参照のこと
