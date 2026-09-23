from common import head, nav, footer, EMAIL, LINKEDIN, RESUME

EXPERIENCE = [
    ("Mar – Jul 2026", "Tencent Games", "Technical Art Intern (Tools & Pipeline)", "TiMi J3 Studio · <em>Delta Force</em>",
     ["Co-developed a centralized shader library that consolidated existing shading solutions and set cross-platform validation benchmarks, streamlining compliant asset production for internal teams and external vendors.",
      "Built AI-powered production tools by integrating proprietary and open-source generative models into existing 2D/3D DCC tools and pipelines (<a href=\"projects/sdMaterialTool.html\" style=\"color:var(--accent)\">Substance Designer</a> · <a href=\"projects/psAiToolkit.html\" style=\"color:var(--accent)\">Photoshop</a>).",
      "Prototyped LoRA-based stylization workflows for project-specific look development and asset generation.",
      "Evaluated multimodal 3D AI technologies and delivered technical recommendations that informed an internal AI-driven art platform."],
     ["Shaders", "Python", "PySide", "ComfyUI", "LoRA"]),
    ("Jan – Mar 2026", "Tencent Games", "Project Management Intern", "TiMi G1 Studio · Unannounced AAA title",
     ["Managed end-to-end production pipelines for gameplay features and Technical Art/VFX assets, from feature planning and risk management through implementation, integration, validation and milestone delivery in an Agile environment.",
      "Coordinated iteration planning and schedules to keep scope, timelines and quality objectives aligned."],
     ["Agile", "TA/VFX pipeline", "Risk management"]),
    ("Aug – Sep 2025", "Marriott International", "Strategy Planning & Communications Intern", "Asia Pacific excluding China",
     ["Supported PMO activities for strategic regional initiatives, coordinating cross-functional stakeholders on scope, milestones, risks and execution.",
      "Synthesized Guest Voice, ITR, RevPAR and cross-functional insights into executive-ready post-opening performance reviews."],
     ["PMO", "Stakeholder comms", "Analysis"]),
    ("Jan – Jul 2025", "Marriott International", "Communications Intern", "Asia Pacific excluding China",
     ["Benchmarked executive LinkedIn performance and recommended leadership-communication best practices.",
      "Assessed 50+ Chinese KOLs and synthesized market insights into an executive-ready China social media playbook."],
     ["Research", "Strategy"]),
    ("Apr – Jul 2024", "Edelman China", "Corporate & Financial Services PR Intern", "",
     ["Turned multi-market performance data into executive-ready analyses. Benchmarking and pitch research contributed to 5+ client renewals and new engagements."],
     ["Research", "Client comms"]),
    ("May – Jul 2023", "Mango TV", "Director Intern · <em>Chengfeng 2023</em>", "",
     ["Analyzed Weibo trends and audience sentiment to shape storyline recommendations for a program that reached 610M+ viewers and drove 12,000+ trending discussions."],
     ["Audience insight", "Narrative"]),
]

PROJECTS = [
    ("Oct 2025", "Rhythm: Echo of the Disciple", "Producer · Developer · Technical Artist", "Global Game Jam × WIPO", "rhythmEcho",
     "Rhythm & puzzle systems in UE5 Blueprints (20-min demo). Optimized lighting, skybox and rendering while reducing build size. Led a 9-person team in two weeks."),
    ("Feb – Apr 2025", "Puppet Mystery", "Lead Developer · Producer", "Malanshan Cup, Mango TV", "puppetMystery",
     "Core mechanics and puzzle systems in Unity (C#). Managed a 7-person team to a 10-minute demo in three months."),
    ("Jan 2025", "Bubble Factory", "Lead Developer · Level Designer · Technical Artist", "Global Game Jam", "bubbleFactory",
     "Gameplay systems in C# in 48 hours. Stylized bubble material in Shader Graph (Fresnel, transparency, normal distortion)."),
    ("Sep – Oct 2024", "Gravitas", "Audio Designer · Narrative Designer", "UCSD Triton Ware · Featured Game", "gravitas",
     "Composed the original soundtrack and SFX, and co-designed narrative and gameplay pacing."),
    ("Feb 2024", "The Village", "Costume & Makeup Head", "NUS KE VII Chinese Drama · NUS Achievement Award", "theVillage",
     "Directed a 29-member team to design costumes and makeup for 33 characters."),
    ("Feb 2023", "The Insanity", "Costume Designer · Assistant Producer", "NUS KE VII Chinese Drama · SGD 7,000 sponsorship", "theInsanity",
     "Secured SGD 7,000 in sponsorship and ran budget, timeline and risk for a show seen by 600 people."),
]


def build():
    exp = ""
    for when, co, title, org, bullets, tags in EXPERIENCE:
        b = "".join(f"<li>{x}</li>" for x in bullets)
        t = "".join(f'<span class="tag">{x}</span>' for x in tags)
        exp += f"""
        <div class="tl-item">
          <div class="tl-when">{when}<span class="co">{co}</span></div>
          <div><h4>{title}</h4><span class="org">{org}</span><ul>{b}</ul><div class="tags">{t}</div></div>
        </div>"""
    proj = ""
    for when, name, role, ev, slug, desc in PROJECTS:
        if slug and slug.startswith("http"):
            link = f' <a href="{slug}" target="_blank" rel="noopener" style="color:var(--accent);font-size:13px">itch.io ↗</a>'
        else:
            link = f' <a href="projects/{slug}.html" style="color:var(--accent);font-size:13px">case study →</a>' if slug else ""
        proj += f"""
        <div class="tl-item">
          <div class="tl-when">{when}<span class="co">{ev}</span></div>
          <div><h4>{name}{link}</h4><span class="org">{role}</span><p style="font-size:14.5px;margin:0">{desc}</p></div>
        </div>"""
    html = head("Resume · Yolanda Liu, Technical Artist", "Resume of Yolanda Liu, Technical Artist: Tencent Games TiMi, USC MFA Interactive Media & Games.")
    html += "<body>\n" + nav("", home=False).replace('href="index.html#', 'href="index.html#')
    html += f"""
<header class="r-hero">
  <div class="wrap">
    <div class="r-head">
      <div>
        <div class="eyebrow">Resume · updated Aug 2026</div>
        <h1>Yolanda Liu <span style="color:var(--muted);font-weight:500">(Liu Xingyan)</span></h1>
      </div>
      <div class="contact" id="contact-top">
        <a href="mailto:{EMAIL}"><i class="fa-solid fa-envelope"></i> {EMAIL}</a>
        <a href="{LINKEDIN}" target="_blank" rel="noopener"><i class="fa-brands fa-linkedin"></i> linkedin.com/in/liu-xingyan-yolanda6</a>
      </div>
    </div>
    <div class="hero-actions">
      <a class="btn primary" href="mailto:{EMAIL}"><i class="fa-solid fa-envelope"></i> Get in touch</a>
      <a class="btn" href="index.html#work"><i class="fa-solid fa-layer-group"></i> See the work</a>
    </div>
    <div class="r-sum">
      <div><b>USC MFA</b><span>Interactive Media &amp; Games, 2026–2029</span></div>
      <div><b>Tencent TiMi ×2</b><span>Technical Art + Project Management</span></div>
      <div><b>DiGRA 2026</b><span>Published paper</span></div>
      <div><b>NUS, Highest Distinction</b><span>GPA 4.60 / 5.00</span></div>
    </div>
  </div>
</header>
<div class="wrap">
  <div class="p-layout">
    <aside class="toc">
      <h4>Sections</h4>
      <ol>
        <li><a href="#education">Education</a></li>
        <li><a href="#experience">Experience</a></li>
        <li><a href="#projects">Projects &amp; leadership</a></li>
        <li><a href="#publication">Publication</a></li>
      </ol>
    </aside>
    <main class="p-content">
      <section class="p-sec" id="education"><h2><span class="n">01</span>Education</h2>
        <div class="tl-item"><div class="tl-when">Aug 2026 – May 2029 (exp.)<span class="co">Los Angeles</span></div><div><h4>University of Southern California</h4><span class="org">Master of Fine Arts, Interactive Media &amp; Games</span></div></div>
        <div class="tl-item"><div class="tl-when">Aug 2022 – Dec 2025<span class="co">Singapore</span></div><div><h4>National University of Singapore</h4><span class="org">B.Soc.Sci. (Honours), Highest Distinction · Communications &amp; New Media · GPA 4.60/5.00</span><p style="font-size:14.5px;margin:0">Courses: Game Design, Computational Communication, Computational Media Literacy, Digital Storytelling</p></div></div>
      </section>
      <section class="p-sec" id="experience"><h2><span class="n">02</span>Professional experience</h2>{exp}
      </section>
      <section class="p-sec" id="projects"><h2><span class="n">03</span>Projects &amp; leadership</h2>{proj}
      </section>
      <section class="p-sec" id="publication"><h2><span class="n">04</span>Publication</h2>
        <div class="pub">X. Liu and A. Mitchell, “Close-Playing War Trauma: The Tension Between Agency and Inevitability in <em>My Child Lebensborn</em> and <em>Bury Me, My Love</em>,” presented at DiGRA 2026, Digital Games Research Association, June 2026. <a href="https://dl.digra.org/index.php/dl/article/view/2814/2798" target="_blank" rel="noopener">Read the paper ↗</a></div>
      </section>
    </main>
  </div>
</div>
"""
    html += footer("")
    return html
