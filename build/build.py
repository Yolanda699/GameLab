import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from home import build as build_home
from projects import ORDER
from project import page
from resume import build as build_resume
from shaderlab import build as build_lab
from typo import polish
SITE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
open(f"{SITE}/index.html", "w").write(polish(build_home()))
open(f"{SITE}/resume.html", "w").write(polish(build_resume()))
open(f"{SITE}/shaders.html", "w").write(polish(build_lab()))
ps = [f() for f in ORDER]
os.makedirs(f"{SITE}/projects", exist_ok=True)
for i, p in enumerate(ps):
    html = page(p, ps[i - 1], ps[(i + 1) % len(ps)])
    open(f"{SITE}/projects/{p['slug']}.html", "w").write(polish(html))
    print("built", p["slug"])
