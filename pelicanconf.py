AUTHOR = 'akikuno'
SITENAME = 'Read Over Heels'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

THEME = "./pelican-themes/simplify-theme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# SNS周りの設定
SOCIAL = (
    ('twitter', 'https://twitter.com/akicuno'),
    ('gitHub', 'https://github.com/akikuno'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.codehilite': {'css_class': 'highlight', 'linenums': True},
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {},
  },
  'output_format': 'html5',
}

SITEURL = 'https://akikuno.github.io/read-over-heels'


# ページ下部にライセンス表記を追加
COPYRIGHT_NAME = "akikuno"
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}
