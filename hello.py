import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension
from markdown.extensions.sane_lists import SaneListExtension
from markdown.extensions.nl2br import Nl2BrExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.wikilinks import WikiLinkExtension
from markdown.extensions.footnotes import FootnoteExtension
from markdown.extensions.tables import TableExtension
import os

text = """
[TOC]
# Title
Here's a brief introduction about the topic.

## Subheading 2
Here's some content for subheading 2. This is a footnote[^1].

### Sub-subheading 3
Some additional details for this sub-subheading.

Here's a simple list:

1. Item 1
3. Item 2

```python
print("This is a code snippet using fenced code.")
```

New lines
will be 
converted to breaks.

[[WikiLink]]

Here's a table:

| Header 1 | Header 2 |
| -------- | -------- |
| Row1Col1 | Row1Col2 |
| Row2Col1 | Row2Col2 |

## Subheading 2
Another subheading with different content.

[^1]: This is the footnote content.
"""

# 使用する拡張のリスト
extensions = [
    CodeHiliteExtension(),
    TocExtension(marker="[TOC]"),
    SaneListExtension(),
    Nl2BrExtension(),
    FencedCodeExtension(),
    WikiLinkExtension(base_url="/wiki/", end_url=".html"),
    FootnoteExtension(),
    TableExtension()
]

# Markdown を HTML に変換
html = markdown.markdown(text, extensions=extensions)
with open("output.html", "w") as f:
    f.write(html)
