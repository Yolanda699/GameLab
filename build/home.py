from common import head, nav, footer, WIP, WIP_BADGE, EMAIL, LINKEDIN, RESUME
from shaderlab import hero_script, orb_script

PROJECTS = [
    dict(slug="sdMaterialTool", cat="pipeline", when="2026 · Tencent Games",
         title="AI Tiling Material Generator for Substance 3D Designer",
         hook="A Substance Designer plugin for generating, tiling and processing PBR materials, developed for the Delta Force art team.",
         role="Technical Artist (Tools & Pipeline) · Delta Force, TiMi J3 Studio",
         tags=["Python", "PySide", "Substance Designer API", "PBR maps", "ONNX", "Seamless tiling"]),
    dict(slug="psAiToolkit", cat="pipeline", when="2026 · Tencent Games",
         title="AI Creative Toolkit for Photoshop",
         hook="A Photoshop extension with eleven AI-assisted image tools, editable layer output and centralised updates for the art team.",
         role="Technical Artist (Tools & Pipeline) · Delta Force, TiMi J3 Studio",
         tags=["Photoshop UXP API", "JavaScript", "ComfyUI", "Multimodal VLM", "Depth masks"]),
    dict(slug="travelTrove", cat="pipeline", when="2025 · Solo",
         title="TravelTrove",
         hook="A travel-app concept with a shared AI-assisted souvenir-art workflow and an interactive Figma prototype.",
         role="Solo: research, UX, concept art pipeline, hi-fi prototype",
         tags=["Figma", "Sora", "Prompt design", "User research"]),
    dict(slug="headspace", cat="render", when="2026 · Team of 14",
         title="Headspace",
         hook="Materials, editor tools and Houdini destruction workflows for a 14-person Unreal Engine team. In development.",
         role="Technical Artist",
         tags=["Unreal 5.8", "Houdini", "Substrate", "RBD", "VEX", "Niagara"]),
    dict(slug="noWayOut", cat="render", when="2026 · Team of 2",
         title="No Way Out",
         hook="Environment art, lighting and effects for a campus escape game, with Maya prop and character work and an AI-assisted Blender workflow.",
         role="3D Art · Lighting · VFX · UI · Rigging",
         tags=["Unity URP", "Blender + AI (MCP)", "Maya", "Rigging", "Lighting", "Particle VFX", "UI Toolkit"]),
    dict(slug="littleWorld", cat="render", when="2026 · Team of 2",
         title="Little World",
         hook="Maya modelling, materials, rigging and animation for a stylised boat ride in Unreal Engine 5.8. Work in progress.",
         role="3D Art · Texturing · Rigging · Animation",
         tags=["Maya", "Unreal 5.8", "Rigging", "Skinning", "Animation", "Material instances"]),
    dict(slug="theFeeding", cat="render", when="2025 · Solo",
         title="The Feeding",
         hook="A solo Unreal Engine short film combining environment art, procedural placement, character animation and cinematic lighting.",
         role="Solo: environment, materials, lighting, characters, cinematics",
         tags=["Unreal 5.6", "PCG", "Materials", "MetaHuman", "Gaea", "Sequencer / MRQ"]),
    dict(slug="rhythmEcho", cat="render", when="2025 · Team of 9",
         title="Rhythm: Echo of the Disciple",
         hook="Lighting, rhythm programming and production for a nine-person Unreal Engine game-jam team.",
         role="Producer · Developer · Technical Artist",
         tags=["Unreal 5.6", "Lumen", "Skies & lighting", "Quartz", "Blueprints"]),
    dict(slug="bubbleFactory", cat="render", when="2025 · Global Game Jam",
         title="Bubble Factory",
         hook="Unity gameplay programming, level design and stylised materials for a 48-hour Global Game Jam project.",
         role="Lead Developer · Level Designer · Technical Artist",
         tags=["Unity URP", "Shader Graph", "Fresnel", "Transparency", "HDR emission"]),
    dict(slug="riverOfForgetting", cat="gameplay", when="2025 · Solo",
         title="River of Forgetting",
         hook="A solo Unity narrative game with a brewing system, lantern-lit environments and endings based on player choices.",
         role="Solo: design, C# systems, environment assets",
         tags=["Unity", "C#", "3D", "Narrative systems"]),
    dict(slug="brokenStage", cat="gameplay", when="2024 · Solo",
         title="Broken Stage",
         hook="Interaction, puzzle and branching-ending systems for a solo bilingual mystery game in Unity.",
         role="Solo: design, C# systems, UI, narrative",
         tags=["Unity", "C#", "2D", "Puzzle systems"]),
    dict(slug="puppetMystery", cat="gameplay", when="2025 · Team of 7",
         title="Puppet Mystery",
         hook="Unity room-loading and puzzle systems for a browser-playable deduction game, developed with a seven-person team.",
         role="Lead Developer · Producer · Level Designer",
         tags=["Unity", "C#", "WebGL", "Scene management", "Team lead"]),
    dict(slug="gravitas", cat="beyond", when="2024 · Team game",
         title="Gravitas",
         hook="Original music, sound effects and narrative design for a pixel-art tower-defense game.",
         role="Audio Designer · Narrative Designer",
         tags=["Original soundtrack", "SFX", "Narrative pacing", "Unity"]),
    dict(slug="theVillage", cat="beyond", when="2024 · NUS",
         title="The Village",
         hook="Costume and makeup direction for 33 characters, leading a 29-person theatre team.",
         role="Costume & Makeup Head",
         tags=["Art direction", "Costume design", "Character styling", "Team lead"]),
    dict(slug="theInsanity", cat="beyond", when="2023 · NUS",
         title="The Insanity",
         hook="Costume design, sponsorship and production coordination for a contemporary ensemble play.",
         role="Costume Designer · Assistant Producer",
         tags=["Costume design", "Production", "Sponsorship", "Budget management"]),
]

CATS = [
    ("render", "Real-time Rendering, Lighting & Shading", "Rendering & Shading"),
    ("pipeline", "Tools & AI Pipeline", "Tools & Pipeline"),
    ("gameplay", "Gameplay Systems & Engine Scripting", "Gameplay Systems"),
    ("beyond", "Beyond the Engine · Audio, Narrative & Art Direction", "Beyond the Engine"),
]
CATSHORT = {k: s for k, _, s in CATS}


def card(p, feature=False, rev=False):
    tags = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
    cls = "card reveal" + (" feature" if feature else "") + (" rev" if rev else "")
    tcls = p["cat"] if p["cat"] != "beyond" else ""
    return f"""
      <a class="{cls}" href="projects/{p['slug']}.html">
        <div class="card-media"><img src="assets/img/{p['slug']}/cover.jpg" alt="{p['title']} key visual" loading="lazy"></div>
        <div class="card-body">
          <div class="card-top"><span class="tag {tcls}">{CATSHORT[p['cat']]}</span><span class="when">{p['when']}</span></div>
          {WIP_BADGE if p['slug'] in WIP else ''}
          <h4>{p['title']}</h4>
          <p class="hook">{p['hook']}</p>
          <p class="role">{p['role']}</p>
          <div class="tags">{tags}</div>
          <span class="more">Read the breakdown <i class="fa-solid fa-arrow-right"></i></span>
        </div>
      </a>"""


def hero():
    return f"""
<header class="hero" id="top">
  <div class="gl-stage hero-bg" aria-hidden="true"><canvas data-shader="frag-hero" data-dpr="1"></canvas></div>
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <div class="eyebrow">Portfolio · 2026</div>
        <h1>Yolanda Liu<span class="role">Technical Artist<br>&amp; Producer</span></h1>
        <p class="lede">I develop DCC tools, shaders and real-time environments. My work includes AI-assisted production tools for Tencent&#8217;s Delta Force art team and game projects in Unreal Engine and Unity.</p>
        <ul class="hero-meta">
          <li><span>Now</span><span>MFA, Interactive Media &amp; Games, USC (2026–2029)</span></li>
          <li><span>Recently</span><span>Technical Art Intern, Tools &amp; Pipeline · <em>Delta Force</em>, Tencent TiMi J3</span></li>
          <li><span>Focus</span><span>DCC tools · AI art pipelines · Lighting &amp; shading · Production</span></li>
        </ul>
        <div class="hero-actions">
          <a class="btn primary" href="#professional"><i class="fa-solid fa-briefcase"></i> Professional work</a>
          <a class="btn" href="shaders.html"><i class="fa-solid fa-code"></i> Shader Lab</a>
          <a class="btn" href="resume.html"><i class="fa-solid fa-file-lines"></i> Resume</a>
          <a class="btn" href="mailto:{EMAIL}"><i class="fa-solid fa-envelope"></i> Email</a>
        </div>
      </div>
      <!-- Not a picture: a Cook-Torrance sphere compiled on the visitor's GPU.
           Drag it to move the key light, pull the sliders, pick a material. -->
      <div class="hero-visual">
        <div class="orb-stage">
          <canvas id="orb" data-shader="frag-orb" data-dpr="1.5"
                  aria-label="Interactive material sphere, drag to move the light"></canvas>
          <span class="orb-hint">drag to relight</span>
        </div>
        <div class="orb-presets" role="group" aria-label="Material presets">
          <button class="on" data-base="0.560,0.570,0.580" data-rough="0.34" data-metal="1" data-detail="0.022" data-dscale="16.0" data-aniso="0.85" data-coat="0" data-trans="0" data-sss="0,0,0" data-thick="0" data-vein="0">Brushed steel</button>
          <button data-base="0.042,0.110,0.080" data-rough="0.14" data-metal="0" data-detail="0.004" data-dscale="7.0" data-aniso="0.0" data-coat="0.85" data-trans="1.0" data-sss="0.210,0.560,0.375" data-thick="2.60" data-vein="1.0">Jade</button>
          <button data-base="0.160,0.018,0.012" data-rough="0.3" data-metal="0" data-detail="0.005" data-dscale="8.0" data-aniso="0.0" data-coat="1.0" data-trans="0" data-sss="0,0,0" data-thick="0" data-vein="0">Red lacquer</button>
          <button data-base="0.820,0.800,0.755" data-rough="0.12" data-metal="0" data-detail="0.004" data-dscale="8.0" data-aniso="0.0" data-coat="0.5" data-trans="0.35" data-sss="0.940,0.915,0.870" data-thick="3.2" data-vein="0.3">Porcelain</button>
          <button data-base="0.230,0.085,0.048" data-rough="0.78" data-metal="0" data-detail="0.055" data-dscale="6.5" data-aniso="0.0" data-coat="0" data-trans="0" data-sss="0,0,0" data-thick="0" data-vein="0">Terracotta</button>
          <button data-base="0.140,0.135,0.125" data-rough="0.9" data-metal="0" data-detail="0.08" data-dscale="5.5" data-aniso="0.0" data-coat="0" data-trans="0" data-sss="0,0,0" data-thick="0" data-vein="0">Weathered stone</button>
        </div>
        <p class="orb-note">Not a render. Every pixel is solved on your GPU each frame: GGX distribution,
          height-correlated Smith visibility, anisotropic microfacets on the brushed metal, and
          Beer-Lambert transmission through the jade. <a href="shaders.html">Read the code &rarr;</a></p>
      </div>
    </div>
    <nav class="jump" aria-label="Jump to section">
      <a href="#professional"><small>01</small><b>Professional Work</b></a>
      <a href="#work-render"><small>02 · PROJECTS</small><b>Rendering &amp; Shading</b></a>
      <a href="#work-pipeline"><small>03 · PROJECTS</small><b>Tools &amp; AI Pipeline</b></a>
      <a href="#work-gameplay"><small>04 · PROJECTS</small><b>Gameplay Systems</b></a>
      <a href="#skills"><small>05</small><b>Core Skills</b></a>
      <a href="shaders.html"><small>06</small><b>Shader Lab <i class="fa-solid fa-arrow-up-right-from-square" style="font-size:.7em;opacity:.6"></i></b></a>
    </nav>
  </div>
</header>"""


def slide(src, cap, contain=False):
    c = " contain" if contain else ""
    return f'<figure class="slide{c}"><img src="{src}" alt="{cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>'


def carousel(slides):
    return f"""<div class="carousel">
          <div class="track">{''.join(slides)}</div>
          <div class="car-ctrl"><button class="prev" aria-label="Previous">‹</button><button class="next" aria-label="Next">›</button><span class="count"></span></div>
        </div>"""


def professional():
    A = "assets/img/psAiToolkit/"
    car1 = carousel([
        slide(A + "ps_hero.jpg", "Photoshop AI toolkit: generation, editing, segmentation and analysis in one panel"),
        slide("assets/img/sdMaterialTool/sd_hero.jpg", "Substance Designer plugin output: tileable PBR material sets"),
        slide("assets/img/sdMaterialTool/sd_in_sd_2.jpg", "Plugin docked beside the material graph in Substance Designer"),
        slide("assets/img/sdMaterialTool/sd_architecture.jpg", "Module map: plugin → gateway → image models, plus local ONNX normal-map inference", True),
        slide(A + "ps_semantic.jpg", "AI semantic layer decomposition in Photoshop", True),
        slide(A + "ps_update.jpg", "Two-level update strategy: silent JS hotfix vs. mandatory installer", True),
    ])
    return f"""
<section id="professional">
  <div class="wrap">
    <div class="section-head">
      <div>
        <div class="eyebrow">Industry experience</div>
        <h2>Professional work</h2>
      </div>
      <p>Two roles at Tencent Games' TiMi Studio Group, one in technical art and one in production. The tabs below cover my contributions in each role.</p>
    </div>

    <div class="pro-head reveal">
      <div class="co">
        <!-- Falls back to the lettermark until the logo file is in place. -->
        <div class="logo"><img src="assets/img/logos/tencent-games.png" alt="Tencent Games"
             onerror="this.parentNode.classList.add('fallback');this.remove()"></div>
        <div>
          <h3>Tencent Games · TiMi Studio Group</h3>
          <p>Technical Art Intern (Tools &amp; Pipeline), J3 Studio · <em>Delta Force</em> · Mar – Jul 2026<br>Project Management Intern, G1 Studio · Unannounced AAA title · Jan – Mar 2026</p>
        </div>
      </div>
      <a class="btn" href="projects/sdMaterialTool.html">Full tools case study <i class="fa-solid fa-arrow-right"></i></a>
    </div>
    <div class="pro-body reveal">
      <div class="tabs" role="tablist" data-tabs="pro">
        <button class="tab active" role="tab" aria-selected="true"><small>01</small>AI tools for artists</button>
        <button class="tab" role="tab" aria-selected="false"><small>02</small>Shader library &amp; standards</button>
        <button class="tab" role="tab" aria-selected="false"><small>03</small>Look-dev &amp; AI R&amp;D</button>
        <button class="tab" role="tab" aria-selected="false"><small>04</small>Production management</button>
      </div>

      <div class="panel active" data-panel-of="pro">
        <div class="panel-grid">
          <div>
            <h4>AI-powered DCC tools</h4>
            <div class="meta">J3 Studio · Delta Force · Python, PySide, SD API, Photoshop UXP, ComfyUI, ONNX</div>
            <ul>
              <li>Designed and built a <strong>PBR tiling-material generator for Substance Designer</strong>: AI seeding, seamless tiling, automatic Base Color / Normal / Roughness / Height / Metallic maps, de-lighting and a searchable material library.</li>
              <li>Built a <strong>Photoshop AI toolkit</strong> with 11 features, including text-to-image, inpainting, canvas expansion, multi-view, object extraction, upscaling, VLM analysis and semantic/depth layer decomposition. Results arrive as non-destructive layers.</li>
              <li>Designed a <strong>shared client interface and gateway routing</strong> so providers could be added without redesigning the panel.</li>
              <li>Co-designed <strong>silent JS hotfixes + mandatory installer updates</strong> to keep a large art team on compatible builds.</li>
            </ul>
            <a class="btn" href="projects/sdMaterialTool.html">Substance Designer case study <i class="fa-solid fa-arrow-right"></i></a>
            <a class="btn" href="projects/psAiToolkit.html">Photoshop case study <i class="fa-solid fa-arrow-right"></i></a>
          </div>
          {car1}
        </div>
      </div>

      <div class="panel" data-panel-of="pro">
        <h4>Centralized shader library</h4>
        <div class="meta">J3 Studio · Delta Force · visuals withheld (confidential)</div>
        <div class="wib">
          <div><small>What</small><p>Co-developed a centralized shader library that consolidated the project's existing shading solutions into one maintained source.</p></div>
          <div><small>How</small><p>Established cross-platform validation benchmarks so shaders and assets could be checked against the same standard on every target platform.</p></div>
          <div><small>Impact</small><p>Streamlined compliant asset production for both internal art teams and external vendors, with fewer one-off shaders to support.</p></div>
        </div>
      </div>

      <div class="panel" data-panel-of="pro">
        <h4>Look development &amp; AI research</h4>
        <div class="meta">J3 Studio · Delta Force · LoRA, multimodal 3D AI</div>
        <div class="wib">
          <div><small>LoRA stylization</small><p>Prototyped LoRA-based stylization workflows to support project-specific look development and asset generation.</p></div>
          <div><small>3D AI evaluation</small><p>Evaluated multimodal 3D AI technologies against production needs.</p></div>
          <div><small>Recommendations</small><p>Delivered technical recommendations that informed the development of an internal AI-driven art platform.</p></div>
        </div>
      </div>

      <div class="panel" data-panel-of="pro">
        <div class="panel-grid">
          <div>
            <h4>Production pipelines for TA / VFX</h4>
            <div class="meta">G1 Studio · Unannounced AAA title · Agile</div>
            <ul>
              <li>Coordinated gameplay and <strong>Technical Art / VFX production</strong>, including planning, risk tracking, asset integration, validation and milestone delivery.</li>
              <li>Coordinated iteration planning and production schedules to keep scope, timelines and quality objectives aligned.</li>
            </ul>
          </div>
          <div class="wib" style="grid-template-columns:1fr">
            <div><small>Why it matters for TA</small><p>Production work showed me how hand-offs, validation and integration affect artists&#8217; time. Those experiences inform the tools I build.</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""


def work():
    groups = ""
    for key, name, _ in CATS:
        ps = [p for p in PROJECTS if p["cat"] == key]
        if key == "render":
            cards = card(ps[0], feature=True) + "".join(card(p) for p in ps[1:])
            grid = "cards"
        elif key == "pipeline":
            cards = "".join(card(p, feature=True, rev=(i % 2 == 1)) for i, p in enumerate(ps))
            grid = "cards"
        elif len(ps) == 3:
            cards = "".join(card(p) for p in ps)
            grid = "cards c3"
        else:
            cards = "".join(card(p) for p in ps)
            grid = "cards"
        groups += f"""
    <div class="work-group" data-cat="{key}" id="work-{key}">
      <h3>{name}</h3>
      <div class="{grid}">{cards}
      </div>
    </div>"""
    return f"""
<section id="work">
  <div class="wrap">
    <div class="section-head">
      <div>
        <div class="eyebrow">Selected projects</div>
        <h2>Projects</h2>
      </div>
      <div class="filters" role="tablist">
        <button class="filter active" data-filter="all">All</button>
        <button class="filter" data-filter="render">Rendering &amp; Shading</button>
        <button class="filter" data-filter="pipeline">Tools &amp; Pipeline</button>
        <button class="filter" data-filter="gameplay">Gameplay Systems</button>
        <button class="filter" data-filter="beyond">Beyond the Engine</button>
      </div>
    </div>
    <div class="paths" style="margin-top:0">
      <a class="path" href="#work-render"><small>Hiring for</small><b>Lighting / rendering TA</b><p>UE5 PCG, material instances, night &amp; firelight lighting, Shader Graph transparency and render optimization.</p><span class="go">The Feeding · Rhythm · Bubble Factory ↓</span></a>
      <a class="path" href="#work-pipeline"><small>Hiring for</small><b>Tools &amp; pipeline TA</b><p>Python/PySide DCC plugins, AI gateways, deployment, and a concept-stage AI workflow.</p><span class="go">AI Art Tools · TravelTrove ↓</span></a>
      <a class="path" href="#work-gameplay"><small>Hiring for</small><b>Technical designer / generalist</b><p>C# systems in Unity: interaction, puzzles, scene management, branching endings.</p><span class="go">River · Broken Stage · Puppet ↓</span></a>
    </div>{groups}
  </div>
</section>"""


SKILLS = [
    ("render", "fa-solid fa-palette", "Shaders & materials",
     ["HLSL custom nodes", "GLSL", "Master / instance architecture", "PBR authoring", "Translucency & refraction", "Flow maps", "Shader libraries & standards", "Shader profiling & optimization"],
     "Tear path material for <a href='projects/headspace.html#materials' style='color:var(--accent)'>Headspace</a> and six live shaders in the <a href='shaders.html' style='color:var(--accent)'>Shader Lab</a>."),
    ("render", "fa-solid fa-lightbulb", "Lighting, rendering & look-dev",
     ["Real-time lighting", "Lumen & Nanite", "Fog & atmosphere", "Skybox design", "Post-process", "Cinematic rendering", "Asset &amp; shader validation", "GPU profiling", "Performance & build-size optimization"],
     "Lit eight cinematic scenes in <a href='projects/theFeeding.html#renders' style='color:var(--accent)'>The Feeding</a>, and cut build size in <a href='projects/rhythmEcho.html#challenges' style='color:var(--accent)'>Rhythm</a>."),
    ("render", "fa-solid fa-burst", "VFX, destruction & procedural",
     ["Rigid-body fracture", "VEX choreography", "Sim-to-engine baking", "Niagara VFX", "Houdini Digital Assets", "PCG", "Procedural terrain", "Mesh processing"],
     "Houdini-driven screen shatter and piano collapse for <a href='projects/headspace.html#destruction' style='color:var(--accent)'>Headspace</a>, and PCG cliffs and moss in The Feeding."),
    ("pipeline", "fa-solid fa-screwdriver-wrench", "Tools & pipeline",
     ["DCC plugin development", "Editor scripting", "Tool UI (PySide / Qt)", "Service & API integration", "Cross-DCC data pipelines", "Asset validation & batch automation", "C++ editor extensions", "Deployment & updates"],
     "Two AI plugins shipped to the Delta Force art team, and the <a href='projects/headspace.html#materials' style='color:var(--accent)'>Headspace Tools</a> editor plugin."),
    ("pipeline", "fa-solid fa-wand-magic-sparkles", "AI for art pipelines",
     ["ComfyUI workflows", "Open-source model research & benchmarking", "LoRA fine-tuning", "Multimodal & 3D generative AI", "Local ONNX inference", "AI-assisted development"],
     "Evaluated multimodal 3D AI and wrote the recommendations behind an internal AI art platform at Tencent."),
    ("gameplay", "fa-solid fa-gamepad", "Gameplay scripting & animation",
     ["Blueprints", "C# systems", "Audio-synced timing", "Scene management", "Animation Blueprints", "Rigging & skinning", "Animation retargeting"],
     "Rhythm engine and level flow in <a href='projects/rhythmEcho.html' style='color:var(--accent)'>Rhythm</a>, puzzle systems in <a href='projects/puppetMystery.html' style='color:var(--accent)'>Puppet Mystery</a>."),
]

SOFT = [
    ("fa-solid fa-lightbulb", "Product mindset for tools", "Interview artists, define an initial scope and revise tools based on how the team uses them."),
    ("fa-solid fa-arrows-left-right", "Cross-discipline communication", "Translate artists&#8217; requests into technical requirements and explain engine or model constraints in practical terms."),
    ("fa-solid fa-sliders", "User-centered tool design", "Group controls by task, choose useful defaults and preserve source assets during editing."),
    ("fa-solid fa-life-ring", "Artist &amp; vendor enablement", "Document shading standards for vendors, prepare onboarding guides and support tool updates."),
    ("fa-solid fa-file-pen", "Technical documentation", "Architecture diagrams, team guides and usage examples. Published research at DiGRA 2026."),
    ("fa-solid fa-list-check", "Production &amp; planning", "Agile sprints, estimation, risk and milestone tracking for TA / VFX pipelines on a AAA title; producer for teams of 7 and 9."),
]

SOFTWARE = [
    ("render", "fa-solid fa-cube", "Engines &amp; profiling", ["Unreal Engine 5", "Unity", "Niagara", "Sequencer · Movie Render Queue", "MetaHuman · Live Link", "Unreal Insights", "RenderDoc"]),
    ("render", "fa-solid fa-shapes", "3D &amp; procedural", ["Houdini", "Maya", "Blender", "ZBrush", "Gaea", "Marvelous Designer", "Mixamo"]),
    ("render", "fa-solid fa-brush", "Texturing &amp; 2D", ["Substance Painter", "Substance Designer", "Photoshop", "Illustrator", "Figma"]),
    ("pipeline", "fa-solid fa-code", "Languages", ["Python", "C++", "HLSL", "GLSL", "VEX", "C#", "JavaScript"]),
    ("pipeline", "fa-solid fa-code-branch", "Pipeline &amp; version control", ["Perforce", "Git", "PySide / Qt", "Unreal Python API", "Geometry Script", "Jira · Confluence"]),
    ("pipeline", "fa-solid fa-microchip", "AI tooling &amp; research", ["ComfyUI", "Hugging Face", "Open-source model benchmarking", "LoRA fine-tuning", "Codex", "Claude Code"]),
]


def skills():
    def tags(xs):
        return "".join(f'<span class="tag">{x}</span>' for x in xs)
    hard = "".join(f"""
      <div class="skill-card {cls}">
        <div class="ico"><i class="{ico}"></i></div>
        <h4>{title}</h4>
        <div class="tags">{tags(t)}</div>
        <p class="proof"><i class="fa-solid fa-check" style="color:var(--accent);margin-right:6px"></i>{proof}</p>
      </div>""" for cls, ico, title, t, proof in SKILLS)
    soft = "".join(f"""
      <div class="skill-card"><div class="ico"><i class="{i}"></i></div><h4>{a}</h4><p style="font-size:14px;margin:0">{b}</p></div>""" for i, a, b in SOFT)
    sw = "".join(f"""
      <div class="skill-card {cls}"><div class="ico"><i class="{ico}"></i></div><h4>{title}</h4><div class="tags">{tags(t)}</div></div>""" for cls, ico, title, t in SOFTWARE)
    return f"""
<section id="skills">
  <div class="wrap">
    <div class="section-head">
      <div>
        <div class="eyebrow">What I bring</div>
        <h2>Core skills</h2>
      </div>
      <p>My experience spans rendering, DCC tools, gameplay scripting and production coordination.</p>
    </div>
    <div class="tabs skills-tabs" role="tablist" data-tabs="skills">
      <button class="tab active" role="tab" aria-selected="true"><small>A</small>Hard skills</button>
      <button class="tab" role="tab" aria-selected="false"><small>B</small>Soft skills</button>
      <button class="tab" role="tab" aria-selected="false"><small>C</small>Software</button>
    </div>
    <div class="skill-panel active" data-panel-of="skills"><div class="skills-grid">{hard}
    </div></div>
    <div class="skill-panel" data-panel-of="skills"><div class="skills-grid">{soft}
    </div></div>
    <div class="skill-panel" data-panel-of="skills"><div class="skills-grid">{sw}
    </div></div>
  </div>
</section>"""


def about():
    thumbs = "".join(f'<img src="assets/img/{"theVillage" if n.startswith("village") else "theInsanity"}/{n}.jpg" alt="Costume portrait" loading="lazy">'
                     for n in ["village_01", "village_03", "village_05", "insanity_04", "insanity_10", "insanity_11"])
    tracks = "".join(f"""
            <div class="track-row"><button class="play" data-audio="assets/audio/{f}" aria-label="Play {t}">▶</button><div><b>{t}</b><span>{d}</span><div class="bar"><i></i></div></div><span class="t"></span></div>"""
                     for f, t, d in [("gravitas_003_main_menu.mp3", "Main Menu", "Gravitas · original score"),
                                     ("gravitas_005_combat_1.mp3", "Combat I", "Gravitas · battle cue"),
                                     ("gravitas_001_interlude.mp3", "Interlude", "Gravitas · story beat")])
    return f"""
<section id="about">
  <div class="wrap">
    <div class="about-grid">
      <div class="about-photo reveal"><img src="assets/img/profile.jpg" alt="Portrait of Yolanda Liu"></div>
      <div class="about-text reveal">
        <div class="eyebrow">About</div>
        <h2>Art, tools and production</h2>
        <p>I'm Yolanda (Liu Xingyan), a Technical Artist pursuing an MFA in Interactive Media &amp; Games at the University of Southern California. Before USC, I was a Technical Art Intern at Tencent Games' TiMi J3 Studio on <em>Delta Force</em>, working on shader development, art pipelines, production tools and AI-assisted workflows.</p>
        <p>My main interests are shaders, real-time VFX, procedural systems and rendering tools. I enjoy working with artists to turn a visual idea into something the team can use and maintain.</p>
        <p>I also work in theatre, music and production:</p>

        <details class="acc">
          <summary><span class="ico"><i class="fa-solid fa-shirt"></i></span><div><b>Costume &amp; makeup design</b><span class="s">→ character readability, palette and visual systems</span></div></summary>
          <div class="acc-body">
            <p>As Costume &amp; Makeup Head for <em>The Village</em>, I led 29 people to style 33 characters in one period look. As costume designer for <em>The Insanity</em>, I used silhouette and color to separate personalities that still read as one ensemble. Both projects taught me to balance a consistent overall style with distinct characters.</p>
            <div class="thumbs">{thumbs}</div>
            <a class="btn" href="projects/theVillage.html">See the costume work <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </details>

        <details class="acc">
          <summary><span class="ico"><i class="fa-solid fa-music"></i></span><div><b>Music &amp; sound</b><span class="s">→ rhythm systems, pacing and feedback</span></div></summary>
          <div class="acc-body">
            <p>I composed the original soundtrack and sound effects for <em>Gravitas</em>, a Featured Game at UCSD Triton Ware 2024. Thinking in cues and tempo helped me design rhythm mechanics in <em>Rhythm: Echo of the Disciple</em> and pace a cinematic in <em>The Feeding</em>.</p>
            <div class="tracks">{tracks}
            </div>
            <a class="btn" href="projects/gravitas.html">All tracks &amp; SFX <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </details>

        <details class="acc">
          <summary><span class="ico"><i class="fa-solid fa-masks-theater"></i></span><div><b>Theatre production</b><span class="s">→ budgets, risk and shipping on a fixed date</span></div></summary>
          <div class="acc-body">
            <p>As assistant producer for <em>The Insanity</em>, I secured SGD 7,000 in sponsorship, managed the budget and coordinated timelines, resources and risk for a show seen by 600 people. This involved planning around a fixed performance date and coordinating several departments.</p>
            <a class="btn" href="projects/theInsanity.html">Production details <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </details>
      </div>
    </div>
  </div>
</section>"""


MARQUEE = '\n<div class="marquee" aria-hidden="true">\n  <div class="marquee-track"><span>Unreal Engine 5</span><span>GLSL / HLSL</span><span>Substance 3D Designer</span><span>Python</span><span>PySide / Qt</span><span>Material instances</span><span>PCG</span><span>Photoshop UXP</span><span>ComfyUI</span><span>Unity URP</span><span>C#</span><span>Shader Graph</span><span>MetaHuman</span><span>Gaea</span><span>Marvelous Designer</span><span>Blender</span><span>Movie Render Queue</span><span>Perforce</span><span>Unreal Engine 5</span><span>GLSL / HLSL</span><span>Substance 3D Designer</span><span>Python</span><span>PySide / Qt</span><span>Material instances</span><span>PCG</span><span>Photoshop UXP</span><span>ComfyUI</span><span>Unity URP</span><span>C#</span><span>Shader Graph</span><span>MetaHuman</span><span>Gaea</span><span>Marvelous Designer</span><span>Blender</span><span>Movie Render Queue</span><span>Perforce</span></div>\n</div>'


def build():
    html = head("Yolanda Liu · Technical Artist",
                "Technical Artist portfolio of Yolanda Liu: AI art pipeline tools, real-time rendering and shading in Unreal Engine 5, and gameplay systems.")
    html += '<body>\n' + nav() + hero() + MARQUEE + professional() + work() + skills() + about() + hero_script() + orb_script() + footer()
    return html
