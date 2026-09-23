from blocks import set_slug, fig, gallery, split, video, steps, code_list, contrib, cs, stats, ul, note, tracks, sfx, code

CATNAME = {"pipeline": "Tools & AI Pipeline", "render": "Rendering & Shading", "gameplay": "Gameplay Systems", "beyond": "Beyond the Engine"}


# ------------------------------------------------------------------ SUBSTANCE DESIGNER PLUGIN
def sd_tool():
    set_slug("sdMaterialTool")
    S = []
    S.append(("overview", "Overview", f"""
<p class="lead">A production plugin for <strong>Adobe Substance 3D Designer</strong> that turns a text prompt into a seamless, tileable PBR material set without leaving the application. Artists stay in Designer; generation, tiling, map extraction, de-lighting, upscaling and library management all happen in one docked panel.</p>
<p>Before it existed, making a material from reference meant scanning or sourcing an image, cleaning it in Photoshop, hand-authoring PBR maps, repairing seams in a third tool, then re-importing. Each hand-off cost time and made material quality inconsistent between artists.</p>
{stats([("5", "PBR maps generated per material"), ("3+", "Foundation models routed"), ("1", "Panel, no tool switching"), ("Local", "ONNX normal-map inference")])}
{note("Built March – July 2026 at Tencent Games · TiMi J3 Studio · <em>Delta Force</em>. Confidential information has been excluded.")}
"""))
    S.append(("contributions", "My contributions", contrib([
        ("fa-brands fa-python", "Plugin development", "Built the panel in Python + PySide against the Substance Designer API, so results land directly as graphs and texture maps in the artist's project."),
        ("fa-solid fa-diagram-project", "Model-agnostic architecture", "Designed a client–server split where the plugin never talks to a model directly; a gateway owns keys, accounts and routing."),
        ("fa-solid fa-layer-group", "PBR & image processing", "Chained seamless tiling, PBR map extraction (including a local ONNX DeepBump model), de-lighting and upscaling into one pass."),
        ("fa-solid fa-flask", "Model research", "Evaluated which foundation models hold up at each stage of tiling-material production, then hid that choice behind one control set."),
        ("fa-solid fa-box-archive", "Material library", "Built create / version / natural-language search / reuse so generated materials become references for the next generation."),
    ])))
    S.append(("pipeline", "End-to-end pipeline", f"""
{fig("sd_hero.jpg", "<b>Output:</b> tileable PBR materials generated and processed inside Substance Designer (Base Color, Normal, Roughness, Height, Metallic).")}
{split(fig("sd_before.jpg", "<b>Before:</b> scan → manual cleanup → hand-made PBR maps → seam fixing → re-import, across multiple tools."), fig("sd_after.jpg", "<b>After:</b> the same brick material generated, tiled, mapped and previewed without leaving Designer."))}
{steps([
    "<b>Authenticate:</b> users sign in through a centralized API gateway that validates keys and manages access to AI services.",
    "<b>Material seeding:</b> generate several material concepts from a text prompt across different foundation models, with configurable resolution, aspect ratio and batch size.",
    "<b>Seamless tiling:</b> convert a generated texture into a tileable material with AI-assisted edge completion.",
    "<b>PBR map extraction:</b> produce Base Color, Roughness, Metallic, Normal and Height, with post-processing per map.",
    "<b>Optimization:</b> de-light and upscale, then save into the material library for reuse.",
])}
{gallery([("sd_step1_auth.jpg", "01 · Authentication"), ("sd_step2_seed.jpg", "02 · Material seeding"), ("sd_step3_tile.jpg", "03 · Seamless tiling"), ("sd_step4_pbr.jpg", "04 · PBR map extraction"), ("sd_step5_opt.jpg", "05 · Optimization")], cols=5, cls="contain", ar="1/2")}
{gallery([("sd_tile_ba.jpg", "Seamless tiling: before / after"), ("sd_delight_ba.jpg", "De-lighting & optimization: before / after")], cols=2, cls="contain", ar="16/10")}
{gallery([("sd_in_sd_1.jpg", "Plugin docked inside Substance Designer"), ("sd_in_sd_2.jpg", "Generation settings next to the material graph")], cols=2, ar="16/9")}
"""))
    S.append(("architecture", "System architecture", f"""
<p>The plugin uses a modular client–server design. It never calls a model endpoint itself: every request goes through a gateway that handles keys, accounts and routing. That keeps credentials out of the client, keeps orchestration in one place, and lets a new foundation model be added <strong>without touching the artist-facing UI</strong>.</p>
{fig("sd_architecture.jpg", "<b>Module map:</b> the plugin entry point reads config and prompts, calls <code>models/</code>, which routes through the AI gateway to the available image models, or runs DeepBump locally via ONNX.")}
{split('<h3>Unified client interface</h3><p>Every model client implements the same <code>generate_image()</code> signature – task type, prompt, negative prompt, reference images, aspect ratio, resolution, PBR target, output path – and returns the same result shape, with success and failure handled identically. Swapping or adding a provider is a new client class, not a UI change.</p>', fig("sd_interface.jpg", "Standardized request / response contract for all supported models."))}
{fig("sd_sequence.jpg", "<b>Request flow:</b> UI → QThread worker → model client (builds the final prompt) → gateway → model, returned as Base64. Async work keeps Designer's UI responsive.")}
"""))
    S.append(("challenges", "Challenges & solutions", cs([
        ("Fragmented material workflow",
         "Texture cleanup, PBR authoring, seam repair and generation each lived in a different tool, so iteration was slow and material quality drifted between artists.",
         "One workflow inside Designer",
         "Consolidated generation, tiling, PBR extraction, optimization and library management into a single docked panel, so the material never leaves the application it will be used in."),
        ("Seams at the tile boundary",
         "A generated texture is a picture, not a material: tiled across a surface it shows an obvious repeating seam.",
         "AI-assisted edge completion, then verify by tiling",
         "The tiling pass regenerates the wrap-around border, and the panel previews the result already tiled so the artist judges the material the way the engine will use it."),
        ("Many providers, many formats",
         "Each provider had a different request structure, output format and size limit.",
         "Unified interface behind a gateway",
         "A standard request/response contract plus provider-specific adapters. New models are added as a class, invisible to the artist."),
        ("Keeping the DCC responsive",
         "Remote generation takes seconds to minutes; a blocking call would freeze Designer.",
         "Asynchronous execution",
         "Requests run on QThread workers and return through signals, keeping interaction, request handling and inference separate."),
    ])))
    S.append(("takeaways", "What I learned", ul([
        "A material generator is only useful if its output survives contact with a real material graph. Judging every result tiled, lit and at map level mattered more than the prompt UI.",
        "Designing for replaceable models from day one paid off, because providers and model versions changed while the tool was in production.",
        "Running one model locally through ONNX (normal-map inference) was worth it: no round trip, no quota, and predictable results.",
    ])))
    return dict(
        slug="sdMaterialTool", title="Tiling Material Generator for Substance 3D Designer", cat="pipeline", catname=CATNAME["pipeline"],
        question="How do you get a seamless, production-ready PBR material set from a prompt without ever leaving Substance Designer?",
        tags=["Python", "PySide", "Substance Designer API", "PBR maps", "ONNX", "Seamless tiling"],
        hero_mode="inset",
        hero="sd_hero.jpg",
        facts=[("Role", "Technical Artist, Tools &amp; Pipeline"), ("Studio", "Tencent Games · TiMi J3 · <em>Delta Force</em>"), ("Year", "2026"), ("Stack", "Python, PySide, Substance Designer API, ONNX"), ("Users", "Production art team")],
        links=[],
        ta=["Shipped a production DCC plugin in Python/PySide for Substance Designer",
            "Automated tileable PBR map generation (Base Color, Normal, Roughness, Height, Metallic)",
            "Designed a gateway-based, model-agnostic architecture",
            "Ran local ONNX inference for normal-map extraction",
            "Built a searchable, versioned material library"],
        sections=S)


# ------------------------------------------------------------------ PHOTOSHOP PLUGIN
def ps_tool():
    set_slug("psAiToolkit")
    S = []
    S.append(("overview", "Overview", f"""
<p class="lead">A <strong>Photoshop</strong> extension that turns the application into a unified AI-assisted concept environment: generation, instruction-based editing, inpainting, canvas expansion, segmentation, upscaling and image analysis, all returning as ordinary editable layers.</p>
<p>Before it existed, artists bounced between Photoshop, web AI services and internal utilities, so nobody used the same model for the same job and every result had to be re-imported by hand. The extension standardizes AI use across the team and keeps the output non-destructive.</p>
{stats([("11", "AI features in one panel"), ("6+", "Providers & workflows routed"), ("2-level", "Update & hotfix system"), ("0", "Overwritten layers")])}
{note("Built March – July 2026 at Tencent Games · TiMi J3 Studio · <em>Delta Force</em>. Confidential information has been excluded.")}
"""))
    S.append(("contributions", "My contributions", contrib([
        ("fa-brands fa-js", "Plugin development", "Built the panel against the Photoshop UXP API so every result arrives positioned, scaled and named as a new layer."),
        ("fa-solid fa-route", "Task routing", "Split traffic between an internal corporate AI platform for general tasks and a studio-managed ComfyUI service for specialized ones such as background removal."),
        ("fa-solid fa-scissors", "Local Photoshop processing", "Kept masks, canvas prep, layer placement, compression and depth-based selection inside Photoshop wherever a round trip wasn't needed."),
        ("fa-solid fa-flask", "Model research & selection", "Evaluated models and ComfyUI workflows per feature, then wrapped them behind one consistent set of controls."),
        ("fa-solid fa-rotate", "Deployment", "Co-designed a centralized version system with silent JS hotfixes and mandatory installer updates for a large art team."),
    ])))
    S.append(("pipeline", "Technical pipeline", f"""
{fig("ps_hero.jpg", "The extension brings concept generation, intelligent editing, segmentation, expansion and analysis into one panel.")}
{gallery([("ps_traditional.jpg", "Traditional workflow: many external tools"), ("ps_new.jpg", "New workflow: one extension inside Photoshop")], cols=2, cls="contain", ar="3/1")}
<p>The plugin doesn't run models locally. It packages prompts, source images, masks, references and settings into standardized requests, routes them, then decodes the response, writes it to a temp file and imports it via the UXP API – <strong>always as a new layer</strong>, so artists keep working non-destructively.</p>
{fig("ps_pipeline.jpg", "Artist input → UXP plugin → request preparation (validation, compression, format conversion) → task router → AI platform or ComfyUI service → response parsing → editable Photoshop layers.")}
<ul>
  <li><strong>Unified model routing:</strong> multiple providers and API formats sit behind one interface, so models can be swapped without changing the artist workflow.</li>
  <li><strong>Provider-specific processing:</strong> the plugin absorbs each provider's request structure, output format, size limit and mask convention.</li>
  <li><strong>Non-destructive output:</strong> results are always new layers, never overwrites.</li>
  <li><strong>Local processing:</strong> masks, canvas prep, layer placement, compression and depth-based selection run inside Photoshop wherever possible.</li>
</ul>
"""))
    S.append(("features", "Core features", f"""
{gallery([
    ("ps_t2i.jpg", "Text to Image: concepts from natural-language prompts"),
    ("ps_i2i.jpg", "Image to Image: edit with language instructions"),
    ("ps_multiview.jpg", "Multi-view: new camera angle via a 3D camera controller"),
    ("ps_inpaint.jpg", "Local inpainting: regenerate only the selection"),
    ("ps_expand.jpg", "Intelligent canvas expansion: detects transparent areas"),
    ("ps_sky.jpg", "Sky generation: new sky and atmosphere, objects kept"),
    ("ps_extract.jpg", "Smart object extraction: isolated subject as a transparent layer"),
    ("ps_upscale.jpg", "Image upscaling"),
    ("ps_analysis.jpg", "Image analysis with a multimodal VLM"),
], cols=3, ar="16/10")}
{split('<h3>Layer decomposition</h3><p><strong>Semantic decomposition</strong> splits an image into layers. Artists describe each layer, or let the model propose object descriptions before extraction.</p><p><strong>Depth-based decomposition</strong> generates a grayscale depth map, then converts selected depth ranges into Photoshop layer masks <em>locally</em> via color-range selection, so artists can fine-tune thresholds themselves instead of re-running a model.</p>', gallery([("ps_semantic.jpg", "Semantic layer decomposition"), ("ps_depth_1.jpg", "Depth map → threshold"), ("ps_depth_2.jpg", "Mask refined with brush")], cols=1, cls="natural"))}
"""))
    S.append(("deployment", "Deployment & update management", f"""
{fig("ps_update.jpg", "Version check on Photoshop start: no update, silent JS hotfix (config, endpoints, prompt presets, workflow IDs, UI text), or mandatory installer update (manifest permissions, UXP behavior, packaged resources, backend-breaking changes).")}
<p>This turned distribution from a social problem (&ldquo;did you get the new link?&rdquo;) into a system guarantee: small fixes reach everyone without interrupting their work, and incompatible builds can't keep calling the backend.</p>
"""))
    S.append(("challenges", "Challenges & solutions", cs([
        ("AI output landed outside the artist's file",
         "Generating in a browser meant downloading, re-importing, scaling and positioning by hand, and losing the original in the process.",
         "Everything returns as a layer",
         "Results are decoded and imported through UXP already positioned, scaled and named, on top of the existing document. Nothing is ever overwritten."),
        ("Many providers, many conventions",
         "Each provider had a different request structure, output format, size restriction and mask convention.",
         "One router, provider-specific adapters",
         "General tasks go to the internal AI platform, specialized ones to a ComfyUI workflow service, and the plugin absorbs the differences so the artist sees one interface."),
        ("Not every step needs a model",
         "Round-tripping simple mask work to a server was slow and gave artists no control over the threshold.",
         "Keep local work local",
         "Depth thresholds, color-range selection, canvas prep and compression run inside Photoshop, so artists can refine a mask with a brush instead of re-prompting."),
        ("Getting every artist on the right version",
         "Updates shared through group chats meant nobody could confirm who had the latest build, so fixed bugs kept getting re-reported and versions drifted.",
         "Two-level update strategy",
         "On launch the plugin checks a central version config. <strong>Silent hotfixes</strong> download, syntax-validate and cache a new JS bundle for the next restart. <strong>Mandatory updates</strong> replace the UI with an update page when the installed version is below the minimum supported one."),
    ])))
    S.append(("takeaways", "What I learned", ul([
        "A TA tool succeeds when artists don't notice the plumbing. Most of the work was hiding model choice, formats and failure cases behind one familiar panel.",
        "Non-destructive output is what made artists adopt it. A tool that can lose your work doesn't get used twice.",
        "Deployment is part of the tool. Versioning and hotfixes mattered as much to adoption as any feature did.",
    ])))
    return dict(
        slug="psAiToolkit", title="AI Creative Toolkit for Photoshop", cat="pipeline", catname=CATNAME["pipeline"],
        question="How do you put eleven AI capabilities inside Photoshop without ever costing an artist a layer, and keep a large team on the same build?",
        tags=["Photoshop UXP API", "JavaScript", "ComfyUI", "Multimodal VLM", "Inpainting", "Depth masks"],
        hero_mode="inset",
        hero="ps_hero.jpg",
        facts=[("Role", "Technical Artist, Tools &amp; Pipeline"), ("Studio", "Tencent Games · TiMi J3 · <em>Delta Force</em>"), ("Year", "2026"), ("Stack", "UXP (JS), Python services, ComfyUI"), ("Users", "Production art team")],
        links=[],
        ta=["Shipped a production Photoshop extension on the UXP API",
            "Routed 6+ AI providers and ComfyUI workflows behind one interface",
            "Built non-destructive layer output and local depth-mask tooling",
            "Co-designed versioning with silent hotfixes for a large team"],
        sections=S)


# ------------------------------------------------------------------ THE FEEDING
def matlib(groups):
    out = '<div class="matlib reveal">'
    for g, mats in groups:
        cells = "".join(f'<figure><img src="../assets/img/theFeeding/{f}" alt="{n}" loading="lazy"><figcaption><b>{c}</b>{n}</figcaption></figure>' for c, n, f in mats)
        out += f'<div class="matgroup"><h4>{g}</h4><div class="matrow">{cells}</div></div>'
    return out + "</div>"


def feeding():
    set_slug("theFeeding")
    S = []
    S.append(("overview", "Overview", f"""
<p class="lead"><em>The Feeding</em> is a short film built in Unreal Engine 5.6 and inspired by the mythology of China's Miao people. A priestess deep in the mountains spreads rumors of a forbidden ritual that can bring the dead back to life, luring curious young people up the mountain only to sacrifice them to feed her parasitic spirit insects (Gu).</p>
<p>I built it solo: Gaea terrain, Blueprint-driven PCG cliffs and moss, a 16-material library, modular environment pieces, MetaHuman characters with retargeted animation, Marvelous Designer cloth, lighting, and a Sequencer cinematic rendered through Movie Render Queue. The film is pre-production for a future narrative horror game, where players explore the mountain and gather evidence of the priestess's scheme.</p>
{video("_LaT0FU4JkQ", "The Feeding · short film")}
"""))
    S.append(("contributions", "My contributions", contrib([
        ("fa-solid fa-palette", "Material library (M1–M16)", "16 materials across terrain, foliage, water, architecture and props, built as instances of a few master materials so every scene could be relit fast."),
        ("fa-solid fa-lightbulb", "Lighting & rendering", "Fog, moonlight, candle and firelight across 8 scene captures, delivered as a Movie Render Queue cinematic."),
        ("fa-solid fa-cubes", "Procedural content (PCG)", "Two PCG graphs: PCG_Cliff to build cliff shapes from rock meshes via Blueprints, and a Moss generator that grows along a light direction."),
        ("fa-solid fa-mountain", "Terrain", "Mountains modelled and textured in Gaea, then exported to Unreal as the base for PCG dressing."),
        ("fa-solid fa-user", "Characters", "A MetaHuman priestess (built from Grace's DNA), villagers, Mixamo → MetaHuman retargeting and Live Link facial capture."),
        ("fa-solid fa-shirt", "Cloth simulation", "Cloaks patterned and simulated in Marvelous Designer, re-simulated to fix hand clipping, and imported as Alembic caches."),
    ])))
    S.append(("renders", "Final renders", f"""
{fig("r1_mountain.jpg", "<b>Scene capture 1:</b> Mountain & god statue. A crane-up reveals the scale of the range, with red firelight igniting below.")}
{gallery([("r2_cliffs.jpg", "Scene capture 2: cliffs at dusk"), ("r3_statue.jpg", "Scene capture 3: the god statue lit by candlelight"), ("r4_priestess.jpg", "Scene capture 4: the priestess (MetaHuman)"), ("r4_temple.jpg", "Scene capture 4: abandoned temple interior")], cols=2, ar="16/8")}
{gallery([("r5_town.jpg", "Scene capture 5: the town before it burned"), ("r6_fire.jpg", "Scene capture 6: the town after it burned")], cols=2, ar="16/8")}
{gallery([("r7_hooded.jpg", "Scene capture 7: the young man in the forest"), ("r8_forest.jpg", "Scene capture 8: firelight in the forest"), ("r8_fire.jpg", "Scene capture 8: the ritual fire")], cols=3, ar="16/9")}
"""))
    S.append(("materials", "Material library", f"""
<p>The film's mood depends on surfaces reading correctly in fog, moonlight and firelight. I built <strong>16 materials in five families</strong> as instances of a few master materials. Each family exposes the same parameters (tint, roughness range, normal strength, tiling, macro variation), so relighting a scene meant adjusting parameters, not rebuilding shaders.</p>
{matlib([
    ("Mountains", [("M1", "Grass", "m01_grass.png"), ("M2", "Grass with Rocks", "m02_grass_rocks.png"), ("M3", "Surface Rocks", "m03_surface_rocks.png"), ("M4", "Rocks", "m04_rocks.png")]),
    ("Plants & Trees", [("M5", "Tree Leaves", "m05_tree_leaves.png"), ("M6", "Tree Wood", "m06_tree_wood.png")]),
    ("Water", [("M7", "Water Instance 1", "m07_water1.png"), ("M8", "Water Instance 2", "m08_water2.png")]),
    ("Architecture", [("M9", "Pillar", "m09_pillar.png"), ("M10", "Roof", "m10_roof.png"), ("M11", "House Attic", "m11_attic.png"), ("M12", "Pedestal", "m12_pedestal.png")]),
    ("Decoration", [("M13", "Wood Instance 1", "m13_wood1.png"), ("M14", "Wood Instance 2", "m14_wood2.png"), ("M15", "Book", "m15_book.png"), ("M16", "Lantern", "m16_lantern.png")]),
])}
<h3>How each family is built in UE 5.6</h3>
{cs([
    ("Mountains · M1–M4", "Landscape material using <strong>Landscape Layer Blend</strong> (Grass, Grass with Rocks, Surface Rocks, Rocks). A <strong>slope mask</strong> from the world-space normal pushes rock onto steep faces, and <strong>height-lerp</strong> blends grass into rock cracks instead of fading it.",
     "Why it works", "Rock meshes and cliffs use a <strong>world-aligned (triplanar)</strong> version, so stretched UVs on vertical faces don't smear. Distance-based tiling hides repetition in wide shots."),
    ("Plants & Trees · M5–M6", "Leaves use the <strong>Two-Sided Foliage</strong> shading model with a masked opacity cut-out and a <strong>subsurface colour</strong>, so leaves glow when backlit by fire. Wind comes from world-position offset. Bark is an opaque tiling material with normal and AO.",
     "Why it works", "Subsurface foliage is what makes the forest firelight in scene 8 feel warm rather than flat."),
    ("Water · M7–M8", "UE5 <strong>Single Layer Water</strong> shading with two <strong>panning normal maps</strong> at different scales and speeds. Absorption and scattering colours set the look: murky jade green (M7) and dark, mirror-like ink (M8) for night.",
     "Why it works", "One master, two instances. Only colour, roughness and ripple speed change between the day town and the night river."),
    ("Architecture · M9–M12", "Stone pillar, roof tile, lacquered attic wood and a weathered pedestal. A <strong>top-down world-normal mask</strong> adds dirt and moss on upward faces, and a height-lerp mask chips red lacquer to reveal wood underneath (M11).",
     "Why it works", "Ageing is procedural, so every modular piece gets unique wear without new textures, which suits an abandoned temple and a burned town."),
    ("Decoration · M13–M16", "Two wood instances (red-brown and dark) from one wood master, aged paper for the book, and a <strong>paper lantern</strong> with a calligraphy texture, two-sided subsurface and an <strong>emissive parameter</strong> with a gentle flicker, paired with a point light.",
     "Why it works", "The lantern's emissive plus its real light source makes candlelit scenes read correctly both in camera and in reflections."),
], labels=("Family", "Result"))}
<h3>Look-dev process</h3>
{steps([
    "<b>Neutral check:</b> validate every instance on a sphere under neutral lighting first, so albedo and roughness values stay physically plausible.",
    "<b>In-context check:</b> re-check the same materials under fog, moonlight and firelight in the actual shot, and only tweak exposed parameters.",
    "<b>Lock exposure:</b> fix camera exposure per sequence so material changes, not auto-exposure, drive how scenes look.",
])}
"""))
    S.append(("environment", "Terrain & PCG", f"""
<h3>Terrain in Gaea</h3>
<p>The mountains were modelled node-by-node in Gaea (erosion, flow and height passes), then textured and exported to Unreal as the macro form of the karst ranges of western Hunan.</p>
{gallery([("gaea_1.jpg", "Gaea node graph · pass 1"), ("gaea_2.jpg", "Gaea node graph · pass 2"), ("gaea_3.jpg", "Gaea node graph · pass 3"), ("gaea_4.jpg", "Gaea node graph · pass 4")], cols=4, ar="16/10")}
{gallery([("ter_mesh.jpg", "Mountain mesh"), ("tex_mtn_4.jpg", "Mountain mesh, alternate"), ("ter_gaea.jpg", "Textured mountain"), ("tex_mtn_1.jpg", "Textured terrain"), ("tex_mtn_2.jpg", "Textured rock mass"), ("tex_mtn_3.jpg", "Textured cliff")], cols=3, cls="contain", ar="16/10")}
<h3>PCG_Cliff: building cliffs from rock meshes</h3>
{steps(["<b>Step 1:</b> find suitable rock static meshes.", "<b>Step 2:</b> assemble the static meshes into PCG assets.", "<b>Step 3:</b> call the PCG assets from Blueprints to form different cliff shapes.", "<b>Step 4:</b> manually adjust parameters to reshape each cliff."])}
{gallery([("pcg_rocks.jpg", "Step 1 · source rock meshes"), ("pcg_cliff.jpg", "Step 2 · static meshes assembled into PCG assets"), ("pcg_1.jpg", "Step 3 · Blueprint-called PCG cliff shape"), ("pcg_3.jpg", "Step 4 · adjusting parameters")], cols=2, ar="16/9")}
<h3>Moss: growing vegetation along a light direction</h3>
{steps(["<b>Step 1:</b> find suitable small rock and plant meshes.", "<b>Step 2:</b> assemble them as a level instance.", "<b>Step 3:</b> test the effect on a simple shape.", "<b>Step 4:</b> test on the mountain model.", "<b>Step 5:</b> add various sampling models for variety.", "<b>Step 6:</b> set a light direction so moss grows where plants realistically would."])}
{gallery([("pcg_rocks2.jpg", "Step 1 · small meshes"), ("mat_leaves.jpg", "Step 2 · assembled as a level instance"), ("pcg_moss_test.jpg", "Step 3 · effect test"), ("pcg_moss.jpg", "Step 4 · on the mountain model"), ("pcg_sampling.jpg", "Step 5 · sampling models"), ("pcg_2.jpg", "Step 6 · light direction")], cols=3, cls="contain", ar="16/10")}
{gallery([("pcg_graph.jpg", "PCG_Cliff graph"), ("pcg_graph2.jpg", "Moss graph")], cols=2, ar="16/7")}
{gallery([("pcg_mtn2.jpg", "Rock groups generated in the defined area"), ("pcg_mtn.jpg", "Moss generator added above the rock groups")], cols=2, ar="16/8")}
"""))
    mods = [f"mod_{i:02d}.jpg" for i in range(25) if i not in (1, 14, 23)]
    S.append(("modelling", "Modelling", f"""
<h3>Character · villagers</h3>
{gallery([(f"villager_{i}.jpg", "") for i in range(7)], cols=7, cls="contain", ar="1/2")}
<h3>Modular components</h3>
<p>A kit of props and architectural pieces (stone tablets, railings, lattice windows, gates, a pavilion roof, braziers, fish carvings, dead trees and branches) used to dress the temple, the town and the mountain path.</p>
{gallery([(m, "") for m in mods] + [("mdl_wall.jpg", "")], cols=6, cls="contain", ar="1/1")}
"""))
    S.append(("characters", "Characters & cinematics", f"""
{split('<h3>MetaHuman priestess</h3><p>I enabled the MetaHuman plugins in UE 5.6 and created the character in the integrated MetaHuman editor. I started from <strong>Grace’s MetaHuman DNA</strong>, blended body presets for an elderly frame with a slight stoop, and focused facial detail on the eyes, mouth corners and nasolabial folds, with skin matched to an older Asian woman. I then exported her as a combined skeletal mesh.</p>', fig("mh_face.jpg", "MetaHuman priestess, face detail pass"))}
{gallery([("mh_base.jpg", "Create character: adjust MetaHuman parameters"), ("mh_body.jpg", "Body blend & proportions"), ("livelink.jpg", "Live Link facial capture")], cols=3, ar="4/3")}
<h3>Mixamo → MetaHuman retargeting</h3>
{gallery([("mh_mixamo.jpg", "Mixamo re-animation"), ("mh_retarget.jpg", "Retarget Manager: rebinding animation to MetaHuman")], cols=2, ar="16/8")}
<h3>Cloth simulation (Marvelous Designer)</h3>
{gallery([("cl_split.jpg", "Create 2D pattern & split lines"), ("cl_md.jpg", "Fabric simulation"), ("cl_ui.jpg", "Simulation in Marvelous Designer")], cols=3, cls="contain", ar="4/3")}
<h3>Sequencer & Movie Render Queue</h3>
{split(steps(["<b>Foundation:</b> create a Level Sequence, enable the Cinematic toolbar, drag actors into tracks.", "<b>Animation & cameras:</b> time each character's animation. Build shots with Cine Camera Actors, tuning focal length and depth of field.", "<b>Polish:</b> spline-interpolate camera moves, sync audio with lip-sync, and export through Movie Render Queue."]), fig("seq.jpg", "Importing Alembic caches and keyframing CineCamera actors in Sequencer"))}
"""))
    S.append(("challenges", "Challenges & solutions", cs([
        ("One environment, very different moods",
         "The same town had to read as peaceful by day and as a burning ruin at night, and the temple had to hold up under a single candle.",
         "Master materials + parameter-only relighting",
         "All 16 materials are instances with shared parameters, so each lighting pass only meant retuning tint, roughness and emissive values."),
        ("Stretched textures on vertical cliffs",
         "Gaea mountains and PCG cliffs have steep faces where standard UVs smear.",
         "Slope masks + world-aligned texturing",
         "Rock goes onto steep faces by slope, and cliff meshes use world-aligned projection, so surfaces stay crisp from any angle."),
        ("Hand-placing a mountain range doesn't scale",
         "Dressing huge karst cliffs with rocks and moss by hand would take too long and look repetitive.",
         "Two PCG graphs",
         "PCG_Cliff builds cliff shapes from rock meshes via Blueprints, and the Moss graph grows vegetation along a light direction."),
        ("Retargeted animation distorted the MetaHuman",
         "Mixamo and MetaHuman skeletons have different root hierarchies and rest poses, so retargeted clips twisted the whole body.",
         "Manual root mapping + custom pose profile",
         "Mapped Mixamo's <code>Hips</code> to MetaHuman's <code>pelvis</code> in the Retarget Manager, and built a pose profile that matches the arms to the MetaHuman T-pose."),
        ("Cloak clipping through hands",
         "The first cloth simulation clipped through the hands during gestures.",
         "Resimulate",
         "Adjusted patterns and collision, re-simulated in Marvelous Designer, and imported the result as an Alembic cache matched to the animation."),
    ])))
    S.append(("research", "Research & pre-production", f"""
<p>I researched Miao culture (Gu sorcery, stilt-house architecture, silver ornaments and ritual), Chinese folk-horror games such as <em>Paper Dolls</em>, and audience data. A YouGov (2024) survey showed psychological and supernatural as top horror subgenres, and Steam's horror tags lean first-person and atmospheric. Both pointed to a first-person, atmosphere-first direction. Two player interviews confirmed it: limited light and environmental storytelling, not jump scares.</p>
{gallery([("ref_town.jpg", "Inspiration: river town in western Hunan"), ("ref_gu.jpg", "Gu creatures"), ("ref_miao_dress.jpg", "Miao traditional clothing"), ("ref_miao_silver.jpg", "Silver ornaments"), ("ref_ritual.jpg", "Traditional ritual"), ("ref_village.jpg", "Miao village"), ("ref_stilt.jpg", "Chinese architecture study"), ("ref_paperdolls.jpg", "<em>Paper Dolls</em> (game research)")], cols=4, ar="1/1")}
<h3>Storyboards</h3>
{gallery([("sb_1.jpg", "Scene 1 · Mountain & god statue"), ("sb_2.jpg", "Scene 2 · Town & memory transition"), ("sb_3.jpg", "Scene 3 · Temple & priest (night)")], cols=3, cls="contain", ar="4/3")}
"""))
    return dict(
        slug="theFeeding", title="The Feeding", cat="render", catname=CATNAME["render"],
        question="How did I build a fog-drenched Miao mountain world in UE 5.6, with a 16-material library, Gaea terrain, PCG cliffs and moss, MetaHumans, lighting and a Movie Render Queue cinematic?",
        tags=["Unreal Engine 5.6", "Material instances", "Landscape materials", "PCG", "Blueprints", "Lighting", "MetaHuman", "Gaea", "Marvelous Designer", "Sequencer / MRQ"],
        hero_mode="wide",
        hero="r1_mountain.jpg",
        facts=[("Role", "Solo: environment, TA, cinematics"), ("Type", "Short film / horror game pre-production"), ("Year", "2025"), ("Engine", "Unreal Engine 5.6"), ("Tools", "Gaea, Marvelous Designer, Mixamo, Blender, Audition, Premiere")],
        links=[("fa-brands fa-youtube", "Watch the film", "https://youtu.be/_LaT0FU4JkQ")],
        ta=["16-material library (M1–M16) built on shared master materials",
            "Landscape layer blend with slope masks and world-aligned cliffs",
            "Two-sided foliage, single-layer water and emissive lantern shading",
            "Two PCG graphs: Blueprint-driven cliffs and light-aware moss",
            "Fog, moonlight, candle and firelight across 8 scene captures",
            "MetaHuman + Mixamo retargeting + Marvelous Designer cloth"],
        sections=S)


# ------------------------------------------------------------------ RHYTHM
def rhythm():
    set_slug("rhythmEcho")
    S = []
    S.append(("overview", "Overview", f"""
<p class="lead"><em>Rhythm: Echo of the Disciple</em> is a first-person 3D rhythm and puzzle adventure made in two weeks for the <strong>Global Game Jam × WIPO "Next Great IP" Game Jam</strong>. You play the Silent One, the last echo of the World Tree Ruomu, travelling through nine forgotten realms to restore harmony after the Resonance Collapse silenced the world. You play sacred instruments to wake lost rhythms.</p>
<p>I was one of two producers, a developer and the team's technical artist: I built core rhythm and puzzle systems in Unreal Blueprints and owned lighting, skybox and rendering performance, all while coordinating nine people across design, programming, art, audio and publishing.</p>
{video("724kNPAQR84", "Rhythm: Echo of the Disciple · trailer")}
{gallery([("itch_1.jpg", "Instrument trial chamber"), ("itch_2.jpg", "The World Tree emblem at dusk"), ("itch_3.jpg", "Instrument altar: trial in progress")], cols=3, ar="16/9")}
"""))
    S.append(("contributions", "My contributions", contrib([
        ("fa-solid fa-lightbulb", "Lighting & skybox", "Lit the realms and built the skybox and atmosphere to carry each realm's mood from dusk-lit desert to glowing tree chamber."),
        ("fa-solid fa-gauge-high", "Rendering optimization", "Optimized lighting and rendering settings to improve visual quality while reducing build size for distribution."),
        ("fa-solid fa-music", "Rhythm & puzzle systems", "Developed core rhythm and puzzle gameplay in UE5 Blueprints, delivering a 20-minute playable demo."),
        ("fa-solid fa-people-group", "Production", "Co-produced a 9-person team across design, programming, art, audio, writing and publishing inside a two-week cycle."),
        ("fa-solid fa-book-open", "IP research", "Researched successful game IP and worldbuilding strategies and helped plan a long-term IP built on ethnic-minority music."),
    ])))
    S.append(("challenges", "Challenges & solutions", cs([
        ("Mood vs. performance on a jam timeline",
         "We wanted atmospheric, mythic realms, but heavy lighting and assets meant a large build and uneven performance for players downloading from itch.io.",
         "Targeted lighting & rendering optimization",
         "I focused on lighting, skybox and rendering settings. The pass improved visual quality while reducing the final build size."),
        ("Nine people, two weeks",
         "Design, programming, art, audio, writing and publishing all had to converge on one playable build.",
         "Producer-led scope and cadence",
         "Coordinated development across disciplines and kept scope anchored to a 20-minute demo so everything shipped inside the two-week cycle."),
    ])))
    S.append(("key-art", "Key art", f"""
{fig("orb.jpg", "The World Tree Ruomu emblem, the game's central motif, lit as a glowing relic.")}
<p>Full credits: Producers Yolanda Liu &amp; Kyrene Zhang · Developers Oley Zhou, Kyrene Zhang, Yolanda Liu · Audio Katria Qin · Writer Bill Dong · Artists Aldo Kai, Cecilia Han, Bi Hongying · Publishing Haley Wang.</p>
"""))
    return dict(
        slug="rhythmEcho", title="Rhythm: Echo of the Disciple", cat="render", catname=CATNAME["render"],
        question="How did I light and optimize a mythic 3D rhythm world in Unreal Engine while producing a 9-person team in two weeks?",
        tags=["Unreal Engine 5.6", "Lighting", "Skybox", "Rendering optimization", "Blueprints", "Production"],
        hero_mode="wide",
        hero="itch_2.jpg",
        facts=[("Role", "Producer · Developer · Technical Artist"), ("Team", "9 people"), ("Year", "2025"), ("Engine", "Unreal Engine 5.6, Blender"), ("Event", "Global Game Jam × WIPO")],
        links=[("fa-brands fa-itch-io", "Download on itch.io", "https://yollienarae.itch.io/rhythmechoofthedisciple"), ("fa-brands fa-youtube", "Trailer", "https://www.youtube.com/watch?v=724kNPAQR84")],
        ta=["Owned lighting, skybox and atmosphere across realms",
            "Rendering optimization: better visuals, smaller build",
            "Rhythm & puzzle systems in UE5 Blueprints",
            "Bridged art and engineering as producer on a 9-person team"],
        sections=S)


# ------------------------------------------------------------------ TRAVELTROVE
PLACES = [
    ("Paris", "the Eiffel Tower, a cafe chair, a wedge of brie"),
    ("Cairo", "the Great Pyramid, a scarab charm, a clay water jar"),
    ("Kyoto", "a torii gate, a paper lantern, a maple leaf"),
    ("Singapore", "the Merlion, a kopi tin, an orchid"),
    ("Honolulu", "a surfboard, a plumeria lei, a pineapple"),
]


def promptlab():
    """Interactive: shows that only the subject tokens move between assets."""
    btns = "".join(
        f'<button class="pl-place{" on" if i == 0 else ""}" data-place="{pl}" data-subj="{sub}">{pl}</button>'
        for i, (pl, sub) in enumerate(PLACES))
    first, firstsub = PLACES[0]
    return f"""
<div class="promptlab reveal">
  <div class="pl-head"><b>comfyui workflow · souvenir_set.json</b><span>pick a city</span></div>
  <div class="pl-places">{btns}</div>
  <div class="pl-body">
    <div class="pl-row pinned"><small>checkpoint</small><code>sd_xl_base_1.0.safetensors</code></div>
    <div class="pl-row pinned"><small>lora</small><code>cozy_isometric_v3.safetensors &nbsp;<i>weight 0.78</i></code></div>
    <div class="pl-row pinned"><small>ip-adapter</small><code>style_ref_shelf_01.png &nbsp;<i>weight 0.45</i></code></div>
    <div class="pl-row pinned"><small>controlnet</small><code>depth &nbsp;<i>silhouette_blockin.png · 0.6</i></code></div>
    <div class="pl-row pinned"><small>sampler</small><code>dpmpp_2m · karras · 28 steps · cfg 5.5</code></div>
    <div class="pl-row pinned"><small>seed</small><code>884213 + index</code></div>
    <div class="pl-row live"><small>prompt</small><code>low-poly 2D hand-drawn cartoon, warm palette, brown outlines, centred on white &ndash; <b class="pl-subj">{firstsub}</b> of <b class="pl-city">{first}</b></code></div>
  </div>
  <p class="pl-foot">Six of the seven lines never change. That is the whole trick: consistency comes from the pinned graph, not from how well the prompt was phrased that day.</p>
</div>"""


def traveltrove():
    set_slug("travelTrove")
    S = []
    S.append(("overview", "Overview", f"""
<p class="lead"><em>TravelTrove</em> is a gamified travel app that turns your trips into a cozy digital home. Exploring real cities earns e-souvenirs to decorate your virtual house, and an AI pet companion plans personalized itineraries, flags safety concerns and connects you with like-minded travelers.</p>
<p>It's a design and research project, but the technical-art story is how I used generative AI <strong>at the concept stage</strong>: I built a pinned ComfyUI workflow – style LoRA, style reference, framing control, fixed sampling – so dozens of independently generated souvenir assets read as one coherent art style, then built everything into a hi-fi Figma prototype.</p>
{fig("banner.jpg", "Final display: the virtual home is the main screen. Souvenirs collected from real trips decorate the room.")}
"""))
    S.append(("contributions", "My contributions", contrib([
        ("fa-solid fa-wand-magic-sparkles", "AI concept-asset pipeline", "Trained a style LoRA, pinned a ComfyUI graph around it, and batched a city\u2019s whole souvenir set through the API so the style held across every asset."),
        ("fa-solid fa-magnifying-glass-chart", "User & market research", "Six first-round interviews, market data on solo and AI-assisted travel, Maslow-based pain-point mapping and a SWOT."),
        ("fa-solid fa-pen-ruler", "UX & prototype", "Low-fi wireframes → prototype testing → hi-fi Figma prototype covering onboarding, home, AI planner, explore map and social features."),
        ("fa-solid fa-comments", "Testing & iteration", "Ran prototype tests with live walkthroughs and folded feedback into customization, privacy and safety features."),
    ])))
    S.append(("ai-pipeline", "AI concept-art pipeline", f"""
<p>The app needs a lot of collectible art: a souvenir for every landmark, in every city, all reading as one game. Hand-painting all of it for a concept wasn't realistic, and a raw text-to-image call drifts in style from run to run. I treated it the way I would treat any asset pipeline: <strong>lock everything except the subject</strong>, then batch it.</p>

<h3>The stack</h3>
{code_list([
    ("ComfyUI", "Node-graph runner, so the whole generation is a saved JSON workflow rather than a chat history. The graph is the thing under version control."),
    ("SDXL checkpoint", "Base model, fixed for the whole set. Changing checkpoints mid-project is the single fastest way to lose style consistency."),
    ("Style LoRA", "Trained in kohya_ss on ~40 curated reference frames in the cozy-isometric look I was targeting (<em>Animal Crossing</em>-style: flat warm palette, brown outlines, soft shading). Applied at a fixed weight – see the section below for how it was trained and tuned."),
    ("IP-Adapter", "A single style reference image on every run, so the LoRA has a second anchor and new subjects can't pull the palette around."),
    ("ControlNet (depth / lineart)", "Feeds a simple silhouette block-in, so each souvenir lands at the same scale, angle and framing instead of a random camera."),
    ("Fixed sampling", "Same sampler, steps, CFG and seed schedule across the batch. Only the subject token moves."),
    ("RMBG + Real-ESRGAN", "Background removal to transparent PNG, then upscale, so assets drop straight into the UI as sprites."),
])}

<h3>Training the style LoRA</h3>
<p>A LoRA is a small low-rank delta added to the base model's attention weights. That one fact decided almost every choice below: because it is a <em>delta</em>, it biases the model rather than filtering the output, and because it is <em>low-rank</em>, it has only so much capacity – which is a feature when what you want it to learn is a look and not a set of objects.</p>

{code_list([
    ("Dataset · ~40 frames", "Curated for style, not subject. I deliberately picked frames with <em>different</em> objects – furniture, exteriors, characters, props – so the network had nothing consistent to latch onto except the rendering. Anything with UI, text or a strong recognisable silhouette was cut."),
    ("Prep · 1024 buckets", "Cropped into SDXL's resolution buckets so nothing was squashed. Aspect distortion teaches the model the distortion."),
    ("Captions · describe the subject, never the style", "This is the part people get backwards. Whatever you caption becomes <em>variable</em>; whatever you leave out gets absorbed into the LoRA itself. So I captioned the contents (&ldquo;a wooden stool, a potted fern&rdquo;) and never wrote &ldquo;warm palette&rdquo; or &ldquo;brown outlines&rdquo; – those had to become the default, not a phrase I would need to remember to type."),
    ("Rank · dim 12 / alpha 6", "Deliberately small. Rank is capacity: a high-rank LoRA has enough room to memorise the training images, and then new subjects start coming out wearing shapes from the dataset. A style is a low-dimensional change, so it should get a low-dimensional adapter."),
    ("Learning rate · 1e-4 UNet, 4e-5 text encoder", "The text encoder is kept on a much shorter leash. Train it hard and the trigger token starts swallowing the whole prompt, so the model stops listening to the subject – exactly the failure I was trying to avoid."),
    ("Schedule · ~1600 steps, saved every epoch", "Batch 2, cosine decay, roughly 10 epochs over 40 images. I saved a checkpoint per epoch and chose between them by generating the same held-out subjects with each, not by looking at the loss curve. Loss going down and the LoRA being usable are different things."),
    ("No regularisation images", "Prior preservation exists to stop a concept bleeding into everything. For a style LoRA the bleed <em>is</em> the product, so it would have worked against me."),
])}

<h3>Reading what the LoRA was doing, and changing strategy</h3>
<p>Once you know it is a low-rank bias on attention, the failure modes stop being mysterious and start telling you which lever to pull. Two symptoms, two very different fixes:</p>
{code_list([
    ("Overfitting · new subjects inherit old shapes", "When a prompt for a souvenir came back looking like a piece of furniture from the training set, that is capacity being spent on memorisation. The fix is at <em>training</em> time – drop the rank, cut epochs, broaden the dataset – not at inference. Turning the weight down instead just gives you a washed-out version of the same wrong thing."),
    ("Underfitting · style drifts between runs", "Outlines thinning out, palette wandering. That is the opposite problem, and lowering the LoRA weight or leaning on style words in the prompt only papers over it. More epochs or a slightly higher rank is the real answer."),
    ("Weight · swept, not guessed", "I generated the same three subjects at 0.4 / 0.6 / 0.8 / 1.0 and read them as a set. Below about 0.6 the palette drifted; at 1.0 the model started ignoring the subject and reproducing composition from the dataset. 0.78 was where style held and prompts were still obeyed."),
    ("Composition · let each tool hold one thing", "Because a LoRA is additive, it stacks with other conditioning instead of competing with it. Rather than pushing the LoRA hard enough to hold palette <em>and</em> framing <em>and</em> colour key – which is how you end up overfitting – I let the LoRA own brushwork and outlines, IP-Adapter own the overall colour key, and ControlNet own scale and framing. Three light constraints at three different injection points beat one heavy one."),
    ("Checkpoint coupling", "The delta is trained against one specific base model, so it is only meaningful on that model. This is the real reason the checkpoint is pinned in the graph: changing it does not degrade the LoRA, it invalidates it."),
])}
{note("The most useful habit was judging every change against the same small set of held-out subjects that never appeared in training. A LoRA can look excellent on things it has seen and fall apart on the first new landmark, and a batch of souvenirs is nothing <em>but</em> new landmarks.")}

<h3>Lock the style, vary only the subject</h3>
<p>Once the graph was stable, the only thing that changed between assets was two tokens. Everything else – model, LoRA, weight, reference image, sampler, seed offset – stayed pinned, which is exactly the master-material-and-instances pattern from a real material library.</p>
{promptlab()}
{steps([
    "<b>Explore:</b> generate candidates for several landmarks off the base checkpoint and measure how far apart they drift on line weight, palette and rendering.",
    "<b>Train:</b> curate ~40 reference frames of the target look, caption only their contents, and train a low-rank style LoRA; pick the epoch by testing it on subjects that were <em>not</em> in the training set.",
    "<b>Pin the graph:</b> freeze checkpoint, LoRA weight, IP-Adapter reference, ControlNet preprocessor and sampler settings into one saved ComfyUI workflow.",
    "<b>Batch:</b> drive that workflow through the ComfyUI API from a list of places, swapping only the subject tokens, so a city's whole souvenir set comes out in one run.",
    "<b>Post:</b> background removal to transparent PNG, upscale, then drop into the Figma UI and judge the set together, not one image at a time.",
])}
{note("Judging generated assets <em>as a set</em> was the part that mattered. Any single souvenir looks fine; style drift only shows up when twelve of them sit on one shelf in the virtual room.")}
{gallery([("final_album.jpg", "Memory album: landmark souvenirs from the same pinned workflow"), ("final_explore.jpg", "Explore page: safety alerts, nearby spots, meet-ups")], cols=1, cls="natural")}
"""))
    S.append(("prototype", "Prototype", f"""
{gallery([("final_init.jpg", "Initialization: customize you & your pet"), ("final_ai.jpg", "AI recommendation: plan by chatting with your pet")], cols=2, cls="contain", ar="4/3")}
{fig("final_page.jpg", "Final display overview: UI system, rating system, invites and meet-ups.")}
{fig("lowfi.jpg", "Low-fidelity prototype across initialization, virtual house, safety community and UI system.")}
"""))
    S.append(("challenges", "Challenges & solutions", cs([
        ("AI assets didn't match each other",
         "Each generation came back with different line weights, palettes and rendering styles, so twelve souvenirs on one shelf didn't read as one game.",
         "Pin the graph, not the prompt",
         "A style LoRA plus a fixed IP-Adapter reference, ControlNet framing and sampler settings, saved as one ComfyUI workflow. Only the subject tokens vary, so consistency is a property of the pipeline rather than of how well I phrased a prompt that day."),
        ("Is it a game, a tool or a social app?",
         "The SWOT flagged an unclear genre fit and strong competitors: cozy games, travel planners and AI chatbots.",
         "Entertainment as the hook, utility as the value",
         "The cozy home and collection loop drives engagement. Planning, safety and community make it useful on a real trip."),
        ("Safety and privacy concerns",
         "Interviewees ranked safety first, but location and home visits raise privacy risks.",
         "Feedback-driven safety features",
         "Added real-time safety alerts, misconduct reporting, an emergency button, close-friend tiers and visit blocking after prototype testing."),
    ])))
    S.append(("research", "Research", f"""
{gallery([("research_page.jpg", "Inspiration, market research and interviews"), ("analysis_page.jpg", "Pain points mapped to Maslow's hierarchy"), ("competitive_page.jpg", "Competitive analysis & SWOT"), ("ideation.jpg", "Ideation: Game × AI Assistant × Social Media")], cols=2, ar="2/1")}
"""))
    return dict(
        slug="travelTrove", title="TravelTrove", cat="pipeline", catname=CATNAME["pipeline"],
        question="How did I set up a controlled AI generation workflow at the concept stage, so independently generated assets read as one coherent art style in a gamified travel app?",
        tags=["ComfyUI", "SDXL + LoRA", "IP-Adapter", "ControlNet", "Batch generation", "Figma"],
        hero_mode="full",
        hero="banner.jpg",
        facts=[("Role", "Solo: research, UX, concept pipeline"), ("Type", "Gamified travel app prototype"), ("Year", "2025"), ("Tools", "ComfyUI, SDXL + LoRA, ControlNet, Figma"), ("Research", "6 interviews + prototype tests")],
        links=[],
        ta=["Trained a style LoRA and pinned a ComfyUI workflow for consistent concept assets",
            "Used IP-Adapter and ControlNet to hold palette, scale and framing across a batch",
            "Drove batch generation through the ComfyUI API from a place list",
            "Automated background removal and upscale so output dropped straight into the UI"],
        sections=S)


# ------------------------------------------------------------------ RIVER OF FORGETTING
def river():
    set_slug("riverOfForgetting")
    S = []
    S.append(("overview", "Overview", f"""
<p class="lead"><em>River of Forgetting</em> (望乡渡) is a 3D first-person narrative game set in a mythic underworld. You're Meng Po's apprentice: she has vanished, leaving a handbook of herbs and recipes, and wandering souls arrive with their final requests. Listen, interpret, and brew the right medicine to guide each soul toward rebirth.</p>
<p>I built it solo in Unity: design, C# systems, and the environment and prop assets that set a moonlit, lantern-lit tone.</p>
{video("PhgodEf7-8c", "River of Forgetting · gameplay")}
"""))
    S.append(("contributions", "My contributions", contrib([
        ("fa-solid fa-code", "Gameplay systems (C#)", "Raycast interaction, NPC order queue, cauldron recipe validation, submission and game-progress scoring."),
        ("fa-solid fa-cube", "Environment & props", "Built the Naihe Bridge scene, boat, furniture, herb boxes and a red spirit tree to set the underworld mood."),
        ("fa-solid fa-lightbulb", "Lighting & mood", "Moonlit night scene with floating lanterns and emissive herbs for readability in the dark."),
        ("fa-solid fa-book", "Narrative & design", "Five NPC stories (burnout, academic pressure, cyberbullying, medical injustice, family conflict) and two endings."),
    ])))
    S.append(("world", "World & assets", f"""
{fig("bridge.jpg", "Naihe Bridge at night: floating lanterns and a red spirit tree frame the crossing souls must make.")}
{gallery([("scene_night.jpg", "Brewing courtyard"), ("herb_boxes.jpg", "Herb boxes, emissive so they read in the dark"), ("handbook.jpg", "Meng Po's handbook: recipes and lore")], cols=3, ar="16/10")}
<h3>General decorations to set the tone</h3>
{gallery([("mdl_table.jpg", "Altar table set, clay"), ("mdl_table2.jpg", "Altar table set, textured"), ("mdl_boat_clay.jpg", "Ferry boat, clay"), ("mdl_boat.jpg", "Ferry boat, textured"), ("mdl_stilt.jpg", "Pavilion house")], cols=5, cls="contain", ar="1/1")}
{gallery([("mat_tree.jpg", "Large · red spirit tree"), ("mdl_bridge.jpg", "Large · Naihe bridge"), ("mdl_temple.jpg", "Large · temple hall")], cols=3, cls="contain", ar="4/3")}
<h3>Herbs: the main objects players interact with</h3>
{gallery([(f"herb_{i:02d}.jpg", "") for i in range(15)], cols=5, cls="contain", ar="1/1")}
"""))
    S.append(("systems", "Systems & code", f"""
<p>The core loop is <strong>listen → interpret → brew → serve</strong>. Each herb has unique effects, so players consult the handbook to match a soul's need to the right combination.</p>
{code_list([
    ("Interact.cs", "Casts a ray from the camera to highlight items under the cursor. On click, disables physics and attaches the item to the player's hand."),
    ("OrderManager.cs", "Activates NPC orders one at a time after a delay, triggering dialogue plus visual and audio cues when a new order starts."),
    ("Cauldron.cs", "Collects ingredients and checks them against recipes. A match spawns a potion with effects. A miss plays a failure sound and shows a hint."),
    ("Submit.cs", "Detects a potion entering the serving zone, submits its ingredients to the current NPC for validation, then destroys it."),
    ("GameProgressManager.cs", "Tracks each NPC's result. Once all are served it computes accuracy (≥ 60%, 3 of 5) and loads the Peaceful Passage or Lingering Regrets ending."),
])}
{gallery([("end_2.jpg", "Ending 1: The Bridge of No Regrets"), ("end_1.jpg", "Ending 2: Memories Left Behind")], cols=2, cls="contain", ar="16/9")}
"""))
    S.append(("challenges", "Challenges & solutions", cs([
        ("Readable interaction in a dark scene",
         "The underworld mood needed low light, but players still had to find and grab small herbs.",
         "Highlight on hover + emissive herbs",
         "Interact.cs highlights anything under the cursor, and herb boxes glow so ingredients read against the night palette."),
        ("Branching outcomes without complex state",
         "Each soul's result needed to feed a meaningful ending without a tangle of flags.",
         "Central progress manager",
         "Each submission records correct or incorrect. One manager computes accuracy after the last NPC and picks the ending."),
    ])))
    S.append(("inspiration", "Inspiration", f"""
<p>Structure from <em>Good Coffee, Great Coffee</em> (request → prepare → serve). Crafting from <em>Potion Craft</em> and <em>Wytchwood</em>. Emotional NPCs from <em>Spiritfarer</em>. Serving-while-listening from <em>VA-11 Hall-A</em>. Mood from <em>The Midnight Walk</em>.</p>
{gallery([("ref_spiritfarer.jpg", "<em>Spiritfarer</em>"), ("ref_coffee.jpg", "<em>Good Coffee, Great Coffee</em>"), ("ref_va11.jpg", "<em>VA-11 Hall-A</em>"), ("ref_midnight.jpg", "<em>The Midnight Walk</em>")], cols=4, ar="16/10")}
"""))
    return dict(
        slug="riverOfForgetting", title="River of Forgetting", cat="gameplay", catname=CATNAME["gameplay"],
        question="How did I build a brewing system and accuracy-based endings for a first-person mythic narrative game, and light it so it still reads in the dark?",
        tags=["Unity", "C#", "3D", "Interaction systems", "Environment art"],
        hero_mode="full",
        hero="bridge.jpg",
        facts=[("Role", "Solo developer & artist"), ("Genre", "First-person narrative / crafting"), ("Year", "2025"), ("Engine", "Unity (C#)"), ("Platform", "Windows")],
        links=[("fa-brands fa-itch-io", "Play on itch.io", "https://yollienarae.itch.io/river-of-forgetting"), ("fa-brands fa-youtube", "Gameplay video", "https://youtu.be/PhgodEf7-8c")],
        ta=["Raycast interaction with hover highlighting",
            "Recipe validation & scoring systems in C#",
            "Moonlit scene lighting with emissive gameplay cues",
            "Modelled and textured props, boat and bridge"],
        sections=S)


# ------------------------------------------------------------------ BROKEN STAGE
def broken():
    set_slug("brokenStage")
    S = []
    S.append(("overview", "Overview", f"""
<p class="lead"><em>Broken Stage</em> (무너진 무대) is a 2D bilingual (English/Korean) mystery game set in K-pop journalism. As a reporter reopening a buried scandal, you infiltrate an entertainment company, solve room-by-room puzzles and decide whether to publish. Your identity changes the outcome.</p>
<p>I designed and built it solo in Unity: interaction and puzzle systems, the password and ending logic, level flow across five floors, and the UI.</p>
{video("TK18FpEI-G8", "Broken Stage · gameplay")}
{gallery([("s_office.jpg", "Office floor"), ("s_desk.jpg", "Investigating a desk"), ("s_meeting.jpg", "Meeting room"), ("s_lockers.jpg", "Locker puzzle"), ("s_keypad.jpg", "Keypad-locked cabinet"), ("s_books.jpg", "Book-ordering puzzle")], cols=3, ar="16/9")}
"""))
    S.append(("contributions", "My contributions", contrib([
        ("fa-solid fa-code", "Puzzle & interaction systems", "Click-to-inspect, drag-and-drop book ordering, two password input systems, and hidden-item reveals."),
        ("fa-solid fa-code-branch", "Branching endings", "An ending manager that tracks player actions (e.g., emails translated) to choose between two endings."),
        ("fa-solid fa-sitemap", "Level flow", "Flowcharts for five levels mapping clues, locks and dependencies before building."),
        ("fa-solid fa-language", "Bilingual UI", "Mixed English/Korean chats, emails and notes that immerse players in the Korean workplace."),
    ])))
    S.append(("systems", "Systems & code", f"""
{code_list([
    ("Click", "Clicking an object shows detailed information or visuals on a canvas so players can examine clues."),
    ("BookOrdering", "Drag-and-drop books into a sequence. The correct order unlocks a hidden shelf compartment."),
    ("PasswordPanel (buttons)", "Players enter a code by clicking on-screen buttons."),
    ("PasswordPanel (keyboard)", "Players type the password directly with the keyboard."),
    ("GameManager", "Chains all scenes in build order and runs the main menu (Start / Quit)."),
    ("EndingManager", "Tracks actions such as translated emails and branches into one of two endings."),
])}
{gallery([("code_password.jpg", "PasswordPanel.cs"), ("code_ending.jpg", "EndingManager.cs"), ("code_game.jpg", "GameManager.cs")], cols=3, cls="contain", ar="3/4")}
<h3>Level flowcharts</h3>
{gallery([("flow_1.jpg", "Level 1"), ("flow_2.jpg", "Level 2"), ("flow_3.jpg", "Level 3"), ("flow_4.jpg", "Level 4"), ("flow_5.jpg", "Level 5")], cols=3, cls="contain", ar="4/3")}
"""))
    S.append(("challenges", "Challenges & solutions", cs([
        ("Replayable puzzles with varied input",
         "Research on replayable escape rooms showed variety keeps players engaged, but each new input type risked one-off code.",
         "Reusable input components",
         "Built button-based and keyboard-based password panels plus a generic click-to-inspect system, reused across rooms."),
        ("Endings that reflect player choices",
         "The story's message depends on the reporter's identity and actions, not a single final choice.",
         "Action-tracking ending manager",
         "Tracked specific in-game actions and branched to <em>Being Fired</em> or <em>Gain Impacts</em> accordingly."),
    ])))
    S.append(("research", "Research", f"""
<p>The story was informed by real K-pop industry cases, including the Burning Sun scandal and the Jang Ja-yeon and Goo Hara cases. It aims to spark conversation about power, exploitation and the media's role, using approachable puzzles so players uncover the truth by interacting with it rather than watching it.</p>
{gallery([("s_room.jpg", "CEO office"), ("s_email.jpg", "Bilingual email clue"), ("s_laptop.jpg", "Laptop password lock"), ("asset_keys.jpg", "Hand-drawn item assets")], cols=4, ar="16/10")}
"""))
    return dict(
        slug="brokenStage", title="Broken Stage", cat="gameplay", catname=CATNAME["gameplay"],
        question="How did I build reusable interaction, puzzle and branching-ending systems for a bilingual 2D mystery game?",
        tags=["Unity", "C#", "2D", "Puzzle systems", "UI", "Bilingual"],
        hero_mode="full",
        hero="banner.jpg",
        facts=[("Role", "Solo developer & designer"), ("Genre", "2D mystery / escape room"), ("Year", "2024"), ("Engine", "Unity (C#)"), ("Platform", "macOS")],
        links=[("fa-brands fa-itch-io", "Play on itch.io", "https://yollienarae.itch.io/broken-stage"), ("fa-brands fa-youtube", "Gameplay video", "https://youtu.be/TK18FpEI-G8")],
        ta=["Reusable click, drag-and-drop and password components",
            "Action-tracking branching ending system",
            "Five-level flow design before implementation",
            "Bilingual UI for cultural immersion"],
        sections=S)


# ------------------------------------------------------------------ PUPPET MYSTERY
GM_SRC = """public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }
    public GameObject phoneUI;            // cross-scene UI (detective phone)
    public GameObject transitionCamera;   // buffer camera shown while a room loads
    public Dictionary<string, object> savedStates = new();

    void Awake()
    {
        if (Instance != null) { Destroy(gameObject); return; }
        Instance = this;
        DontDestroyOnLoad(gameObject);
        DontDestroyOnLoad(phoneUI);
        DontDestroyOnLoad(transitionCamera);
    }

    public void EnterRoom(string roomScene)
    {
        HideRootObjects(mainMapScene);                     // park the map, don't unload it
        Scene existing = SceneManager.GetSceneByName(roomScene);
        if (existing.IsValid() && existing.isLoaded)       // room visited before?
        {
            ShowRootObjects(existing);                     // restore it exactly as the player left it
            EnableRoomCamera(roomScene);
            return;
        }
        StartCoroutine(LoadRoomSceneAsync(roomScene));     // first visit: load additively
    }

    IEnumerator LoadRoomSceneAsync(string scene)
    {
        ShowTransitionCamera(); phoneUI.SetActive(false);
        var load = SceneManager.LoadSceneAsync(scene, LoadSceneMode.Additive);
        while (!load.isDone) yield return null;
        EnableRoomCamera(scene); EnableSceneEventSystem(scene);
        HideTransitionCamera(); phoneUI.SetActive(true);
    }

    public void ExitRoom()   // hide, don't unload: puzzle state survives
    {
        foreach (var go in SceneManager.GetSceneByName(currentRoomScene).GetRootGameObjects())
            go.SetActive(false);
        ShowRootObjects(mainMapScene);
    }
}"""

WINE_SRC = """public class WineDraggableItem : MonoBehaviour, IBeginDragHandler, IDragHandler, IEndDragHandler
{
    public Transform targetSlot;
    public float snapDistance = 100f;
    public AudioSource placeSound, unlockSound;
    static List<WineDraggableItem> allItems = new();

    public void OnDrag(PointerEventData e)
    {
        RectTransformUtility.ScreenPointToLocalPointInRectangle(
            canvas.transform as RectTransform, e.position, canvas.worldCamera, out Vector2 p);
        transform.localPosition = p;                       // follow the pointer in canvas space
    }

    public void OnEndDrag(PointerEventData e)
    {
        canvasGroup.blocksRaycasts = true;
        if (Vector3.Distance(transform.position, targetSlot.position) <= snapDistance)
        {
            transform.position = targetSlot.position;      // snap into the correct slot
            transform.SetParent(targetSlot);
            placeSound?.Play();
            CheckIfAllCorrect();
        }
        else transform.position = originalPosition;        // wrong spot: spring back
    }

    void CheckIfAllCorrect()
    {
        foreach (var item in allItems)
            if (item.transform.parent != item.targetSlot) return;
        unlockSound?.Play();
        UnlockAndCleanUI();   // grant clue keys, un-blur evidence, close the puzzle canvas
    }
}"""


def puppet():
    set_slug("puppetMystery")
    S = []
    S.append(("overview", "Overview", f"""
<p class="lead"><em>Puppet Mystery</em> (木偶之家：古堡谜案) reimagines a case from Mango TV's <em>Who's the Murderer</em> as a first-person 2D deduction game. Players explore a mansion, collect clues, solve puzzles and vote to uncover the truth of an incident buried for ten years.</p>
<p>Made for the Malanshan Cup Game Innovation & Entrepreneurship competition. As lead developer and producer I built the core Unity architecture and puzzle systems and managed a 7-person team to a 10-minute playable demo in three months. It's playable in the browser (WebGL).</p>
{video("4LisNuyYGOQ", "Puppet Mystery · trailer")}
"""))
    S.append(("contributions", "My contributions", contrib([
        ("fa-solid fa-sitemap", "Scene architecture", "A persistent GameManager that loads rooms additively and hides rather than unloads them, so every puzzle keeps its state."),
        ("fa-solid fa-puzzle-piece", "Puzzle systems", "Drag-and-drop ordering with snap validation, clue unlocking, blurred-evidence reveals and audio feedback."),
        ("fa-solid fa-mobile-screen", "Persistent phone UI", "A cross-scene detective phone (singleton) that holds clues and the final suspect vote."),
        ("fa-solid fa-people-group", "Team lead & producer", "Managed 7 people across design, narrative, art and programming over a three-month cycle."),
    ])))
    S.append(("gameplay", "Gameplay", f"""
{gallery([("itch_1.jpg", "Exploring the mansion"), ("frame_33.jpg", "Wine-bottle ordering puzzle"), ("frame_48.jpg", "Toy shelf puzzle"), ("frame_36.jpg", "Searching a bedroom"), ("frame_60.jpg", "Voting for the culprit"), ("itch_2.jpg", "Detective phone UI")], cols=3, cls="tall")}
{gallery([("frame_18.jpg", "Intro sequence"), ("frame_24.jpg", "Character portrait")], cols=2, cls="contain", ar="1/1")}
"""))
    S.append(("code", "Code deep-dive", f"""
<p>Two systems carry most of the game. Excerpts are condensed from the original Unity C# source, with comments translated to English.</p>
<h3>1 · Additive room loading that preserves state</h3>
<p>Each room is its own scene. Instead of reloading scenes (which would reset every drawer, lock and clue), the <code>GameManager</code> loads a room <strong>additively the first time</strong>, then just <strong>hides and restores its root objects</strong> on later visits. A transition camera covers the async load, and the phone UI and manager survive with <code>DontDestroyOnLoad</code>.</p>
{code("GameManager.cs", "Unity · C# · excerpt", GM_SRC)}
<h3>2 · Drag-and-drop puzzle with snap validation</h3>
<p>The wine-bottle puzzle uses Unity's EventSystem drag interfaces. Bottles follow the pointer in canvas space, snap into their slot within a distance threshold or spring back, and a static registry checks whether <em>all</em> bottles are placed before unlocking the next clue.</p>
{code("WineBottleSorting.cs", "Unity · C# · excerpt", WINE_SRC)}
"""))
    S.append(("audio", "Audio", f"""
<p>Sound tells the player a move worked: a place sound on every correct snap, an unlock sting when a puzzle resolves, over a looping mansion theme.</p>
{tracks([("puppet_bgm.mp3", "Puppet House · BGM", "Looping exploration theme (60-second excerpt)")])}
{sfx([("puppet_unlock.mp3", "Unlock"), ("puppet_laugh.mp3", "Puppet laugh")])}
"""))
    S.append(("challenges", "Challenges & solutions", cs([
        ("Room scenes reset when revisited",
         "Loading each room as a normal scene would wipe opened drawers, placed bottles and found clues whenever players returned.",
         "Additive loading + hide/restore",
         "Rooms load additively once, then their root objects are hidden and restored, so state persists without a save system."),
        ("Narrative and puzzles drifting apart",
         "Adapting a TV mystery risked puzzles that felt disconnected from the deduction story.",
         "Clue-driven progression",
         "Each puzzle unlocks clue keys and un-blurs evidence that feeds the final vote, so solving puzzles is how players advance the case."),
        ("Seven people, three months",
         "Design, narrative, art and code all had to land in one competition build.",
         "Lead-dev + producer role",
         "Owned the core systems myself while running the schedule, keeping scope to a polished 10-minute demo."),
    ])))
    return dict(
        slug="puppetMystery", title="Puppet Mystery", cat="gameplay", catname=CATNAME["gameplay"],
        question="How did I architect additive room loading and drag-and-drop puzzles for a browser-playable deduction game, while producing a 7-person team in three months?",
        tags=["Unity", "C#", "WebGL", "Scene management", "UI / EventSystem", "Team lead"],
        hero_mode="wide",
        hero="hero_wide.jpg",
        facts=[("Role", "Lead Developer · Producer · Level Designer"), ("Team", "7 people"), ("Year", "2025"), ("Engine", "Unity (C#)"), ("Platform", "WebGL (browser)")],
        links=[("fa-brands fa-itch-io", "Play in browser", "https://yollienarae.itch.io/puppetmystery"), ("fa-brands fa-youtube", "Trailer", "https://www.youtube.com/watch?v=4LisNuyYGOQ")],
        ta=["Additive scene loading that preserves puzzle state",
            "Persistent cross-scene phone UI and manager singletons",
            "EventSystem drag-and-drop with snap validation",
            "Audio feedback wired into puzzle states",
            "WebGL build for instant browser play",
            "Led a 7-person team as producer"],
        sections=S)


# ------------------------------------------------------------------ GRAVITAS
def gravitas():
    set_slug("gravitas")
    S = []
    S.append(("overview", "Overview", f"""
<p class="lead"><em>Gravitas</em> is a pixel-art tower-defense game. You play a hero who summons allies onto a gravity-controlled battlefield to save a magic world and restore the balance between light and darkness. It was selected as a <strong>Featured Game at UCSD Triton Ware (Fall 2024)</strong>.</p>
<p>I was the team's <strong>Audio Designer and Narrative Designer</strong>. I composed the original soundtrack and sound effects, and co-designed the narrative and gameplay pacing that frame each battle.</p>
{fig("background.jpg", "Gravitas key art")}
"""))
    S.append(("contributions", "My contributions", contrib([
        ("fa-solid fa-music", "Original soundtrack", "Composed the score: main menu, interlude, several combat cues of rising intensity, tarot and magic-book themes, a death cue and the ending."),
        ("fa-solid fa-wave-square", "Sound effects", "Created UI and combat feedback such as pawn placement, melee, archer, magic, dragon fire, hits and clicks."),
        ("fa-solid fa-feather", "Narrative design", "Co-designed the story frame (the light/dark balance, the wizard's tarot readings) and how story beats pace the battles."),
        ("fa-solid fa-sliders", "Implementation-ready audio", "Delivered cues as discrete Unity-ready clips so each game state could trigger its own music and SFX."),
    ])))
    S.append(("music", "Soundtrack", f"""
<p>Each game state gets its own musical identity, so players always know where they are: calm at the menu, tension rising through the combat cues, mystery for the tarot and magic-book moments. Excerpts are 60 seconds.</p>
{tracks([
    ("gravitas_003_main_menu.mp3", "Main Menu", "Title theme"),
    ("gravitas_001_interlude.mp3", "Interlude", "Story beat between battles"),
    ("gravitas_005_combat_1.mp3", "Combat I", "Opening battle"),
    ("gravitas_007_combat_2.mp3", "Combat II", "Escalation"),
    ("gravitas_009_combat_4.mp3", "Combat IV", "Late-game battle"),
    ("gravitas_012_tarot.mp3", "Tarot", "Fate-reading scene"),
    ("gravitas_010_magic_book.mp3", "Magic Book", "Wizard encounter"),
    ("gravitas_017_dead.mp3", "Defeat", "Death cue"),
    ("gravitas_002_game_end.mp3", "Game End", "Ending theme"),
])}
"""))
    S.append(("sfx", "Sound effects", f"""
<p>Short, readable feedback matters on a busy pixel battlefield. Click to play:</p>
{sfx([("gravitas_019_place_pawn.mp3", "Place pawn"), ("gravitas_011_melee.mp3", "Melee"), ("gravitas_008_archer.mp3", "Archer"), ("gravitas_014_magica.mp3", "Magic"), ("gravitas_016_dragon_fire.mp3", "Dragon fire"), ("gravitas_015_get_hit.mp3", "Get hit"), ("gravitas_004_stone.mp3", "Stone"), ("gravitas_020_klee.mp3", "Character voice"), ("gravitas_013_click.mp3", "UI click")])}
{gallery([("gameplay_01.jpg", "Battlefield: summon and place units"), ("gameplay_02.jpg", "The wizard's narrative encounter"), ("gameplay_03.jpg", "Tarot draw: upright blessings, reversed challenges")], cols=3, ar="16/9")}
"""))
    S.append(("challenges", "Challenges & solutions", cs([
        ("Keeping long battles from feeling repetitive",
         "Tower-defense rounds run long, and one battle loop quickly wears thin.",
         "A family of combat cues",
         "Wrote several combat tracks of increasing intensity, so the music escalates with the game instead of looping one theme."),
        ("Feedback on a crowded screen",
         "Dozens of pixel units act at once, and players need to know what their input did.",
         "Distinct, short SFX per action",
         "Gave placing, attacking, casting and taking damage their own short sounds so the soundscape stays readable."),
        ("Story that doesn't interrupt play",
         "Narrative had to frame the light/dark conflict without stalling the strategy loop.",
         "Story at natural breaks",
         "Placed story beats (interludes, the wizard, tarot readings) between battles, each with its own musical cue."),
    ])))
    S.append(("ta-link", "Why it matters for technical art", ul([
        "Audio taught me to design for <strong>game states</strong> and triggers, the same way I think about lighting states and VFX cues.",
        "Composing for pacing is why I can build rhythm systems (<a href='rhythmEcho.html' style='color:var(--accent)'>Rhythm</a>) and time cameras and sound in cinematics (<a href='theFeeding.html' style='color:var(--accent)'>The Feeding</a>).",
    ])))
    return dict(
        slug="gravitas", title="Gravitas", cat="beyond", catname=CATNAME["beyond"],
        question="How did I score and sound-design a pixel tower-defense game so that every game state has its own identity, and pace its story between battles?",
        tags=["Original soundtrack", "Sound design", "Narrative design", "Unity", "Game jam"],
        hero_mode="wide",
        hero="gameplay_01.jpg",
        facts=[("Role", "Audio Designer · Narrative Designer"), ("Year", "2024"), ("Event", "UCSD Triton Ware · Featured Game"), ("Genre", "Pixel tower defense"), ("Deliverables", "11 music cues + SFX set")],
        links=[("fa-brands fa-itch-io", "Play on itch.io", "https://misakizzzzz.itch.io/gravitas")],
        ta=["Original score mapped to game states",
            "Readable SFX for dense combat",
            "Narrative pacing between battles",
            "Unity-ready audio delivery"],
        sections=S)


# ------------------------------------------------------------------ THE VILLAGE
def village():
    set_slug("theVillage")
    S = []
    S.append(("overview", "Overview", f"""
<p class="lead">Costume &amp; Makeup Head for <em>The Village</em>, NUS King Edward VII Hall Chinese Drama. I directed a 29-member team to design and produce costumes and makeup for <strong>33 characters</strong> – one visual language across a whole cast, with hard practical constraints.</p>
<p>The production received the <strong>NUS Achievement Award (Commendation) for Arts Production of the Year</strong>.</p>
{stats([("33", "Characters styled"), ("29", "Team members led"), ("1", "Shared period palette"), ("Award", "Arts Production of the Year")])}
"""))
    S.append(("contributions", "My contributions", contrib([
        ("fa-solid fa-palette", "Cast-wide visual language", "Fixed a shared palette, silhouette vocabulary and set of traditional collars and closures so 33 characters read as one world."),
        ("fa-solid fa-user-pen", "Character styling concepts", "Derived each look from the character's personality, narrative arc and position in the stage composition, rather than from costume references alone."),
        ("fa-solid fa-users", "Leading a 29-person team", "Broke the cast into character concepts and production tasks so the team could work in parallel toward one look, with clear briefs and ownership."),
        ("fa-solid fa-scissors", "Production under constraints", "Chose silhouettes and materials that survived movement, quick changes and stage lighting."),
    ])))
    S.append(("looks", "The cast", f"""
{gallery([(f"village_0{i}.jpg", "") for i in range(1, 9)], cols=4, ar="2/3")}
<p>The cast shares a restrained, period palette and traditional collars and closures, while pattern, texture and hair styling tell individual characters apart – a style guide with per-character variation.</p>
<h3>Production video</h3>
{video("jYukGMt2NT4", "The Village · King Edward VII Hall Chinese Drama")}
"""))
    S.append(("challenges", "Challenges & solutions", cs([
        ("33 characters, one world",
         "Every character needed to be instantly distinct, but the cast had to read as one coherent period on a single stage.",
         "Shared rules, individual variation",
         "Fixed a shared palette and garment language for the whole cast, then varied texture, pattern and hair per character – the same structure as a master material with per-asset instances."),
        ("Art intent vs. performance constraints",
         "Costumes had to survive movement, quick changes and hot stage lighting while still looking right from the back row.",
         "Design inside the technical budget",
         "Chose silhouettes and materials that held up in performance. That is the same trade-off a technical artist makes between art intent and frame budget."),
        ("A 29-person art team",
         "Large art teams drift without clear direction and hand-offs.",
         "Clear briefs and ownership",
         "Split the cast into character concepts and production tasks so work ran in parallel without the look fragmenting."),
    ])))
    S.append(("ta-link", "Why it matters for technical art", ul([
        "Look-dev is costume design at scale: a <strong>style guide plus per-asset variation</strong>, always checked under the final lighting.",
        "Directing a 29-person art team toward one visual target is the same job as holding art direction across a shared shader and material library.",
    ])))
    return dict(
        slug="theVillage", title="The Village", cat="beyond", catname=CATNAME["beyond"],
        question="How did I lead a 29-person costume & makeup team to give 33 characters one cohesive visual language?",
        tags=["Art direction", "Costume design", "Makeup", "Character styling", "Team leadership"],
        hero_mode="poster", hero_caption="Production poster &middot; 寶島一村 &middot; NUS King Edward VII Hall Chinese Drama",
        hero="poster.jpg",
        facts=[("Role", "Costume &amp; Makeup Head"), ("Production", "NUS KE VII Hall Chinese Drama"), ("Year", "2024"), ("Team", "29 people"), ("Award", "NUS Achievement Award (Commendation)")],
        links=[("fa-brands fa-youtube", "Watch The Village", "https://www.youtube.com/watch?v=jYukGMt2NT4")],
        ta=["Built a cast-wide visual language across 33 characters (look-dev in fabric)",
            "Led a 29-person art team to a single look",
            "Balanced art intent against practical performance constraints"],
        sections=S)


# ------------------------------------------------------------------ THE INSANITY
def insanity():
    set_slug("theInsanity")
    S = []
    S.append(("overview", "Overview", f"""
<p class="lead">Costume Designer and Assistant Producer for <em>The Insanity</em> (你好，疯子！), NUS King Edward VII Hall Chinese Drama – a contemporary chamber piece where clothing has to do the characterization, and where I also ran the money and the schedule.</p>
<p>I secured <strong>SGD 7,000</strong> in external sponsorship and managed the production budget for a performance seen by <strong>600 people</strong>.</p>
{stats([("SGD 7,000", "Sponsorship secured"), ("600", "Audience"), ("7", "Principal looks designed"), ("End-to-end", "Production management")])}
"""))
    S.append(("contributions", "My contributions", contrib([
        ("fa-solid fa-shirt", "Costume design", "Designed the principal looks so each reads instantly on its own and still sits together as one ensemble under a single stage light."),
        ("fa-solid fa-handshake", "Sponsorship", "Secured SGD 7,000 in external sponsorship by writing funding proposals, pitching to stakeholders and negotiating partnerships."),
        ("fa-solid fa-chart-gantt", "Production management", "Oversaw timeline planning, budget tracking, resource allocation, risk coordination and cross-functional collaboration end to end."),
    ])))
    S.append(("looks", "The ensemble", f"""
<p>In a contemporary setting, clothing carries character: a floral shirt, a lab coat, a lanyard and pinstripe, a tailored suit, a red slip dress. Each look is a silhouette-and-colour read at distance, then a texture read up close.</p>
{gallery([("insanity_02.jpg", "Ensemble"), ("insanity_12.jpg", "Staged ensemble moment")], cols=2, ar="16/9")}
{gallery([(f"insanity_{i:02d}.jpg", "") for i in (4, 5, 7, 8, 9, 10, 11, 6)], cols=4, ar="2/3")}
"""))
    S.append(("challenges", "Challenges & solutions", cs([
        ("Contemporary clothes have no costume shorthand",
         "In a period piece the palette does the work; in modern dress everyone is just wearing clothes, and characters blur together.",
         "One signature per character",
         "Gave each character a single dominant garment idea – pattern, uniform, cut or colour – and kept everything else neutral, so the ensemble stays readable as a group shot."),
        ("A sponsored production has a hard budget",
         "Design ambition and available money were set by different people at different times.",
         "Own both sides",
         "Running sponsorship and the budget myself meant costume decisions were made with the real number in view, not negotiated after the fact."),
        ("Many moving parts, one date",
         "Rehearsal, build, publicity and venue all converged on a fixed performance date.",
         "Timeline and risk tracking",
         "Planned the schedule backwards from the performance with explicit owners and risk coordination across functions."),
    ])))
    S.append(("ta-link", "Why it matters for technical art", ul([
        "Producing a show on a sponsored budget is the same discipline as the <a href='../index.html#professional' style='color:var(--accent)'>production and pipeline management side of TA work</a>: fixed date, fixed budget, cross-functional dependencies.",
        "Designing for instant readability in a group shot is character look-dev – the silhouette and value read matter before any detail does.",
    ])))
    return dict(
        slug="theInsanity", title="The Insanity", cat="beyond", catname=CATNAME["beyond"],
        question="How did I design a contemporary cast that stays readable as an ensemble, while securing the sponsorship and running the production?",
        tags=["Costume design", "Character styling", "Production", "Sponsorship", "Budget management"],
        hero_mode="wide",
        hero="insanity_02.jpg",
        facts=[("Roles", "Costume Designer · Assistant Producer"), ("Production", "NUS KE VII Hall Chinese Drama"), ("Year", "2023"), ("Sponsorship", "SGD 7,000 secured"), ("Audience", "600")],
        links=[],
        ta=["Designed a contemporary ensemble around one signature per character",
            "Secured SGD 7,000 sponsorship and managed the production budget",
            "Ran end-to-end production: timeline, resources, risk, cross-functional coordination"],
        sections=S)


# ------------------------------------------------------------------ BUBBLE FACTORY
ITCH = "https://img.itch.zone/aW1hZ2UvMzI1NDkwMy8"
BF_SHOTS = {
    "menu": ITCH + "yMDM3ODY1My5wbmc=/original/SL0Fj%2B.png",
    "corridor": ITCH + "xOTQzMzk3OC5wbmc=/original/zojdEs.png",
    "platform": ITCH + "yMDM3ODY1Mi5wbmc=/original/rD2oA1.png",
    "pickup": ITCH + "yMDM3ODY1NC5wbmc=/original/YZf2T0.png",
    "lake": ITCH + "yMDM3ODY1NS5wbmc=/original/scntXw.png",
}

BUBBLE_SRC = """public class MovingBubble : MonoBehaviour
{
    public Vector3 startPosition, endPosition;
    public float moveDuration = 4f;
    public float minInterval = 1f, maxInterval = 3f;
    public AudioSource bubbleAudioSource;
    public Transform player;
    public float maxDistance = 10f;           // sound fully fades out beyond this

    IEnumerator MoveAndResetRoutine()
    {
        while (true)
        {
            bubbleAudioSource?.Play();
            for (float t = 0; t < moveDuration; t += Time.deltaTime)
            {
                float k = Mathf.SmoothStep(0, 1, t / moveDuration);   // ease in/out drift
                transform.position = Vector3.Lerp(startPosition, endPosition, k);
                yield return null;
            }
            bubbleAudioSource?.Stop();
            transform.position = startPosition;                        // respawn
            yield return new WaitForSeconds(Random.Range(minInterval, maxInterval));
        }
    }

    void Update()   // distance-attenuated bubble sound
    {
        float d = Vector3.Distance(player.position, transform.position);
        bubbleAudioSource.volume = d < maxDistance ? Mathf.Lerp(1f, 0f, d / maxDistance) : 0f;
    }
}"""

GUM_SRC = """public abstract class GumBase : MonoBehaviour
{
    public AudioClip chewingSound;
    public void PlayChewingSound() { audioSource.PlayOneShot(chewingSound); }
    public void HideGum() { gameObject.SetActive(false); }
    public abstract void ActivateEffect();      // each gum defines its own power-up
}

public class JumpGum : GumBase
{
    public override void ActivateEffect()
    {
        playerController.ActivateJump();
        PlayChewingSound(); HideGum();
    }
}

public class TimeShieldGum : GumBase
{
    public override void ActivateEffect()
    {
        playerTimeShieldManager.ActivateTimeShield();   // bubble shield with a 5 s timer
        PlayChewingSound(); HideGum();
    }
}"""


def bubble():
    set_slug("bubbleFactory")
    S = []
    S.append(("overview", "Overview", f"""
<p class="lead"><em>Bubble Factory</em> is a 3D platformer made in 48 hours for <strong>Global Game Jam 2025</strong> (theme: <em>Bubble</em>). You play a bubble-gum-loving character crossing a candy-pink factory: chew different gums to unlock jumps and bubble shields, dodge cannon fire, and cross a glossy gum lake.</p>
<p>I was lead developer, level designer and technical artist. I built the gameplay systems in Unity (URP, C#) and <strong>authored the game's signature materials</strong>: the translucent bubbles and bubble shield, the gum-lake surface, the candy sky and the emissive interaction highlights. I also wrote the narrative and worldbuilding, using Figma flow diagrams to line the story up with the level layout.</p>
{fig("cover.jpg", "Title screen")}
"""))
    S.append(("contributions", "My contributions", contrib([
        ("fa-solid fa-circle-half-stroke", "Bubble material", "Stylized translucent bubble in Shader Graph: Fresnel rim, transparency blending and normal distortion to fake reflection and refraction. Used on floating bubbles and the player's bubble shield."),
        ("fa-solid fa-water", "Gum-lake surface", "Re-tuned a normal-mapped, specular water material into a glossy pink bubble-gum lake that reads as sticky and soft."),
        ("fa-solid fa-lightbulb", "Emissive feedback", "HDR emissive Highlight and Collect materials that bloom when players look at or pick up gum."),
        ("fa-solid fa-code", "Gameplay systems (C#)", "An abstract GumBase power-up system, shields with hit counts and timers, drifting bubbles with distance-attenuated audio, and cannons."),
        ("fa-solid fa-route", "Level design & narrative", "Level layout and story flow planned in Figma so progression and narrative beats line up."),
        ("fa-solid fa-people-group", "Lead developer", "Led programming across a 3-person code team to ship a playable build in 48 hours."),
    ])))
    S.append(("materials", "Materials & shading", f"""
<p>The whole game had to read as one candy-colored world at a glance. I built a small set of URP materials that do most of the visual work:</p>
{cs([
    ("Bubble & bubble shield", "Transparent URP surface with <strong>premultiplied alpha</strong> and <strong>ZWrite off</strong> in the transparent queue (3000), so overlapping bubbles layer cleanly and highlights stay bright. <strong>Environment/cubemap reflections</strong> give the soap-film sheen. A Shader Graph layer adds a <strong>Fresnel rim</strong> and <strong>normal distortion</strong> for the fake refraction.",
     "Where it's used", "Assigned to the drifting bubbles (<code>Bubble1–3</code>) and the player's <code>Shield</code>, so the pickup and the power-up it grants share one visual language."),
    ("Gum-lake surface", "A normal-mapped, specular water material retinted and re-tuned into glossy pink bubble gum rather than water.",
     "Why", "Getting a reflective, wavy surface from an existing shader and tuning it to the art direction saved hours in a 48-hour jam."),
    ("Candy sky", "An emissive pink SKY material (base ≈ #F57882, red emission) plus a stylized skybox set the warm, sugary palette for the level.",
     "Palette", "Every material shares the same pink/coral family, so the scene holds together even with placeholder geometry."),
    ("Interaction highlights", "<code>Highlight</code> (white, HDR emission ≈ 2.1) and <code>Collect</code> (pink, HDR emission ≈ 1.6) push past 1.0 so they <strong>bloom</strong>.",
     "System hook", "<code>GumInteraction.cs</code> swaps in the highlight material when the camera looks at a gum, so players know what they can chew."),
], labels=("Material", "In the game"))}
{gallery([("gum_lake.jpg", "Gum-lake surface: normal-mapped and re-tinted to bubble-gum pink"), (BF_SHOTS["lake"], "Crossing the gum lake")], cols=2, ar="16/9")}
"""))
    S.append(("gameplay", "Gameplay", f"""
{gallery([(BF_SHOTS["corridor"], "Gum-lake corridor"), (BF_SHOTS["pickup"], "Gum pickup with interaction prompt"), (BF_SHOTS["platform"], "Platforming section")], cols=3, ar="16/9")}
"""))
    S.append(("code", "Code", f"""
<p>Excerpts are condensed from the jam source, with comments translated to English.</p>
<h3>Power-ups through one abstract class</h3>
<p>Every gum inherits from <code>GumBase</code> and only implements <code>ActivateEffect()</code>, so adding a new power-up mid-jam was one small class.</p>
{code("GumBase.cs · JumpGum.cs · TimeShieldGum.cs", "Unity · C# · excerpt", GUM_SRC)}
<h3>Drifting bubbles with spatial audio</h3>
{code("MovingBubble.cs", "Unity · C# · excerpt", BUBBLE_SRC)}
"""))
    S.append(("challenges", "Challenges & solutions", cs([
        ("Transparent bubbles sorting badly",
         "Overlapping translucent bubbles and the shield can flicker or darken if they write depth or blend like opaque surfaces.",
         "Premultiplied, depth-write-off transparency",
         "Rendered bubbles in the transparent queue with ZWrite off and premultiplied alpha, so they layer correctly and keep bright specular highlights."),
        ("Players not knowing what's interactive",
         "In a busy, uniformly pink level, gum pickups blended into the scene.",
         "HDR emissive highlight on focus",
         "Swapped in an HDR emissive material on look-at, so interactables glow and bloom without extra UI."),
        ("A whole look in 48 hours",
         "No time to model and texture a detailed environment.",
         "Let materials carry the art direction",
         "A few strong materials (bubbles, gum lake, candy sky, glowing pickups) establish the world over simple prototype geometry."),
    ])))
    return dict(
        slug="bubbleFactory", title="Bubble Factory", cat="render", catname=CATNAME["render"],
        question="How did I make materials carry a whole art direction in 48 hours, with translucent bubble shields, a glossy gum lake and glowing pickups, while leading gameplay programming?",
        tags=["Unity URP", "Shader Graph", "Fresnel", "Transparency", "HDR emission", "C#", "Game jam"],
        hero_mode="inset",
        hero="gum_lake.jpg",
        facts=[("Role", "Lead Developer · Level Designer · Technical Artist"), ("Year", "2025"), ("Event", "Global Game Jam · 48 hours"), ("Engine", "Unity (URP), C# · Windows"), ("Team", "Art, audio & 3 programmers")],
        links=[("fa-brands fa-itch-io", "Play on itch.io", "https://yollienarae.itch.io/bubble-factory"), ("fa-brands fa-github", "Source on GitHub", "https://github.com/Yolanda699/ggj")],
        ta=["Translucent bubble/shield material: Fresnel, normal distortion, premultiplied alpha",
            "Glossy gum-lake surface tuned to the art direction",
            "HDR emissive interaction highlights for bloom",
            "Abstract C# power-up system",
            "Spatial audio tied to moving VFX objects",
            "Shipped in 48 hours as lead developer"],
        sections=S)


ORDER = [feeding, rhythm, bubble, sd_tool, ps_tool, traveltrove, river, broken, puppet, gravitas, village, insanity]
