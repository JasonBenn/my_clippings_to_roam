import re
import sys
from datetime import datetime
from itertools import groupby
from operator import attrgetter
from typing import Tuple

import attr
from dateutil import parser


# Configure this script by changing these two constants:
MY_CLIPPINGS_PATH = "/Users/jasonbenn/Desktop/Kindle/My Clippings.txt"
CUSTOM_HASHTAGS = ["ML papers", "TODO"]


@attr.s
class Highlight:
    title_line: str = attr.ib()
    title: str = attr.ib()
    author: str = attr.ib()
    pages: Tuple[int, int] = attr.ib()
    location: Tuple[int, int] = attr.ib()
    added: datetime = attr.ib()
    content: str = attr.ib()


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def formatted_date(dt = datetime.now()):
    return dt.strftime('%B {S}, %Y').replace('{S}', str(dt.day) + suffix(dt.day))


text = open(MY_CLIPPINGS_PATH, encoding='utf-8-sig').read()
annotations = [x for x in text.split("==========\n") if x]

highlights = []
for annotation in annotations:
    title_line, highlight_line, blank_line, *content = annotation.split("\n")
    *title_parts, author = title_line.split(" - ")
    title = " - ".join(title_parts)

    page_start, page_end, location_start, location_end, added_str = re.match(r"- Your (?:Highlight|Bookmark|Note) on(?: Page (\d+)-?(\d+)?)?(?: \|)?(?: Location (\d+)-?(\d+))? \| Added on (.*)", highlight_line, re.IGNORECASE).groups()

    highlights.append(Highlight(
        title_line=title_line.strip(),
        title=title.strip(),
        author=author.strip(),
        location=(int(location_start) if location_start else None, int(location_end) if location_end else None),
        pages=(int(page_start) if page_start else None, int(page_end) if page_end else None),
        added=parser.parse(added_str),
        content="\n".join(content).strip()
    ))


BYTE_ORDER_MARK = '\ufeff'  # hack warning: decoding with utf-8-sig doesn't remove all BOMs?!
grouped = {k.strip(BYTE_ORDER_MARK): list(v) for k, v in groupby(sorted(highlights), attrgetter("title_line"))}

if len(sys.argv) > 1:
    query_parts = sys.argv[1:]
    query = " ".join(query_parts)
    query_results = {k: v for k, v in grouped.items() if query.lower() in k.lower()}
else:
    query_results = grouped

if len(query_results) != 1:
    for k, v in sorted(query_results.items()):
        print(f"{len(v):>3}: {k}")
else:
    title, highlights = list(query_results.items())[0]
    highlight = highlights[0]
    formatted_dates = {f"#[[{formatted_date(x.added)}]]" for x in highlights}
    custom_hashtags = "]] #[[".join(CUSTOM_HASHTAGS)

    print(title)
    print(f"Tags:: {' '.join(formatted_dates)} #[[{highlight.author}]] #[[{custom_hashtags}]]")
    for highlight in highlights:
        print("-", highlight.content)
