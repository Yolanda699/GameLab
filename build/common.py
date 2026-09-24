"""Shared layout pieces for the site generator."""

EMAIL = "xingyan@usc.edu"
LINKEDIN = "https://www.linkedin.com/in/liu-xingyan-yolanda6"
ITCH = "https://yollienarae.itch.io"
RESUME = "assets/YolandaLIU_Resume.pdf"

FA = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">'


def head(title, desc, root=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="theme-color" content="#F2EEE6">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' fill='%23F2EEE6'/><text x='32' y='44' font-family='Georgia,serif' font-size='34' text-anchor='middle' fill='%23A8412A'>YL</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..700&family=Inter:wght@300..600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/site.css">
{FA}
</head>
"""


MENU = [
    ("Rendering & Shading", [("theFeeding", "The Feeding", "UE 5.6 · PCG, materials, lighting"), ("rhythmEcho", "Rhythm: Echo of the Disciple", "Skies, lighting, rhythm engine"), ("bubbleFactory", "Bubble Factory", "Shader Graph bubbles · URP materials")]),
    ("Tools & AI Pipeline", [("sdMaterialTool", "AI Tiling Material Generator", "Substance 3D Designer plugin · PBR maps"), ("psAiToolkit", "AI Creative Toolkit", "Photoshop UXP plugin · 11 features"), ("travelTrove", "TravelTrove", "Stylized concept-art workflow")]),
    ("Gameplay Systems", [("riverOfForgetting", "River of Forgetting", "Unity · brewing & endings"), ("brokenStage", "Broken Stage", "Unity · puzzle systems"), ("puppetMystery", "Puppet Mystery", "Unity · lead dev & producer")]),
    ("Beyond the Engine", [("gravitas", "Gravitas", "Audio & narrative design"), ("theVillage", "The Village", "Costume & makeup head · 33 characters"), ("theInsanity", "The Insanity", "Costume design & production")]),
    ("Written by hand", [("__lab", "Shader Lab", "Live GLSL: fog, PBR, water, bubble, POM, dissolve")]),
]


def nav(root="", home=True):
    h = "" if home else f"{root}index.html"
    groups = ""
    for g, items in MENU:
        links = "".join(
            f'<a href="{root}shaders.html">{t}<span>{d}</span></a>' if s == "__lab"
            else f'<a href="{root}projects/{s}.html">{t}<span>{d}</span></a>'
            for s, t, d in items)
        groups += f'<div class="grp"><small>{g}</small>{links}</div>'
    return f"""<nav class="nav">
  <div class="wrap">
    <a class="brand" href="{root}index.html">
      <span class="brand-text">Yolanda Liu<small>TECHNICAL ARTIST &amp; PRODUCER</small></span>
    </a>
    <button class="nav-toggle" aria-label="Menu"><i class="fa-solid fa-bars"></i></button>
    <ul class="nav-links">
      <li><a href="{h}#professional">Professional Work</a></li>
      <li class="has-menu"><a href="{h}#work">Projects</a><div class="menu">{groups}</div></li>
      <li><a href="{root}shaders.html">Shader Lab</a></li>
      <li><a href="{h}#skills">Skills</a></li>
      <li><a href="{h}#about">About</a></li>
      <li><a href="{root}resume.html">Resume</a></li>
      <li><a class="btn-nav" href="{root}resume.html#contact-top">Contact</a></li>
    </ul>
  </div>
</nav>
"""


def footer(root="", scripts=()):
    extra = "".join(f'<script src="{root}assets/js/{x}"></script>\n' for x in scripts)
    return f"""<footer class="footer" id="contact">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h3>Let's build better art pipelines.</h3>
        <p>Open to Technical Art roles &amp; collaborations – <a href="mailto:{EMAIL}" style="color:var(--accent)">{EMAIL}</a></p>
      </div>
      <div class="socials">
        <a href="mailto:{EMAIL}" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
        <a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
        <a href="{ITCH}" target="_blank" rel="noopener" aria-label="itch.io"><i class="fa-brands fa-itch-io"></i></a>
        <a href="{root}resume.html" aria-label="Resume"><i class="fa-solid fa-file-lines"></i></a>
      </div>
    </div>
    <div class="copyright">© 2026 Yolanda Liu · All rights reserved</div>
  </div>
</footer>
<script src="{root}assets/js/gl.js"></script>
{extra}<script src="{root}assets/js/site.js"></script>
</body>
</html>
"""
