"""Original editable vector model sheet; dimensions describe the Week 2 housing."""
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent/'reference'
OUT.mkdir(exist_ok=True)

def svg(width,height,body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><rect width="100%" height="100%" fill="#eff3f4"/><style>text{{font-family:Segoe UI,sans-serif;fill:#213341}} .line{{stroke:#334f63;stroke-width:8;fill:none;stroke-linejoin:round}} .dim{{stroke:#54768b;stroke-width:3;fill:none}} .label{{font-size:40px}} .note{{font-size:32px;fill:#54768b}}</style>{body}</svg>'

def main():
    # Front image canvas spans 0.8 m, putting the 0.6 m housing between x=200 and 1400.
    front='''<rect x="200" y="300" width="1200" height="1000" fill="#c3d1d8" stroke="#334f63" stroke-width="8"/>
    <rect x="300" y="400" width="1000" height="800" fill="#eff3f4" stroke="#334f63" stroke-width="8"/>
    <path class="dim" d="M200 230V180H1400V230 M200 170V200 M1400 170V200 M1450 300H1500V1300H1450"/>
    <text x="800" y="145" text-anchor="middle" class="label">0.60 m</text>
    <text x="800" y="840" text-anchor="middle" class="label">OPENING 0.50 × 0.40 m</text>
    <text x="800" y="1430" text-anchor="middle" class="label">FRONT · looking along +Y</text>
    <text x="800" y="1490" text-anchor="middle" class="note">0.05 m walls · outer height 0.50 m</text>'''
    side='''<path d="M350 300H1150V1300H350V1200H1050V400H350Z" fill="#c3d1d8" stroke="#334f63" stroke-width="8"/>
    <path class="dim" d="M350 230V180H1150V230 M350 170V200 M1150 170V200"/>
    <text x="750" y="145" text-anchor="middle" class="label">0.40 m</text>
    <text x="720" y="780" text-anchor="middle" class="label">0.35 m cavity</text>
    <path class="dim" d="M400 830H1000"/>
    <text x="750" y="1430" text-anchor="middle" class="label">SIDE SECTION · front at left</text>
    <text x="750" y="1490" text-anchor="middle" class="note">0.05 m back wall · section is explanatory</text>'''
    iso='''<path d="M200 500L600 220L1400 520L1000 800Z" fill="#d6e0e5" stroke="#334f63" stroke-width="8"/>
    <path d="M1000 800L1400 520V1220L1000 1500Z" fill="#94adbc" stroke="#334f63" stroke-width="8"/>
    <path d="M200 500L1000 800V1500L200 1200Z" fill="#bfd0da" stroke="#334f63" stroke-width="8"/>
    <path d="M267 625L933 875V1375L267 1125Z" fill="#47677b" stroke="#334f63" stroke-width="8"/>
    <path d="M267 625L517 720V1030L267 1125Z" fill="#8ca9ba"/>
    <path d="M267 1125L517 1030L933 1186V1375Z" fill="#a8c0cd"/>
    <path class="line" d="M267 625L933 875V1375L267 1125Z"/>
    <text x="800" y="1640" text-anchor="middle" class="label">THREE-QUARTER · shape guide</text>'''
    (OUT/'housing_front.svg').write_text(svg(1600,1600,front),encoding='utf-8')
    (OUT/'housing_side_section.svg').write_text(svg(1600,1600,side),encoding='utf-8')
    sheet='''<text x="180" y="160" style="font-size:80px;font-weight:650">LUMEN · EQUIPMENT HOUSING</text>
    <text x="180" y="235" style="font-size:42px;fill:#54768b">Lecture 2 / 14 · original modeling reference · dimensions in metres</text>'''
    sheet+=f'<g transform="translate(120,380) scale(.72)">{front}</g>'
    sheet+=f'<g transform="translate(1340,380) scale(.72)">{side}</g>'
    sheet+=f'<g transform="translate(2550,320) scale(.72)">{iso}</g>'
    sheet+='''<text x="180" y="1880" style="font-size:44px">Keep the opening, walls and back as one solid shell. The removable lid stays a separate object.</text>
    <text x="180" y="1960" style="font-size:36px;fill:#54768b">Front and side are orthographic. Three-quarter view explains depth; do not use it to align an orthographic model.</text>
    <text x="180" y="2050" style="font-size:32px;fill:#54768b">Original SECourses companion artwork · CC0 · editable SVG supplied</text>'''
    (OUT/'housing_reference.svg').write_text(svg(3840,2160,sheet),encoding='utf-8')
    (OUT/'LICENSE.txt').write_text('Original SECourses Blender Lecture 2 housing diagrams, 2026. Dedicated to the public domain under CC0 1.0.\nhttps://creativecommons.org/publicdomain/zero/1.0/\nNo third-party source images.\n',encoding='utf-8')
    print('Created editable original housing SVGs in',OUT)

if __name__=='__main__':main()
