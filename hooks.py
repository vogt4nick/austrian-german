"""Locally defined mkdocs build plugins.

Hooks Docs:
    https://www.mkdocs.org/user-guide/configuration/#hooks
"""

import re

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page


def on_page_markdown(markdown, *, page: Page, config: MkDocsConfig, files: Files):
    markdown = preprocess_spoilers(markdown)
    return markdown


def preprocess_spoilers(markdown):
    """Markup !!spoiler!! as spans with class .spoiler.

    Basic example:
        md:   This is a !!spoiler.!!
        html: This is a <span class="spoiler">spoiler.</span>

    Internal punctuation is respected:
        md:   I can't believe !!Snape killed Dumbledore!!!
        html: I can't believe <span class="spoiler">Snape killed Dumbledore!</span>
    """

    def replace(match: re.Match):
        text = match.group("text")  # must match named group in re.sub pattern
        return f'<span class="spoiler">{text}</span>'

    markdown = re.sub(
        r"(\!{2})(?P<text>.*?)(\!{2})(?!\!)",
        replace,
        markdown,
        flags=re.I | re.M,
    )

    return markdown
