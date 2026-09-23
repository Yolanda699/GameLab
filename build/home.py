from common import head, nav, footer, EMAIL, LINKEDIN, RESUME
from shaderlab import hero_script, orb_script

PROJECTS = [
    dict(slug="sdMaterialTool", cat="pipeline", when="2026 · Tencent Games",
         title="Tiling Material Generator for Substance 3D Designer",
         hook="How do you get a seamless, production-ready PBR material set from a prompt without ever leaving Substance Designer?",
         role="Technical Artist (Tools & Pipeline) · Delta Force, TiMi J3 Studio",
         tags=["Python", "PySide", "Substance Designer API", "PBR maps", "ONNX", "Seamless tiling"]),
    dict(slug="psAiToolkit", cat="pipeline", when="2026 · Tencent Games",
         title="AI Creative Toolkit for Photoshop",
         hook="How do you put eleven AI capabilities inside Photoshop without ever costing an artist a layer?",
         role="Technical Artist (Tools & Pipeline) · Delta Force, TiMi J3 Studio",
         tags=["Photoshop UXP API", "JavaScript", "ComfyUI", "Multimodal VLM", "Depth masks"]),
    dict(slug="travelTrove", cat="pipeline", when="2025 · Solo",
         title="TravelTrove",
         hook="How did I set up a controlled AI generation workflow so independently generated concept assets read as one art style?",
         role="Solo: research, UX, concept art pipeline, hi-fi prototype",
         tags=["Figma", "Sora", "Prompt design", "User research"]),
    dict(slug="theFeeding", cat="render", when="2025 · Solo",
         title="The Feeding",
         hook="How did I build a fog-drenched Miao mountain world in UE 5.6, from terrain and PCG foliage to materials, MetaHumans and a cinematic render?",
         role="Solo: environment, materials, lighting, characters, cinematics",
         tags=["Unreal 5.6", "PCG", "Materials", "MetaHuman", "Gaea", "Sequencer / MRQ"]),
    dict(slug="rhythmEcho", cat="render", when="2025 · Team of 9",
         title="Rhythm: Echo of the Disciple",
         hook="How did I light and optimize a mythic 3D rhythm world while producing a 9-person jam team?",
         role="Producer · Developer · Technical Artist",
         tags=["Unreal 5.6", "Lighting", "Skybox", "Optimization", "Blueprints"]),
    dict(slug="bubbleFactory", cat="render", when="2025 · Global Game Jam",
         title="Bubble Factory",
         hook="How did I make materials carry a whole art direction in 48 hours, with translucent bubble shields, a gum lake and glowing pickups?",
         role="Lead Developer · Level Designer · Technical Artist",
         tags=["Unity URP", "Shader Graph", "Fresnel", "Transparency", "HDR emission"]),
    dict(slug="riverOfForgetting", cat="gameplay", when="2025 · Solo",
         title="River of Forgetting",
         hook="How did I build a brewing system and accuracy-based endings for a first-person mythic narrative game?",
         role="Solo: design, C# systems, environment assets",
         tags=["Unity", "C#", "3D", "Narrative systems"]),
    dict(slug="brokenStage", cat="gameplay", when="2024 · Solo",
         title="Broken Stage",
         hook="How did I build interaction, puzzle and branching-ending systems for a bilingual 2D mystery game?",
         role="Solo: design, C# systems, UI, narrative",
         tags=["Unity", "C#", "2D", "Puzzle systems"]),
    dict(slug="puppetMystery", cat="gameplay", when="2025 · Team of 7",
         title="Puppet Mystery",
         hook="How did I architect additive room loading and drag-and-drop puzzles while leading a 7-person team?",
         role="Lead Developer · Producer · Level Designer",
         tags=["Unity", "C#", "WebGL", "Scene management", "Team lead"]),
    dict(slug="gravitas", cat="beyond", when="2024 · Team game",
         title="Gravitas",
         hook="How did I score and sound-design a pixel tower-defense game so every game state has its own identity?",
         role="Audio Designer · Narrative Designer",
         tags=["Original soundtrack", "SFX", "Narrative pacing", "Unity"]),
    dict(slug="theVillage", cat="beyond", when="2024 · NUS",
         title="The Village",
         hook="How did I lead a 29-person costume & makeup team to give 33 characters one cohesive visual language?",
         role="Costume & Makeup Head",
         tags=["Art direction", "Costume design", "Character styling", "Team lead"]),
    dict(slug="theInsanity", cat="beyond", when="2023 · NUS",
         title="The Insanity",
         hook="How did I design a contemporary cast that stays readable as an ensemble, while securing the sponsorship and running the production?",
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
        <p class="lede">I build the tools, shaders and pipelines that let artists move faster, from AI-assisted material and concept workflows shipped to a AAA art team at Tencent to real-time scenes lit and rendered in Unreal Engine 5.</p>
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
      <p>Two roles at Tencent Games' TiMi Studio Group, one in technical art and one in production. Pick a tab to see each area of ownership.</p>
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
              <li>Architected a <strong>gateway-based, model-agnostic</strong> client so new providers plug in without UI changes.</li>
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
              <li>Managed end-to-end production pipelines for gameplay features and <strong>Technical Art / VFX assets</strong>, from feature planning and risk management through implementation, asset integration, validation and milestone delivery.</li>
              <li>Coordinated iteration planning and production schedules to keep scope, timelines and quality objectives aligned.</li>
            </ul>
          </div>
          <div class="wib" style="grid-template-columns:1fr">
            <div><small>Why it matters for TA</small><p>Seeing the TA/VFX pipeline from the producer's side taught me where assets actually stall (hand-offs, validation, integration). I now design tools to remove those bottlenecks.</p></div>
          </div>
        </div>
      </div>
    </div>

    <div class="also">
      <a href="resume.html#experience"><b>Marriott International</b><span>Strategy Planning &amp; Communications · 2025</span></a>
      <a href="resume.html#experience"><b>Edelman China</b><span>Corporate &amp; Financial Services PR · 2024</span></a>
      <a href="resume.html#experience"><b>Mango TV</b><span>Director Intern, <em>Chengfeng 2023</em> · 2023</span></a>
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
    ("render", "fa-solid fa-palette", "Shaders & Materials · PBR",
     ["GLSL (hand-written)", "PBR maps (Albedo, Normal, Roughness, Metallic, Height)", "UE material networks", "Material instancing", "Unity Shader Graph", "Fresnel / transparency / refraction", "Shared shader library"],
     "Co-developed a centralized shader library at Tencent, and wrote six live GLSL shaders for the <a href=\'shaders.html\' style=\'color:var(--accent)\'>Shader Lab</a>."),
    ("render", "fa-solid fa-lightbulb", "Lighting, Look-dev & Optimization",
     ["Real-time lighting", "Fog & firelight", "Skybox & atmosphere", "Asset / lighting validation", "Cross-platform benchmarks", "Render & build-size optimization"],
     "Lit 8 cinematic scenes in UE 5.6, and optimized lighting and rendering in Rhythm while reducing build size."),
    ("render", "fa-solid fa-cube", "Unreal Engine & Procedural",
     ["Unreal Engine 5", "Blueprints", "PCG", "Sequencer / Movie Render Queue", "MetaHuman · Live Link", "IK Retargeting", "Unity (C#)"],
     "Blueprint-driven PCG cliff and moss generators, plus a Mixamo → MetaHuman retargeting pipeline."),
    ("pipeline", "fa-solid fa-screwdriver-wrench", "Tools & Pipeline · Python / DCC APIs",
     ["Python", "PySide / Qt", "Substance Designer API", "Photoshop UXP (JS)", "DCC plugin development", "Service / API integration", "Versioned deployment", "Git · Perforce"],
     "Shipped two AI plugins to the Delta Force art team with a gateway, a unified model interface and silent hotfix updates."),
    ("pipeline", "fa-solid fa-wand-magic-sparkles", "ML / AI for Art Pipelines",
     ["ComfyUI workflows", "Model evaluation & selection", "LoRA stylization", "Multimodal VLMs", "3D generative AI", "ONNX inference", "Prompt templating"],
     "Evaluated multimodal 3D AI and wrote the recommendations behind an internal AI art platform."),
    ("gameplay", "fa-solid fa-mountain-sun", "DCC & Content Creation",
     ["Substance Designer", "Photoshop", "Blender", "Gaea", "Marvelous Designer", "Mixamo", "Figma", "Illustrator"],
     "Gaea terrain, Marvelous Designer cloth and Photoshop/Substance texture work in one UE pipeline."),
]

SOFT = [
    ("fa-solid fa-comments", "Bridging art & engineering", "I turn artists' pain points into tool specs, and engine/model limits back into plain-language workflows. That's how our plugins got adopted across a large art team."),
    ("fa-solid fa-life-ring", "Artist & vendor support", "Built shading standards that internal teams and external vendors could follow, and designed tool updates so artists never had to chase the right build."),
    ("fa-solid fa-file-pen", "Technical documentation", "I write design goals, architecture diagrams and request-flow docs for the tools I build. Published research at DiGRA 2026."),
    ("fa-solid fa-list-check", "Production & project management", "Agile PM intern at TiMi G1, coordinating TA/VFX asset pipelines from planning and risk through validation and milestones."),
    ("fa-solid fa-people-group", "Team leadership", "Producer for teams of 9 (two-week jam) and 7 (three-month cycle), and Costume &amp; Makeup Head leading 29 people on an award-winning production."),
    ("fa-solid fa-eye", "Visual judgement", "Years of costume, makeup and character styling trained my eye for silhouette, palette and readability, which I now apply to lighting and look-dev."),
]

MATRIX = [
    ("Pipeline tools & scripts in Python / DCC APIs", "Substance Designer and Photoshop plugins (Python, PySide, SD API, UXP) used in production at Tencent", "projects/sdMaterialTool.html", "Substance Designer plugin"),
    ("Real-time materials & shaders in a PBR workflow", "Automated Albedo/Normal/Roughness/Metallic/Height generation, a shared shader library, a UE material-instance library, and a translucent Shader Graph bubble", "projects/bubbleFactory.html#materials", "Bubble Factory · Materials"),
    ("Writing &amp; debugging shader code", "Four hand-written GLSL fragment shaders running live in the browser: fBm volumetric fog, a Cook-Torrance GGX sphere, a water surface and thin-film refraction", "shaders.html", "Shader Lab"),
    ("Performance, validation & optimization", "Cross-platform shader validation benchmarks at Tencent. Lighting and render optimization with a smaller build in Rhythm", "projects/rhythmEcho.html#challenges", "Rhythm · Optimization"),
    ("Procedural systems", "Blueprint-driven PCG generators for cliffs, rock groups and light-aware moss", "projects/theFeeding.html#environment", "The Feeding · PCG"),
    ("Lighting & look-dev", "Night, fog and firelight lighting across 8 scenes. Skybox and atmosphere across realms", "projects/theFeeding.html#renders", "The Feeding · Renders"),
    ("Unreal Engine workflows", "Blueprints, material networks, PCG, Sequencer, Movie Render Queue, MetaHuman", "projects/theFeeding.html", "The Feeding"),
    ("ML / AI in art pipelines", "ComfyUI workflows, model evaluation, LoRA look-dev, multimodal 3D AI evaluation, local ONNX inference", "#professional", "Professional work"),
    ("Supporting artists & external vendors", "Shader standards for vendor asset production. Silent hotfix and forced-update deployment for a large art team", "projects/psAiToolkit.html#deployment", "Photoshop toolkit · Deployment"),
    ("Technical documentation", "Architecture, interface and request-sequence diagrams for production tools", "projects/sdMaterialTool.html#architecture", "Substance Designer plugin · Architecture"),
    ("Collaboration across art, design & engineering", "PM for TA/VFX pipelines on a AAA title. Producer and developer on two multidisciplinary teams", "projects/puppetMystery.html", "Puppet Mystery"),
    ("Scripting in C# and engine code", "Additive scene loading, EventSystem drag-and-drop puzzles, recipe validation and branching endings", "projects/puppetMystery.html#code", "Puppet Mystery · Code"),
    ("Version control", "Git (this site) and Perforce (current USC team project in Unreal)", None, None),
]


def skills():
    hard = ""
    for cls, ico, title, tags, proof in SKILLS:
        t = "".join(f'<span class="tag">{x}</span>' for x in tags)
        hard += f"""
      <div class="skill-card {cls}">
        <div class="ico"><i class="{ico}"></i></div>
        <h4>{title}</h4>
        <div class="tags">{t}</div>
        <p class="proof"><i class="fa-solid fa-check" style="color:var(--accent);margin-right:6px"></i>{proof}</p>
      </div>"""
    soft = "".join(f"""
      <div class="skill-card"><div class="ico"><i class="{i}"></i></div><h4>{a}</h4><p style="font-size:14px;margin:0">{b}</p></div>""" for i, a, b in SOFT)
    rows = ""
    for r, e, h, l in MATRIX:
        cell = f'<a href="{h}">{l} →</a>' if h else '<span class="muted">·</span>'
        rows += f'<tr><th scope="row">{r}</th><td>{e}</td><td>{cell}</td></tr>'
    return f"""
<section id="skills">
  <div class="wrap">
    <div class="section-head">
      <div>
        <div class="eyebrow">What I bring</div>
        <h2>Core skills</h2>
      </div>
      <p>A technical artist sits between art, engineering and production. Hard skills, soft skills, and a quick map from what studios ask for to where you can see it in my work.</p>
    </div>
    <div class="tabs skills-tabs" role="tablist" data-tabs="skills">
      <button class="tab active" role="tab" aria-selected="true"><small>A</small>Hard skills · technical &amp; art</button>
      <button class="tab" role="tab" aria-selected="false"><small>B</small>Soft skills · communication &amp; production</button>
      <button class="tab" role="tab" aria-selected="false"><small>C</small>Requirement → evidence</button>
    </div>
    <div class="skill-panel active" data-panel-of="skills"><div class="skills-grid">{hard}
    </div></div>
    <div class="skill-panel" data-panel-of="skills"><div class="skills-grid">{soft}
    </div></div>
    <div class="skill-panel" data-panel-of="skills">
      <div class="matrix-wrap"><table class="matrix">
        <thead><tr><th>Typical technical-art requirement</th><th>Where I've done it</th><th>See it</th></tr></thead>
        <tbody>{rows}</tbody>
      </table></div>
    </div>
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
        <h2>An artist's eye, an engineer's toolbox, a producer's instincts.</h2>
        <p>I'm Yolanda (Liu Xingyan), an MFA student in Interactive Media &amp; Games at USC. I came to games through communications and new media at NUS, and found my place where art and technology meet: building the pipelines, shaders and tools that turn a team's creative intent into something that runs in real time.</p>
        <p>A lot of my work draws on Chinese mythology and cultural heritage, like Miao Gu sorcery, Meng Po's tea of forgetting and ethnic-minority music. Outside the engine, three other crafts feed straight back into how I work as a TA:</p>

        <details class="acc">
          <summary><span class="ico"><i class="fa-solid fa-shirt"></i></span><div><b>Costume &amp; makeup design</b><span class="s">→ character readability, palette and visual systems</span></div></summary>
          <div class="acc-body">
            <p>As Costume &amp; Makeup Head for <em>The Village</em>, I led 29 people to style 33 characters in one period look. As costume designer for <em>The Insanity</em>, I used silhouette and color to separate personalities that still read as one ensemble. It's the same problem as look-dev: keep one style while every asset stays readable.</p>
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
            <p>As assistant producer for <em>The Insanity</em>, I secured SGD 7,000 in sponsorship, managed the budget and coordinated timelines, resources and risk for a show seen by 600 people. Opening night doesn't move, which is good practice for milestones.</p>
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
