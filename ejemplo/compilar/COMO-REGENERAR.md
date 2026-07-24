# Cómo regenerar los manuales de ejemplo

Los manuales `ejemplo/manual-ignacia.html` y `ejemplo/manual-valentina.html` son
archivos finales autocontenidos: llevan las tipografías incrustadas en base64. No
se editan a mano. Se compilan desde el material de esta carpeta.

Para cada manual hay dos piezas:

- `manual-<nombre>.src.html` — el HTML editable, con un marcador `/*FONTS*/` en el
  `<style>` donde van las fuentes. **Aquí se edita el contenido.**
- `fuentes-<nombre>.css` — las reglas `@font-face` con las tipografías en base64.

## 1. Editar

Abre el `.src.html` y cambia lo que necesites: texto, paleta (los tokens en
`:root`), estructura. El marcador `/*FONTS*/` se queda donde está.

## 2. Armar el HTML final

Reemplaza el marcador por el CSS de fuentes y escribe el archivo publicado. Desde
esta carpeta:

```bash
python -c "src=open('manual-valentina.src.html',encoding='utf-8').read(); css=open('fuentes-valentina.css',encoding='utf-8').read(); open('../manual-valentina.html','w',encoding='utf-8').write(src.replace('/*FONTS*/',css,1))"
```

(Para Ignacia, cambia los tres nombres de archivo.)

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

## 4. Verificar

Revisa el PDF página por página: que no haya páginas en blanco, que los números
del índice cuadren con las páginas reales y que la partición de palabras no deje
nada feo. La paginación (numeración, encabezado, pie, filete) la dibujan las cajas
`@page` del CSS; no hace falta ninguna librería.

## Las tipografías

- **Valentina** usa IBM Plex (Sans y Mono), SIL OFL 1.1. El `fuentes-valentina.css`
  se generó con `subset-plex.py`, que subconjunta a Latin y comprime a woff2. Solo
  hace falta correrlo si cambian las fuentes o los pesos; para editar contenido, no.
- **Ignacia** usa Fraunces, Nunito Sans y Space Mono, también OFL. Su
  `fuentes-ignacia.css` es el bloque `@font-face` tal como quedó incrustado; no se
  guardó su script de subconjuntado.

## La imagen de muestra (opcional)

Las tiras `ejemplo/muestra-<nombre>.png` del README se arman con páginas del PDF:

```bash
pdftoppm -png -r 150 -f 1 -l 1 ../manual-valentina.pdf p1   # repetir por página
magick montage p1*.png p9*.png p7*.png -tile 3x1 -geometry +45+45 \
  -border 1 -bordercolor '#D4D2CB' -background '#EBEAE6' -shadow full.png
magick full.png -resize 2200x -background '#EBEAE6' -flatten -depth 8 -strip \
  ../muestra-valentina.png
```
