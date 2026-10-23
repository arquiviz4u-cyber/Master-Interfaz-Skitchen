# Análisis del manual «El Cocinator» contra el master (21/10/2026)

Fuente: `F:\00_Drawlibri\Fuentes y referencias\Manual_Cocinas_Erick_Alejandro_Moya_Olmos.pdf` (233 páginas, versión 1.0).
Licencia del ejemplar: personal, prohibida su redistribución. De aquí se toman **datos y criterios** (medidas, cantidades, reglas), nunca texto ni figuras.
El libro es práctica de un taller mexicano, no una norma: donde difiera de NKBA o del master decide el usuario. Leído: partes II a VII, IX y anexos B, C y D. Solo hojeado: parte I (estética), pasos 35–43 y parte VIII (SketchUp / render con IA).

## 1. Coincide con el master (sin cambios)

| Dato | Libro | Master |
|---|---|---|
| Holgura entre puertas | 3 mm | `PLAN_HOLGURA_PUERTA = .3` |
| Separación entre frentes de cajón sin amarre | 3 mm | `separacionFrentes: .3` |
| Fondo de mueble bajo | 60 cm | `fondoBajos: 60` |
| Salpicadero (separación cubierta–altos) | 60 cm | `separacionAltos: 60` |
| Espesor de cuerpo y frentes | 18 mm | `espesorFrente: 1.8`, `PLAN_CUERPO.lateral: 1.8` |
| Corredera: cajón 2.6 cm menor que el ancho interior | 2.6 cm | `PLAN_CAJA.holgura 1.3` por lado |
| Holgura de ventilación trasera del refri | 5–10 cm | `holguraRefri: 5` |
| Ventilación del horno | según ficha | `ventilacionHorno: 5` |
| Pasillo mínimo con gabinetes | 90 cm | aviso a 107 cm (NKBA) |

## 2. Diferencias a decidir (el master dice una cosa, el libro otra)

| Tema | Libro | Master (MX) | Nota |
|---|---|---|---|
| Altura total de la cubierta | 90–92 cm (85 si el usuario mide < 1.55 m; 95–100 si > 1.85 m) | `baseBajos 10 + altoBajos 72 + cubierta 3 = 85` | Suponiendo que esos tres campos suman la altura de trabajo. **Verificar**: si es así, el valor de inicio queda en el extremo bajo. |
| Zócalo | 13 cm de alto, 50 cm de fondo | `baseBajos: 10` | El libro hace 13 + 75 (caja) + 2 (cubierta) = 90. |
| Fondo de altos | 30–32 cm (25–28 sobre la tarja) | `fondoAltos: 35` | Argumento del libro: alcance del brazo y platos de 27 cm. |
| Pasillo | 90 mínimo / 110 cómodo / 120 ideal | aviso a 107 | 107 es NKBA (US); en MX el 90 del libro es el mínimo. Decidir por región. |
| Espesor de cubierta | 2 cm cuarzo, 3 cm granito | `espesorCubierta: 3` | Solo opción por material. |

## 3. Reglas que el master no tiene (candidatas a avisos o a geometría)

Ordenadas por valor para Skitchen. «Aviso» = mismo mecanismo que los avisos NKBA ya existentes.

**Alta**
1. **Sistema 32** (cap. 51): taladros en cuadrícula de 32 mm, serie desde 37 mm del borde, dos filas (37 mm del frente y 37 mm del fondo), repisas ajustables en esos puntos. No existe en el master; lo necesitan la lista de despiece y el plano para taller.
2. **Separación mínima de 10 cm entre cajones internos** cuando hay puerta delante (bisagra de 6.2 cm); con bisagra de 165° se aceptan 8 cm. Frente de cajón interior 2 mm hacia adentro.
3. **Número de bisagras por alto de puerta**: 2 hasta 90 cm, 3 de 90 a 150, 4 más. A 10 cm de los extremos. El master lo tiene anotado como «sin resolver» (A-nota de la auditoría Blum, p. 77/413); esta es una regla simple para cerrarlo.
4. **Plano de instalaciones** (parte de la hoja de ruta «pro»): contactos a 115 cm sobre la cubierta (mínimo 2 por cubierta de trabajo), contacto de campana a 180 cm, contacto dentro del mueble a 15 cm de la pared, en esquina a ≥ 60 cm del rincón, ningún mueble tapa un apagador. El libro da la lista de qué acotar.
5. **Dos medidas por equipo: reposo y uso** (tapa de cristal de la parrilla levantada contra la campana, puerta del refri abierta, canasta del lavavajillas). El master ya dibuja abatimientos; falta el chequeo tapa-contra-campana.
6. **Torres hasta 244 cm** (largo del tablero estándar); más alto se parte en dos muebles superpuestos. Microondas centrado a 1.50 m (rango 1.40–1.60), rejilla del horno a 1.10 m (rango 0.90–1.20), ventilación del microondas 3–5 cm a los lados y arriba.
7. **Refrigerador**: no en la esquina interna ni a menos de 45 cm si su puerta abre hacia ella; ≥ 15 cm de una ventana; ≥ 30 cm de la estufa si son contiguos; 8–10 cm de holgura al ancho del hueco; 5 cm arriba.
8. **Estufa**: ≥ 30 cm de cubierta a cada lado; ≥ 60 cm (ideal 90) a la tarja; no centrada en pared con ventana; nada de cubertero metálico debajo.

**Media**
9. **Pasillos por situación**: 90 / 110 / 120 (una persona); 110–140 (una trabaja y otra pasa); 120–160 (dos trabajando); 120–180 (silla de ruedas). Frente a cada equipo 90 libres. En paralela con pasillo de 90, desfasar tarja y estufa.
10. **Triángulo de trabajo**: lados 1.2–2.1 m (refri–tarja, tarja–estufa) y 1.2–2.7 m (estufa–refri); suma 4–8 m. Aviso informativo.
11. **Isla / barra / península**: pasillo alrededor 90 mínimo, 120 ideal; volado de barra 30–45 cm; 60–75 cm de ancho por taburete; alturas 75 / 90 / 110. Península sin espacio para cuatro accesos.
12. **Esquineros**: puerta ≥ 30 cm; 90 cm libres al frente (si no, ciego); cubierta ≥ 90 cm de profundidad en la esquina; tira de relleno 5–8 cm; jaladera a 5 cm del costado vecino. Las cuatro opciones en orden: L, ciego, diamante, frente sólido.
13. **Modulación**: múltiplos de 15 cm (20 cm en cocinas pequeñas); sobrante → tira de relleno (hasta 15 cm), panel terminal o mueble fuera de módulo (> 25 cm). Anchos usuales 30/45/60/75/90/100.
14. **Margen alto–techo 3 cm** y plafón. Nichos y vidrio: no más de un tercio de los altos.
15. **Cajones**: proporción de alturas 1 : 1.2 : 1.6 (superior, medio, inferior); privilegiar cajones sobre puertas (excepto tarja y parrilla de empotrar); cajón mínimo útil.
16. **Cajón por dentro** (cap. 53): fondo de 6 mm estándar (3, 9, 12–15 según uso), ranura a 5 mm del borde inferior, fondo atornillado solo desde 12 mm, un tornillo 4×16 por cada 30 cm de ancho, testero posterior sin ranura.

**Baja o de producto**
17. **Cantos y despiece**: canto de 2 mm preferido (0.45 / 1 / 2 / 3); el canto suma a la medida (2 mm × 2 por dirección); frentes con 4 cantos, laterales con 1 canto al frente, fondos sin canto; lista de piezas con letra, nombre, cantidad, largo, ancho, material y espesor, cantos; hoja 2440 × 1220; veta a lo largo del tablero (122 cm).
18. **Melamina RH** (resistente a humedad) en el costado hacia el lavavajillas y bajo la tarja; regatones bajo lavavajillas y refri.
19. **Uniones**: confirmat (taladro 7 mm en la pieza que pasa, 5 mm en el canto), espigos de 6 u 8 mm con cola, grapas de 32–40 mm, pocket hole a 15°. Útil para el instructivo de armado.
20. **Anclaje**: 2 + 2 puntos hasta 60 cm de ancho, 3 + 3 en más anchos; mampostería 5×60 mm; tablaroca con anclaje específico o refuerzo.
21. **Nomenclatura** de muebles `a-apv-6` (letra de orden – tipo – número de piezas) con códigos apv, aph, bpv, bc, bpc, esl, esc, esd, T, TR, Th, bex, bf, bh. Opción para exportar despiece en MX. **Decisión 22/10: no se usa; el despiece llevará una nomenclatura convencional propia (A447).**
22. **Glosario con sinónimos de Latinoamérica** (anexo A): fregadero = tarja (MX) = pileta (AR) = lavaplatos (CL, CO). Sirve para la interfaz en español por región.
23. **Checklist de entrega** (anexo C, por paso) y **lista de errores frecuentes** (anexo D): 40–60 comprobaciones que casi todas ya son avisos o pueden serlo. Una vista «Revisión final» en Presentar.
24. **Parte I (estética)**: 60/30/10, regla 5-7 de luz, temperaturas de color (2700–3000 cálida, 3500–4000 cocina, 5000–6500 tarea precisa), regla de tres texturas. Material para el asistente de color, no para la geometría.

## 4. Advertencias sobre el libro

- Algunas cifras son prácticas de un taller, sin cita (por ejemplo «altura de mueble bajo 75–90 sin cubierta» y «cubierta 90–92» no cuadran sin el zócalo de 13 cm).
- Para herrajes manda el catálogo del fabricante (Blum ya está extraído en el proyecto); el libro solo da reglas generales.
- Sistema 32: el libro no distingue entre construcción sin marco (europea) y con marco de cara (US). Skitchen debería aplicarlo solo donde corresponda.
- El libro no cubre NKBA; las convenciones de EE. UU. siguen saliendo de ahí.

## 5. Siguiente paso propuesto

1. El usuario marca qué diferencias de la sección 2 se corrigen y qué reglas de la sección 3 entran.
2. Cada una entra al master como regla con nota PENDIENTE DE INTEGRAR y prueba en `pruebasPlanDePiezas` (o aviso con texto en español).
3. Cambios que toquen el plan de piezas se coordinan con «Skitchen for sketchup» y «Skitchen for Revit».
