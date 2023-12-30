# read-over-heels

## Setup
```bash
pip install -U pip pelican markdown ghp-import
```

```bash
pelican-quickstart
```


```bash
make html
make serve
```

## Themeの適応

```bash
git clone --recursive https://github.com/getpelican/pelican-themes ./pelican-themes
```

`pecicannonf.py`に以下を追加

```python
THEME = './pelican-themes/simplify-theme'
```

## GitHub Pagesへのデプロイ

```bash
pelican content -s pelicanconf.py -t ./pelican-themes/simplify-theme
ghp-import output -b gh-pages
git push origin gh-pages
```
