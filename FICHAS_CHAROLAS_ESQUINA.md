# Charolas de esquina (ciego): fichas de fabricantes y propuesta para Skitchen

Investigado el 22/10/2026. Objetivo (pedido del usuario): tener el dato del ancho mínimo de puerta y de gabinete en varias marcas, para saber qué proponer en Skitchen si el cliente compra un herraje distinto al integrado.

**Confianza:** *Ficha* = leída en el documento del fabricante o su distribuidor oficial. *Listado* = ficha de un revendedor (puede estar mal copiada). Los nombres de marca aparecen aquí solo como fuente de datos; en el generador siguen sin ir (regla del 21/10).

## 1. Datos encontrados

Medidas en mm (pulgadas entre paréntesis donde la fuente las da así). **A** = abertura libre de la puerta del gabinete; **B** = ancho interior del gabinete.

| Herraje | Abertura mín. de puerta (A) | Ancho interior (B) | Otros mínimos | Fuente / confianza |
|---|---|---|---|---|
| **LeMans II (45)** | 410 con marco · 435 sin marco | 820 | puerta abre ≥ 85°; fondo libre 500; alto libre 545; espesor de puerta ≤ 19 | Ficha de instalación MA 402121 (21/03/2012), página 3 |
| **LeMans II (50)** | 450 con marco · 475 sin marco | 920 | igual | misma ficha |
| **LeMans II (60)** | 540 con marco · 565 sin marco | 965 | igual | misma ficha |
| **MagicCorner II** | 495 (19 ½″) | fondo de ciego 960 a 1 170 (37¾″ a 46″) | fondo de gabinete 500 (19¾″); alto libre 525 (20⅝″); 9 kg por charola | Ficha del distribuidor (Würth, PDF de la propia marca) |
| MagicCorner II (otra fuente) | 520 (20½″) y holgura para la bisagra | — | cap. 1 138 in² | Listado (Microvellum, Häfele) · **discrepa 25 mm con la ficha de arriba** |
| **MagicCorner I** | 396 (15⅝″) con charola frontal de 295 · 492 (19⅜″) con la de 390 | interior 974 a 1 115 | charolas 295/390 × 470 × 88; 14 kg y 18 kg; puertas de 450 a 600; alto libre 525; gabinete exterior de 900 o 1 000 | Listados + página del fabricante (EE. UU.) |
| **MagicCorner Comfort** | — | exterior 900 a 1 000 | fondo 500; alto 545; puerta abre 90° | Listado (Clutterfree) |
| **Le-Mans (cuatro charolas, Reino Unido)** | puerta 450 → interior mín. 860 · 500 → 960 · 600 → 960 | ver columna A | abre ≥ 85°; solo puertas sobrepuestas; fondo 500; alto 600 a 750 | Listado de instalador |
| **Hettich Magic Corner universal** | puerta de 450 | gabinete 900 o 1 000 | 608 × 455 × 584; 20 kg | Listados (la marca no publica la tabla en lo encontrado) |
| **Rev-A-Shelf (optimizer, EE. UU.)** | 15″ o 18″ (381 o 457) | gabinetes de 45″ | fondo de abertura 20¼″ a 22 13/32″; alto 22″ a 25″ | Listados de revendedor |
| **Vauth-Sagel (Cornerstone, Scalea)** | 15″, 17½″, 21″ o 24″ con marco; +1⅛″ sin marco en 21″ | — | solo mínimos de abertura de cada modelo | Listados |

## 2. Qué se repite en todas las marcas

1. **La abertura de la puerta depende de la charola delantera, no del gabinete.** Sale entre 396 y 565 mm: la de la charola más ancha que tiene que cruzar el hueco, más 2 a 3 cm de holgura y la bisagra.
2. **El gabinete se mide en el ancho total (B), no en el de la puerta.** 820 a 965 (LeMans) y 974 a 1 115 (Magic Corner).
3. **Con marco vs sin marco** cambia la abertura unos 25 mm (el marco la reduce), y solo en EE. UU.
4. **La puerta tiene que abrir a 85° o más** y casi todos piden puertas **sobrepuestas**, por la bisagra.
5. **Fondo libre 500 mm y alto libre 525 a 600 mm** son comunes a todos.
6. **No hay un dato universal.** Cada modelo y cada tamaño de charola traen el suyo; los listados de revendedor discrepan hasta 25 mm entre sí.

## 3. Lo que tiene hoy Skitchen (A407 a A415)

- Modelo integrado: charolas de ≈ 80 cm de largo con puerta de **50.2 cm** (del mecanismo, no fija) y ancho mínimo del ciego **120.5 cm con fondos de 60** (A413, incluye la bisagra de 155° y la zona del brazo).
- Es de la clase MagicCorner I/II (puerta 450 a 600, interior 97 a 111 cm). Su puerta de 50.2 cm cae dentro del rango de todas las fichas de esa clase.

## 4. Propuesta para Skitchen si el cliente compra otro herraje

1. **Catálogo de herrajes de esquina por modelo, con datos y sin marca**: cada entrada guarda `{ aberturaPuerta (con y sin marco), anchoInterior {min, max}, fondoLibre, altoLibre, anguloPuerta, sobrepuesta }`. Hoy esos datos están fijos en `CHAROLAS` del master; pasarían a una lista de modelos y el editor elegiría uno («Charolas de esquina, clase A / B / C»).
2. **El ancho del ciego sale de la ficha elegida**: `ancho mínimo = max(B.min, aberturaPuerta + espesores + parte ciega)`; si el usuario pone menos, se avisa y el ciego crece (igual que hoy con `charolasAnchoMin`).
3. **Sin ficha (modelo desconocido o el cliente solo dice «magic corner»)**: valores genéricos conservadores, que son los que más se repiten: puerta ≥ **500 mm** (≥ 450 con marco), gabinete **≥ 900 mm** de interior, fondo ≥ 500, alto ≥ 545, puerta abre ≥ 85° y sobrepuesta. Ahí el editor **avisa**, no bloquea.
4. **Con marco (EE. UU.)**: restar 25 mm a la abertura efectiva y pedir puerta sobrepuesta.
5. **Pendiente de decisión del usuario**: cuántos modelos entran al catálogo y si se piden las fichas oficiales a cada marca (los datos de esta tabla son de revendedores salvo LeMans II y MagicCorner II, que sí vienen de documentos de la marca).

## 5. Fuentes

- Kesseböhmer, *LeMans II* ficha de instalación MA 402121 0000 (21/03/2012), vía Richelieu / Häfele (PDF leído en la sesión).
- Würth, *MagicCorner II Blind Corner Solution* (PDF de la hoja de especificaciones): `xcart.wurthlac.com/skin/common_files/files/specs/MagicCorner-SpecSheet.pdf`
- Kesseböhmer EE. UU., página del MagicCorner I: `kesseboehmer.us/kitchen/corner-cabinets/magic-corner`
- Microvellum, *Foundation Hardware Highlight: Kesseböhmer* (MagicCorner II, 520 mm).
- Clutterfree Kitchens, *Le-Mans Fluid Corner System*, y *Peka Libell Magic Corner Comfort* (tabla puerta/ancho interior).
- Häfele EE. UU., *Peka Magic Corner II* (listado); ferguson/dkhardware/cabinetparts (listados de LeMans II y Magic Corner Series).
- Hettich Magic Corner universal: listados en home-run.co, kyzo.in, hardwaredepot.in (sin ficha oficial).
- Rev-A-Shelf y Vauth-Sagel: listados de wurthlac.com y cabinetparts.com (sin hoja de instalación oficial).
