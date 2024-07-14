"""Locally defined mkdocs build plugins.

Hooks Docs:
    https://www.mkdocs.org/user-guide/configuration/#hooks
"""

import re

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page


def on_page_markdown(markdown, *, page: Page, config: MkDocsConfig, files: Files):
    markdown = preprocess_subtitles(markdown)
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


def preprocess_subtitles(markdown):
    """Create a span with a `lang` (language) attribute.

    The span applies to the entire line until a line break.

    Basic example:
        pre:  |at|> I wüü bitte a Hoibe.
        post: <span lang="at">I wüü bitte a Hoibe.</span>
    """

    def replace(match: re.Match):
        blockquote = match.group("blockquote")
        lang = match.group("lang")
        text = match.group("text")
        trailing_whitespace = match.group("trailing_whitespace")

        replacement = (
            f'{blockquote}<span lang="{lang}">{text}</span>{trailing_whitespace}'
        )
        # print(replacement)

        return replacement

    markdown = re.sub(
        # named patterns should return empty strings when there is no match
        r"^(?P<blockquote>>?\s?)(\|(?P<lang>\w{2})\|>\s?)(?P<text>.*?)(?P<trailing_whitespace>\s*?)$",
        replace,
        markdown,
        flags=re.I | re.M,
    )

    return markdown


if __name__ == "__main__":
    markdown = """
> |at|> :factory_worker: Prost, Oida.
> |de|> Prost, Alter.
> |at|> :man_bald_tone1: Du sogst olle "Oida" zu mia, !!heast!!. Haaß Mundl.
> |de|> Du sagst alle "Alter" zu mir, hörst du. Ich heiße Mundl.
> |at|> :factory_worker: Servas.
> |de|> Servus.
""".strip()

    markdown = preprocess_subtitles(markdown)
    print(markdown)
