/* Client-side replacements for custom markup.

Subtitles wrap the rest of the line in a span with a `lang` attribute:
    md:   |at|> I wüü bitte a Hoibe.
    html: <span lang="at">I wüü bitte a Hoibe.</span>

Spoilers wrap text in a span with class .spoiler:
    md:   This is a !!spoiler.!!
    html: This is a <span class="spoiler">spoiler.</span>
*/

const SUBTITLE = /^\s*\|(\w{2})\|>\s?/;
const SPOILER = /!!(.+?)!!(?!!)/g;

function textNodes(root) {
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  const nodes = [];
  while (walker.nextNode()) nodes.push(walker.currentNode);
  return nodes;
}

function markupSpoilers(root) {
  for (const node of textNodes(root)) {
    if (!SPOILER.test(node.data)) continue;
    SPOILER.lastIndex = 0;
    const span = document.createElement("span");
    span.innerHTML = node.data
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(SPOILER, '<span class="spoiler">$1</span>');
    node.replaceWith(...span.childNodes);
  }
}

function markupSubtitles(paragraph) {
  // split text nodes so every newline is its own node, then group into lines
  for (const node of [...paragraph.childNodes]) {
    if (node.nodeType !== Node.TEXT_NODE || !node.data.includes("\n")) continue;
    const parts = node.data.split(/(\n)/).filter(Boolean);
    node.replaceWith(...parts.map((part) => document.createTextNode(part)));
  }

  const lines = [[]];
  for (const node of [...paragraph.childNodes]) {
    const isBreak = node.nodeName === "BR" || node.data === "\n";
    isBreak ? lines.push([]) : lines.at(-1).push(node);
  }

  for (const line of lines) {
    const first = line[0];
    const match = first?.nodeType === Node.TEXT_NODE && first.data.match(SUBTITLE);
    if (!match) continue;
    first.data = first.data.slice(match[0].length);
    const span = document.createElement("span");
    span.lang = match[1];
    first.before(span);
    span.append(...line);
  }
}

function markup() {
  for (const paragraph of document.querySelectorAll(".md-typeset p")) {
    if (paragraph.textContent.includes("|>")) markupSubtitles(paragraph);
  }
  markupSpoilers(document.querySelector(".md-typeset") ?? document.body);
}

// re-run after instant navigation when the theme exposes document$
if (typeof document$ !== "undefined") {
  document$.subscribe(markup);
} else {
  document.addEventListener("DOMContentLoaded", markup);
}
