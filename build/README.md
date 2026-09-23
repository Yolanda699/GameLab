# Site generator

The HTML pages (index.html and projects/*.html) are generated from these Python files, so all pages share one layout.

- `home.py`: home page content (hero, project cards, skills, resume, about)
- `projects.py`: every project page (overview, contributions, challenges & solutions, galleries)
- `common.py` / `project.py` / `blocks.py`: shared layout and components

Edit the text, then run:

    pip install pillow
    python3 build/build.py

Images live in `assets/img/<projectSlug>/`. Styles are in `assets/css/site.css`.
