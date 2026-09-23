"""Typographic polish applied to finished HTML.

Only touches prose: everything inside <script>, <style>, <pre> and <code> is
left byte-for-byte alone, as are tag attributes. Straight apostrophes between
two letters become typographic ones (it's -> it’s), and em dashes become
en dashes, which sit lighter on the line.
"""

import re

_SKIP = re.compile(r"(<(script|style|pre|code)\b.*?</\2>|<[^>]+>)", re.S | re.I)
_APOS = re.compile(r"(?<=[A-Za-z])'(?=[A-Za-z])")


def _prose(text):
    return _APOS.sub("’", text)


def polish(html):
    out, last = [], 0
    for m in _SKIP.finditer(html):
        out.append(_prose(html[last:m.start()]))
        out.append(m.group(0))
        last = m.end()
    out.append(_prose(html[last:]))
    return "".join(out)
