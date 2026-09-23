"""HTML block helpers for project pages. Image paths are relative to the project's image folder."""
import os
from PIL import Image

SITE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_CUR = {"slug": None}


def set_slug(slug):
    _CUR["slug"] = slug


def _src(name):
    return f"../assets/img/{_CUR['slug']}/{name}"


def _check(name):
    p = os.path.join(SITE, "assets/img", _CUR["slug"], name)
    if not os.path.exists(p):
        raise FileNotFoundError(p)
    return Image.open(p).size


def img(name, alt, cls=""):
    if name.startswith("http"):
        c = f' class="{cls}"' if cls else ""
        return f'<img src="{name}" alt="{alt}" loading="lazy" referrerpolicy="no-referrer"{c}>'
    w, h = _check(name)
    c = f' class="{cls}"' if cls else ""
    return f'<img src="{_src(name)}" alt="{alt}" width="{w}" height="{h}" loading="lazy"{c}>'


def fig(name, cap, alt=None):
    return f'<figure class="fig reveal">{img(name, alt or cap)}<figcaption>{cap}</figcaption></figure>'


def gallery(items, cols=3, cls="", ar=None):
    style = f' style="--ar:{ar}"' if ar else ""
    inner = "".join(
        f'<figure>{img(n, c)}<figcaption>{c}</figcaption></figure>' if c else f'<figure>{img(n, "Project image")}</figure>'
        for n, c in items)
    return f'<div class="gallery g{cols} {cls} reveal"{style}>{inner}</div>'


def split(text_html, figure_html, rev=False):
    return f'<div class="split{" rev" if rev else ""}"><div>{text_html}</div>{figure_html}</div>'


def video(yt, title):
    return (f'<div class="video reveal"><iframe src="https://www.youtube-nocookie.com/embed/{yt}" title="{title}" '
            f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
            f'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen loading="lazy"></iframe></div>')


def steps(items):
    return '<ol class="steps">' + "".join(f"<li>{x}</li>" for x in items) + "</ol>"


def code_list(items):
    return '<div class="code-list">' + "".join(f"<div><code>{a}</code><p>{b}</p></div>" for a, b in items) + "</div>"


def contrib(items):
    return '<div class="contrib">' + "".join(
        f'<div class="c reveal"><h4><i class="{i}"></i>{t}</h4><p>{d}</p></div>' for i, t, d in items) + "</div>"


def cs(items, labels=("Challenge", "Solution")):
    out = '<div class="cs">'
    for ct, cd, st, sd in items:
        out += (f'<div class="cs-item reveal"><div class="ch"><small>{labels[0]}</small><h4>{ct}</h4><p>{cd}</p></div>'
                f'<div class="so"><small>{labels[1]}</small><h4>{st}</h4><p>{sd}</p></div></div>')
    return out + "</div>"


def stats(items):
    return '<div class="stat-row">' + "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in items) + "</div>"


def ul(items):
    return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def note(t):
    return f'<p class="note">{t}</p>'


def tracks(items, root="../"):
    rows = "".join(
        f'<div class="track-row"><button class="play" data-audio="{root}assets/audio/{f}" aria-label="Play {t}">▶</button>'
        f'<div><b>{t}</b><span>{d}</span><div class="bar"><i></i></div></div><span class="t"></span></div>'
        for f, t, d in items)
    return f'<div class="tracks reveal">{rows}</div>'


def sfx(items, root="../"):
    b = "".join(f'<button data-audio="{root}assets/audio/{f}" data-label="♪ {t}">♪ {t}</button>' for f, t in items)
    return f'<div class="sfx">{b}</div>'


def code(title, lang_note, src):
    import html as _h
    return (f'<div class="code-head"><b>{title}</b><span>{lang_note}</span></div>'
            f'<pre class="code">{_h.escape(src)}</pre>')
