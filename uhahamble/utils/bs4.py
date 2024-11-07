import re

from bs4 import Tag

TAG_RE = re.compile(r"<[^>]+>")


def innerHTML(html_tag: Tag) -> str:
    text = ""
    for c in html_tag.contents:
        text += str(c)
    return text


def strip_html(html_in: str) -> str:
    return TAG_RE.sub("", html_in)
