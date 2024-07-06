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
    """Preprocess subtitles.

    Basic example:
        pre:  I wüü bitte a Hoibe. <!-- class:beer -->
        post: <span class="spoiler">I wüü bitte a Hoibe.</span>

    Only trailing whitespace after the comment is respected.
        pre:  > :man_tone1: Schoafe Schoaf. Danke.  <!-- class:subtitles_at -->
        post: > :man_tone1: <span class="subtitles_at">Schoafe Schoaf. Danke.</span>
    """

    def replace(match: re.Match):
        blockquote = match.group("blockquote")
        text = match.group("text")
        print(text)
        class_value = match.group("class_value")
        trailing_whitespace = match.group("trailing_whitespace")

        replacement = f'{blockquote}<span class="{class_value}">{text}</span>{trailing_whitespace}'
        # print(replacement)

        return replacement

    markdown = re.sub(
        # named patterns should return empty strings when there is no match
        r"^(?P<blockquote>>?\s?)(?P<text>.*?)\s*?<!-- class:(?P<class_value>\w+?) -->(?P<trailing_whitespace>\s*?)$",
        replace,
        markdown,
        flags=re.I | re.M,
    )

    return markdown


if __name__ == "__main__":
    markdown = """
> :man_tone1: Schoafe Schoaf. Danke.            <!-- class:subtitles_at -->
> Scharfe Scharf. Danke.                        <!-- class:subtitles_de -->
> :woman: Sog, wos is a schoafe Schoaf?         <!-- class:subtitles_at -->
> Sag, was ist eine "scharfe Scharf?"           <!-- class:subtitles_de -->
> :man_tone1: Sie san von Wien? :woman: _Ja._   <!-- class:subtitles_at -->
> Sie sind von Wien? _Ja._                      <!-- class:subtitles_de -->
> :man_tone1: Warum kennat's des ned? (1)       <!-- class:subtitles_at -->
> Warum kennte sie das nicht?                   <!-- class:subtitles_de -->
> :man_tone1: Schoafe Schoaf is a schoafe Burnwurst mid schoafm Senf. Schoaf, Schoaf.  <!-- class:subtitles_at -->
> "Scharfe Scharf" ist eine scharfe Burenwurst mit scharfem Senf. Scharf, Scharf. <!-- class:subtitles_de -->
> :man_tone1: Also, packma ned mehrere Sochn. Song so, muss einfoch "schoaf Schoaf."  <!-- class:subtitles_at -->
> Also, packen wir nicht mehrere Sachen. Sagen so, (es) muss einfach "scharf Scharf." <!-- class:subtitles_de -->
> :man_tone1: "Schoafe Schoaf" is "schoafe Schoaf."  <!-- class:subtitles_at -->
> "Scharfe Scharf" ist "scharfe Scharf." <!-- class:subtitles_de -->
> :man_tone1: Es is, is irgendwo verständlich, oder hob mi -- hob mi mehr, richtig auch.  <!-- class:subtitles_at -->
> Es ist, ist irgendwo verständlich, oder habe mich -- habe mich mehr, richtig auch. <!-- class:subtitles_de -->
""".strip()

    markdown = preprocess_subtitles(markdown)
    print(markdown)
