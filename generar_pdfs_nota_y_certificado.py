"""Genera dos PDFs:
- Nota dirigida a la Defensoría del Pueblo de San Juan
- Modelo de certificado médico para el amparo
"""
from pathlib import Path
from weasyprint import HTML, CSS

# ============================================================
# NOTA A LA DEFENSORÍA DEL PUEBLO DE SAN JUAN
# ============================================================

NOTA_HTML = """<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Nota Defensoría</title></head>
<body>

<div class="fecha-lugar">San Juan, [_____] de [____________] de 2026.</div>

<div class="destinatario">
  <p><strong>Sra. Defensora del Pueblo de San Juan</strong><br>
  <strong>Dra. Florencia Peñaloza</strong><br>
  <strong>Su Despacho</strong></p>
</div>

<div class="asunto">
  <p><strong>Asunto:</strong> Solicitud de intervención urgente — Persona con discapacidad afiliada a PAMI sin red de contención familiar en la provincia.</p>
</div>

<div class="ref">
  <p><strong>Ref.:</strong> Sra. [NOMBRE Y APELLIDO DE CRISTINA], DNI N° [_______________], afiliada PAMI N° [_______________].</p>
</div>

<p>De mi mayor consideración:</p>

<p>Me dirijo a Ud. a fin de solicitar la <strong>intervención urgente</strong> de la Defensoría del Pueblo de la Provincia de San Juan, en su carácter de garante de los derechos humanos y, en particular, de los derechos de las personas mayores y de las personas con discapacidad, conforme las atribuciones que le competen.</p>

<h3>I. IDENTIFICACIÓN DEL PRESENTANTE</h3>

<p>Quien suscribe, <strong>[NOMBRE Y APELLIDO DEL HERMANO]</strong>, DNI N° [_______________], con domicilio real en [_____________________________________________], provincia de Córdoba, teléfono de contacto [_______________], correo electrónico [_______________], en mi carácter de <strong>hermano y único familiar referente</strong> de la afiliada arriba identificada, vengo a poner en conocimiento de esa Defensoría la siguiente situación.</p>

<h3>II. HECHOS</h3>

<p><strong>1.</strong> Mi hermana, Sra. [NOMBRE Y APELLIDO DE CRISTINA], de [___] años de edad, padece <strong>paraplejia con dependencia funcional total</strong> para las actividades de la vida diaria, conforme surge del certificado médico que se acompaña como Anexo I.</p>

<p><strong>2.</strong> Su estado de salud requiere <strong>asistencia y acompañamiento durante las veinticuatro (24) horas del día</strong>, no pudiendo permanecer sola sin riesgo cierto para su vida e integridad física.</p>

<p><strong>3.</strong> La afiliada reside actualmente en su domicilio particular sito en [DOMICILIO COMPLETO EN SAN JUAN], en la provincia de San Juan, <strong>completamente sola y sin red de contención familiar alguna</strong> en esta provincia.</p>

<p><strong>4.</strong> Quien suscribe es su único familiar y reside en la Provincia de Córdoba. Me encuentro en este momento acompañándola en San Juan de manera transitoria, no pudiendo prolongar mi estadía por razones laborales y familiares en mi provincia de residencia.</p>

<p><strong>5.</strong> Hasta la fecha <strong>no se ha iniciado ningún trámite ante PAMI</strong> tendiente a obtener una plaza en el Programa de Residencias de Larga Estadía (RLE), por lo que la situación de vulnerabilidad es de absoluta urgencia.</p>

<p><strong>6.</strong> Asimismo, encontrándose la afiliada imposibilitada de trasladarse a oficinas públicas en virtud de su patología, <strong>tampoco cuenta con el Certificado Único de Discapacidad (CUD)</strong>, instrumento indispensable para acceder a la cobertura integral prevista en la Ley 24.901.</p>

<h3>III. DERECHO INVOCADO</h3>

<p>La situación expuesta configura una clara vulneración del derecho a la salud, a la vida digna y a los cuidados, garantizados por:</p>

<ul>
  <li>La <strong>Constitución Nacional</strong> (arts. 33, 42, 75 inc. 22 y 23);</li>
  <li>La <strong>Convención sobre los Derechos de las Personas con Discapacidad</strong> (Ley 26.378, con jerarquía constitucional);</li>
  <li>La <strong>Convención Interamericana sobre la Protección de los Derechos Humanos de las Personas Mayores</strong> (Ley 27.360);</li>
  <li>La <strong>Ley 24.901</strong> — Sistema de Prestaciones Básicas en Habilitación y Rehabilitación Integral a favor de las Personas con Discapacidad, que obliga a los agentes de salud estatales como el INSSJP (PAMI) a la cobertura del 100% de las prestaciones requeridas;</li>
  <li>La <strong>Ley 22.431</strong> — Sistema de Protección Integral de las Personas con Discapacidad.</li>
</ul>

<p>La jurisprudencia federal es uniforme en sostener la obligación de PAMI de cubrir la internación geriátrica de personas con discapacidad y dependencia total, aun en establecimientos no incluidos en su cartilla, incluyendo el adicional del 35% por dependencia previsto en el Nomenclador.</p>

<h3>IV. OBJETO DE LA PRESENTACIÓN</h3>

<p>En virtud de lo expuesto, solicito a esa Defensoría:</p>

<p><strong>1.</strong> Tenga por iniciada la presente actuación y disponga su intervención inmediata ante el INSSJP — UGL San Juan, a fin de obtener:</p>

<ul>
  <li>La <strong>evaluación socio-sanitaria urgente</strong> por parte del equipo interdisciplinario de PAMI;</li>
  <li>La asignación de una <strong>plaza en Residencia de Larga Estadía (RLE) en la Provincia de Córdoba</strong>, donde la afiliada cuenta con red de contención familiar;</li>
  <li>La autorización del <strong>traslado interprovincial</strong> en ambulancia conforme protocolo del CODE.</li>
</ul>

<p><strong>2.</strong> Inste a la Junta Evaluadora provincial a realizar una <strong>visita domiciliaria</strong> a los fines de la emisión del Certificado Único de Discapacidad, atento la imposibilidad física de traslado de la afiliada.</p>

<p><strong>3.</strong> Derive el caso, en caso de corresponder, a la <strong>Red Federal de Patrocinio Jurídico Gratuito</strong> o asesore sobre los pasos para la presentación de un eventual amparo judicial con medida cautelar ante el Juzgado Federal de San Juan.</p>

<p><strong>4.</strong> Mantenga informado al suscripto de cada actuación, al correo y teléfono indicados ut supra.</p>

<h3>V. DOCUMENTACIÓN QUE SE ACOMPAÑA</h3>

<ul class="anexos">
  <li>Anexo I — Certificado médico de la afiliada</li>
  <li>Anexo II — Fotocopia de DNI de la afiliada</li>
  <li>Anexo III — Fotocopia de credencial de afiliación PAMI</li>
  <li>Anexo IV — Fotocopia de DNI del suscripto</li>
  <li>Anexo V — Declaración jurada del suscripto como referente familiar en la provincia de destino</li>
</ul>

<h3>VI. PETITORIO</h3>

<p>Por todo lo expuesto, solicito a la Sra. Defensora del Pueblo:</p>

<p><strong>a)</strong> Tenga por presentada la presente y por constituido domicilio según se indica.</p>
<p><strong>b)</strong> Disponga la intervención urgente solicitada.</p>
<p><strong>c)</strong> Provea de conformidad.</p>

<p class="cierre">Sin otro particular, saludo a Ud. con atenta y distinguida consideración.</p>

<div class="firma">
  <div class="linea-firma">_________________________________</div>
  <p>Firma y aclaración<br>
  [NOMBRE Y APELLIDO DEL HERMANO]<br>
  DNI N° [_______________]</p>
</div>

</body></html>
"""

# ============================================================
# CERTIFICADO MÉDICO
# ============================================================

CERTIFICADO_HTML = """<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Certificado Médico</title></head>
<body>

<div class="encabezado-medico">
  <p class="lugar-medico">[Membrete del médico o sello correspondiente]</p>
</div>

<h1 class="titulo-cert">CERTIFICADO MÉDICO</h1>

<div class="fecha-cert">[Localidad], [_____] de [____________] de 2026.</div>

<p>El que suscribe, Dr./a. <strong>[NOMBRE Y APELLIDO DEL MÉDICO]</strong>, M.P. N° [_______________], M.N. N° [_______________], especialista en [_______________], <strong>CERTIFICA</strong> que:</p>

<p>La paciente <strong>[NOMBRE Y APELLIDO DE CRISTINA]</strong>, DNI N° [_______________], de [___] años de edad, con domicilio en [_____________________________________________], se encuentra bajo mi atención médica y presenta el siguiente cuadro clínico:</p>

<h3>1. DIAGNÓSTICO</h3>

<p><strong>Paraplejia</strong> [especificar etiología: traumática / por enfermedad / congénita / otra: _______________], con evolución desde [___________] (mes/año aproximado).</p>

<p>CIE-10: [G82.2 — paraplejia, no especificada / o el código que corresponda al caso].</p>

<h3>2. ANTECEDENTES Y EVOLUCIÓN</h3>

<p>[Reseñar brevemente: antecedentes médicos relevantes, tratamientos realizados, estado neurológico actual, estudios complementarios pertinentes.]</p>

<p>____________________________________________________________________________</p>
<p>____________________________________________________________________________</p>
<p>____________________________________________________________________________</p>

<h3>3. ESTADO FUNCIONAL ACTUAL</h3>

<p>La paciente presenta <strong>dependencia funcional total</strong> para la realización de las <strong>Actividades Básicas de la Vida Diaria (ABVD)</strong>, incluyendo:</p>

<ul class="abvd">
  <li>Higiene personal y baño</li>
  <li>Vestido</li>
  <li>Alimentación</li>
  <li>Continencia y uso del baño</li>
  <li>Movilidad y transferencias</li>
  <li>Deambulación (imposibilitada en forma autónoma)</li>
</ul>

<p>Se trata de una situación clínica de <strong>carácter permanente e irreversible</strong>, sin posibilidades razonables de recuperación funcional al momento de emisión del presente.</p>

<h3>4. NECESIDAD DE ASISTENCIA</h3>

<p>En virtud del cuadro descripto, la paciente requiere <strong>asistencia y acompañamiento de un tercero durante las veinticuatro (24) horas del día</strong>, los siete días de la semana, no pudiendo permanecer sola sin riesgo cierto para su vida e integridad física.</p>

<p>La ausencia de dicha asistencia implica <strong>riesgo de:</strong></p>
<ul>
  <li>Caídas y lesiones derivadas de la imposibilidad de movilizarse</li>
  <li>Úlceras por decúbito por permanencia prolongada en una misma posición</li>
  <li>Complicaciones urinarias y digestivas por falta de cambios y cuidados</li>
  <li>Desnutrición y deshidratación por imposibilidad de alimentarse de manera autónoma</li>
  <li>Eventos médicos agudos sin posibilidad de pedir auxilio</li>
</ul>

<h3>5. IMPOSIBILIDAD DE TRASLADO</h3>

<p>Se deja expresa constancia de que la paciente <strong>se encuentra imposibilitada de trasladarse a oficinas públicas, sedes administrativas o juntas evaluadoras</strong>, en razón de su cuadro de paraplejia y dependencia total. Cualquier trámite que requiera su presencia personal debe realizarse mediante <strong>visita domiciliaria</strong>.</p>

<h3>6. PERTINENCIA DE INSTITUCIONALIZACIÓN</h3>

<p>Atento al cuadro descripto, a la imposibilidad de garantizar la asistencia continua en el domicilio actual y a la ausencia de red de contención familiar en su provincia de residencia, se considera <strong>clínicamente justificada y necesaria</strong> su <strong>institucionalización en una Residencia de Larga Estadía con atención psicogerontológica</strong> que asegure asistencia integral 24 hs, conforme el régimen de la Ley 24.901.</p>

<p>El presente se extiende a pedido del/de la interesado/a, para ser presentado ante autoridades administrativas, sanitarias y/o judiciales que lo requieran.</p>

<div class="firma-cert">
  <div class="linea-firma">_________________________________</div>
  <p>Firma y sello del médico tratante<br>
  Dr./a. [NOMBRE Y APELLIDO]<br>
  M.P. N° [___________] — M.N. N° [___________]<br>
  Especialidad: [_______________]</p>
</div>

</body></html>
"""

CSS_DOCS = """
@page {
  size: A4;
  margin: 2.5cm 2.2cm;
  @bottom-right {
    content: counter(page) " / " counter(pages);
    font-size: 9pt;
    color: #888;
  }
}

body {
  font-family: "Times New Roman", "Liberation Serif", serif;
  font-size: 12pt;
  line-height: 1.55;
  color: #111;
  text-align: justify;
}

.fecha-lugar {
  text-align: right;
  margin-bottom: 1cm;
  font-style: italic;
}

.destinatario {
  margin-bottom: 0.8cm;
}

.asunto, .ref {
  margin-bottom: 0.5cm;
}

h3 {
  font-size: 12.5pt;
  margin-top: 0.7cm;
  margin-bottom: 0.3cm;
  text-decoration: underline;
}

ul {
  margin: 0.3cm 0;
  padding-left: 1cm;
}

ul.anexos, ul.abvd {
  list-style: none;
  padding-left: 0.5cm;
}

ul.anexos li::before {
  content: "▸ ";
  color: #2c5282;
}

ul.abvd li::before {
  content: "• ";
}

.cierre {
  margin-top: 0.8cm;
}

.firma, .firma-cert {
  margin-top: 2.5cm;
  text-align: center;
}

.linea-firma {
  margin-bottom: 0.2cm;
}

.encabezado-medico {
  text-align: center;
  margin-bottom: 1cm;
  border-bottom: 1px solid #ccc;
  padding-bottom: 0.4cm;
}

.lugar-medico {
  color: #888;
  font-style: italic;
  font-size: 10pt;
}

.titulo-cert {
  text-align: center;
  font-size: 18pt;
  letter-spacing: 2px;
  margin: 0.5cm 0;
  border-bottom: 2px solid #111;
  padding-bottom: 0.3cm;
}

.fecha-cert {
  text-align: right;
  margin-bottom: 0.8cm;
  font-style: italic;
}

p {
  margin: 0.3cm 0;
}
"""


def main():
    out_dir = Path(__file__).parent

    (out_dir / "nota_defensoria_san_juan.html").write_text(NOTA_HTML, encoding="utf-8")
    HTML(string=NOTA_HTML).write_pdf(
        out_dir / "nota_defensoria_san_juan.pdf",
        stylesheets=[CSS(string=CSS_DOCS)],
    )

    (out_dir / "certificado_medico_modelo.html").write_text(CERTIFICADO_HTML, encoding="utf-8")
    HTML(string=CERTIFICADO_HTML).write_pdf(
        out_dir / "certificado_medico_modelo.pdf",
        stylesheets=[CSS(string=CSS_DOCS)],
    )

    print("Generados:")
    print(f"  - {out_dir / 'nota_defensoria_san_juan.pdf'}")
    print(f"  - {out_dir / 'certificado_medico_modelo.pdf'}")


if __name__ == "__main__":
    main()
