# Botes colgantes (extraíble de basura con botes en una estructura sobre correderas): fichas y propuesta para Skitchen

Investigado el 22/10/2026. Objetivo (pedido del usuario): hacer con el bote colgante lo mismo que con las charolas de esquina: conocer los tamaños comerciales, sus mínimos y adaptar el modelo integrado a ellos.

**Confianza:** *Fabricante* = página oficial del fabricante. *Distribuidor* = ficha de un distribuidor o instalador. *Listado* = revendedor (puede traer errores). Nombres de marca solo como fuente; en el generador siguen sin ir (regla del 21/10).

## 1. Lo que tenemos integrado (A419–A426)

Extraíble de dos botes colgados uno tras otro, con sus propias correderas y su placa de amarre al frente (modelo del usuario `basura_colgante`):

| Dato | Valor |
|---|---|
| Ancho del modelo | 41.05 cm (cabe en un gabinete de **45 cm** de ancho: 45 − 2 × 1.8 de laterales = 41.4) |
| Fondo | 50.7 cm; recorrido 47 cm |
| Alto | 43.4 cm (con patas) |
| Botes | 2, de unos 34 × 23.5 × 35.5 cm (≈ 28 L cada uno) |
| Regla actual | A426: pide un gabinete de 45 como mínimo; si no cabe, avisa y pone el de piso y bastidor |

## 2. Tamaños comerciales encontrados

Ancho = ancho del gabinete que pide el fabricante. Medidas en mm.

| Ancho del gabinete | Herraje (nombre genérico → fuente) | Botes | Medidas de montaje | Confianza |
|---|---|---|---|---|
| **300** | Extraíble de puerta, 3 × 10 L (Tek, Häfele) | 30 L | ancho de instalación 265 · fondo 480 · alto 415 | Listado (Häfele) |
| **300 a 400** | Bin-it Duo I (Hettich), detrás del frente, corredera de extensión total | 20 L + 10 L | no publica medidas en su página | **Fabricante** |
| **400** | Easywaste 2 × 16 L (Häfele) | 32 L | ancho 336 · fondo 469 · alto 356; mín. 400 | Listado |
| **400** | Waste Boss Duo 2 × 32 L (Häfele) | 64 L | ancho 337 · fondo 483; mín. 400 | Listado |
| **450 a 500** | Bin.it Smart (Hettich), se mete en un frente extraíble | 16 + 8 + 8 L = 32 L | ancho 450 a 500 · alto 350 · fondo recortable de 462 a 523; correderas de 470/520 o 500/550 | **Distribuidor** (SFS) |
| **450** | Juego Atira (Hettich) con cajón | 29 + 29 L | alto 510 · ancho 418 · fondo 480 | Listado (kitchenlibrary) |
| **500** | Bin.it Space (Hettich) | 2 × 15 L | hueco 455 × 320 × 320 | Listado |
| **15″ (381)** | Doble inferior de alambre (Rev-A-Shelf) | 2 × 27 a 50 qt (≈ 26 a 47 L) | abertura mín. 15″ con marco; fondo 22¼″ (565); alto 23¼″ (590) | Listado |
| **18″ (457)** | Doble (Vauth-Sagel Envi Space) | 2 × 37 qt (≈ 35 L) | abertura mín. 18″ | Listado |
| **600** | Legra-Bin 52 L / 84 L (Blum, distribuidor) | 2 × 26 L o 2 × 42 L | alto 177 (cajón); ancho interior 564 con marco | Distribuidor (Interfit) |
| **600** | Tandem-Bin 84 L (Blum) | 84 L | corredera de 500 + 3; alto libre 600 | Distribuidor |
| **600** | Envi Space XX Pro (Vauth-Sagel) | 85 L (3 botes) u 88 L (2 botes) | laterales de 16 a 19 | Distribuidor |

## 3. Lo que se repite

1. **Cuatro anchos de gabinete cubren el mercado:** 300, 400, 450 (a 500) y 600 mm. El de 450 es el más común.
2. **El fondo casi no cambia:** 470 a 520 mm (el largo de la corredera). Lo que cambia es el ancho.
3. **El ancho de instalación es unos 25 a 35 mm menor que el interior del gabinete** (336 con 364; 418 con 414; 564 con el interior).
4. **Hasta 500 los botes van uno tras otro** (en tándem); a 600 se ponen lado a lado o se usan tres.
5. **Capacidad total:** 30 L (300), 32 a 64 L (400), 32 a 58 L (450 a 500), 84 a 88 L (600).
6. **Alto del herraje:** 350 a 510 mm; en el gabinete queda el resto hasta la repisa o la cubierta.
7. **No hay ficha técnica completa en las páginas oficiales:** Hettich publica solo el rango de gabinete y las capacidades; las medidas vienen de distribuidores y listados.

## 4. Dónde cae nuestro modelo

Es de la **clase de 450 mm**: 41 cm de ancho (≈ al de 418 de Atira), 50.7 de fondo (≈ 480 a 520) y dos botes de ≈ 28 L (≈ 29 L de Atira, o 2 × 32 L de Waste Boss).

## 5. Propuesta (igual que con las charolas)

1. **Cinco tamaños por ancho de gabinete:** 300, 400, 450 (el modelo, de fábrica), 500 y 600. El interior sale de restar los laterales (30 → 26.4, 40 → 36.4, 45 → 41.4, 50 → 46.4, 60 → 56.4).
2. **Se escala solo a lo ancho, con k = interior / 41.05:** 0.64, 0.89, 1.00, 1.13 y 1.37. El fondo, el alto y el recorrido quedan fijos, porque la corredera y la altura no cambian con el ancho. Los botes en tándem se ensanchan; los herrajes y la corredera se estiran en X.
3. **Aviso, no bloqueo**, igual que con las charolas: si el gabinete queda angosto, alto o bajo para el tamaño, el panel avisa y se genera igual.
4. **El de 600 es el de menos fidelidad:** el mercado lo hace con botes lado a lado y no tándem. Estirar x1.37 deja botes muy anchos (46 × 23.5 cm). Se acepta como aproximación, y un modelo específico de 600 se agrega cuando haya archivo.
5. **Mínimos que se avisan:** ancho del gabinete (por tamaño), alto libre (≥ 45 cm), fondo (≥ 52 cm).

## 6. Fuentes

- Hettich: *Bin.it Duo I 300–400 mm* (página del fabricante, artículo 49476): `shop.hettich.com`.
- Hettich *Bin.it Smart 16 L / 2×8 L, KB 450–500* (SFS, distribuidor suizo): `sfs.ch/CH/en/dl/p/2123369`.
- Hettich *Bin.it Space*, *Atira* (kitchenlibrary.au, dexis.be): listados.
- Häfele (Easywaste, Waste Boss Duo, Tek, listados): `hafele.co.uk` y retailers; las páginas del fabricante devolvieron 403 al leerlas, los datos salen de los buscadores.
- Rev-A-Shelf y Vauth-Sagel: listados de cabinetparts.com y revendedores.
- Blum (Legra-Bin, Tandem-Bin): `interfitco.com` (distribuidor).
