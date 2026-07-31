[English](README.md) · **Español**

# Identidad Personal

Una skill de Claude Code que te guía, con preguntas, a construir tu propio manual de identidad de marca personal, y te entrega el manual terminado.

> Disponible en español e inglés. La skill detecta o te pregunta el idioma al empezar.

## 1. Qué es y a quién sirve

Un manual de identidad de marca personal fija cómo se ve y cómo suena todo lo que produces: color, tipografía, composición y voz, resueltos una vez para no rediscutirlos en cada pieza.

Esta skill no te da una plantilla para rellenar ni un logotipo hecho al vuelo. Te conduce por el método que produce ese manual con criterio: cierra cada decisión de diseño antes de pasar a la siguiente, te explica por qué conviene una u otra y se detiene a consultarte cuando la elección es tuya. El resultado es un sistema propio, no tu nombre puesto encima de una plantilla ajena.

Sirve a quien produce trabajo a su nombre y quiere que se vea y suene consistente sin contratar un estudio de diseño: profesionales independientes, consultores, docentes, emprendedores.

## 2. Qué hace / Qué no hace

**Qué hace**

- Conduce el proceso de construir tu manual de identidad de marca personal: qué preguntar, en qué orden, qué decidir antes de avanzar y cuándo parar a consultar.
- Te hace tomar las decisiones de diseño con criterio, no eligiendo de un menú: dirección de color, tipografía, jerarquía, firma o logotipo, composición.
- Entrega el manual terminado en HTML autocontenido, listo para imprimir a PDF paginado desde un navegador Chromium.
- Entrega además una **ficha de identidad de una hoja**: la paleta, la tipografía, la firma y las reglas que más se rompen, en una sola página. Es la que tienes abierta mientras trabajas y la que le pasas a quien produzca algo con tu marca. El manual zanja las discusiones; la ficha lleva los valores.
- Documenta y sistematiza tu logotipo si ya tienes uno, o construye la firma nominal tipográfica si no.
- Deja los tokens del sistema (colores por rol, escala tipográfica, versión clara y oscura) para que reutilices la identidad en otras piezas.

**Qué no hace**

- No diseña tu logotipo ni ninguna marca gráfica. Documenta uno que ya exista, no lo dibuja.
- No rellena una plantilla con tus datos. Es un método, no un formulario. Sin tus decisiones, sale un manual correcto y sin carácter.
- No te inventa el propósito ni el posicionamiento. Te ayuda a articular lo que ya haces, no a fabricar una identidad que no tienes.
- No hace identidad corporativa. Es marca de una persona, no de una empresa.
- No produce fotografía ni ilustración, ni gestiona tus redes o tu plan de contenidos. Es el sistema visual y verbal, no la estrategia de difusión.
- No produce por sí misma un .docx de Word. Un documento editable es tarea de [`ooxmlkit`](https://github.com/Carlos-Padilla-Bravo/ooxmlkit), una librería aparte; la skill entrega el HTML y su PDF.
- No reemplaza a un diseñador cuando el encargo excede un sistema documentado.

## 3. Cómo funciona

La skill te va haciendo preguntas y tú respondes. Con eso direcciona el diseño según tus preferencias, cierra cada decisión antes de pasar a la siguiente y al final te entrega el manual.

No traes archivos escritos de antemano. Lo que en otro caso serían tu perfil o tu tono, la skill los arma preguntando. Si ya tienes un bio o notas sobre ti, los puedes entregar para acelerar, pero no es requisito.

El recorrido tiene tres momentos:

**Fundamento: quién eres.** Primero lo que no se ve. La skill extrae, una decisión a la vez, tu esencia (qué haces en una frase), tu territorio (en qué áreas trabajas y qué queda fuera), tu propósito, tu personalidad (marcada con ejemplos de opuestos: más cercano o más sobrio, más técnico o más divulgativo), tus audiencias y tu tono. Esto direcciona todo lo visual: el sistema traduce quién eres, no al revés.

**Sistema visual: cómo se ve.** Con el fundamento cerrado, la skill construye el color (primero la dirección, después los valores: un neutro dominante, un primario y un color de señal racionado, con el contraste verificado por número), la tipografía (primero el carácter, luego una familia de licencia libre y una jerarquía con tope de estilos), tu firma o tu logotipo según lo que tengas, y la composición. En los puntos caros de revertir, color, tipografía y firma, se detiene a consultarte antes de fijar nada.

**El entregable.** La skill arma el manual como HTML autocontenido de una sola página, con las fuentes incrustadas y sin dependencias externas, en versión clara y oscura. En pantalla se lee continuo; al imprimirlo a PDF desde un navegador Chromium sale paginado, con numeración, encabezado y pie. Cierra con la ficha de tokens (colores por rol, escala tipográfica, familias) para que reutilices la identidad en otras piezas. Y te entrega la ficha de una hoja: un manual tiene que justificarse y por eso sale largo, pero nadie abre cuarenta páginas para mirar un hexadecimal, así que los valores de todos los días viven en una hoja aparte.

## 4. Requisitos

- **Claude Code**, o un entorno que soporte skills. Es el motor que ejecuta la skill; sin él, copiar la carpeta no hace nada.
- **Un navegador Chromium** (Chrome o Edge) para el PDF paginado: se imprime con «Gráficos de fondo» activado. No hace falta nada más, y corre en cualquier sistema. En pantalla el manual se lee sin eso.

## 5. Instalación

Esta skill es una carpeta con un archivo `SKILL.md` dentro. Instalarla es dejar esa carpeta donde Claude Code busca sus skills.

1. **Descarga el repositorio.** Con GitHub Desktop, clónalo; o desde la página del repo, «Code» → «Download ZIP» y descomprímelo.
2. **Déjalo en tu carpeta de skills** con el nombre `identidad-personal`, de modo que el `SKILL.md` quede así:

   - macOS y Linux: `~/.claude/skills/identidad-personal/SKILL.md`
   - Windows: `%USERPROFILE%\.claude\skills\identidad-personal\SKILL.md`, es decir `C:\Users\TU-USUARIO\.claude\skills\identidad-personal\SKILL.md`

   El comando sale del nombre de la carpeta, así que debe llamarse `identidad-personal`. Para instalarla solo en un proyecto, usa `.claude/skills/identidad-personal/` dentro de ese proyecto en vez de tu carpeta personal.
3. **Reinicia Claude Code** si la carpeta `skills` no existía antes; si ya existía, la skill aparece sin reiniciar.

Para usarla, pídele a Claude que construya tu manual de identidad de marca personal, o invócala directo con `/identidad-personal`.

## 6. Idioma

La skill funciona en español y en inglés. Detecta el idioma o lo pregunta al empezar, y produce el manual en el idioma que elijas.

## 7. Casos de muestra

El repo incluye dos manuales completos hechos con la skill, uno por cada rama de la decisión de marca. Las dos personas son ficticias, construidas para esto; ningún manual es real.

**Ignacia Fuentes**, nutricionista de consulta y divulgación, de tono cálido y cercano. Su marca es una **firma nominal**, sin logotipo. Paleta cálida (crema, un verde primario y una terracota de señal) y las familias Fraunces, Nunito Sans y Space Mono.

![Tres páginas del manual de Ignacia Fuentes: portada con la firma nominal, sistema de color con la paleta y los contrastes WCAG, y la escala tipográfica.](ejemplo/muestra-ignacia.png)

**Valentina Ortúzar**, arquitecta, de tono preciso y estructural. Su marca es un **logotipo**: un monograma geométrico, así que su manual documenta el módulo de logo (versiones, área de resguardo, tamaño mínimo, usos correctos e incorrectos). Neutros de hormigón cálidos bajo un **azul de plano** frío que estructura y numera, con un amarillo de obra de señal que marca rellenando en vez de teñir el texto, y la familia IBM Plex.

![Tres páginas del manual de Valentina Ortúzar: portada con el monograma, la sección de logotipo con sus versiones y reglas, y el sistema de color.](ejemplo/muestra-valentina.png)

Los dos parten de tonos opuestos, para mostrar que el sistema saca el carácter de cada persona en vez de imponer uno. Cada caso trae el entregable completo: el manual, que se abre en cualquier navegador (`.html`) o se lee como PDF paginado, y su **ficha de identidad de una hoja**.

- Ignacia: manual [`.html`](ejemplo/manual-ignacia.html) · [`.pdf`](ejemplo/manual-ignacia.pdf) de 13 páginas — ficha [`.html`](ejemplo/ficha-ignacia.html) · [`.pdf`](ejemplo/ficha-ignacia.pdf)
- Valentina: manual [`.html`](ejemplo/manual-valentina.html) · [`.pdf`](ejemplo/manual-valentina.pdf) de 15 páginas — ficha [`.html`](ejemplo/ficha-valentina.html) · [`.pdf`](ejemplo/ficha-valentina.pdf)

Vale la pena leer las dos fichas seguidas: llevan la misma estructura y aun así no se parecen, porque cada una está compuesta con los valores de su dueña. Las dos vienen en versión oscura, que es la decisión que corresponde a una pieza que se consulta en pantalla; el botón de la esquina cambia a clara.

## 8. Para qué sirve tu manual

Un manual de identidad no es un documento que archivas. Es la fuente única que mantiene coherente todo lo que produces después. Con él ya construido puedes:

- **Convertirlo en una skill de identidad que conversa con otras skills.** Tu manual puede volverse una skill que las demás consultan: la de presentaciones, la de informes, la de páginas web. Cada una produce su pieza leyendo tu identidad de una sola fuente, sin que tengas que redecidir el color o la tipografía cada vez, y sin que las piezas se desvíen entre sí.
- **Entregárselo a quien trabaje contigo.** Un diseñador o un colaborador produce sobre tu marca sin supervisión, porque las reglas ya están escritas.
- **Resolver casos nuevos con criterio.** Cuando aparece algo que el manual no previó, sus decisiones te dicen qué es coherente con tu marca y qué no.
- **Hacer reconocible tu trabajo con el tiempo.** La consistencia es el activo: piezas hechas en meses distintos se leen como de la misma persona.

## 9. Licencia y estado

Publicado bajo licencia **MIT**. Copyright (c) 2026 Carlos Padilla Bravo. Puedes usar, copiar y modificar la skill, incluso en trabajo pagado, conservando el aviso de autoría.

**Estado: mantención ocasional.** La skill se actualiza cuando el manual de identidad del autor evoluciona y la lección sirve más allá de su caso. No hay promesa de soporte ni de tiempos de respuesta, y los issues están desactivados, así que este no es un canal de soporte. Puedes hacer un fork sin pedir permiso: para eso está la licencia MIT de arriba.

---

Autor: **Carlos Padilla Bravo**

[`ooxmlkit`](https://github.com/Carlos-Padilla-Bravo/ooxmlkit) es una librería aparte, para desarrolladores que quieren una capa que genere un .docx de Word. Esta skill no la usa ni la incluye: entrega el manual en HTML, que imprime el PDF paginado formal en cualquier sistema. `ooxmlkit` solo importa si necesitas un .docx editable, y pide un equipo que esta skill no pide: cerrar el documento exige Windows y Microsoft Word.
