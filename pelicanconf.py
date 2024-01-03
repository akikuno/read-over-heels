AUTHOR = 'akikuno'
SITENAME = 'Read Over Heels'
SITEURL = 'https://akikuno.github.io/read-over-heels'
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'ja'
DATE_FORMATS = {'ja': '%Y-%m-%d'}

PATH = "content"
THEME = "./pelican-themes/simplify-theme"

ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_PRIMARY_PATH = 'blog'

PAGE_PATHS = ['pages']

# Advanced Settings
FORMATTED_FIELDS = [] # removed 'summary'
STATIC_PATHS = [
	'images',
	'favicon.ico',
    'logo.png',
	'.htaccess',
	'robots.txt'
]


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = {
    'github': 'https://github.com/akikuno',
    'twitter': 'https://twitter.com/akicuno',
}

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


RELATED_POSTS_MAX = 5
RELATED_POSTS_SKIP_SAME_CATEGORY = False
