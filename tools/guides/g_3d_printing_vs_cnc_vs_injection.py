GUIDE = {
    'fa': {
        'slug': '3d-printing-vs-cnc-vs-injection',
        'title': 'پرینت سه‌بعدی، CNC یا تزریق پلاستیک؟ انتخاب روش ساخت بر اساس تعداد',
        'seo_title': 'پرینت سه\u200cبعدی، CNC یا تزریق؟ انتخاب بر اساس تعداد',
        'desc': 'برای چند قطعه پرینت سه‌بعدی، برای ده‌ها تا صدها قطعه پرینت یا CNC و برای هزاران قطعه تزریق پلاستیک؛ منطق انتخاب روش ساخت بر اساس تیراژ، جنس و دقت.',
        'lead': 'اگر فقط یک تا چند قطعه لازم دارید، پرینت سه‌بعدی معمولاً ارزان‌ترین و سریع‌ترین راه است. برای ده‌ها تا صدها قطعه، بسته به جنس، هندسه و دقت، پرینت سه‌بعدی یا ماشین‌کاری CNC انتخاب می‌شود. وقتی تیراژ به هزاران قطعه می‌رسد، هزینه‌ی قالب سرشکن می‌شود و تزریق پلاستیک کمترین قیمت هر قطعه را می‌دهد.',
        'updated': '2026-11-15',
        'service': 'services',
        'img': 'assets/img/hero-parts.webp',
        'sections': [
            {
                'h': 'فرق پرینت سه‌بعدی، CNC و تزریق پلاستیک چیست؟',
                'p': [
                    'این سه روش رایج ساخت قطعه منطق هزینه‌ی کاملاً متفاوتی دارند. پرینت سه‌بعدی (3D Printing)، که «پرینت سه بعدی» یا «چاپ سه‌بعدی» هم نوشته می‌شود، قطعه را بدون هیچ ابزار و قالبی لایه‌به‌لایه از روی فایل می‌سازد. ماشین‌کاری CNC (CNC Machining) قطعه را با فرز و تراش از یک تکه‌ی خام درمی‌آورد. تزریق پلاستیک (Injection Molding) پلیمر ذوب‌شده را درون قالب فولادی می‌فرستد و هر ضرب یک یا چند قطعه‌ی یکسان بیرون می‌دهد.',
                    'تفاوت اصلی در هزینه‌ی راه‌اندازی است. پرینت سه‌بعدی تقریباً هزینه‌ی راه‌اندازی ندارد، CNC به برنامه‌نویسی و بستن قطعه نیاز دارد و تزریق پلاستیک بدون طراحی و ساخت قالب (قالب‌سازی) شروع نمی‌شود. در عوض، قیمت هر قطعه در تزریق با بالا رفتن تیراژ به‌شدت پایین می‌آید، در حالی که در پرینت سه‌بعدی تقریباً ثابت می‌ماند.',
                ],
                'table': {
                    'head': ['معیار', 'پرینت سه‌بعدی', 'ماشین‌کاری CNC', 'تزریق پلاستیک'],
                    'rows': [
                        ['هزینه‌ی راه‌اندازی', 'تقریباً صفر؛ بدون ابزار و قالب', 'کم؛ برنامه‌نویسی و فیکسچر', 'زیاد؛ طراحی و ساخت قالب'],
                        ['قیمت هر قطعه با افزایش تعداد', 'تقریباً ثابت؛ فقط تخفیف پلکانی', 'کمی کاهش پیدا می‌کند', 'به‌شدت کاهش پیدا می‌کند'],
                        ['تیراژ مناسب', 'یک تا ده‌ها قطعه', 'یک تا صدها قطعه', 'هزاران قطعه و بیشتر'],
                        ['متریال در هایپرفب', 'PLA، PETG، ABS، TPU و رزین', 'پلی‌اتیلن، پلی‌استال، تفلون، نایلون، پلکسی، برنج', 'پلی‌اتیلن، پلی‌پروپیلن، ABS، نایلون، پلی‌کربنات، پلی‌استال'],
                        ['دقت و سطح', 'مناسب نمونه؛ رزینی جزئیات ریزتری دارد', 'بیشترین کنترل روی ابعاد و سطح', 'تکرارپذیر؛ وابسته به قالب و جمع‌شدگی'],
                        ['تغییر طرح', 'آسان؛ فقط فایل عوض می‌شود', 'آسان؛ برنامه اصلاح می‌شود', 'پرهزینه؛ قالب باید اصلاح شود'],
                        ['قیمت‌گذاری در هایپرفب', 'FDM آنلاین و لحظه‌ای در hyperfab.ir', 'پس از بررسی نقشه', 'هزینه‌ی قالب + هزینه‌ی هر ضرب، تلفنی'],
                    ],
                },
            },
            {
                'h': 'برای یک تا چند قطعه کدام روش ارزان‌تر است؟',
                'p': [
                    'وقتی فقط یک نمونه یا چند قطعه لازم دارید، هزینه‌ی راه‌اندازی تعیین‌کننده است. پرینت سه‌بعدی FDM در این بازه تقریباً همیشه ارزان‌ترین گزینه است، چون نه قالبی لازم است و نه برنامه‌ی ماشین‌کاری؛ فایل STL یا 3MF مستقیم به قطعه تبدیل می‌شود. در هایپرفب حداقل سفارش یک قطعه است و تخمین‌گر آنلاین قیمت در hyperfab.ir قیمت FDM را همان لحظه نشان می‌دهد.',
                    'برای قطعه‌ی کوچک با جزئیات ریز یا سطح صاف، مثل مدل نمایشی یا قطعه‌ی دقیق مونتاژی، پرینت رزینی (SLA / DLP) نتیجه‌ی بهتری می‌دهد. اگر قطعه باید از جنس واقعی مهندسی مثل تفلون، پلی‌استال یا برنج باشد، یا روی آن رزوه و سطح آب‌بندی دقیق لازم است، ماشین‌کاری CNC حتی برای یک قطعه هم منطقی است.',
                ],
            },
            {
                'h': 'برای ده‌ها تا صدها قطعه پرینت سه‌بعدی بهتر است یا CNC؟',
                'p': [
                    'در این بازه، انتخاب بیشتر به هندسه و جنس بستگی دارد تا به تعداد. پرینت سه‌بعدی برای قطعات با هندسه‌ی پیچیده، حفره‌های داخلی یا شکل‌های ارگانیک مناسب است، چون پیچیدگی تقریباً هزینه‌ای اضافه نمی‌کند. تخفیف پلکانی قیمت واحد را پایین می‌آورد، اما هر قطعه همچنان زمان چاپ و متریال خودش را می‌خواهد.',
                    'ماشین‌کاری CNC برای قطعات منشوری و ساده‌تر، مثل بوش، واشر، غلتک و فیکسچر، و هر جا که جنس واقعی و دقت ابعادی اهمیت دارد برنده است. وقتی برنامه‌ی ماشین‌کاری یک بار نوشته شد، هزینه‌ی راه‌اندازی بین قطعات تقسیم می‌شود. برای قطعات چرخشی فلزی در تیراژ بالاتر، مثل اتصالات برنجی، تراشکاری CNC تیراژی هایپرفب مسیر جداگانه‌ای است.',
                ],
            },
            {
                'h': 'تزریق پلاستیک از چه تیراژی به‌صرفه است؟',
                'p': [
                    'وقتی تعداد به هزاران قطعه و بیشتر می‌رسد، تزریق پلاستیک معمولاً اقتصادی‌ترین روش است. هزینه‌ی ساخت قالب یک بار پرداخت می‌شود و بین همه‌ی قطعات سرشکن می‌شود. بعد از آن، قیمت هر قطعه بیشتر به جنس، وزن قطعه و زمان سیکل بستگی دارد.',
                    'تزریق علاوه بر قیمت، یکنواختی هم می‌دهد: قطعه‌ی آخر همان ابعاد قطعه‌ی اول را دارد. در هایپرفب پروژه‌ی تزریق با بررسی قالب‌پذیری طرح شروع می‌شود و هزینه‌ی ساخت قالب و هزینه‌ی هر ضرب جدا و شفاف اعلام می‌شود. این مسیر تلفنی هماهنگ می‌شود، نه از راه سفارش آنلاین.',
                ],
            },
            {
                'h': 'جنس و دقت قطعه چطور روش ساخت را تغییر می‌دهد؟',
                'p': [
                    'تعداد تنها معیار نیست و گاهی جنس قطعه انتخاب را از پیش مشخص می‌کند. اگر قطعه باید از برنج، تفلون (PTFE) یا پلی‌استال باشد، پرینت سه‌بعدی جایگزین واقعی آن نیست و CNC گزینه‌ی طبیعی است. اگر قطعه از پلی‌اتیلن یا پلی‌پروپیلن و در تیراژ بالا لازم است، تزریق پلاستیک همان جنس را با هزینه‌ی کمتر می‌دهد.',
                    'در دقت هم تفاوت روشن است. CNC بیشترین کنترل را روی ابعاد و کیفیت سطح دارد و برای سطوح جفت‌شونده و جای بلبرینگ مناسب است. تزریق پلاستیک ابعاد تکرارپذیر می‌دهد، اما دقت نهایی به طراحی قالب و جمع‌شدگی (Shrinkage) پلیمر وابسته است. پرینت FDM خطوط لایه دارد و استحکامش در جهت عمود بر لایه‌ها کمتر است.',
                ],
            },
            {
                'h': 'نقطه‌ی سربه‌سر بین روش‌ها چطور مشخص می‌شود؟',
                'p': [
                    'منطق مقایسه حتی بدون عدد ساده است. هزینه‌ی کل هر روش دو بخش دارد: هزینه‌ی ثابت (ابزار، قالب، برنامه‌نویسی) و هزینه‌ی متغیر (قیمت هر قطعه ضرب در تعداد). پرینت سه‌بعدی هزینه‌ی ثابت تقریباً صفر و هزینه‌ی متغیر بالاتری دارد. تزریق پلاستیک برعکس است: هزینه‌ی ثابت زیاد و هزینه‌ی هر قطعه‌ی کم. CNC میان این دو قرار می‌گیرد.',
                    'اگر هزینه‌ی کل هر روش را بر حسب تعداد روی یک نمودار رسم کنید، خط‌ها جایی همدیگر را قطع می‌کنند؛ آن نقطه، نقطه‌ی سربه‌سر (Break-even) است. پایین‌تر از آن روش بدون قالب ارزان‌تر است و بالاتر از آن قالب هزینه‌ی خودش را برمی‌گرداند. جای دقیق این نقطه برای هر قطعه فرق می‌کند، پس باید برای هر پروژه جداگانه حساب شود. پیش از تصمیم، به این پرسش‌ها جواب دهید:',
                ],
                'ul': [
                    'کل تیراژ در طول عمر محصول چقدر است، نه فقط سفارش اول؟',
                    'آیا طرح نهایی است یا هنوز احتمال تغییر دارد؟',
                    'قطعه باید از چه جنسی باشد و چه بار، دما یا محیطی را تحمل کند؟',
                    'کدام ابعاد واقعاً حساس‌اند و چه کیفیت سطحی لازم است؟',
                    'هندسه‌ی قطعه پیچیده است یا منشوری و ساده؟',
                ],
            },
            {
                'h': 'قیمت ساخت قطعه با هر روش به چه عواملی بستگی دارد؟',
                'p': [
                    'قیمت هیچ‌کدام از این روش‌ها بدون دیدن فایل یا نقشه قابل اعلام نیست؛ عوامل اصلی این‌ها هستند:',
                    'برای پرینت سه‌بعدی FDM، قیمت را همین حالا با بارگذاری فایل در تخمین‌گر آنلاین hyperfab.ir ببینید؛ برای CNC هم فایل یا نقشه را در همان سایت بارگذاری کنید تا پس از بررسی، قیمت اعلام شود. برای پروژه‌ی قالب‌سازی و تزریق پلاستیک، یا اگر مطمئن نیستید کدام روش برای تیراژ شما مناسب است، با ۰۹۹۶۲۲۳۳۸۹۸ تماس بگیرید تا پس از بررسی طرح، روش و قیمت دقیق پیشنهاد شود.',
                ],
                'ul': [
                    'پرینت سه‌بعدی: حجم و وزن متریال، زمان چاپ، ضخامت لایه، میزان پرشدگی (Infill)، نوع فیلامنت یا رزین و تعداد.',
                    'ماشین‌کاری CNC: جنس و اندازه‌ی ماده‌ی خام، تعداد عملیات و دفعات بستن قطعه، تلرانس‌ها و کیفیت سطح، و تعداد.',
                    'تزریق پلاستیک، بخش قالب: اندازه و پیچیدگی قطعه، تعداد حفره‌ها، زیربرش‌ها و کشویی‌ها، کیفیت سطح و جنس فولاد قالب.',
                    'تزریق پلاستیک، بخش تولید: جنس و وزن قطعه، زمان سیکل و تیراژ.',
                ],
            },
        ],
        'faq': [
            ('برای ده قطعه کدام روش ارزان‌تر است؟',
             'برای ده قطعه معمولاً پرینت سه‌بعدی FDM ارزان‌ترین گزینه است، چون هزینه‌ی راه‌اندازی ندارد و قیمتش را همان لحظه در تخمین‌گر آنلاین hyperfab.ir می‌بینید. اگر قطعه باید از جنس مهندسی مثل تفلون یا برنج باشد یا دقت بالایی بخواهد، ماشین‌کاری CNC انتخاب بهتری است. ساخت قالب تزریق برای این تعداد توجیه اقتصادی ندارد.'),
            ('قالب تزریق از چه زمانی هزینه‌ی خودش را برمی‌گرداند؟',
             'وقتی صرفه‌جویی در قیمت هر قطعه، ضرب در تعداد کل، از هزینه‌ی ساخت قالب بیشتر شود. این نقطه به اندازه، پیچیدگی و جنس قطعه بستگی دارد و معمولاً در تیراژهای بالا رخ می‌دهد. هایپرفب پس از بررسی طرح، هزینه‌ی قالب و هزینه‌ی هر ضرب را جدا اعلام می‌کند تا بتوانید مقایسه کنید.'),
            ('آیا قطعه‌ی پرینت سه‌بعدی به اندازه‌ی کافی محکم است؟',
             'برای نمونه‌ی اولیه، فیکسچر، جیگ و بسیاری از قطعات کاربردی با بار متوسط بله، به‌ویژه با PETG یا ABS و جهت‌گیری درست در چاپ. قطعه‌ی FDM در جهت عمود بر لایه‌ها ضعیف‌تر است، پس برای بار سنگین یا سایش دائمی، ماشین‌کاری CNC از نایلون یا پلی‌استال یا تزریق پلاستیک مطمئن‌تر است.'),
            ('می‌توانم بعداً روش ساخت را عوض کنم؟',
             'بله و مسیر رایج همین است: نمونه با پرینت سه‌بعدی، تیراژ کم با پرینت یا CNC و در نهایت تزریق پلاستیک. اگر از اول زاویه‌ی خروج، ضخامت دیواره‌ی یکنواخت و ریب‌ها را در طرح رعایت کنید، انتقال به قالب بدون طراحی دوباره انجام می‌شود.'),
        ],
        'related': ['injection-mould-making-steps', 'brass-cnc-turning-batch'],
    },
    'en': {
        'slug': '3d-printing-vs-cnc-vs-injection',
        'title': '3D Printing vs CNC vs Injection Moulding: Choosing by Quantity',
        'seo_title': '3D Printing vs CNC vs Injection Moulding by Quantity',
        'desc': 'One to a few parts: 3D printing. Tens to hundreds: printing or CNC. Thousands: injection moulding. How quantity, material and accuracy decide the process.',
        'lead': 'For one to a few parts, 3D printing is usually the cheapest and quickest option. For tens to hundreds, choose between 3D printing and CNC machining based on material, geometry and accuracy. Once you need thousands, the mould cost spreads across the run and injection moulding gives the lowest cost per part.',
        'updated': '2026-11-15',
        'service': 'services',
        'img': 'assets/img/hero-parts.webp',
        'sections': [
            {
                'h': '3D printing vs CNC vs injection moulding: what is the difference?',
                'p': [
                    'These three processes follow very different cost logic. 3D printing builds a part layer by layer straight from a file, with no tooling at all. CNC machining cuts the part out of a solid block by milling and turning. Injection moulding (injection molding in US spelling) forces molten polymer into a steel mould, and every shot produces one or more identical parts.',
                    'The key difference is set-up cost. 3D printing has almost none, CNC needs programming and fixturing, and injection moulding cannot start until a mould has been designed and built. In return, the cost per moulded part falls steeply as quantity rises, while the cost per printed part stays roughly flat.',
                ],
                'table': {
                    'head': ['Factor', '3D printing', 'CNC machining', 'Injection moulding'],
                    'rows': [
                        ['Set-up cost', 'Almost none; no tooling', 'Low; programming and fixturing', 'High; mould design and build'],
                        ['Cost per part as quantity rises', 'Roughly flat; stepped discounts only', 'Falls a little', 'Falls steeply'],
                        ['Typical quantity', 'One to tens', 'One to hundreds', 'Thousands and up'],
                        ['Materials at HyperFab', 'PLA, PETG, ABS, TPU and resins', 'PE, acetal, PTFE, nylon, acrylic, brass', 'PE, PP, ABS, nylon, polycarbonate, acetal'],
                        ['Accuracy and finish', 'Fine for prototypes; resin gives finer detail', 'Tightest control of size and finish', 'Repeatable; depends on mould and shrinkage'],
                        ['Design changes', 'Easy; swap the file', 'Easy; edit the program', 'Costly; the mould must be modified'],
                        ['How HyperFab prices it', 'FDM instantly online at hyperfab.ir', 'After drawing review', 'Mould cost plus cost per shot, by phone'],
                    ],
                },
            },
            {
                'h': 'Cheapest way to make one to a few parts',
                'p': [
                    'When you need a single prototype or a handful of parts, set-up cost dominates. FDM 3D printing is almost always the cheapest option here because there is no mould and no machining program: your STL or 3MF file goes straight to the printer. HyperFab’s minimum order is one part, and the online price estimator on hyperfab.ir shows the FDM price the moment you upload.',
                    'For small parts with fine detail or a smooth surface, such as display models or precise assembly parts, resin printing (SLA / DLP) gives a better result. If the part must be made from a real engineering material such as PTFE, acetal or brass, or needs threads and accurate sealing faces, CNC machining makes sense even for a single piece.',
                ],
            },
            {
                'h': 'Tens to hundreds of parts: 3D printing or CNC?',
                'p': [
                    'In this range, geometry and material matter more than the count. 3D printing suits complex shapes, internal cavities and organic forms, because complexity adds little to the cost. Stepped discounts lower the unit price, but every part still needs its own print time and material.',
                    'CNC machining wins on simpler, prismatic parts such as bushings, washers, rollers and fixtures, and wherever the real material and dimensional accuracy matter. Once the program is written, its set-up cost is shared across the batch. For turned metal parts in larger quantities, such as brass fittings, HyperFab’s batch CNC turning is a separate service.',
                ],
            },
            {
                'h': 'At what quantity does injection moulding pay off?',
                'p': [
                    'Once you need thousands of parts or more, injection moulding is usually the most economical process. The mould is paid for once and its cost is spread across every part. After that, the cost per part depends mainly on material, part weight and cycle time.',
                    'Moulding also brings consistency: the last part matches the first. At HyperFab, an injection project starts with a mouldability review of the design, and the mould cost and cost per shot are quoted separately. These projects are arranged by phone rather than through online ordering.',
                ],
            },
            {
                'h': 'How material and accuracy change the choice',
                'p': [
                    'Quantity is not the only factor; sometimes the material decides for you. If the part must be brass, PTFE or acetal, 3D printing is no real substitute and CNC is the natural route. If you need polyethylene or polypropylene parts in high volumes, injection moulding gives you that material at a lower cost.',
                    'Accuracy differs too. CNC gives the most control over dimensions and surface finish, which suits mating faces and bearing seats. Injection moulding is highly repeatable, but final accuracy depends on mould design and polymer shrinkage. FDM parts show layer lines and are weaker across the layers.',
                ],
            },
            {
                'h': 'Break-even between processes, explained without numbers',
                'p': [
                    'The logic is simple even without figures. Each process has a fixed cost (tooling, mould, programming) and a variable cost (price per part times quantity). 3D printing has almost no fixed cost and a higher variable cost. Injection moulding is the opposite: a high fixed cost and a low cost per part. CNC sits in between.',
                    'Plot total cost against quantity for each process and the lines cross somewhere; that crossing is the break-even point. Below it, the tool-free process is cheaper; above it, the mould pays for itself. Where the lines cross is different for every part, so it has to be worked out project by project. Before you decide, answer these questions:',
                ],
                'ul': [
                    'What is the total volume over the product’s life, not just the first order?',
                    'Is the design frozen, or is it still likely to change?',
                    'What material does the part need, and what load, temperature or environment must it handle?',
                    'Which dimensions are truly critical, and what surface finish do you need?',
                    'Is the geometry complex, or simple and prismatic?',
                ],
            },
            {
                'h': 'What affects the cost of each process?',
                'p': [
                    'None of these processes can be priced without seeing the file or drawing, but the main cost drivers are clear:',
                    'For FDM 3D printing, upload your file to the online price estimator at hyperfab.ir and see the price now; for CNC, upload your model or drawing there too and receive a quote after review. For mould making and injection moulding, or if you are unsure which process fits your quantity, call 09962233898 and HyperFab will review the design and recommend a process with an exact quote.',
                ],
                'ul': [
                    '3D printing: material volume and weight, print time, layer height, infill, filament or resin type, and quantity.',
                    'CNC machining: stock material and size, number of operations and set-ups, tolerances and surface finish, and quantity.',
                    'Injection moulding, the mould: part size and complexity, number of cavities, undercuts and slides, surface finish and mould steel.',
                    'Injection moulding, production: part material and weight, cycle time and run quantity.',
                ],
            },
        ],
        'faq': [
            ('Which process is cheapest for ten pieces?',
             'For ten pieces, FDM 3D printing is usually cheapest because there is no set-up cost, and you can see the price instantly in the online estimator on hyperfab.ir. If the part must be an engineering material such as PTFE or brass, or needs high accuracy, CNC machining is the better choice. A mould is not worth building for that quantity.'),
            ('When does an injection mould pay off?',
             'When the saving per part, multiplied by the total quantity, exceeds the cost of building the mould. That point depends on part size, complexity and material, and it usually falls at high volumes. HyperFab quotes the mould cost and the cost per shot separately after reviewing the design, so you can compare.'),
            ('Are 3D-printed parts strong enough?',
             'For prototypes, jigs, fixtures and many functional parts under moderate load, yes, especially in PETG or ABS with the right print orientation. FDM parts are weaker across the layers, so for heavy loads or constant wear a part machined from nylon or acetal, or an injection-moulded part, is the safer choice.'),
            ('Can I switch methods later?',
             'Yes, and that is the usual path: prototype with 3D printing, make small batches by printing or CNC, then move to injection moulding. If the design includes draft, uniform wall thickness and ribs from the start, it can move to a mould without a redesign.'),
        ],
        'related': ['injection-mould-making-steps', 'brass-cnc-turning-batch'],
    },
}
