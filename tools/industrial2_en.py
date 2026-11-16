"""Industrial production, part two — English: welding, batch CNC turning, aluminium extrusion,
plating and anodizing, powder coating. Mirrors industrial2_fa.py; ordering is by phone."""
from common import SITE, MAIN, CONTACT
from industrial_en import TEL, TEL_EN, CTA_BTNS
from industrial2_fa import IMG

BATCH_NOTE = ('<b>For production runs only:</b> this service is for batch production; one-off parts are accepted only rarely. '
              'A suitable quantity is recommended after reviewing the project.')

ORDER_PHONE = 'By phone (' + TEL_EN + ') or Bale (@hyperfab_pro)'
LOCATION = 'Tehran, Iran'


def svc(name, alt, stype, path, desc):
    return [{'@type': 'Service', 'name': name, 'alternateName': alt, 'serviceType': stype, 'url': SITE + path,
             'description': desc, 'provider': {'@id': MAIN + '/#organization'}, 'areaServed': {'@type': 'Country', 'name': 'Iran'}}]


def hero_btns():
    return [('btn-red', 'Call for a project consultation', TEL), ('hfs-btn-ghost', 'Chat on Bale', CONTACT['bale_pro_url'])]


WELDING = {
    'depth': 2,
    'answer': ('<b>TIG and MIG welding of stainless steel and 6000-series aluminium</b>, including 6061 and 6063, and <b>TIG welding of St37 carbon steel</b> are offered by HyperFab, '
               'a manufacturing company in Tehran, Iran, together with fabrication of welded machine structures and large platform structures '
               'to the client’s approved drawings. VT, PT and phased-array ultrasonic (PAUT) weld testing is available on request, and HyperFab '
               'has built many units for the medical and marine industries. Welding projects are priced by material, weld length and type, '
               'structure size and requested tests; call ' + TEL_EN + '.'),
    'key_facts': [
        ('Service', 'TIG and MIG (argon-shielded) welding and welded fabrication'),
        ('Materials', 'Stainless steel, St37 carbon (mild) steel by TIG, 6000-series aluminium (6061, 6063)'),
        ('Weld testing', 'VT, PT, PAUT and other tests on request'),
        ('Pricing model', 'By material, weld length and type, structure size and requested tests'),
        ('Ordering', ORDER_PHONE),
        ('Location', LOCATION),
    ],
    'hero': {
        'crumb': 'Welding & Welded Structures',
        'h1': '<em>TIG and MIG welding</em><br>Stainless steel, steel, aluminium and welded structures',
        'lead': 'TIG and MIG welding of stainless steel and 6000-series aluminium, TIG welding of St37 steel, fabrication and assembly of welded structures for machines, and large platform structures — with VT, PT and phased-array weld testing on request, from drawing to delivery.',
        'ticks': [('Processes:', 'TIG and MIG (argon shielded)', False), ('Materials:', 'stainless steel, 6000-series aluminium, St37 steel (TIG)', False),
                  ('Weld testing:', 'VT · PT · PAUT and other tests as required', False)],
        'buttons': hero_btns(),
        'img': IMG['welding'], 'img_alt': 'TIG welding of a HyperFab stainless steel sealing assembly',
        'stats': [('sparkle', 'TIG · MIG', 'argon', 'stainless, steel and aluminium'), ('layers', '6000', 'series', 'aluminium'),
                  ('search', 'VT · PT · PAUT', '', 'weld testing on request'), ('shield', '1', 'owner', 'from drawing to delivery')],
    },
    'sections': [
        {'kicker': 'WHAT WE DO', 'title': 'TIG or MIG welding for stainless steel and aluminium?', 'id': 'what',
         'sub': 'TIG gives clean, precise welds on thin sheet and sensitive parts; MIG is faster for long and structural welds. HyperFab does both on stainless steel and 6000-series aluminium, and TIG welds St37 steel.',
         'paras': [
             'Argon-shielded welding — <b>TIG</b> (GTAW) and <b>MIG</b> (GMAW) — is the main way to join <b>stainless steel</b> and <b>6000-series aluminium</b> in machine and equipment building. HyperFab also TIG welds <b>St37 carbon steel</b> (mild steel); one example is a <a href="../portfolio/mechanism-frame-st37/">mechanism frame made from St37 box section and sheet</a>.',
             'HyperFab’s work is not just laying welds; it is building and assembling the project from drawing to delivery. That covers cutting and preparing parts, fixturing, welding with distortion control, weld finishing and testing. HyperFab has built many units for the <b>medical</b> and <b>marine</b> industries, where weld cleanliness and corrosion resistance are critical.',
             'The experience goes beyond small parts. HyperFab has built large platform structures, including a framed chassis mounted on wheels that runs on rails — a structure where flatness, alignment and dimensional accuracy over long lengths decide everything.',
             'If a welded part also needs a finish, it can be <a href="../powder-coating/">powder coated at HyperFab</a> and delivered as a finished part in one place. Flat sheet parts can also be ordered through <a href="https://hyperfab.ir/services/laser-metal/">metal laser cutting on hyperfab.ir</a>.',
         ],
         'gallery': [('assets/img/works/flange-steel-2.jpg', 'Stainless sealing assembly: drawing, parts and assembly'),
                     ('assets/img/works/flange-steel-3.jpg', 'AISI 304 parts of the same assembly before welding'),
                     ('assets/img/real-pt-test.jpg', 'PT test of the welds on the same assembly')]},
        {'kicker': 'SERVICES', 'title': 'Which welding services does HyperFab offer?', 'id': 'scope',
         'sub': 'TIG welding of stainless steel, TIG and MIG welding of 6000-series aluminium, welded machine structures, large platform structures and weld testing on request.',
         'adv': [
             ('sparkle', 'TIG welding of stainless steel', 'Clean, precise welds on stainless steel for medical, food and marine equipment, with heat control to preserve corrosion resistance.'),
             ('layers', '6000-series aluminium welding', 'TIG and MIG welding of 6000-series alloys such as 6061 and 6063, for chassis, frames and light structures.'),
             ('cube', 'Welded machine structures', 'Chassis, frames, housings and enclosures for many kinds of machines in stainless steel, St37 steel or aluminium, from cut parts to assembled structure.'),
             ('ruler', 'Large platform structures', 'Large platforms and framed chassis, including a structure mounted on wheels that runs on rails.'),
             ('shield', 'Medical and marine industries', 'Many units built for medical equipment and marine applications, meeting those industries’ cleanliness and corrosion requirements.'),
             ('search', 'Weld testing', 'Visual testing (VT), liquid penetrant (PT), phased-array ultrasonics (PAUT) and other tests on request.'),
         ],
         'figure': {'img': IMG['tig'], 'alt': 'TIG welding of a stainless steel pipe', 'caption': 'TIG welding on stainless steel pipe.'}},
        {'kicker': 'YOUR DESIGN', 'title': 'Does HyperFab design the welded structure?', 'id': 'design',
         'paras': [
             'Usually the structural design is the client’s, and HyperFab fabricates to your approved drawings; on some projects HyperFab has also designed the mechanism and frame, so ask when you enquire. Before work starts, the drawings are reviewed for manufacturability: welding sequence, joint access, distortion control and tolerances that can realistically be held. Anything worth flagging is discussed with you before fabrication.',
             'For large and platform structures, complete approved drawings are essential before fabrication starts. HyperFab takes responsibility for fabrication, follow-up and quality control through to delivery.',
         ]},
        {'kicker': 'WELD TESTING', 'title': 'Which weld tests are available?', 'id': 'testing',
         'sub': 'Visual testing (VT), liquid penetrant testing (PT), phased-array ultrasonic testing (PAUT) and other tests, carried out on request to suit the project’s requirements.',
         'table': [
             ('Test', 'What it checks'),
             ('VT — visual testing', 'Weld shape and size, surface cracks, undercut, spatter and visible defects'),
             ('PT — liquid penetrant', 'Surface-breaking cracks and discontinuities; suited to non-magnetic stainless steel and aluminium'),
             ('PAUT — phased-array ultrasonics', 'Internal weld defects such as lack of fusion, internal cracks and porosity, with a cross-section image of the weld'),
             ('Other tests', 'As the project and client require'),
         ],
         'figure': {'img': IMG['ndt'], 'alt': 'Ultrasonic weld testing', 'caption': 'Ultrasonic testing finds internal weld defects.'}},
        {'kicker': 'HOW IT WORKS', 'title': 'How is a welding project quoted and run?', 'id': 'steps',
         'sub': 'Send drawings, material, quantity and required tests; the job is priced by material, weld length and type, structure size and requested tests after a manufacturability review.',
         'steps': [
             ('Send drawings', 'Send the structure or part drawings, material, quantity and required tests, or describe them by phone.'),
             ('Manufacturability review', 'Welding sequence, joint access and distortion control are reviewed.'),
             ('Quotation', 'Priced by material, weld length and type, structure size and requested tests.'),
             ('Fabrication and welding', 'Parts are prepared, fixtured, welded and finished as needed.'),
             ('Testing and delivery', 'Requested tests are carried out and the structure is delivered.'),
         ]},
        {'kicker': 'WHY HYPERFAB', 'title': 'Why choose HyperFab for welding?', 'id': 'why',
         'sub': 'Welding planned before work starts, experience in the medical and marine industries, and weld quality proven by testing.',
         'why': [
             ('file', 'Engineering before welding', 'Welding sequence and fixturing are planned before work starts so the structure stays flat and true to the drawing.'),
             ('shield', 'Experience in demanding industries', 'Many units for medical and marine use, plus large platform structures on wheels and rails.'),
             ('search', 'Quality you can verify', 'VT, PT and PAUT on request: weld quality is proven by testing, not by words.'),
         ]},
    ],
    'faq': [
        ('Does HyperFab do TIG welding of stainless steel?', 'Yes. HyperFab does TIG and MIG welding of stainless steel and has built many units for the medical and marine industries. Stainless welded structures are fabricated and assembled from drawing to delivery.'),
        ('Does HyperFab weld 6061 and 6063 aluminium?', 'Yes. HyperFab does TIG and MIG welding of 6000-series aluminium, including 6061 and 6063, for chassis, frames and light structures.'),
        ('Do you weld mild steel (St37)?', 'Yes. HyperFab does argon TIG welding of St37 steel; for example, a mechanism frame made from St37 box section and sheet, shown in HyperFab’s portfolio.'),
        ('TIG or MIG welding for stainless steel — which is better?', 'TIG gives cleaner, more precise welds and suits thin sheet, cosmetic parts and medical and food equipment. MIG is faster and more economical for long and structural welds. HyperFab does both and recommends the right process by material, thickness and use.'),
        ('How is welding priced at HyperFab?', 'HyperFab prices a welding project by material, weld length and type, structure size and the weld tests requested. The quotation follows a manufacturability review of your drawings.'),
        ('What should I send for a welding quote?', 'Send HyperFab the structure or part drawings, the material, the quantity and any weld tests you need, or describe them by phone on ' + TEL_EN + '.'),
        ('Does HyperFab design the welded structure?', 'Structural design is usually the client’s and HyperFab fabricates to the approved drawings; on some projects HyperFab has also designed the mechanism and frame, so ask when you enquire. The drawings are reviewed for manufacturability before fabrication and any issues are discussed with you.'),
        ('Which weld tests does HyperFab offer?', 'HyperFab offers visual testing (VT), liquid penetrant testing (PT), phased-array ultrasonic testing (PAUT) and other tests, on request and to suit the project’s requirements.'),
        ('Does HyperFab build large welded structures?', 'Yes. HyperFab has built large platform structures, including a framed chassis mounted on wheels that runs on rails.'),
        ('Where is HyperFab’s welding service based?', 'HyperFab is based in Tehran, Iran. Welding projects are discussed and quoted by phone on ' + TEL_EN + ' or on Bale (@hyperfab_pro).'),
    ],
    'cta_h': 'Tell us about your welding project',
    'cta_p': 'Send the structure drawings or call. HyperFab’s industrial projects specialist answers by phone.',
    'cta_btns': CTA_BTNS,
    'schema': svc('HyperFab Welding and Welded Fabrication', ['TIG welding', 'MIG welding', 'جوشکاری آرگون'],
                  'TIG and MIG welding of stainless steel and aluminium and welded structure fabrication', '/en/welding/',
                  'TIG and MIG welding of stainless steel and 6000-series aluminium and TIG welding of St37 steel, fabrication and assembly of welded machine structures and large platform structures to the client’s drawings, with VT, PT and PAUT weld testing; experience in the medical and marine industries.'),
}

TURNING = {
    'depth': 2,
    'answer': ('<b>Batch CNC turning</b> is the production of rotational parts — shafts, bushings, pins, nozzles, fittings and mating parts — '
               'in runs where every part must be as good as the approved first article. HyperFab, a manufacturing company in Tehran, Iran, '
               'produces batch turned parts to drawing in brass, MO40 (42CrMo4) and CK45 (C45) steel and other metals, with each part’s '
               'critical points engineered before production. Pricing is by material, complexity, tolerances and quantity and is quoted '
               'after drawing review; call ' + TEL_EN + '.'),
    'key_facts': [
        ('Service', 'Batch CNC turning to drawing, for production runs'),
        ('Materials', 'Brass, MO40 (42CrMo4), CK45 (C45), stainless steel, aluminium and other metals'),
        ('Quality control', 'First-article approval and dimensional inspection'),
        ('Pricing model', 'By material, complexity, tolerances and quantity, after drawing review'),
        ('Ordering', ORDER_PHONE),
        ('Location', LOCATION),
    ],
    'hero': {
        'crumb': 'Batch CNC Turning',
        'h1': '<em>CNC turning</em> of industrial parts<br>Production runs with proven precision',
        'lead': 'Batch production of turned parts in brass, MO40 alloy steel, CK45 steel and other metals, to drawing and with precise fit tolerances. The critical points of every part are engineered and checked before production, from the first sample to the last part of the run.',
        'ticks': [('For:', 'production runs', False), ('Materials:', 'brass, MO40 (42CrMo4), CK45 (C45) and other metals', False),
                  ('Precision:', 'fit tolerances, mating parts and gauges', False)],
        'buttons': hero_btns(),
        'img': IMG['turning'], 'img_alt': 'CNC lathe and boxes of batch-produced PTFE parts at HyperFab',
        'stats': [('wrench', 'MO40 · CK45', '', 'alloy and carbon steel'), ('target', 'CuZn', 'brass', 'mating parts'),
                  ('layers', 'PTFE · 304', '', 'PTFE and stainless'), ('file', '1st', 'article', 'approved before the run')],
    },
    'sections': [
        {'kicker': 'WHAT WE DO', 'title': 'What is batch CNC turning?', 'id': 'what',
         'paras': [
             'CNC turning is the main way to make rotational parts: shafts, bushings, pins, nuts, nozzles, fittings and parts that must fit precisely into each other. In batch production, the real challenge is not making one good part. It is making hundreds or thousands of parts that are all exactly that good part.',
             'HyperFab has produced batch turned parts for a long time. They range from <b>brass parts with fit tolerances</b> that must mate with each other to <b>gauge parts</b> in <b>MO40</b> alloy steel and <b>CK45</b> steel. They were made to high precision and approved by the customers.',
             'Behind that precision is engineering before turning. Before production starts, each part’s critical points are engineered and briefed to the machinist: fit surfaces, critical diameters, concentricity and surface finish at specific points. The machinist then knows exactly where the part needs which accuracy. For each part, the production method and precision level are chosen to match its requirements — no more expensive than needed, never below requirements.',
         ],
         'note': BATCH_NOTE,
         'gallery': [('assets/img/works/ptfe-part-1.jpg', 'Batch PTFE parts packed for delivery'),
                     ('assets/img/works/alu-cone-1.jpg', 'CNC-turned CK45 steel hub'),
                     ('assets/img/works/spline-shaft-1.jpg', 'Splined steel shaft'),
                     ('assets/img/works/steel-bush-1.jpg', 'AISI 304 bushing with precise steps and grooves'),
                     ('assets/img/works/flange-steel-4.jpg', 'Turning an AISI 304 stainless part'),
                     ('assets/img/works/misc-parts-1.jpg', 'Precision brass, stainless and polymer parts')]},
        {'kicker': 'MATERIALS & PARTS', 'title': 'Which materials and parts does HyperFab turn?', 'id': 'scope',
         'sub': 'Brass, MO40 (42CrMo4) and CK45 (C45) steel, stainless steel, aluminium and other metals — for mating parts, gauges, shafts, pins, bushings and fittings.',
         'adv': [
             ('coin', 'Brass parts', 'Brass bushings, nozzles, fittings, pins and mating parts with fit tolerances and a clean finish.'),
             ('wrench', 'MO40 steel (42CrMo4)', 'Chromium-molybdenum alloy steel for loaded parts and gauges, with high strength and toughness.'),
             ('layers', 'CK45 steel (C45)', 'Medium-carbon steel for shafts, pins, machine parts and gauges.'),
             ('target', 'Gauge parts', 'Dimensional inspection gauges that are themselves the precision reference of a production line.'),
             ('ruler', 'Mating parts', 'Sliding and press fits between parts, with control of critical diameters and concentricity.'),
             ('cube', 'Other metals', 'Stainless steel, aluminium and other steels, depending on the project.'),
         ]},
        {'kicker': 'PRECISION', 'title': 'How is precision held across a production run?', 'id': 'precision',
         'sub': 'By engineering the drawing before production, briefing the machinist on every critical point, approving a first article and inspecting dimensions during production and before delivery.',
         'checks': [
             '<b>Drawing engineering before production:</b> identifying fit surfaces, critical dimensions and measurement datums.',
             '<b>Technical briefing for the machinist:</b> the accuracy of each critical point, the operation sequence and the measurement method.',
             '<b>Precision matched to requirements:</b> the precision level and cost are set by each part’s importance — no more than needed, no less.',
             '<b>First-article approval</b> before the production run starts.',
             '<b>Dimensional inspection</b> during production and before delivery.',
             '<b>Suitable packing</b> so precision fit surfaces are not damaged.',
         ],
         'figure': {'img': 'assets/img/vz-cnc-lathe.jpg', 'alt': 'Steel workpieces in the chucks of CNC lathes', 'caption': 'CNC turning of steel workpieces.'}},
        {'kicker': 'MORE THAN TURNING', 'title': 'Can turned parts be plated, coated or welded?', 'id': 'after',
         'paras': [
             'Yes. A turned part usually needs a finish or assembly too. At HyperFab you can include <a href="../plating-anodizing/">silver and gold plating, anodizing and chromate</a>, <a href="../powder-coating/">powder coating</a> and <a href="../welding/">welding</a> in the same project, and receive the finished, ready-to-use part.',
             'For one-off parts and prototypes, see <a href="https://hyperfab.ir/services/cnc/">CNC machining on the HyperFab website</a>.',
         ]},
        {'kicker': 'HOW IT WORKS', 'title': 'How does a batch turning order work?', 'id': 'steps',
         'sub': 'Send a dimensioned drawing with tolerances, the material and the quantity; after engineering review and a quotation, a first article is made for your approval before the run starts.',
         'steps': [
             ('Send the drawing', 'Send a dimensioned drawing with tolerances, the material and the quantity, or describe them by phone.'),
             ('Engineering review', 'Fit surfaces and critical dimensions are identified and production notes are set.'),
             ('Quotation', 'Priced by material, complexity, tolerances and quantity.'),
             ('First article', 'The first part is made and inspected; the run starts after your approval.'),
             ('Production and delivery', 'The run is produced with dimensional inspection and delivered.'),
         ]},
    ],
    'faq': [
        ('Does HyperFab do batch CNC turning?', 'Yes. HyperFab produces batch turned parts to drawing. Examples include brass parts with fit tolerances and gauge parts in MO40 and CK45 steel, made to high precision and approved by the customers.'),
        ('Does HyperFab turn MO40 and CK45 steel?', 'Yes. MO40 (equivalent to 42CrMo4) and CK45 (equivalent to C45) are among the materials HyperFab has used for gauge parts and batch industrial parts.'),
        ('Does HyperFab make precision mating brass parts?', 'Yes. Brass parts that must fit into each other with sliding or press fits are one of HyperFab’s core experiences. Critical diameters and concentricity are engineered before production and checked during it.'),
        ('How is batch CNC turning priced?', 'HyperFab prices batch turning by material, part complexity, tolerances and quantity, after reviewing the drawing. The production method and precision level are matched to the part’s requirements, so the price matches its importance and precision.'),
        ('Is there a minimum quantity for batch CNC turning?', 'HyperFab’s batch turning service is for production runs; one-off parts are accepted only rarely, and a suitable quantity is recommended after reviewing the project. For single parts and prototypes, see CNC machining on hyperfab.ir.'),
        ('What should I send for a CNC turning quote?', 'Send HyperFab a dimensioned drawing with tolerances, the material and the quantity, or describe them by phone on ' + TEL_EN + '. Fit surfaces and critical dimensions are identified in the engineering review before the quotation.'),
        ('Can HyperFab plate or coat turned parts?', 'Yes. Silver and gold plating, anodizing and chromate, and powder coating are also available at HyperFab, and the finished part is delivered.'),
        ('Where is HyperFab’s batch CNC turning service based?', 'HyperFab is based in Tehran, Iran. Batch turning projects are discussed by phone on ' + TEL_EN + ' or on Bale (@hyperfab_pro), and a first article is approved before each production run.'),
    ],
    'cta_h': 'Send the drawing of your batch part',
    'cta_p': 'Send the drawing with tolerances, material and quantity, or call. HyperFab’s industrial projects specialist answers by phone.',
    'cta_btns': CTA_BTNS,
    'schema': svc('HyperFab Batch CNC Turning', ['CNC turning', 'تراشکاری CNC'], 'Batch production of CNC turned parts', '/en/cnc-turning/',
                  'Batch production of CNC turned parts in brass, MO40 (42CrMo4), CK45 (C45) and other metals, with fit tolerances, mating parts and gauges; critical points engineered before production, first-article approval and dimensional inspection.'),
}

EXTRUSION = {
    'depth': 2,
    'answer': ('<b>Custom aluminium extrusion</b> makes long aluminium profiles with your own constant cross-section by pushing a hot billet '
               'through a dedicated steel die. HyperFab, a manufacturing company in Tehran, Iran, specialises in aluminium extrusion: you bring '
               'the required tonnage and pay for the die, and HyperFab’s engineering team handles section consultation, die making, profile '
               'production, quality control and delivery. Die cost and profile price are quoted separately; call ' + TEL_EN + '.'),
    'key_facts': [
        ('Service', 'Custom aluminium profile extrusion with a dedicated die'),
        ('Material', 'Aluminium only'),
        ('Minimum order', 'By tonnage, advised after section consultation'),
        ('Pricing model', 'Die cost plus profile price by alloy, weight and tonnage, quoted separately'),
        ('Ordering', ORDER_PHONE),
        ('Location', LOCATION),
    ],
    'hero': {
        'crumb': 'Aluminium Extrusion',
        'h1': '<em>Aluminium profile extrusion</em><br>Your cross-section, with a dedicated die',
        'lead': 'Aluminium profiles in the cross-section you need. HyperFab’s engineering team advises on the section geometry, then a dedicated extrusion die is built and the profile is produced. You need the required tonnage and pay for the die; HyperFab’s engineering team handles the rest.',
        'ticks': [('Speciality:', 'aluminium extrusion only', False), ('Your part:', 'required tonnage + die cost', False),
                  ('Our part:', 'section consultation, die, production, QC and delivery', False)],
        'buttons': hero_btns(),
        'img': IMG['extrusion'], 'img_alt': 'Extruded aluminium profiles',
        'stats': [('layers', '6063 · 6061', 'alloys', 'most used for extrusion'), ('ruler', 'Custom', 'section', 'your geometry'),
                  ('wrench', 'Die', 'tooling', 'dedicated to your profile'), ('shield', '1', 'owner', 'from consultation to delivery')],
    },
    'sections': [
        {'kicker': 'WHAT IT IS', 'title': 'What is aluminium extrusion?', 'id': 'what',
         'paras': [
             '<b>Aluminium extrusion</b> pushes a hot aluminium billet under pressure through a steel die to make a long profile with a constant cross-section. Almost any section you can draw can be made with a dedicated die: solid, hollow, slotted, finned or with screw ports. That makes extrusion the most economical way to make long, uniform aluminium parts.',
             'HyperFab <b>specialises in aluminium extrusion</b>. The model is simple: you bring the required tonnage and pay for the die. Section design consultation, die making, profile production, quality control and delivery are handled by HyperFab’s engineering team. The result is a profile with exactly the section you need, not the closest one available on the market.',
             'Consultation before the die matters. Extrusion dies are expensive, and a poorly designed section can lead to warped profiles, uneven surfaces or a broken die. Before the die is made, HyperFab’s engineering team reviews your section for wall thickness, symmetry, corner radii and tongue ratios and suggests changes, so the die is built once, and built right.',
         ],
         'note': '<b>Aluminium only:</b> in extrusion, HyperFab works exclusively with aluminium. Orders are by tonnage, and the right tonnage for each section is advised after consultation.'},
        {'kicker': 'WHO DOES WHAT', 'title': 'Who does what in a custom extrusion order?', 'id': 'roles',
         'sub': 'You define the use, approve the section and pay for the die; HyperFab designs and builds the die, produces the profile at the ordered tonnage and handles quality control and delivery.',
         'table': [
             ('Step', 'Who'),
             ('Defining the use and initial section', 'You'),
             ('Consultation and final section geometry', 'HyperFab’s engineering team, with your approval'),
             ('Paying for the die', 'You'),
             ('Extrusion die design and manufacture', 'HyperFab'),
             ('Profile production at the ordered tonnage', 'HyperFab'),
             ('Quality control and delivery', 'HyperFab'),
         ]},
        {'kicker': 'PROFILES', 'title': 'Which aluminium profiles can HyperFab extrude?', 'id': 'profiles',
         'sub': 'Industrial and T-slot profiles, heat sinks, housings and enclosures, architectural profiles, hollow sections and rails — each in your own cross-section.',
         'adv': [
             ('stack', 'Industrial and T-slot profiles', 'Structural and slotted profiles for machine frames, workbenches and production lines.'),
             ('bolt', 'Heat sinks and finned profiles', 'Finned profiles for heat dissipation in power electronics, drives and LEDs.'),
             ('box', 'Housings and enclosures', 'Device housings and electronic enclosures with a section dedicated to your product.'),
             ('sparkle', 'Architectural and decorative profiles', 'Frames, edges, handles and decorative profiles.'),
             ('layers', 'Hollow and multi-cavity profiles', 'Hollow and multi-cavity sections that are both light and strong.'),
             ('ruler', 'Rails and guides', 'Rails, linear guides and light parts for equipment and transport.'),
         ]},
        {'kicker': 'DESIGN TIPS', 'title': 'How should an extrusion section be designed?', 'id': 'design',
         'sub': 'Keep walls uniform, round sharp corners, balance the section and control slot depth: these extend die life and lower the cost per kilo, and all of them are reviewed in consultation.',
         'checks': [
             '<b>Uniform wall thickness:</b> large thickness differences unbalance metal flow and warp the profile.',
             '<b>Rounded corners:</b> give sharp corners a small radius for longer die life and a better surface.',
             '<b>Balanced section:</b> symmetric, balanced sections extrude more stably and accurately.',
             '<b>Die tongues:</b> deep, narrow slots weaken the die tongue; the depth-to-width ratio must be controlled.',
             '<b>Section size:</b> the section must fit the production range; the right size is set in consultation.',
             '<b>Tolerances:</b> keep tight tolerances for functional dimensions only.',
         ]},
        {'kicker': 'AFTER EXTRUSION', 'title': 'Can extruded profiles be anodized, coated or machined?', 'id': 'after',
         'paras': [
             'Yes. An extruded profile is usually not yet the finished product. At HyperFab you can add <a href="../plating-anodizing/">aluminium anodizing</a>, <a href="../powder-coating/">powder coating</a>, <a href="../cnc-turning/">machining</a>, <a href="../punching/">punching</a> and <a href="../welding/">aluminium welding</a>, and receive a part that is ready to assemble.',
         ],
         'figure': {'img': 'assets/img/arc-extrusion-coating.jpg', 'alt': 'Aluminium profiles on a powder coating line', 'caption': 'Extruded aluminium profiles on a coating line.'}},
        {'kicker': 'HOW IT WORKS', 'title': 'How is a custom aluminium profile ordered and priced?', 'id': 'steps',
         'sub': 'After section consultation, the die cost and the profile price — by alloy, weight and tonnage — are quoted separately; a sample profile is approved before production.',
         'steps': [
             ('Send the section or idea', 'Send the section drawing, a DXF or even a sketch and the profile’s use, or describe it by phone.'),
             ('Section consultation', 'The engineering team reviews and optimises the section for extrusion and advises the right tonnage.'),
             ('Quotation', 'Die cost and profile price, by alloy, weight and tonnage, are quoted separately.'),
             ('Die and sample', 'The die is built and a sample profile is produced for your approval.'),
             ('Production and delivery', 'The profile is produced at the ordered tonnage, inspected and delivered.'),
         ]},
    ],
    'faq': [
        ('Does HyperFab extrude aluminium profiles?', 'Yes, as a specialisation: aluminium profiles in the customer’s own cross-section, with a dedicated die. Section consultation, die making, production and delivery are handled by HyperFab’s engineering team.'),
        ('What do I need to order a custom aluminium profile?', 'The required tonnage and payment for the die. To start, send the section drawing, a DXF or a sketch and the profile’s use. The section is finalised after consultation with HyperFab’s engineering team, which also handles everything else, from die making to profile delivery.'),
        ('How is custom aluminium extrusion priced?', 'HyperFab quotes two items separately: the cost of the dedicated extrusion die, which the customer pays, and the profile price by alloy, weight and tonnage.'),
        ('What is the minimum order for aluminium extrusion?', 'HyperFab takes extrusion orders by tonnage. The right tonnage depends on the section’s size and weight and is advised after consultation.'),
        ('Does HyperFab design the profile section?', 'HyperFab’s engineering team advises on the section geometry and optimises it for extrusion: wall thickness, symmetry, corner radii and tongue ratios. The final section is made with your approval.'),
        ('Does HyperFab extrude materials other than aluminium?', 'No. In extrusion, HyperFab works with aluminium only.'),
        ('Can HyperFab anodize or powder-coat extruded profiles?', 'Yes. Anodizing, powder coating, machining, punching and welding of profiles are also available at HyperFab.'),
        ('Where is HyperFab’s aluminium extrusion service based?', 'HyperFab is based in Tehran, Iran. Custom profile projects start with a consultation by phone on ' + TEL_EN + ' or on Bale (@hyperfab_pro).'),
    ],
    'cta_h': 'Tell us about your profile section',
    'cta_p': 'Send the section drawing or sketch, or call. HyperFab’s engineering team advises on the section, tonnage and die.',
    'cta_btns': CTA_BTNS,
    'schema': svc('HyperFab Aluminium Extrusion', ['Aluminum extrusion', 'Custom aluminium profiles', 'اکسترود آلومینیوم'],
                  'Specialised aluminium profile extrusion with custom sections and dedicated dies', '/en/aluminium-extrusion/',
                  'Specialised extrusion of aluminium profiles in the customer’s cross-section: section design consultation, dedicated extrusion die, production at the ordered tonnage, quality control and delivery. The customer has the required tonnage and pays for the die.'),
}

PLATING = {
    'depth': 2,
    'answer': ('<b>Gold and silver plating</b> on brass and other metals, and <b>anodizing</b> and <b>chromate conversion (Alodine)</b> on '
               'aluminium, are offered by HyperFab, a manufacturing company in Tehran, Iran, for decorative, electrical and industrial parts. '
               'The service is for production runs, with the same preparation and checks for every part in a batch. To get a quote, tell '
               'HyperFab the part material, finish and quantity or send a sample; call ' + TEL_EN + '.'),
    'key_facts': [
        ('Service', 'Silver and gold plating, anodizing and chromate (Alodine)'),
        ('Base metals', 'Brass and other metals for plating; aluminium for anodizing and chromate'),
        ('Quantity', 'Production runs; one-off work is accepted only rarely'),
        ('Quote', 'From part material, finish and quantity, or a sample part'),
        ('Ordering', ORDER_PHONE),
        ('Location', LOCATION),
    ],
    'hero': {
        'crumb': 'Plating & Anodizing',
        'h1': '<em>Silver and gold plating</em>, anodizing and chromate<br>Finishing for batch metal parts',
        'lead': 'Silver and gold plating on brass and other metals, and anodizing and chromate conversion (Alodine) on aluminium — for decorative, electrical and industrial uses, with consistent quality across the run.',
        'ticks': [('Plating:', 'silver and gold on brass and other metals', False), ('Aluminium:', 'anodizing and chromate (Alodine)', False),
                  ('For:', 'production runs', False)],
        'buttons': hero_btns(),
        'img': IMG['plating'], 'img_alt': 'Machined aluminium parts with black and silver anodizing',
        'stats': [('sparkle', 'Ag', 'silver', 'on brass and other metals'), ('coin', 'Au', 'gold', 'on brass and other metals'),
                  ('layers', 'Al', 'anodizing', 'on aluminium'), ('shield', 'Alodine', 'chromate', 'conversion coating')],
    },
    'sections': [
        {'kicker': 'WHAT WE DO', 'title': 'Does HyperFab do gold plating, silver plating and anodizing?', 'id': 'what',
         'sub': 'Yes. HyperFab does silver and gold plating on brass and other metals, and anodizing and chromate conversion (Alodine) on aluminium, for production runs.',
         'paras': [
             'Surface finish is the last and most visible step in making a part. It sets the part’s appearance and its resistance to corrosion and wear, and its electrical behaviour.',
             'The service covers both <b>decorative</b> and <b>technical</b> parts. For decorative parts, a bright, lasting appearance matters: décor items, hardware, statuettes and corporate gifts. For technical parts, conductivity, corrosion resistance and a good paint base matter: connectors, contacts and electronic and industrial parts. It is for production runs, and it pairs well with HyperFab’s <a href="../cnc-turning/">batch CNC turning</a>: a turned brass part is delivered plated and ready.',
         ],
         'note': BATCH_NOTE},
        {'kicker': 'COATINGS', 'title': 'Which plating and anodizing finishes are available?', 'id': 'coatings',
         'sub': 'Silver plating, gold plating, aluminium anodizing and chromate (Alodine), on brass, aluminium and other metals.',
         'adv': [
             ('sparkle', 'Silver plating', 'The highest electrical conductivity of any metal; for contacts, connectors, busbars and electrical parts, and for decorative items with a bright silver look.'),
             ('coin', 'Gold plating', 'Excellent resistance to oxidation and stable contact resistance; for connectors and electronics, and for jewellery, hardware and luxury items.'),
             ('layers', 'Aluminium anodizing', 'A hard oxide layer grown on aluminium that raises corrosion and wear resistance; for housings, profiles and industrial and decorative parts.'),
             ('shield', 'Chromate (Alodine)', 'A thin conversion coating on aluminium that prevents corrosion, keeps the surface electrically conductive and makes a good paint base.'),
             ('cube', 'On brass and other metals', 'Plating on brass and other metals, from turned parts to castings and sheet parts.'),
             ('stack', 'Consistent across the run', 'The same preparation and checks for every part in a batch, so colour and appearance match from first part to last.'),
         ],
         'figure': {'img': IMG['anodizing'], 'alt': 'Gold-plated connectors', 'caption': 'Gold plating on connectors.'}},
        {'kicker': 'COMPARE', 'title': 'Silver, gold, anodizing or chromate: which finish suits your part?', 'id': 'compare',
         'sub': 'Silver for the highest conductivity, gold for oxidation resistance and stable contact resistance, anodizing for a hard, corrosion- and wear-resistant layer on aluminium, and chromate for a conductive, paintable surface on aluminium.',
         'table': [
             ('Finish', 'Base metal', 'Main property', 'Typical uses'),
             ('Silver plating', 'Brass, copper and other metals', 'Highest conductivity, silver appearance', 'Contacts and connectors, busbars, RF parts, decorative items'),
             ('Gold plating', 'Brass, copper and other metals', 'Oxidation-resistant, stable contact resistance, gold appearance', 'Connectors and electronics, jewellery, luxury hardware'),
             ('Anodizing', 'Aluminium', 'Hard oxide layer, corrosion- and wear-resistant', 'Housings, profiles, industrial and decorative parts'),
             ('Chromate (Alodine)', 'Aluminium', 'Corrosion protection with a conductive surface, paint base', 'Electronic parts, enclosures, parts before painting'),
         ]},
        {'kicker': 'APPLICATIONS', 'title': 'What are plating and anodizing used for?', 'id': 'uses',
         'checks': [
             '<b>Electrical and electronic parts:</b> contacts, connectors, terminals and busbars with silver or gold plating.',
             '<b>Decorative items and gifts:</b> statuettes, badges, hardware and décor with gold and silver plating.',
             '<b>Device housings and frames:</b> anodized or chromated aluminium parts, including <a href="../aluminium-extrusion/">custom aluminium extrusion profiles</a>.',
             '<b>Turned brass parts:</b> fittings and precision parts with protective or decorative plating.',
             '<b>Aluminium parts before painting:</b> chromate as an adhesion base, for example before <a href="../powder-coating/">powder coating</a>.',
         ]},
    ],
    'faq': [
        ('Does HyperFab do gold and silver plating?', 'Yes. HyperFab does silver and gold plating on brass and other metals for decorative, electrical and industrial uses. The service is for production runs.'),
        ('Does HyperFab anodize aluminium?', 'Yes. HyperFab does anodizing and chromate conversion (Alodine) on aluminium parts, for production runs.'),
        ('What is chromate or Alodine?', 'Chromate is a thin conversion coating on aluminium that prevents corrosion and, unlike anodizing, keeps the surface electrically conductive. It is also a good paint base. Alodine is the well-known trade name of this kind of coating.'),
        ('Silver or gold plating — which is better?', 'Silver has the highest conductivity and costs less but tarnishes over time in air. Gold conducts less but does not oxidise, so its contact resistance stays stable. The choice depends on use, environment and budget.'),
        ('Is there a minimum quantity for plating and anodizing?', 'HyperFab’s plating and anodizing service is for production runs; one-off work is accepted only rarely, and a suitable quantity is recommended after reviewing the project.'),
        ('What should I send for a plating or anodizing quote?', 'Tell us the part material, the finish you need and the quantity, or send a sample part. HyperFab’s industrial projects specialist answers by phone on ' + TEL_EN + '.'),
        ('Can HyperFab make the part as well as plate it?', 'Yes. You can also have the part made by HyperFab through batch CNC turning, punching or injection moulding, and receive it finished.'),
        ('Where is HyperFab’s plating and anodizing service based?', 'HyperFab is based in Tehran, Iran. Plating, anodizing and chromate projects are handled by phone on ' + TEL_EN + ' or on Bale (@hyperfab_pro).'),
    ],
    'cta_h': 'Send your parts for plating or anodizing',
    'cta_p': 'Tell us the part material, finish and quantity, or send a sample. HyperFab’s industrial projects specialist answers by phone.',
    'cta_btns': CTA_BTNS,
    'schema': svc('HyperFab Plating and Anodizing', ['Gold plating', 'Silver plating', 'Anodizing', 'Chromate conversion', 'Alodine'],
                  'Silver and gold plating, anodizing and chromate (Alodine)', '/en/plating-anodizing/',
                  'Silver and gold plating on brass and other metals, and anodizing and chromate conversion (Alodine) on aluminium, for decorative, electrical and industrial uses; for production runs.'),
}

COATING = {
    'depth': 2,
    'answer': ('<b>Powder coating</b> is a dry, electrostatically charged powder that is oven-cured into a hard, even layer, more durable than '
               'liquid paint. HyperFab, a manufacturing company in Tehran, Iran, powder-coats batch parts in steel, iron, aluminium and other '
               'metals, in standard, pearl, hammer and textured finishes, gloss or matt, in a wide range of colours including RAL codes. '
               'Pricing depends on part size and surface area, finish, preparation and quantity and is quoted after review; call ' + TEL_EN + '.'),
    'key_facts': [
        ('Service', 'Electrostatic, oven-cured powder coating of steel, iron, aluminium and other metals'),
        ('Finishes', 'Powder, pearl, hammer, texture and wrinkle; gloss, satin or matt; RAL colours'),
        ('Quantity', 'Production runs; one-off work is accepted only rarely'),
        ('Pricing model', 'By size and surface area, finish, preparation and quantity, after review'),
        ('Ordering', ORDER_PHONE),
        ('Location', LOCATION),
    ],
    'hero': {
        'crumb': 'Powder Coating',
        'h1': '<em>Powder coating</em> (electrostatic, oven-cured)<br>Durable finishes for batch parts',
        'lead': 'Electrostatic powder coating in pearl, hammer and textured finishes, gloss and matt, on batch metal parts — a hard, even, durable finish for machine housings, structures, industrial parts and consumer products.',
        'ticks': [('Finishes:', 'powder, pearl, hammer, texture, gloss and matt', False), ('On:', 'steel, iron, aluminium and other metals', False),
                  ('For:', 'production runs', False)],
        'buttons': hero_btns(),
        'img': IMG['coating'], 'img_alt': 'Electrostatic powder coating of a metal part',
        'stats': [('layers', 'Powder', 'coating', 'electrostatic'), ('sparkle', 'Pearl', 'finish', 'metallic and pearlescent'),
                  ('wrench', 'Hammer', 'finish', 'hides imperfections'), ('target', 'RAL', 'colours', 'standard codes')],
    },
    'sections': [
        {'kicker': 'WHAT IT IS', 'title': 'What is powder coating?', 'id': 'what',
         'paras': [
             '<b>Powder coating</b> applies a dry powder to a metal part. The electrically charged powder clings to the part, which is then cured in an oven so the powder melts into a continuous, hard layer. The result is thicker, more even and more resistant to impact, scratches and corrosion than liquid paint.',
             'HyperFab powder-coats batch metal parts with high quality at a fair price: machine housings and chassis, structures, industrial parts and consumer products. If the part is also made at HyperFab — by <a href="../punching/">punching</a>, <a href="../welding/">welding</a> or <a href="../cnc-turning/">turning</a> — you receive the coated, finished part in one place. On aluminium, <a href="../plating-anodizing/">chromate conversion</a> as a base improves paint adhesion.',
         ],
         'note': BATCH_NOTE},
        {'kicker': 'FINISHES', 'title': 'Which powder coating finishes are available?', 'id': 'types',
         'sub': 'Electrostatic powder, pearl, hammer, texture and wrinkle finishes, in gloss, satin or matt and a wide range of colours, including standard RAL codes.',
         'adv': [
             ('layers', 'Electrostatic powder', 'The most common powder coating: an even, solvent-free finish with strong adhesion and durability.'),
             ('sparkle', 'Pearl (metallic and pearlescent)', 'A metallic or pearlescent sheen for cosmetic parts, décor and premium products.'),
             ('wrench', 'Hammer finish', 'A texture like hammered metal that hides imperfections; common on machine housings, cabinets and tools.'),
             ('stack', 'Texture and wrinkle', 'A rough, matt surface that hides fingerprints and scratches; for high-touch parts.'),
             ('target', 'Gloss, satin and matt', 'The gloss level to suit the use and look of the product.'),
             ('chat', 'Wide colour range', 'A wide range of colours, including standard RAL codes.'),
         ]},
        {'kicker': 'PROCESS', 'title': 'How does powder coating work, step by step?', 'id': 'process',
         'sub': 'Surface preparation, electrostatic powder application, oven curing, then inspection and delivery.',
         'steps': [
             ('Surface preparation', 'Degreasing and cleaning, plus other preparation where needed for better adhesion.'),
             ('Powder application', 'Charged powder is sprayed evenly onto the part.'),
             ('Oven curing', 'The part is cured in an oven so the powder melts into a hard, continuous layer.'),
             ('Inspection and delivery', 'Appearance and evenness are checked and parts are packed and delivered.'),
         ]},
        {'kicker': 'APPLICATIONS', 'title': 'What is powder coating used for?', 'id': 'uses',
         'checks': [
             '<b>Machine housings and chassis</b> and industrial equipment.',
             '<b>Electrical cabinets</b>, enclosures and metal boxes.',
             '<b>Metal structures, shelving and racks.</b>',
             '<b>Metal furniture</b> and décor.',
             '<b>Car and motorcycle parts</b>, wheels and body parts.',
             '<b>Home appliances</b> and metal consumer products.',
         ]},
        {'kicker': 'WHY POWDER', 'title': 'Powder coating or ordinary paint: which lasts longer?', 'id': 'why',
         'sub': 'Powder coating gives a thicker, harder layer that lasts longer than ordinary liquid paint against impact, scratches and corrosion.',
         'why': [
             ('shield', 'More durable', 'A thicker, harder layer that lasts longer against impact, scratches and corrosion.'),
             ('layers', 'Consistent across the run', 'The same thickness and look on every part in a batch, with no runs or blotches.'),
             ('sparkle', 'Many looks', 'From matt and gloss to pearl, hammer and textured, for every taste and use.'),
         ]},
    ],
    'faq': [
        ('What is powder coating?', 'Powder coating is an electrostatically charged powder that clings to a metal part and is cured in an oven into a hard, even layer. It is more durable than liquid paint. HyperFab powder-coats batch metal parts.'),
        ('Which powder coatings does HyperFab offer?', 'HyperFab offers electrostatic powder, pearl (metallic and pearlescent), hammer, texture and wrinkle finishes, in gloss, satin or matt and a wide range of colours, including standard RAL codes.'),
        ('What is a pearl finish?', 'A powder coating with metallic or pearlescent particles that gives a metallic or pearl-like sheen; popular for cosmetic parts and premium products.'),
        ('Does HyperFab powder-coat aluminium?', 'Yes. HyperFab powder-coats steel, iron, aluminium and other metals. On aluminium, chromate as a base improves paint adhesion.'),
        ('How is powder coating priced?', 'HyperFab prices powder coating by part size and surface area, finish type and texture, preparation required and quantity. The price is quoted after review.'),
        ('Is there a minimum quantity for powder coating?', 'HyperFab’s powder coating service is for production runs; one-off work is accepted only rarely, and a suitable quantity is recommended after reviewing the project.'),
        ('What should I send for a powder coating quote?', 'Tell us the part size, the finish you want and the quantity, or send a sample part. HyperFab’s industrial projects specialist answers by phone on ' + TEL_EN + '.'),
        ('Where is HyperFab’s powder coating service based?', 'HyperFab is based in Tehran, Iran. Powder coating projects are handled by phone on ' + TEL_EN + ' or on Bale (@hyperfab_pro).'),
    ],
    'cta_h': 'Send your batch parts for powder coating',
    'cta_p': 'Tell us the part size, finish and quantity, or send a sample. HyperFab’s industrial projects specialist answers by phone.',
    'cta_btns': CTA_BTNS,
    'schema': svc('HyperFab Powder Coating', ['Electrostatic powder coating', 'Oven-cured paint', 'رنگ کوره‌ای'],
                  'Electrostatic powder coating of metal parts', '/en/powder-coating/',
                  'Electrostatic powder coating in pearl, hammer and textured finishes, gloss and matt, on batch metal parts; for machine housings, structures, industrial parts and consumer products.'),
}


TUBELASER = {
    'depth': 2,
    'answer': ('<b>Tube and profile laser cutting</b> cuts box section, pipe and profiles to length and adds holes, slots and joint-ready ends '
               'in one programmed setup. HyperFab, a manufacturing company in Tehran, Iran, does this on square and rectangular tube, round pipe, '
               'angle, channel and special sections in mild steel, stainless steel and aluminium, from samples and small first runs to batch orders, '
               'using your material or material sourced by HyperFab. The price depends on the section, material, number of cuts and holes per part '
               'and quantity; call ' + TEL_EN + '.'),
    'key_facts': [
        ('Service', 'Laser cutting, hole-making and end preparation of tube and profiles'),
        ('Sections', 'Square and rectangular tube (box section), round pipe, angle, channel and U, oval and special sections'),
        ('Materials', 'Mild steel, stainless steel and aluminium'),
        ('Quantities', 'Samples and small first runs, and batch orders'),
        ('Material supply', 'Supplied by you, or sourced by HyperFab'),
        ('Ordering', ORDER_PHONE),
        ('Location', LOCATION),
    ],
    'hero': {
        'crumb': 'Tube & Profile Laser Cutting',
        'h1': '<em>Tube and profile laser cutting</em><br>Box section, pipe, angle and channel in steel, stainless and aluminium',
        'lead': 'HyperFab carries out precise, clean laser cutting, hole-making and end preparation of box section, pipe and open profiles in mild steel, stainless steel and aluminium, from the first sample to batch production.',
        'ticks': [('Sections:', 'box section, round pipe, angle, channel and special sections', False),
                  ('Materials:', 'mild steel, stainless steel and aluminium', False),
                  ('Orders:', 'from samples and first runs to batches', False)],
        'buttons': hero_btns(),
        'img': IMG['tubelaser'], 'img_alt': 'Laser head cutting a steel profile with sparks (stock image, AI-generated)',
        'stats': [('stack', 'Box · Pipe · Angle', '', 'sections'), ('layers', 'Steel · Stainless · Al', '', 'materials'),
                  ('chart', 'Sample to batch', '', 'orders'), ('shield', 'Drawing to delivery', '', 'one responsible party')],
    },
    'sections': [
        {'kicker': 'WHAT IT IS', 'title': 'What is tube and profile laser cutting?', 'id': 'what',
         'paras': [
             '<b>Tube and profile laser cutting</b> is laser cutting applied to long sections instead of flat sheet. A cutting program is generated from the part drawing, and the cut to length, holes, slots and end shapes are made on the different faces of the section in one sequence, without re-clamping the part. What comes off is a part ready for welding or assembly, not a length of stock that still needs sawing, drilling and grinding.',
             'These sections go by many names. <b>Box section</b> — square or rectangular hollow tube — is itself a kind of profile. Alongside it, <b>round pipe</b>, open profiles such as <b>angle</b>, <b>channel</b> and U sections, and <b>oval and special sections</b> can all be laser cut. HyperFab does this work in <b>mild steel</b>, <b>stainless steel</b> and <b>aluminium</b>.',
             'HyperFab’s team has long experience in profile laser cutting and focuses on what shows up at assembly: accurate lengths and hole positions, clean cut edges and parts that match across a batch. Orders are not limited to production runs either: samples and small first runs are accepted, so the part can be tried in a real assembly before the batch is cut.',
         ],
         'note': '<b>Your material or ours:</b> you can supply the tube, pipe or profile yourself, or have HyperFab source it. Just say which when you ask for a quote.'},
        {'kicker': 'WHAT CAN BE CUT', 'title': 'Which features can be cut on tube and profiles?', 'id': 'features',
         'sub': 'Cut to length, round and shaped holes, slots and windows, coped pipe ends, mitred ends and tab-and-slot features for welded frames; what is possible depends on the section and material.',
         'adv': [
             ('ruler', 'Cut to length', 'Lengths cut accurately with clean ends, so every part in a batch comes out the same — no sawing or marking out.'),
             ('target', 'Round and shaped holes', 'Round, oval, square or any other hole shape on the faces of the section, positioned accurately from the part end. Very small holes relative to the wall thickness are confirmed after review.'),
             ('sheet', 'Slots and windows', 'Slots for fasteners and adjustment, windows for cable routing or weight saving, and decorative cut-outs in tube and pipe walls.'),
             ('link', 'Coped pipe ends', 'Pipe ends shaped to fit the mating pipe (fish-mouth or saddle cuts), so the two sit without gaps and weld evenly. On thick-wall pipe, after reviewing the drawing.'),
             ('cube', 'Mitred ends', 'Angled end cuts for frame and box corners; the achievable angle depends on the section.'),
             ('stack', 'Tab-and-slot frames', 'Tabs and slots that locate frame members in the right place before welding, reducing fixturing and improving frame accuracy.'),
         ],
         'note': '<b>On request, after review:</b> weld-prep bevels and laser marking or etching can be considered on request, depending on the section. On open profiles and special sections, the range of features is confirmed once the drawing has been reviewed.'},
        {'kicker': 'WHY LASER', 'title': 'Why laser cut instead of sawing, drilling and punching?', 'id': 'why',
         'sub': 'Every cut and hole in one setup and one program, with no tooling cost, holes positioned accurately from the part end and matching parts across the batch.',
         'table': [
             ('Aspect', 'Tube laser cutting', 'Saw, drill and punch'),
             ('Operations', 'Cut to length, holes and slots in one setup', 'Several steps, with repeated handling and measuring'),
             ('Tooling', 'No tooling; shapes are programmed from the drawing', 'Shaped holes need a die or special tool'),
             ('Hole position', 'Accurate relative to the part end and to each other', 'Depends on marking out and operator skill'),
             ('Cut edge', 'Clean edge with little finishing', 'Usually needs deburring and grinding'),
             ('Repeatability', 'Parts in a batch match', 'Varies from part to part'),
             ('Design changes', 'Update the drawing and program', 'New tool or template'),
         ],
         'note': '<b>Choosing fairly:</b> if a part has only a few simple, repeated holes and the volume is very high, <a href="../punching/">tube and sheet punching</a> can be more economical once the die is made. HyperFab does both and recommends the right process for the geometry and quantity.'},
        {'kicker': 'DESIGN TIPS', 'title': 'How should a tube or profile part be drawn?', 'id': 'design',
         'sub': 'A 3D STEP or IGES file is the best input; state the section, material and quantity, keep holes off the corner radii and allow for the weld seam of welded tube.',
         'checks': [
             '<b>3D file:</b> a STEP or IGES model of the part is the best input. If you do not have one, a 2D drawing, DXF or PDF is accepted, as long as the section and dimensions are clearly stated.',
             '<b>Section, material and quantity:</b> note the section size and wall thickness, the material (mild steel, stainless steel or aluminium) and the quantity of each part.',
             '<b>Clear of corner radii:</b> box section has rounded corners, and a hole that runs onto the radius changes shape. Keep the edges of holes and slots on the flat part of the face.',
             '<b>Tab-and-slot clearance:</b> leave a little clearance in tabs and slots so parts fit together without forcing.',
             '<b>Weld seam:</b> welded tube and pipe have a weld seam on the inside. If a hole or slot must not land on the seam, say so on the drawing.',
             '<b>Visible faces:</b> if a face will be visible in the finished product, mark it so feature placement and handling take it into account.',
             '<b>Threads in thin sheet and walls:</b> thin sheet or tube wall cannot hold a strong tapped thread, so holes are cut for rivet nuts instead, which give screws a proper thread (<a href="../portfolio/mechanism-frame-st37/">St37 mechanism frame case study</a>).',
         ]},
        {'kicker': 'ONE CHAIN', 'title': 'Can HyperFab also weld and finish the frame?', 'id': 'chain',
         'paras': [
             'Yes. A tube or profile part is usually one member of a frame, chassis or structure. After laser cutting, you can also hand HyperFab the <a href="../welding/">TIG and MIG welding and frame fabrication</a>, followed by <a href="../powder-coating/">powder coating</a> or <a href="../plating-anodizing/">plating and anodizing</a>. Sheet parts for the same structure, such as base plates, brackets and gussets, can be ordered online through <a href="https://hyperfab.ir/services/laser-metal/">sheet metal laser cutting</a> and <a href="https://hyperfab.ir/services/bending/">sheet metal bending</a> on hyperfab.ir.',
             'The advantage of one chain is one responsible party. If tabs and slots were designed for welding, HyperFab, having been responsible for the cut, is also responsible for welding the frame and checking the final dimensions. The part is not passed between workshops, and if something is wrong, it is clear who fixes it.',
         ]},
        {'kicker': 'HOW IT WORKS', 'title': 'How is tube and profile laser cutting ordered?', 'id': 'steps',
         'sub': 'Five steps: send the drawing, engineering review and quote, sample or first run, batch production, and inspection and delivery.',
         'steps': [
             ('Send the drawing', 'Send a STEP file or drawing on Bale, or call and give the section, material and quantity.'),
             ('Review and quote', 'The drawing is checked for cuttability and priced by section, material, number of cuts and holes and quantity; material from you or from HyperFab.'),
             ('Sample or first run', 'The first few parts are cut so they can be tried and approved in a real assembly or weld.'),
             ('Batch production', 'Once approved, the whole order is cut with the same program so the parts match.'),
             ('Inspection and delivery', 'Parts are inspected and delivered, or moved on to welding and finishing.'),
         ]},
    ],
    'faq': [
        ('Which sections and materials can be laser cut?', 'Square and rectangular tube (box section), round pipe, open profiles such as angle, channel and U, and oval and special sections, in mild steel, stainless steel and aluminium.'),
        ('Do you accept samples or small quantities?', 'Yes. HyperFab accepts samples and small first runs so the part can be tried in a real assembly before batch production. Once approved, the same program is used for the batch order.'),
        ('Can I supply my own tube or profile?', 'Yes. You can supply the material yourself or have HyperFab source it. Say which you prefer when you ask for a quote.'),
        ('What file do you need for tube laser cutting?', 'A 3D STEP or IGES file is the best input. A 2D drawing, DXF or PDF is also accepted, as long as the section, material and dimensions are clear. If you only have a physical sample part, you can bring that too.'),
        ('What are the maximum size, wall thickness and accuracy?', 'They depend on the section and material. What is achievable for each project is confirmed by phone after the drawing has been reviewed: ' + TEL_EN + '.'),
        ('Can you also weld and paint the frame?', 'Yes. After laser cutting, TIG and MIG welding and frame fabrication, powder coating, and plating or anodizing are also available at HyperFab, so the structure arrives finished.'),
        ('How is tube laser cutting different from sheet laser cutting?', 'Sheet laser cutting works on flat sheet and is ordered online at hyperfab.ir with an instant price. Tube and profile laser cutting works on tube, pipe and profiles, covers several faces and end shapes, and is ordered by phone after the drawing has been reviewed.'),
        ('Where is HyperFab’s tube laser cutting service based?', 'HyperFab is based in Tehran, Iran. Tube and profile laser cutting is ordered by phone on ' + TEL_EN + ' or on Bale (@hyperfab_pro).'),
    ],
    'cta_h': 'Send us your tube or profile drawing',
    'cta_p': 'Send a STEP file or drawing with the section, material and quantity, or call. HyperFab’s industrial projects specialist answers by phone.',
    'cta_btns': CTA_BTNS,
    'schema': svc('HyperFab Tube & Profile Laser Cutting', ['Tube laser cutting', 'Profile laser cutting', 'Box section laser cutting', 'برش لیزر پروفیل و لوله'],
                  'Laser cutting and hole-making of metal tube, pipe and profiles', '/en/tube-laser-cutting/',
                  'Laser cutting, hole-making and end preparation of box section, round pipe, angle, channel and special sections in mild steel, stainless steel and aluminium, from samples and first runs to batch orders, with customer-supplied or HyperFab-sourced material.'),
}


THREADROLL = {
    'depth': 2,
    'answer': ('<b>Thread rolling</b> forms a thread on a shaft by pressing it between threaded rolls, with no chips: the metal is not cut away '
               'but displaced into the shape of the thread. HyperFab, a manufacturing company in Tehran, Iran, uses a thread rolling machine to turn '
               'stainless steel and mild steel shafts into strong screws. A rolled thread is stronger and longer-lasting than a machined one, and the '
               'process is very cost-effective for this kind of part. Thread size and pitch are checked when you enquire; call ' + TEL_EN + '.'),
    'key_facts': [
        ('Service', 'Thread rolling and screw making from shafts'),
        ('Materials', 'Stainless steel and mild steel shafts'),
        ('Advantage', 'Stronger, longer-lasting threads than machined threads; cost-effective'),
        ('Size and pitch', 'Ask when you enquire'),
        ('Ordering', ORDER_PHONE),
        ('Location', LOCATION),
    ],
    'hero': {
        'crumb': 'Thread Rolling',
        'h1': '<em>Thread rolling</em><br>strong screws from stainless and steel shafts',
        'lead': 'HyperFab uses a thread rolling machine to turn stainless steel and mild steel shafts into strong screws. A rolled thread is formed by pressure, with no chips, so it is stronger and longer-lasting than a thread cut on a lathe or with a die — and for these parts the process is very cost-effective.',
        'ticks': [('Process:', 'cold forming with threaded rolls, no chips', False), ('Materials:', 'stainless steel and mild steel shafts', False),
                  ('Advantage:', 'stronger and longer-lasting than cut threads', False)],
        'buttons': hero_btns(),
        'img': IMG['threadroll'], 'img_alt': 'Steel shaft on a CNC lathe (stock image)',
        'stats': [('wrench', 'Cold formed · no chips', '', 'process'), ('layers', 'Stainless · Steel', '', 'shaft material'),
                  ('shield', 'Stronger than cut threads', '', 'advantage'), ('file', 'Drawing to delivery', '', 'one responsible party')],
    },
    'sections': [
        {'kicker': 'WHAT IT IS', 'title': 'What is thread rolling, and what does HyperFab do?', 'id': 'what',
         'paras': [
             '<b>Thread rolling</b> — also called <b>roll threading</b> or <b>rolled threads</b> — forms a thread without cutting. The shaft turns between rolls that carry the thread form, and under their pressure the surface metal of the shaft is shaped into the thread. No chips are removed; metal moves from the root of the thread up into its crest.',
             'HyperFab uses a thread rolling machine to turn <b>stainless steel</b> and <b>mild steel</b> shafts into <b>strong screws</b>. A screw made this way is stronger and lasts longer than one whose thread was cut by machining. The process itself is very cost-effective, and it suits this kind of application well.',
         ]},
        {'kicker': 'WHY STRONGER', 'title': 'Why is a rolled thread stronger than a cut thread?', 'id': 'why',
         'sub': 'Because the metal is not cut: its grain follows the thread form, the surface is work-hardened by cold forming and the thread root comes out smoother.',
         'adv': [
             ('layers', 'Grain flow is not cut', 'Machining cuts straight through the grain of the metal. In rolling, the grain bends to follow the thread profile and stays continuous, so the thread carries load better.'),
             ('shield', 'Work-hardened surface', 'The pressure of the rolls compresses and hardens the thread surface while cold, so the thread resists wear and damage from repeated assembly better.'),
             ('target', 'Smoother thread root', 'The thread root is where cracks start in screws under fluctuating load. The smooth, tool-mark-free surface of a rolled thread helps the screw last longer.'),
             ('coin', 'Less material wasted', 'With no chips removed, less raw material is wasted and threading is faster — one reason rolling is cost-effective.'),
         ]},
        {'kicker': 'COMPARE', 'title': 'Thread rolling or thread cutting on a lathe or with a die?', 'id': 'compare',
         'sub': 'For strong, repeated screws, rolling wins; for one-off parts and special thread profiles, cutting on a lathe or with a die may be the better choice.',
         'table': [
             ('Aspect', 'Thread rolling', 'Thread cutting (lathe or die)'),
             ('Chips', 'None; metal is displaced', 'Metal is removed as chips'),
             ('Grain flow', 'Follows the thread form and stays continuous', 'Cut through at the thread'),
             ('Thread surface', 'Smooth and work-hardened', 'Tool marks on the flanks and root'),
             ('Material waste', 'Low', 'Higher, by the volume of chips'),
             ('Speed in series', 'Fast and consistent', 'Slower'),
             ('One-offs and special profiles', 'Needs rolls for that thread; ask', 'Usually simpler'),
         ],
         'note': '<b>Choosing fairly:</b> if you need only one or a few parts with a special thread, cutting the thread on a lathe may make more sense. When you enquire, say which screw you need and how many, and the right process will be recommended.'},
        {'kicker': 'MATERIALS & PARTS', 'title': 'Which materials and parts can be rolled?', 'id': 'scope',
         'paras': [
             'HyperFab rolls threads on <b>stainless steel</b> and <b>mild steel</b> shafts. If your part is in another material, ask when you enquire.',
         ],
         'checks': [
             '<b>Screws:</b> stainless steel and mild steel shafts turned into strong screws.',
             '<b>Common uses of thread rolling:</b> rolling is also commonly used for studs, threaded rods and shafts with threaded ends; for these parts, ask when you enquire.',
         ]},
        {'kicker': 'DESIGN TIPS', 'title': 'What should I know before ordering rolled screws?', 'id': 'design',
         'sub': 'The blank is prepared smaller than the thread’s outside diameter; send the drawing, material, thread specification and quantity.',
         'checks': [
             '<b>The blank is smaller than the thread:</b> rolling displaces metal outward and raises the thread crest, so the blank is prepared smaller than the thread’s outside diameter. Do not machine the shaft to the nominal thread size yourself.',
             '<b>Drawing and thread specification:</b> give the part drawing, the material, the thread type and size, the pitch and the threaded length.',
             '<b>Quantity:</b> say how many screws or parts you need; it affects the price and the process.',
             '<b>Turned parts:</b> if the shaft or part to be threaded also needs turning, see <a href="../cnc-turning/">batch CNC turning</a>.',
         ]},
        {'kicker': 'HOW IT WORKS', 'title': 'How is thread rolling ordered?', 'id': 'steps',
         'sub': 'Four steps: send the drawing and specification, review and quote, rolling, and delivery.',
         'steps': [
             ('Send the drawing', 'Send the screw drawing or specification, shaft material, thread specification and quantity on Bale, or describe them by phone.'),
             ('Review and quote', 'Thread size, pitch and material are reviewed and a price is given.'),
             ('Thread rolling', 'The shafts are threaded on the rolling machine.'),
             ('Delivery', 'The screws and threaded parts are checked and delivered.'),
         ]},
    ],
    'faq': [
        ('What is thread rolling?', 'Thread rolling forms a thread on a shaft by pressing it between threaded rolls, with no chips. The metal is not cut away but displaced into the shape of the thread.'),
        ('Why is a rolled screw stronger?', 'In rolling, the grain of the metal is not cut but bends to follow the thread form, the thread surface is work-hardened by cold forming and the root comes out smoother. The result is a screw that is stronger and longer-lasting than one with a machined thread.'),
        ('Do you roll threads on stainless steel?', 'Yes. HyperFab uses a thread rolling machine to turn stainless steel and mild steel shafts into strong screws.'),
        ('Which thread sizes and pitches can you roll?', 'Thread size and pitch are reviewed for each order. Send the screw drawing or specification, or call ' + TEL_EN + '.'),
        ('What is the minimum order for thread rolling?', 'Ask when you enquire. Tell us how many screws or parts you need and the feasibility and price will be confirmed.'),
        ('How is thread rolling priced?', 'The price depends on the shaft material and size, the thread specification and length, and the quantity, and is given after the drawing or specification has been reviewed. Rolling itself is a cost-effective way to make screws.'),
        ('Where is HyperFab’s thread rolling service based?', 'HyperFab is based in Tehran, Iran. Thread rolling is ordered by phone on ' + TEL_EN + ' or on Bale (@hyperfab_pro).'),
    ],
    'cta_h': 'Send us your screw or shaft specification',
    'cta_p': 'Send the screw drawing or specification, material and quantity, or call. HyperFab’s industrial projects specialist answers by phone.',
    'cta_btns': CTA_BTNS,
    'schema': svc('HyperFab Thread Rolling', ['Rolled threads', 'Roll threading', 'رولینگ رزوه'],
                  'Thread rolling and screw making from stainless steel and mild steel shafts', '/en/thread-rolling/',
                  'Thread rolling: stainless steel and mild steel shafts turned into strong screws on a thread rolling machine; stronger, longer-lasting threads than machined threads, by a cost-effective process.'),
}


def page(key, slug, title, desc, kw):
    return {'key': key, 'file': 'en/' + slug + '/index.html', 'path': '/en/' + slug + '/', 'alt_path': '/' + slug + '/',
            'alt_rel': slug + '/', 'priority': '0.8', 'title': title, 'desc': desc, 'keywords': kw}


PAGES = {
    'page_tubelaser': page('tubelaser', 'tube-laser-cutting', 'Tube & Profile Laser Cutting in Tehran, Iran | HyperFab',
                           'HyperFab in Tehran, Iran laser-cuts box section, round pipe, angle and channel in steel, stainless and aluminium: clean, accurate cuts, sample to batch.',
                           'tube laser cutting, profile laser cutting, box section laser cutting, RHS SHS laser cutting, round pipe laser cutting, angle and channel laser cutting, stainless steel tube laser cutting, aluminium profile laser cutting, tube laser cutting Tehran, tube laser cutting Iran, HyperFab'),
    'page_threadroll': page('threadroll', 'thread-rolling', 'Thread Rolling: Rolled Screws in Tehran, Iran | HyperFab',
                            'HyperFab in Tehran, Iran turns stainless and steel shafts into strong screws by thread rolling: cold-formed threads, stronger than cut threads, cost-effective.',
                            'thread rolling, rolled threads, rolled vs cut threads, custom rolled screws, thread rolling Tehran, thread rolling Iran, HyperFab'),
    'page_welding': page('welding', 'welding', 'TIG & MIG Welding, Stainless & Aluminium, Tehran | HyperFab',
                         'HyperFab in Tehran, Iran: TIG and MIG welding of stainless and 6000-series aluminium, TIG welding of St37 steel, welded structures to drawing, VT/PT/PAUT.',
                         'TIG welding stainless steel Tehran, TIG welding Iran, St37 steel TIG welding, mild steel welding Tehran, MIG welding Iran, stainless steel welding Tehran, aluminium welding Iran, 6061 aluminium welding, welded fabrication Iran, stainless frame fabrication, weld testing PT PAUT, HyperFab'),
    'page_turning': page('turning', 'cnc-turning', 'Batch CNC Turning in Tehran, Iran: Brass & Steel | HyperFab',
                         'HyperFab in Tehran, Iran produces batch CNC turned parts to drawing in brass, MO40 and CK45 steel, with fit tolerances and first-article approval.',
                         'CNC turning batch production Iran, CNC turning Tehran, batch turning Iran, precision brass parts Iran, MO40 42CrMo4 turning, CK45 C45 turning, gauge manufacturing, turned parts supplier Iran, HyperFab'),
    'page_extrusion': page('extrusion', 'aluminium-extrusion', 'Custom Aluminium Extrusion Profiles, Tehran, Iran | HyperFab',
                           'HyperFab in Tehran, Iran extrudes aluminium profiles in your own cross-section with a dedicated die. You order by tonnage and pay for the die.',
                           'custom aluminium extrusion profiles Iran, aluminium extrusion Tehran, aluminum extrusion Iran, custom aluminium profile, extrusion die, T-slot profile, heat sink extrusion, aluminium profile manufacturer Iran, HyperFab'),
    'page_plating': page('plating', 'plating-anodizing', 'Gold & Silver Plating and Anodizing, Tehran, Iran | HyperFab',
                         'HyperFab in Tehran, Iran does gold and silver plating on brass and other metals, and anodizing and chromate (Alodine) on aluminium, for production runs.',
                         'gold plating Tehran, gold plating Iran, silver plating brass Iran, anodizing Tehran, aluminium anodizing Iran, chromate conversion, Alodine, connector plating, HyperFab'),
    'page_coating': page('coating', 'powder-coating', 'Powder Coating in Tehran, Iran: Pearl & Hammer | HyperFab',
                         'HyperFab in Tehran, Iran powder-coats batch metal parts in pearl, hammer, textured, gloss and matt finishes. Priced by size, finish and quantity.',
                         'powder coating Tehran, powder coating Iran, electrostatic powder coating, oven-cured paint, pearl powder coat, hammer finish, RAL powder coating, aluminium powder coating, HyperFab'),
}

FEATURE_PARAS = [
    'When a part moves from prototype to volume, the process has to change. For industrial and batch production, HyperFab offers a complete chain: <a href="punching/">sheet and tube punching</a>, <a href="tube-laser-cutting/">tube and profile laser cutting</a>, <a href="injection-molding/">mould making and injection moulding</a>, <a href="cnc-turning/">batch CNC turning</a>, <a href="thread-rolling/">thread rolling</a>, <a href="aluminium-extrusion/">aluminium extrusion</a>, <a href="welding/">welding and welded fabrication</a>, <a href="plating-anodizing/">plating and anodizing</a> and <a href="powder-coating/">powder coating</a>. A part can go from production to final finish in one place.',
    'HyperFab’s engineering team comes from Iran’s top universities, including Sharif University of Technology, and has worked in industry for years. It has taken four polyethylene injection moulds from build to commissioning, and more than 80,000 parts have been produced with them. Its record also includes quality control of 8,000 punched tubes, mating brass parts and MO40 and CK45 gauges, and stainless and aluminium structures for the medical and marine industries.',
]

FEATURE_POINTS = [
    '<b><a href="punching/">Sheet and tube punching</a>:</b> metal and polyethylene; punching die design and manufacture and production runs.',
    '<b><a href="tube-laser-cutting/">Tube and profile laser cutting</a>:</b> box section, pipe, angle and channel in mild steel, stainless and aluminium; from sample to batch.',
    '<b><a href="injection-molding/">Mould making and injection moulding</a>:</b> mould making, sampling and production in PE, PP, ABS and nylon.',
    '<b><a href="cnc-turning/">Batch CNC turning</a>:</b> brass parts with fit tolerances and gauge parts in MO40 and CK45.',
    '<b><a href="thread-rolling/">Thread rolling</a>:</b> stainless and mild steel shafts turned into strong screws; stronger and longer-lasting than cut threads.',
    '<b><a href="aluminium-extrusion/">Aluminium extrusion</a>:</b> your section with a dedicated die; you bring tonnage and die cost, we do the rest.',
    '<b><a href="welding/">TIG and MIG welding</a>:</b> stainless steel and 6000-series aluminium, TIG welding of St37 steel, welded structures and platforms, with VT, PT and PAUT.',
    '<b><a href="plating-anodizing/">Plating and anodizing</a>:</b> silver and gold on brass and other metals, anodizing and chromate on aluminium.',
    '<b><a href="powder-coating/">Powder coating</a>:</b> powder, pearl, hammer and textured finishes.',
    f'<b>Phone consultation:</b> HyperFab’s industrial projects specialist: <a href="{TEL}">{TEL_EN}</a>.',
]

HOME_FAQ = [
    ('Does HyperFab weld stainless steel and aluminium?', 'Yes. HyperFab does TIG and MIG welding of stainless steel and 6000-series aluminium, TIG welding of St37 steel, and builds welded machine structures and large platform structures to the client’s drawings. VT, PT and PAUT testing is available on request, and many units have been built for the medical and marine industries. Laser cutting of the structure’s tube and box-section members can also be handled by HyperFab.'),
    ('Does HyperFab do batch CNC turning?', 'Yes. HyperFab produces batch turned parts to drawing, including brass parts with fit tolerances and gauge parts in MO40 and CK45 steel. Each part’s critical points are engineered and checked before production.'),
    ('Does HyperFab extrude aluminium profiles?', 'Yes, as a specialisation and for aluminium only. Profiles are made in the customer’s own section with a dedicated die. The customer has the required tonnage and pays for the die, and HyperFab’s engineering team handles everything from section consultation to delivery.'),
    ('Does HyperFab do plating, anodizing and powder coating?', 'Yes, for production runs. HyperFab does silver and gold plating on brass and other metals, and anodizing and chromate (Alodine) on aluminium. Powder coating in powder, pearl, hammer and textured finishes is also available.'),
]


def apply(C):
    C.update({'welding': WELDING, 'turning': TURNING, 'plating': PLATING, 'coating': COATING, 'extrusion': EXTRUSION, 'tubelaser': TUBELASER, 'threadroll': THREADROLL})
    C.update(PAGES)
    C['tool_keys'] = ['estimator', 'tekeyab', 'punching', 'tubelaser', 'injection', 'turning', 'threadroll', 'extrusion', 'welding', 'plating', 'coating']
    f = C['home']['ind_feature']
    f.update({'title': 'Industrial and batch production: from moulds and turning to welding, plating and coating',
              'sub': 'A complete chain for batch parts, from production to final finish, with one responsible engineering team.',
              'paras': FEATURE_PARAS, 'points': FEATURE_POINTS,
              'img': 'assets/img/works/flange-steel-4.jpg', 'img_alt': 'Turning an AISI 304 stainless part on a HyperFab project', 'caption': 'Real photo: turning an AISI 304 stainless part on a HyperFab project.', 'img_w': 868, 'img_h': 1156,
              'more_rel': 'en/cnc-turning/', 'more': 'Batch CNC turning', 'try_url': 'en/welding/', 'try': 'Welding and welded fabrication'})
    C['industrial_links'][1:1] = [('Tube and profile laser cutting', 'en/tube-laser-cutting/')]  # right after punching
    C['industrial_links'] += [('Batch CNC turning', 'en/cnc-turning/'), ('Thread rolling', 'en/thread-rolling/'), ('Aluminium extrusion', 'en/aluminium-extrusion/'),
                              ('Welding and welded fabrication', 'en/welding/'), ('Plating and anodizing', 'en/plating-anodizing/'),
                              ('Powder coating', 'en/powder-coating/')]
    for name, d, path in (('HyperFab Batch CNC Turning', TURNING, '/en/cnc-turning/'), ('HyperFab Aluminium Extrusion', EXTRUSION, '/en/aluminium-extrusion/'),
                          ('HyperFab Welding and Welded Fabrication', WELDING, '/en/welding/'), ('HyperFab Plating and Anodizing', PLATING, '/en/plating-anodizing/'),
                          ('HyperFab Powder Coating', COATING, '/en/powder-coating/'),
                          ('HyperFab Tube & Profile Laser Cutting', TUBELASER, '/en/tube-laser-cutting/'), ('HyperFab Thread Rolling', THREADROLL, '/en/thread-rolling/')):
        C['tools_as_services'].append({'title': name, 'paras': [d['schema'][0]['description']], 'url': SITE + path})
    C['knows_about'] += ['CNC turning', 'batch production', 'TIG welding', 'MIG welding', 'stainless steel welding', 'aluminium welding',
                         'welded fabrication', 'non-destructive weld testing', 'gold plating', 'silver plating', 'anodizing',
                         'chromate conversion coating', 'powder coating', 'aluminium extrusion', 'custom aluminium profiles',
                         'tube laser cutting', 'profile laser cutting', 'box section laser cutting', 'thread rolling']
    C['org_desc'] = C['org_desc'].rstrip('.') + ', tube and profile laser cutting, batch CNC turning, thread rolling, aluminium extrusion, welding and welded fabrication, plating and anodizing, and powder coating.'
    C['home']['faq'][-1:-1] = HOME_FAQ
    cnc = next(s for s in C['services'] if s['key'] == 'cnc')
    cnc['paras'].append('CNC machining at HyperFab is not only for mould making. HyperFab makes all kinds of parts to customers’ drawings with high quality and precision, from single parts and prototypes to <a href="cnc-turning/">batch production of turned parts</a> in brass and MO40 and CK45 steel.')
    cnc['specs'].append(('Batch production', '<a href="cnc-turning/">Batch CNC turning</a>'))
