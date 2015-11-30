#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "funcool org"
SITENAME = "funcool"
SITEURL = "http://localhost:8000"
TIMEZONE = "UTC"

PATH = "content"
STATIC_PATHS = ["blog", "downloads"]
ARTICLE_PATHS = ["blog"]

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"
# FILENAME_METADATA = "(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)"

DEFAULT_PAGINATION = 20
USE_FOLDER_AS_CATEGORY = True

GITHUB = "https://github.com/funcool"
RELATIVE_URLS = False

THEME = "themes/funcool"
LOCALE = ["en_US"]
DEFAULT_LANG = "en_US"

FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_RSS = "feeds/%s.rss.xml"

TEMPLATE_PAGES = {"extra/about.jinja": "about.html"}

STATIC_PATHS = [
    "extra/robots.txt",
]

EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
}

