#!/usr/bin/env python3
"""
Genera fuentes-valentina.css: subconjunta las cuatro caras de IBM Plex a Latin,
las convierte a woff2 y las incrusta como base64 en reglas @font-face.

Solo hace falta si cambian las fuentes o los pesos del manual de Valentina.
Para solo editar contenido no se usa: basta el fuentes-valentina.css ya generado.

Requiere:  pip install fonttools brotli
Fuentes:   IBM Plex (SIL OFL 1.1) — https://github.com/IBM/plex
           se necesitan los .ttf de IBM Plex Sans (Regular/SemiBold/Bold) y
           IBM Plex Mono (Regular).

Uso:  python subset-plex.py  RUTA/A/IBM-Plex-ttf  >  fuentes-valentina.css
"""
import sys, base64, io
from fontTools.subset import Subsetter, Options
from fontTools.ttLib import TTFont

FACES = [
    ("IBM Plex Sans", 400, "IBMPlexSans-Regular.ttf"),
    ("IBM Plex Sans", 600, "IBMPlexSans-SemiBold.ttf"),
    ("IBM Plex Sans", 700, "IBMPlexSans-Bold.ttf"),
    ("IBM Plex Mono", 400, "IBMPlexMono-Regular.ttf"),
]
# Latin básico + suplemento + puntuación tipográfica usada en el manual
RANGES = "0020-007E,00A0-00FF,2010-2015,2018-201F,2022,2026,2039,203A,20AC,2212,2192"


def unicodes():
    us = set()
    for part in RANGES.split(","):
        if "-" in part:
            a, b = part.split("-"); us.update(range(int(a, 16), int(b, 16) + 1))
        else:
            us.add(int(part, 16))
    return us


def main(fonts_dir):
    us = unicodes()
    out = []
    for fam, weight, fn in FACES:
        opts = Options()
        opts.flavor = "woff2"
        opts.desubroutinize = True
        opts.layout_features = ["kern", "liga", "calt", "tnum", "onum"]
        ss = Subsetter(options=opts)
        f = TTFont(f"{fonts_dir}/{fn}")
        ss.populate(unicodes=us)
        ss.subset(f)
        buf = io.BytesIO(); f.save(buf)
        b64 = base64.b64encode(buf.getvalue()).decode()
        out.append(
            f"@font-face{{font-family:'{fam}';font-weight:{weight};font-style:normal;"
            f"font-display:swap;src:url(data:font/woff2;base64,{b64}) format('woff2')}}"
        )
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("uso: python subset-plex.py RUTA/A/IBM-Plex-ttf > fuentes-valentina.css")
    main(sys.argv[1])
