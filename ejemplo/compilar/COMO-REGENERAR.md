# Cómo regenerar los ejemplos

Los cuatro archivos publicados en `ejemplo/` —los manuales
`manual-ignacia.html` y `manual-valentina.html`, y las fichas de una hoja
`ficha-ignacia.html` y `ficha-valentina.html`— son archivos finales
autocontenidos: llevan las tipografías incrustadas en base64. No se editan a
mano. Se compilan desde el material de esta carpeta.

Para cada persona hay tres piezas:

- `manual-<nombre>.src.html` — el manual editable, con un marcador `/*FONTS*/` en
  el `<style>` donde van las fuentes. **Aquí se edita el contenido.**
- `ficha-<nombre>.src.html` — la ficha de una hoja, con el mismo marcador. Sus
  tokens son una copia literal de los del manual: si cambia la paleta, se
  cambian en los dos, o la ficha miente.
- `fuentes-<nombre>.css` — las reglas `@font-face` con las tipografías en base64,
  compartidas por el manual y la ficha.

## 1. Editar

Abre el `.src.html` y cambia lo que necesites: texto, paleta (los tokens en
`:root`), estructura. El marcador `/*FONTS*/` se queda donde está.

## 2. Armar el HTML final

Reemplaza el marcador por el CSS de fuentes y escribe el archivo publicado. Desde
esta carpeta:

```bash
python -c "
for n in ['valentina','ignacia']:
    css = open(f'fuentes-{n}.css', encoding='utf-8').read()
    for k in ['manual','ficha']:
        src = open(f'{k}-{n}.src.html', encoding='utf-8').read()
        open(f'../{k}-{n}.html','w',encoding='utf-8').write(src.replace('/*FONTS*/', css, 1))
"
```

## 3. Sacar el PDF

El PDF paginado sale al imprimir desde un navegador Chromium (Chrome o Edge). A
mano: abre el `.html`, `Ctrl+P`, «Guardar como PDF», activa **Gráficos de fondo**.
Sin ventana:

```bash
chrome --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="RUTA/ejemplo/manual-valentina.pdf" \
  "file:///RUTA/ejemplo/manual-valentina.html"
```

Pasa el HTML como URL `file://` con ruta absoluta. En Windows con Git Bash no uses
una ruta relativa ni `$(pwd)` (da `/c/...`, que Chrome no resuelve): usa la letra
de unidad, p. ej. `file:///C:/Users/.../ejemplo/manual-valentina.html`. Y no
redirijas el error a `/dev/null`: si el render falla, Chrome no escribe el PDF y te
quedas con el viejo sin darte cuenta.

Son cuatro PDF: los dos manuales y las dos fichas.

**Los manuales imprimen en claro y las fichas en oscuro**, y es a propósito. El
manual es un documento que se lee en papel; la ficha se consulta en pantalla
mucho más de lo que se cuelga en una pared. Por eso el `<html>` de cada ficha
lleva `data-theme="dark"` y su CSS de impresión respeta la versión activa en vez
de forzar blanco. Para sacarlas en claro, cambia ese atributo a `"light"` y
vuelve a imprimir; no hay que tocar nada más.

## 4. Verificar

Revisa el PDF página por página: que no haya páginas en blanco, que los números
del índice cuadren con las páginas reales y que la partición de palabras no deje
nada feo. La paginación (numeración, encabezado, pie, filete) la dibujan las cajas
`@page` del CSS; no hace falta ninguna librería.

**El índice se desfasa solo.** Sus números están escritos a mano en el `.src`, así
que cualquier cambio de contenido puede correr la paginación sin que nada falle.
Después de editar, contrasta el índice contra las páginas reales:

```bash
for p in $(seq 1 20); do
  echo "p$p: $(pdftotext -f $p -l $p ../manual-valentina.pdf - | head -4 | tr '\n' ' ')"
done
```

Cuidado al leerlo: `pdftotext` no puede extraer las vocales acentuadas de estas
fuentes subconjuntadas y las devuelve como caracteres de reemplazo. Compara por el
número de sección, no por el título.

**Las fichas se verifican por una sola cosa: que impriman en una página.** Es su
única mecánica y es la que se rompe.

```bash
python -c "
import re
d = open('../ficha-valentina.pdf','rb').read()
print(len(re.findall(rb'/Type\s*/Page[^s]', d)), 'páginas')
"
```

Si da más de una, se arregla recortando contenido, no bajando el cuerpo de 7,5 pt.
Una ficha que no cabe está cargando argumento, y el argumento va en el manual.

## Las tipografías

- **Valentina** usa IBM Plex (Sans y Mono), SIL OFL 1.1. El `fuentes-valentina.css`
  se generó con `subset-plex.py`, que subconjunta a Latin y comprime a woff2. Solo
  hace falta correrlo si cambian las fuentes o los pesos; para editar contenido, no.
- **Ignacia** usa Fraunces, Nunito Sans y Space Mono, también OFL. Su
  `fuentes-ignacia.css` es el bloque `@font-face` tal como quedó incrustado; no se
  guardó su script de subconjuntado.

## La imagen de muestra

No es opcional: si cambia un color o la paginación, la tira del README queda
mostrando valores que el manual ya no tiene. Cada persona lleva la suya, con sus
propias páginas y sus propios colores de fondo y filete:

| | páginas | fondo | filete |
|---|---|---|---|
| Valentina | 1 · 10 · 7 — portada, logotipo, color | `#EBEAE6` | `#D4D2CB` |
| Ignacia | 1 · 7 · 8 — portada, color, tipografía | `#FAF6EF` | `#E5DBCB` |

**Los números de página cambian si cambia la paginación**, así que confírmalos
contra el PDF antes de montar.

```bash
pdftoppm -png -r 150 -f 1 -l 1 ../manual-valentina.pdf p1   # repetir por página
magick montage p1*.png p10*.png p7*.png -tile 3x1 -geometry +45+45 \
  -border 1 -bordercolor '#D4D2CB' -background '#EBEAE6' -shadow full.png
magick full.png -resize 2200x -background '#EBEAE6' -flatten -depth 8 -strip \
  ../muestra-valentina.png
```
