from bs4 import Tag


def innerHTML(html_tag: Tag) -> str:
    text = ""
    for c in html_tag.contents:
        text += str(c)
    return text
