# Genera ui_prototype_drawlibri.html: la interfaz master con la marca Drawlibri (paleta A «Colibri»).
# El master sigue siendo ui_prototype.html; volver a correr este script tras cada cambio del master.
#   python build_drawlibri.py
import re, os

HERE = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(HERE, 'ui_prototype.html'), encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:120])
    s = s.replace(a, b)

# ---------- paletas del lienzo (claro y oscuro) ----------
LIGHT = {
    'ink': '#0F7B5F', 'title': '#13212B', 'accent': '#0F7B5F', 'select': '#0F7B5F', 'focus': '#C2410C', 'snap': '#B0124F',
    'line': '#5A6872', 'inactive': '#9AA49F', 'swing': '#6E7E86', 'selFill': '#DCEFE7', 'interiorSel': '#E8F5EF',
    'dimLine': '#0F7B5F', 'paperHover': '#E7F3EE', 'hoverMod': 'rgba(15,123,95,.55)', 'hoverPart': 'rgba(15,123,95,.45)',
    'boxFill': 'rgba(15,123,95,.08)', 'swapFill': 'rgba(15,123,95,.22)', 'selOverlay': 'rgba(61,214,163,.22)',
    'muted': '#5A6872', 'sub': '#5A6872', 'empty': '#8A9690', 'pieceFill': 'rgba(15,123,95,.25)', 'planSel': 'rgba(220,239,231,.9)',
    'proj': '#3E5A66', 'tap': '#0F7B5F', 'wallLine': '#13212B',
}
DARK = {
    'ink': '#3DD6A3', 'title': '#F7F7F4', 'accent': '#3DD6A3', 'select': '#3DD6A3', 'focus': '#F07A3E', 'snap': '#FF5C93',
    'line': '#8C9BA5', 'inactive': '#4B5D69', 'swing': '#6F8591', 'box': '#6F818C', 'front': '#1C2C37', 'selFill': '#173D33',
    'interior': '#16242E', 'interiorSel': '#183329', 'shelf': '#3A4D59', 'shaker': '#61737E', 'handle': '#C9D2D8',
    'planCover': '#22333F', 'planSel': 'rgba(61,214,163,.22)', 'wall': '#3E505C', 'wallBand': '#18272F', 'wallLine': '#93A2AC',
    'dimLine': '#4E8F7B', 'paper': 'rgba(19,33,43,.88)', 'paperHover': '#163A31', 'labelBg': 'rgba(19,33,43,.92)',
    'hoverMod': 'rgba(61,214,163,.6)', 'hoverPart': 'rgba(61,214,163,.55)', 'boxFill': 'rgba(61,214,163,.10)', 'swapFill': 'rgba(61,214,163,.22)',
    'selOverlay': 'rgba(61,214,163,.22)', 'muted': '#93A2AC', 'sub': '#8C9BA5', 'empty': '#8C9BA5', 'flat': '#15232D', 'gripRing': '#13212B',
    'pieceFill': 'rgba(61,214,163,.28)', 'proj': '#7FB8A4', 'tap': '#3DD6A3', 'metal': '#55636C', 'glass': '#1A262E',
}
for name, over in (('LIGHT', LIGHT), ('DARK', DARK)):
    i = s.index('const %s = {' % name); j = s.index('};', i)
    blk = s[i:j]
    for k, v in over.items():
        blk, n = re.subn(r"\b%s:'[^']*'" % k, "%s:'%s'" % (k, v), blk)
        assert n == 1, (name, k, n)
    s = s[:i] + blk + s[j:]

# ---------- interfaz: tema oscuro sobre tinta y primario en verde claro (texto en tinta) ----------
rep("html[data-theme=dark] .btn-primary { background: #2F75B5; border-color: #2F75B5; color: #fff; }",
    "html[data-theme=dark] .btn-primary { background: #3DD6A3; border-color: #3DD6A3; color: #13212B; }")
rep("html[data-theme=dark] .btn-primary:hover { background: #3A84C6; border-color: #3A84C6; }",
    "html[data-theme=dark] .btn-primary:hover { background: #5FE0B5; border-color: #5FE0B5; }\n  html[data-theme=dark] .btn-primary svg path { stroke: #13212B; }")

# ---------- colores sueltos (CSS, iconos SVG, dialogos) ----------
MAP = {
    # tinta de marca -> verde colibri
    '#266096': '#0F7B5F', '#1E5080': '#0A5A45', '#194468': '#08483A', '#E6EFF7': '#E7F3EE', '#DCE8F3': '#D7ECE3', '#1E90FF': '#0F7B5F',
    # papel y grises calidos de la marca
    '#F6F7F8': '#F7F7F4', '#DDE1E4': '#E9EAE4', '#F4F7FA': '#F3F6F2', '#E1E7ED': '#DADFD9', '#DADFE3': '#DADFD9', '#CDD3D9': '#D3D8D1',
    '#F1F4F7': '#F1F3EE', '#E7ECF0': '#E6E9E2', '#B8C0C8': '#BCC3BC', '#E9EEF3': '#F7F7F4', '#DCE3E9': '#EEEFE9', '#B9C2C9': '#DADFD9',
    '#1f1f1f': '#13212B', '#1F2A33': '#13212B', '#2b2b2b': '#13212B', '#6B7680': '#5A6872', '#5A6570': '#5A6872', '#3A4650': '#33424C', '#4A5560': '#33424C',
    # avisos y estados: fucsia para alertas, verde para listo
    '#C07A12': '#B0124F', '#FDF1DC': '#F6E6EC', '#2E8B57': '#0F7B5F', '#E6F4EC': '#E7F3EE', '#B5433B': '#B0124F', '#FBEDEB': '#F6E6EC', '#E2B5B0': '#E3B4C6',
    # tema oscuro: tinta y verde claro
    '#8DBBE3': '#3DD6A3', '#22374A': '#173D33', '#5C9BD1': '#2FA37E', '#2C2F34': '#1C2C37', '#363A40': '#243541', '#4A4F57': '#34495A',
    '#15171A': '#0B141A', '#25272B': '#13212B', '#1E2024': '#0F1B23', '#33363B': '#22323D', '#3A3E44': '#2A3C48', '#181A1D': '#101C24',
    '#36393E': '#22333F', '#2A2D31': '#182833', '#9AA3AD': '#93A2AC', '#B9C0C7': '#B7C3CA', '#C9CED4': '#C9D2D8', '#E2E5E9': '#F0F2EE', '#8E98A2': '#8C9BA5',
}
pat = re.compile('|'.join(re.escape(k) for k in MAP), re.I)
low = {k.lower(): v for k, v in MAP.items()}
s = pat.sub(lambda m: low[m.group(0).lower()], s)
# los mismos colores dentro de SVG en data URI (flecha de los combos): '#' va como %23
for k, v in MAP.items(): s = re.sub(re.escape('%23' + k[1:]), '%23' + v[1:], s, flags=re.I)

# ---------- tipografia: IBM Plex Sans en la interfaz, Bricolage Grotesque en titulos, Plex Mono en datos ----------
rep("family=Inter:wght@400;500;600;700&", "family=IBM+Plex+Sans:wght@400;500;600;700&family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&")
rep("""ctx.fillStyle = C.title; ctx.font = "600 15px 'Inter'";""", """ctx.fillStyle = C.title; ctx.font = "700 16px 'Bricolage Grotesque'";""")
s = s.replace('"Inter"', '"IBM Plex Sans"').replace("'Inter'", "'IBM Plex Sans'")
rep(".m-title { font-size: 15px; font-weight: 600; color: var(--text); }",
    ".m-title { font-family: 'Bricolage Grotesque', 'IBM Plex Sans', sans-serif; font-size: 16px; font-weight: 600; color: var(--text); }")

# ---------- barra de titulo: icono de la marca, producto (Skitchen / Drawdrobe) y firma ----------
ICON = ('<svg width="18" height="18" viewBox="0 0 100 100" aria-hidden="true"><path fill="#0F7B5F" d="M19 54 L36 40 L2 14 Z"/>'
        '<path class="ic-ink" fill="#13212B" fill-rule="evenodd" d="M18 62 A22 22 0 1 0 62 62 A22 22 0 1 0 18 62 Z M28 62 A12 12 0 1 1 52 62 A12 12 0 1 1 28 62 Z"/>'
        '<path class="ic-ink" fill="#13212B" d="M51 84 L62 84 L89 9 L85 8 Z"/><circle cx="44" cy="57" r="3.2" fill="#B0124F"/></svg>')
rep("""<span><span id="winTitle">Cocina &middot; Distribuci&oacute;n</span> &middot; Cabynetry Kitchen (prototipo SketchUp)</span>""",
    """<span class="brandbar">%s<span class="prod" id="prodName"><b>Skit</b>chen</span><span class="by">by drawlibri</span><span class="bsep">&middot;</span><span id="winTitle">Cocina &middot; Distribuci&oacute;n</span><span class="bsep">&middot; prototipo</span></span>""" % ICON)
rep("""  .cmdsel { display: flex;""", """  .brandbar { display: flex; align-items: center; gap: 7px; white-space: nowrap; }
  .brandbar .prod { font-family: 'Bricolage Grotesque', sans-serif; font-size: 15px; font-weight: 400; letter-spacing: -0.02em; color: #13212B; }
  .brandbar .prod b { font-weight: 800; color: #C2410C; }
  .brandbar .prod.drobe b { color: #5B3FA0; }
  .brandbar .by { font-family: 'IBM Plex Mono', monospace; font-size: 10.5px; color: #5A6872; }
  .brandbar .bsep { color: #8A9690; }
  html[data-theme=dark] .brandbar .prod { color: #F7F7F4; }
  html[data-theme=dark] .brandbar .prod b { color: #F07A3E; }
  html[data-theme=dark] .brandbar .prod.drobe b { color: #A58BE6; }
  html[data-theme=dark] .brandbar .by { color: #93A2AC; }
  html[data-theme=dark] .brandbar .ic-ink { fill: #F7F7F4; }
  .cmdsel { display: flex;""")
rep("""  document.getElementById('winTitle').textContent = isla ? 'Isla · Distribución' : closet ? 'Closet · Distribución' : 'Cocina · Distribución';""",
    """  document.getElementById('winTitle').textContent = isla ? 'Isla · Distribución' : closet ? 'Closet · Distribución' : 'Cocina · Distribución';
  /* producto de la familia drawlibri: Skitchen (cocinas e islas, tomate) o Drawdrobe (closets, ciruela) */
  const pn = document.getElementById('prodName'); pn.innerHTML = closet ? '<b>Draw</b>drobe' : '<b>Skit</b>chen'; pn.classList.toggle('drobe', closet);""")
s = re.sub(r'<title>[^<]*</title>', '<title>Skitchen · drawlibri</title>', s, count=1)

# ---------- aviso en el encabezado ----------
rep("<!DOCTYPE html>\n<!--\n", "<!DOCTYPE html>\n<!--\n  VARIANTE DE MARCA DRAWLIBRI (paleta A Colibri): generada por build_drawlibri.py\n  desde ui_prototype.html, que sigue siendo el master. No editar este archivo.\n\n", 1)
i = s.index('<!--'); j = s.index('-->', i); assert '--' not in s[i+4:j]

open(os.path.join(HERE, 'ui_prototype_drawlibri.html'), 'w', encoding='utf-8').write(s)
print('ui_prototype_drawlibri.html generado')
