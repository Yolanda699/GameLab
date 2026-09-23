from common import head, nav, footer
from blocks import set_slug, _src, _check


def page(p, prev_p, next_p):
    """p: dict(slug,title,cat,catname,question,tags,hero,facts,links,ta,sections)"""
    set_slug(p["slug"])
    _check(p["hero"])
    tags = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
    facts = "".join(f"<div><small>{k}</small><span>{v}</span></div>" for k, v in p["facts"])
    links = "".join(
        f'<a class="btn{" primary" if i == 0 else ""}" href="{u}" target="_blank" rel="noopener"><i class="{ic}"></i> {t}</a>'
        for i, (ic, t, u) in enumerate(p.get("links", [])))
    toc = "".join(f'<li><a href="#{sid}">{st}</a></li>' for sid, st, _ in p["sections"])
    ta = "".join(f"<li>{x}</li>" for x in p["ta"])
    body = ""
    for i, (sid, st, html) in enumerate(p["sections"], 1):
        body += f'\n<section class="p-sec" id="{sid}"><h2><span class="n">{i:02d}</span>{st}</h2>\n{html}\n</section>'

    nav_next = f"""
    <div class="p-next">
      <a href="{prev_p['slug']}.html"><small>← PREVIOUS</small><b>{prev_p['title']}</b></a>
      <a class="r" href="{next_p['slug']}.html"><small>NEXT PROJECT →</small><b>{next_p['title']}</b></a>
    </div>"""

    html = head(f"{p['title']} · Yolanda Liu, Technical Artist", p["question"], root="../")
    html += "<body>\n" + nav("../", home=False)
    # Each project's key art gets the treatment its own proportions deserve,
    # rather than every page being cropped into the same band.
    #   wide   - cinematic still, cropped into a full-width band
    #   full   - a composed banner, shown whole at its own aspect ratio
    #   inset  - a UI capture, framed in a narrower column with paper around it
    #   poster - portrait artwork, standing beside the title
    mode = p.get("hero_mode", "wide")
    img = f'<img src="{_src(p["hero"])}" alt="{p["title"]} key visual">'
    head_block = f"""<div class="crumbs"><a href="../index.html#work">Work</a> / <a href="../index.html#work-{p['cat']}">{p['catname']}</a> / {p['title']}</div>
    <span class="tag {p['cat']}">{p['catname']}</span>
    <h1{' class="long"' if len(p['title']) > 24 else ''}>{p['title']}</h1>
    <p class="q">{p['question']}</p>
    <div class="tags">{tags}</div>"""

    if mode == "poster":
        hero_html = f"""
<header class="p-hero h-poster">
  <div class="wrap">
    <div class="poster-grid">
      <div class="poster-text">{head_block}</div>
      <figure class="poster-art">{img}<figcaption>{p.get('hero_caption', '')}</figcaption></figure>
    </div>
  </div>
</header>"""
    else:
        hero_html = f"""
<header class="p-hero h-{mode}">
  <div class="wrap">
    {head_block}
  </div>
  <div class="bg">{img}</div>
</header>"""
    html += hero_html
    html += f"""
<div class="wrap">
  <div class="facts">{facts}</div>
  <div class="p-links">{links}</div>
  <div class="p-layout">
    <aside class="toc">
      <h4>On this page</h4>
      <ol>{toc}</ol>
      <div class="next-proj"><a href="{next_p['slug']}.html"><small>NEXT PROJECT</small>{next_p['title']} →</a></div>
    </aside>
    <main class="p-content">
      <div class="ta-box reveal"><h3><i class="fa-solid fa-bolt"></i> Technical art highlights</h3><ul>{ta}</ul></div>
      {body}
      {nav_next}
    </main>
  </div>
</div>
"""
    html += footer("../")
    return html
