"""Genera el PDF del plan de acción para el hermano de Cristina."""
from pathlib import Path
from weasyprint import HTML, CSS

HTML_DOC = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Plan de acción — Cristina</title>
</head>
<body>

<header class="portada">
  <h1>Plan de acción</h1>
  <h2>Traslado de Cristina a un geriátrico de PAMI en Córdoba</h2>
  <p class="subtitulo">Guía operativa para la familia</p>
  <p class="fecha">Mayo 2026</p>
</header>

<section class="intro">
  <h2>Antes de empezar — leer esto primero</h2>
  <p>Este documento contiene un <strong>plan concreto y verificado</strong> para lograr que PAMI cubra el traslado de Cristina a un geriátrico en Córdoba, donde sí cuenta con familia. Está organizado en tres bloques de tiempo, en orden de prioridad. Cada paso indica <strong>dónde ir, qué llevar y qué decir</strong>.</p>

  <div class="caja-azul">
    <h3>Cinco ideas que conviene tener claras</h3>
    <ol>
      <li><strong>La ley está a favor de Cristina.</strong> La paraplejia con dependencia total activa la Ley 24.901, que obliga a PAMI a cubrir el 100% del geriátrico, incluso fuera de su cartilla y en otra provincia. Hay jurisprudencia firme y casos idénticos ganados.</li>
      <li><strong>No hay que esperar el trámite administrativo de PAMI.</strong> Puede tardar meses. La vía rápida es el <strong>amparo judicial con medida cautelar</strong>, que se resuelve en 48 a 72 horas en casos urgentes como éste.</li>
      <li><strong>El amparo se hace en San Juan, no en Córdoba.</strong> El juzgado federal que corresponde es el del domicilio actual de Cristina. Desde ahí el juez puede ordenar la cobertura en un geriátrico de Córdoba.</li>
      <li><strong>El tiempo en que estás en San Juan es la ventana crítica.</strong> Todo lo presencial conviene hacerlo ahora, antes de tu regreso.</li>
      <li><strong>Cristina no debe quedarse sola ni un día.</strong> Si tenés que regresar antes de obtener la cautelar, hay que contratar un cuidador privado pago (después se pide reintegro) o evaluar internación clínica transitoria.</li>
    </ol>
  </div>
</section>

<div class="page-break"></div>

<section>
  <h2 class="bloque rojo">BLOQUE 1 — Próximas 72 horas</h2>
  <p class="subbloque">Mientras estés en San Juan. Esta es la ventana crítica.</p>

  <article class="paso">
    <h3>Paso 1 — Conseguir un certificado médico (HOY)</h3>
    <p>Pedile a la médica de cabecera de Cristina (de PAMI o particular) un certificado que diga <strong>expresamente</strong>:</p>
    <ul>
      <li>Diagnóstico: paraplejia</li>
      <li>Dependencia total para Actividades de la Vida Diaria (AVD)</li>
      <li>Necesidad de asistencia las 24 horas</li>
      <li><strong>Imposibilidad de trasladarse</strong> a oficinas públicas (esto habilita la visita domiciliaria de la Junta Evaluadora del CUD)</li>
      <li>Riesgo cierto para su salud si queda sin asistencia</li>
      <li>Firma y sello del médico</li>
    </ul>
    <p class="tip">📌 Pedí <strong>4 copias originales</strong>. Cada trámite se lleva una.</p>
  </article>

  <article class="paso">
    <h3>Paso 2 — Iniciar el CUD con pedido de visita domiciliaria</h3>
    <p>Ir presencialmente a:</p>
    <div class="contacto">
      <p><strong>📍 Dirección de Personas con Discapacidad</strong></p>
      <p>Rivadavia 697 (oeste), San Juan</p>
      <p>Tel. <strong>264-421-6606</strong></p>
      <p>Lunes a viernes 7:30 a 12:30 hs</p>
    </div>
    <p>Llevá:</p>
    <ul>
      <li>DNI de Cristina (original y copia)</li>
      <li>Certificado médico del Paso 1</li>
      <li>Resumen de historia clínica</li>
      <li>Nota firmada por vos pidiendo <strong>visita domiciliaria de la Junta Evaluadora</strong> por imposibilidad de traslado de Cristina</li>
    </ul>
    <p class="tip">📌 El CUD ya no tiene vencimiento desde 2024. Una vez emitido, es para siempre.</p>
  </article>

  <article class="paso">
    <h3>Paso 3 — Defensoría del Pueblo de San Juan</h3>
    <p>Este es probablemente el camino más rápido y eficaz, y es gratuito.</p>
    <div class="contacto">
      <p><strong>📍 Defensoría del Pueblo de San Juan</strong></p>
      <p>Dra. Florencia Peñaloza</p>
      <p>Mitre 13 (Este), Capital</p>
      <p>Tel. <strong>(0264) 432-2249 / 432-0333</strong></p>
      <p>Lunes a viernes 7:00 a 13:00 hs</p>
      <p>Web: defensoriadelpueblosj.org</p>
    </div>
    <p>Presentá el caso oralmente y dejá <strong>denuncia escrita</strong> con todos los datos. La Defensoría:</p>
    <ul>
      <li>Puede intervenir directamente ante PAMI y acelerar trámites</li>
      <li>Tiene antecedente reciente: ganaron un amparo colectivo por pensiones por discapacidad en San Juan</li>
      <li>Derivan a un abogado de confianza que litiga en el Juzgado Federal de San Juan</li>
      <li>Es gratuita</li>
    </ul>
  </article>

  <div class="page-break"></div>

  <article class="paso">
    <h3>Paso 4 — Agencia PAMI San Juan (dejar expediente abierto)</h3>
    <p>Acercate a la <strong>agencia PAMI de San Juan</strong> y pedí entrevista con la <strong>trabajadora social</strong> (no con el médico). Explicá la situación: paraplejia, dependencia total, ausencia de red en San Juan, hermano único en Córdoba.</p>
    <p>Pedí:</p>
    <ul>
      <li>Apertura de expediente de <strong>RLE (Residencia de Larga Estadía)</strong> con argumento de vulnerabilidad social</li>
      <li>Visita domiciliaria del equipo interdisciplinario</li>
      <li>Constancia escrita del inicio del trámite</li>
    </ul>
    <p>Llamá también a la línea <strong>138</strong> (PAMI Escucha, 24/7) para dejar registro telefónico de la urgencia.</p>
  </article>

  <article class="paso">
    <h3>Paso 5 — CAJ (Centro de Acceso a la Justicia)</h3>
    <div class="contacto">
      <p><strong>📍 CAJ San Juan</strong></p>
      <p>Sarmiento 184 (Sur), Capital</p>
      <p>Línea nacional <strong>137</strong> (24/7)</p>
    </div>
    <p>Brinda <strong>patrocinio jurídico gratuito federal</strong>. Es alternativa o complemento al abogado privado, por si la Defensoría no asume el caso de inmediato.</p>
  </article>

  <article class="paso">
    <h3>Paso 6 — Contactar abogado especialista (en paralelo)</h3>
    <p>Si la Defensoría o el CAJ no toman el caso de inmediato, contactá uno de estos estudios. Todos atienden todo el país por formulario web:</p>
    <table>
      <thead>
        <tr><th>Estudio</th><th>Web</th></tr>
      </thead>
      <tbody>
        <tr><td>Breit &amp; Asociados / Abogados Amparo</td><td>breit-abogados.ar — abogados-amparo.ar</td></tr>
        <tr><td>Derecho Geriátrico</td><td>derechogeriatrico.com.ar</td></tr>
        <tr><td>Amparando Salud</td><td>amparandosalud.com.ar</td></tr>
      </tbody>
    </table>
    <div class="caja-amarilla">
      <p><strong>Frase clave</strong> para mandar en el primer mensaje (cualquiera de los tres):</p>
      <p class="cita">"Mujer afiliada PAMI en San Juan, paraplejia con dependencia total, sola sin red familiar, CUD en trámite con pedido de visita domiciliaria. Hermano único familiar referente vive en Córdoba. Necesitamos amparo urgente con cautelar para internación geriátrica en Córdoba más acompañamiento 24 hs como medida provisional."</p>
      <p>Eso activa el protocolo de urgencia y suelen responder en horas.</p>
    </div>
  </article>
</section>

<div class="page-break"></div>

<section>
  <h2 class="bloque amarillo">BLOQUE 2 — Días 4 a 10 (amparo en marcha)</h2>
  <p class="subbloque">Una vez identificado el abogado, se presenta el amparo.</p>

  <article class="paso">
    <h3>El amparo de salud</h3>
    <ul>
      <li>Ante el <strong>Juzgado Federal de San Juan</strong></li>
      <li>Contra el INSSJP (PAMI)</li>
      <li>Pidiendo cobertura del 100% de geriátrico en Córdoba</li>
    </ul>
  </article>

  <article class="paso">
    <h3>La medida cautelar innovativa (lo decisivo)</h3>
    <p>Es lo que resuelve la urgencia. Se pide al juez que ordene:</p>
    <ul>
      <li>Cobertura inmediata del 100% del geriátrico</li>
      <li>Si no hay plaza disponible: <strong>acompañante terapéutico 24 hs en domicilio</strong> mientras tanto</li>
      <li>Cobertura de medicamentos, kinesiología, pañales descartables</li>
      <li>35% adicional por dependencia total (Nomenclador)</li>
      <li>Autorización de traslado en ambulancia entre provincias</li>
    </ul>
    <p>Pedir además <strong>beneficio de litigar sin gastos</strong>: no se paga tasa de justicia. Si se gana (que es lo más probable), los honorarios los paga PAMI.</p>
  </article>

  <article class="paso">
    <h3>Mientras se tramita</h3>
    <p>Vos buscás <strong>geriátrico concreto en Córdoba</strong> que acepte el ingreso de Cristina (PAMI conveniado o no, da igual a efectos del amparo). Tener el nombre del geriátrico identificado al momento del amparo le facilita al juez conceder la cautelar.</p>
  </article>
</section>

<section>
  <h2 class="bloque verde">BLOQUE 3 — Tras la cautelar (días 10 a 30)</h2>
  <ol>
    <li>Con la cautelar firme: coordinar el <strong>traslado en ambulancia autorizada</strong> por PAMI desde San Juan a Córdoba.</li>
    <li>Cuando Cristina ingrese al geriátrico de Córdoba: <strong>nota del establecimiento</strong> dirigida a PAMI acreditando internación. La UGL cambia automáticamente a Córdoba.</li>
    <li>Seguir el amparo de fondo (puede tardar meses), pero la cobertura está garantizada desde el día 1 por la cautelar.</li>
  </ol>
</section>

<div class="page-break"></div>

<section>
  <h2>Qué NO hacer</h2>
  <table class="no-si">
    <thead><tr><th class="no">❌ NO</th><th class="si">✅ SÍ</th></tr></thead>
    <tbody>
      <tr><td>Esperar que salga el CUD para iniciar el amparo</td><td>Iniciar amparo con CUD en trámite + certificado médico</td></tr>
      <tr><td>Esperar la respuesta administrativa de PAMI</td><td>Vía judicial en paralelo al trámite administrativo</td></tr>
      <tr><td>Dejar a Cristina sola sin acompañamiento ni un día</td><td>Cuidador privado o internación clínica transitoria si vos volvés antes de la cautelar</td></tr>
      <tr><td>Aceptar plaza geriátrica en San Juan "transitoria"</td><td>Insistir en Córdoba directamente</td></tr>
      <tr><td>Firmar nada de PAMI sin que el abogado lo revise</td><td>Todo por escrito y revisado</td></tr>
    </tbody>
  </table>
</section>

<section>
  <h2>Checklist de documentación para tener lista</h2>
  <ul class="check">
    <li>☐ DNI de Cristina (original + 4 copias)</li>
    <li>☐ DNI tuyo (original + 4 copias)</li>
    <li>☐ Credencial PAMI</li>
    <li>☐ Último recibo de jubilación de Cristina</li>
    <li>☐ Certificado médico con los puntos exactos del Paso 1 (4 originales)</li>
    <li>☐ Resumen de historia clínica reciente (no más de 12 meses)</li>
    <li>☐ Nota escrita tuya sobre ausencia de red familiar en San Juan</li>
    <li>☐ Declaración jurada tuya como referente en Córdoba (con DNI, domicilio, teléfono)</li>
    <li>☐ Nombre y dirección del geriátrico de destino en Córdoba (si ya identificado)</li>
  </ul>
</section>

<section>
  <h2 class="alerta">🚨 Si la situación se complica</h2>
  <p>Si PAMI dilata, si la cautelar tarda, si Cristina queda en riesgo en cualquier momento:</p>
  <ol>
    <li>Llamar a la <strong>Defensoría del Pueblo de la Nación: 0800-333-3762</strong></li>
    <li>Llamar a la <strong>Línea 137</strong> (asesoramiento legal 24/7)</li>
    <li><strong>Internar a Cristina en una clínica</strong>: eso activa la urgencia médica y los plazos del juez se aceleran</li>
    <li>Llamar al <strong>abogado al celular</strong> (no email): estas situaciones son cautelares "de hora"</li>
  </ol>
</section>

<div class="page-break"></div>

<section>
  <h2>Resumen visual del orden</h2>
  <pre class="esquema">
HOY
 │
 ├── Médico → certificado con puntos clave
 │
 ├── Rivadavia 697 oeste → CUD + visita domiciliaria
 │
 ├── Mitre 13 Este → Defensoría del Pueblo San Juan
 │
 ├── Agencia PAMI San Juan → trabajadora social, expediente RLE
 │
 ├── Sarmiento 184 Sur → CAJ (patrocinio gratuito)
 │
 └── En paralelo: contactar estudio jurídico online

DÍAS 4 a 10
 │
 ├── Amparo en Juzgado Federal de San Juan
 ├── Pedido de cautelar (resolución 48 a 72 hs)
 └── Identificar geriátrico en Córdoba

DÍAS 10 a 30
 │
 ├── Traslado en ambulancia (autorizado por PAMI por orden judicial)
 ├── Ingreso al geriátrico en Córdoba
 └── Cambio de UGL a Córdoba (con nota del establecimiento)
  </pre>
</section>

<footer class="pie">
  <p>Plan elaborado con información verificada a mayo de 2026.</p>
  <p>Las condiciones pueden variar; consultar con abogado antes de cada paso decisivo.</p>
</footer>

</body>
</html>
"""

CSS_DOC = """
@page {
  size: A4;
  margin: 2cm 1.8cm 2cm 1.8cm;
  @bottom-right {
    content: "Página " counter(page) " de " counter(pages);
    font-size: 9pt;
    color: #888;
  }
  @bottom-left {
    content: "Plan de acción — Cristina";
    font-size: 9pt;
    color: #888;
  }
}

body {
  font-family: "Helvetica", "Arial", sans-serif;
  font-size: 11pt;
  line-height: 1.5;
  color: #222;
}

.portada {
  text-align: center;
  padding: 4cm 0 3cm 0;
  border-bottom: 3px solid #2c5282;
  margin-bottom: 1.5cm;
}

.portada h1 {
  font-size: 32pt;
  color: #2c5282;
  margin: 0;
  letter-spacing: -1px;
}

.portada h2 {
  font-size: 18pt;
  color: #444;
  margin: 0.3cm 0;
  font-weight: 500;
}

.portada .subtitulo {
  font-size: 13pt;
  color: #666;
  margin-top: 1cm;
  font-style: italic;
}

.portada .fecha {
  margin-top: 2cm;
  color: #888;
}

h2 {
  color: #2c5282;
  font-size: 17pt;
  border-bottom: 2px solid #e0e0e0;
  padding-bottom: 0.2cm;
  margin-top: 1cm;
}

h2.bloque {
  color: white;
  padding: 0.4cm 0.6cm;
  border-radius: 4px;
  border-bottom: none;
}

h2.bloque.rojo { background: #c53030; }
h2.bloque.amarillo { background: #d69e2e; }
h2.bloque.verde { background: #2f855a; }

h2.alerta {
  color: #c53030;
  border-bottom-color: #c53030;
}

.subbloque {
  color: #666;
  font-style: italic;
  margin-top: -0.3cm;
  margin-bottom: 0.6cm;
}

h3 {
  color: #2c5282;
  font-size: 12pt;
  margin-top: 0.6cm;
}

.paso {
  margin-bottom: 0.5cm;
  padding-bottom: 0.3cm;
}

.contacto {
  background: #f7fafc;
  border-left: 4px solid #2c5282;
  padding: 0.3cm 0.5cm;
  margin: 0.3cm 0;
  font-size: 10.5pt;
}

.contacto p { margin: 0.1cm 0; }

.caja-azul {
  background: #ebf8ff;
  border: 1px solid #bee3f8;
  border-radius: 4px;
  padding: 0.4cm 0.6cm;
  margin: 0.5cm 0;
}

.caja-azul h3 {
  margin-top: 0;
  color: #2c5282;
}

.caja-amarilla {
  background: #fffbeb;
  border: 1px solid #fde68a;
  border-radius: 4px;
  padding: 0.4cm 0.6cm;
  margin: 0.4cm 0;
}

.cita {
  font-style: italic;
  background: white;
  padding: 0.3cm 0.5cm;
  border-left: 3px solid #d69e2e;
  margin: 0.3cm 0;
}

.tip {
  background: #f0fff4;
  border-left: 3px solid #38a169;
  padding: 0.2cm 0.4cm;
  margin-top: 0.3cm;
  font-size: 10.5pt;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.3cm 0;
  font-size: 10.5pt;
}

th, td {
  border: 1px solid #ccc;
  padding: 0.2cm 0.3cm;
  text-align: left;
  vertical-align: top;
}

th {
  background: #edf2f7;
  font-weight: 600;
}

table.no-si th.no { background: #fed7d7; color: #742a2a; }
table.no-si th.si { background: #c6f6d5; color: #22543d; }

ul.check {
  list-style: none;
  padding-left: 0.3cm;
  font-size: 11pt;
  line-height: 1.7;
}

.esquema {
  background: #f7fafc;
  padding: 0.6cm;
  border-radius: 4px;
  font-family: "Courier New", monospace;
  font-size: 10pt;
  line-height: 1.4;
  white-space: pre;
}

.page-break {
  page-break-after: always;
}

.pie {
  margin-top: 2cm;
  padding-top: 0.5cm;
  border-top: 1px solid #e0e0e0;
  font-size: 9.5pt;
  color: #888;
  text-align: center;
}

section { page-break-inside: avoid; }
article.paso { page-break-inside: avoid; }
"""


def main():
    out_dir = Path(__file__).parent
    html_path = out_dir / "plan_accion_hermano.html"
    pdf_path = out_dir / "plan_accion_hermano.pdf"

    html_path.write_text(HTML_DOC, encoding="utf-8")
    HTML(string=HTML_DOC).write_pdf(
        pdf_path,
        stylesheets=[CSS(string=CSS_DOC)],
    )
    print(f"PDF generado: {pdf_path}")


if __name__ == "__main__":
    main()
