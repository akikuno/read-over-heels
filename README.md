# read-over-heels


https://akikuno.github.io/read-over-heels/


## Setup
```bash
pip install -U pip pelican markdown ghp-import
```

```bash
[ -f pelicanconf.py ] || pelican-quickstart
```


```bash
make html
make serve
```

## Themeの適応

```bash
[ -d pelican-themes/simplify-theme ] || git clone --recursive https://github.com/vuquangtrong/simplify-theme ./pelican-themes/simplify-theme

git clone https://github.com/alexandrevicenzi/Flex.git ./pelican-themes/flex
```

`pecicannonf.py`に以下を追加

```python
THEME = './pelican-themes/simplify-theme'
```

## GitHub Pagesへのデプロイ

```bash
rm -rf output
pelican content -s pelicanconf.py -t ./pelican-themes/simplify-theme
ghp-import output -b gh-pages
git push origin gh-pages
```
