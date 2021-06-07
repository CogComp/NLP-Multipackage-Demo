/**
 * xel_langs {hashmap} maps abbreviations to the actual names of the languages
 */
var xel_langs = {
    "eng": "English",
	"cmn": "Mandarin",
	"spa": "Spanish",
	"fre": "French",
	"ger": "German",
	"jpn": "Japanese",
	"ita": "Italian",
	"dut": "Dutch",
	"prt": "Portuguese",
	"ara": "Arabic",
	"rus": "Russian"
}

/**
 * xel_examples {hashmap} maps each language to 1-5 exmaples
 */

var xel_examples = {
    "eng": [
		"St. Michael's Church is on 5th st. near the light.",
		"Hello world. My name is Mr. Smith. I work for the U.S. Government and I live in the U.S. I live in New York.",
		"Mr.O'Neill thinks that the boys' stories about Chile's capital aren't amusing.",
		"You can find it at N°. 1026.253.553. That is where the treasure is.",
		"I wasn’t really ... well, what I mean...see . . . what I'm saying, the thing is . . . I didn’t mean it.",
		"One further habit which was somewhat weakened . . . was that of combining words into self-interpreting compounds. . . . The practice was not abandoned. . . .",
		"The Indo-European Caucus won the all-male election 58-32.",
		"1) The first item. 2) The second item.",
		"1. The first item 2. The second item",
		"1. The first item. 2. The second item."
	],
	"cmn": [
		"巴拉克·奥巴马在夏威夷出生。他喜欢寿司。",
		"黄山位于安徽省南部黄山市境内，有72峰，主峰莲花峰海拔1864米，与光明顶、天都峰并称三大黄山主峰，为36大峰之一。黄山是安徽旅游的标志。",
		"这里有结婚的和尚未结婚的人。",
		"真的是这样吗... 怎么这么多事儿！",
		"你家用什么样的电脑？我家用家用电脑。",
		"你的牙刷了吗？我的牙刷不见了。",
		"把手举起来！这个把手是木制的。",
		"一行行行行行，一行不行行行不不行。",
		"小龙女说：\"我想过过过儿过过的生活。\"",
		"另一个宿舍的人说你们宿舍的地得扫了。",
		"校长说衣服上除了校徽别别别的。",
		"来到儿子等校车的地方，邓超对孙俪说:\"我也想等等等等等过的那辆车。\"",
		"一位友好的哥谭市民。",
	],
	"spa": [
		"Mohandas Karamchand Gandhi (Porbandar, India británica; 2 de octubre de 1869–Nueva Delhi, Unión de la India; 30 de enero de 1948) fue el dirigente más destacado del Movimiento de independencia de la India contra el Raj británico, para lo que practicó la desobediencia civil no violenta, además de pacifista, político, pensador y abogado hinduista indio.",
        "Sigmund Freud fue un neurólogo austriaco y fundador del psicoanálisis, un método clínico para tratar la psicopatología a través del diálogo entre un paciente y un psicoanalista. Freud nació de padres judíos gallegos en la ciudad morava de Freiberg, en el Imperio austríaco. Se graduó como doctor en medicina en 1881 en la Universidad de Viena. Freud vivió y trabajó en Viena, donde estableció su práctica clínica en 1886. En 1938, Freud dejó Austria para escapar de la persecución nazi. Murió exiliado en el Reino Unido en 1939.",
		"Barack Hussein Obama II es un político y abogado estadounidense que se desempeñó como el 44º presidente de los Estados Unidos de 2009 a 2017. Miembro del Partido Demócrata, Obama fue el primer presidente afroamericano de los Estados Unidos. Anteriormente se desempeñó como senador de Estados Unidos por Illinois de 2005 a 2008 y como senador del estado de Illinois de 1997 a 2004. ",
		"Mohandas Karamchand Gandhi fue un abogado indio, nacionalista anticolonial y especialista en ética política, que empleó la resistencia no violenta para liderar la exitosa campaña por la independencia de la India del dominio británico y, a su vez, inspiró movimientos por los derechos civiles y la libertad en todo el mundo. El Mahātmā honorífico, que se le aplicó por primera vez en 1914 en Sudáfrica, ahora se usa en todo el mundo."
	], 
	"fre": [
		"Apple cherche à acheter une start-up anglaise pour 1 milliard de dollars.",
		"Nous avons atteint la fin du sentier.",
		"Le comité de sécurité de l’AEM « examinera plus en détail les informations demain [mardi], et a convoqué une réunion extraordinaire le jeudi 18 mars pour statuer quant aux informations recueillies et à toute autre mesure qui pourrait s’avérer nécessaire », a ainsi déclaré à Amsterdam le régulateur européen, par voie de communiqué.",
		"Vous êtes un(e) mordu(e) de sneakers ou bien tout simplement fan de la marque, économisez sur vos prochaines commandes grâce à nos codes promo Nike ! Agrandissez votre collection ou votre équipez vous à prix réduit. Cette semaine, voici les promotions à ne pas louper: 15% de réduc supplémentaire avec notre code promo NIke."
	],
	"ger": [
		"Die ganze Stadt ist ein Startup: Shenzhen ist das Silicon Valley für Hardw",
		"Sigmund Freud war ein österreichischer Neurologe und der Begründer der Psychoanalyse, einer klinischen Methode zur Behandlung der Psychopathologie im Dialog zwischen einem Patienten und einem Psychoanalytiker. Freud wurde als Sohn galizischer jüdischer Eltern im mährischen Freiberg im österreichischen Reich geboren. Er qualifizierte sich 1881 als Doktor der Medizin an der Universität Wien. Freud lebte und arbeitete in Wien, nachdem er dort 1886 seine klinische Praxis eingerichtet hatte. 1938 verließ Freud Österreich, um der nationalsozialistischen Verfolgung zu entgehen. Er starb 1939 im britischen Exil.",
		"Volkswagen eifert immer stärker dem Rivalen Tesla nach: Bis 2030 will der Konzern sechs Fabriken zur Fertigung von Batteriezellen aufbauen. Auch ein europaweites Netz von Schnelllade-Stationen für Elektroautos soll entstehen.",
		"Er habe große Sorge, dass der Mallorca-Ansturm ein erneutes Ansteigen der Fallzahlen verursachen werde. Es würde ihn nicht wundern, wenn die Insel in drei Wochen wieder in einen harten Lockdown müsse, sagte Schmude. Hotels und Airlines hätten zwar umfassende Hygienekonzepte umgesetzt, aber \"wir wissen, dass sich Menschen im Urlaub anders als im Alltag verhalten\". Generell versuchten viele Menschen, Probleme im Urlaub auszublenden. \"Und aktuell wollen diese Leute ja ganz bewusst raus aus der Corona-Situation in Deutschland\", so Schmude.",
		"Einsteins Hauptwerk, die Relativitätstheorie, machte ihn weltberühmt. Im Jahr 1905 erschien seine Arbeit mit dem Titel Zur Elektrodynamik bewegter Körper, deren Inhalt heute als spezielle Relativitätstheorie bezeichnet wird. 1915 publizierte er die allgemeine Relativitätstheorie. Auch zur Quantenphysik leistete er wesentliche Beiträge. „Für seine Verdienste um die theoretische Physik, besonders für seine Entdeckung des Gesetzes des photoelektrischen Effekts“, erhielt er den Nobelpreis des Jahres 1921, der ihm 1922 überreicht wurde. Seine theoretischen Arbeiten spielten – im Gegensatz zur weit verbreiteten Meinung – beim Bau der Atombombe und der Entwicklung der Kernenergie nur eine indirekte Rolle."
	],
	"jpn": [
		"アップルがイギリスの新興企業を１０億ドルで購入を検討",
		"第二次世界大戦後の日本において、闇市として発展した。その後、高度経済成長とともに多様な電子機器や部品（ハードウェア）およびソフトウェアを取り扱う店舗などが建ち並ぶ世界有数の電気街として発展した。世界的な観光地の顔も有する。秋葉（あきば）・アキバ・AKIBAの略称で呼ばれる。",
		"江戸時代、神田川に万世橋はなく、筋違橋（すじかいばし）と呼ばれる橋がやや上流に架かっており、街道はここから現在のコトブキヤ秋葉原館やAKIBAカルチャーズZONEのある道（現：特別区道千第678号）を通って、住友不動産秋葉原ビルに突き当たって右に折れ、中央通りに出るルートをとっていた[4]。この道は徳川将軍家の寛永寺参詣道であったことから下谷御成街道と呼ばれた。総武本線ガードの御成街道架道橋に名残を留める。",
		"富士山が日本を代表する名峰であることから、日本の各地に「富士」の付く地名が多数存在している。富士山麓では静岡県に富士市や富士宮市、富士郡、山梨県に富士吉田市や富士河口湖町、富士川町がある。他によくあるものとして富士山が見える場所を富士見と名づけたり（例：埼玉県富士見市）、富士山に似ている山（主に成層火山）に「富士」の名を冠する例（信濃富士など）がある。日本国外に移住した日本人たちも、居住地付近の山を「○○富士」と呼ぶことがある。",
		"江戸時代には、1767年（明和4年）に河村岷雪が絵本『百富士』を出版し、富士図の連作というスタイルを提示した。葛飾北斎は、河村岷雪の手法を援用した、富士図の連作版画『冨嶽三十六景』（1831-34年・天保2-5年頃）、及び、絵本『富嶽百景』（全三編。初編1834年・天保5年）を出版した。前者において、舶来顔料を活かした藍摺などの技法を駆使して富士を描き、夏の赤富士を描いた『凱風快晴』や『山下白雨』、荒れ狂う大波と富士を描いた『神奈川沖浪裏』などが知られる。後者は墨単色摺で、旧来の名所にこだわらず、天候描写に拘るなど、抽象性が高まっている。"
	],
	"ita": [
		"Apple vuole comprare una startup del Regno Unito per un miliardo di dollari",
		"La matrigna Albiera morì appena ventottenne nel 1464, quando la famiglia risiedeva già a Firenze, venendo sepolta in San Biagio. Ser Piero si risposò altre tre volte: una seconda (1464) con la quindicenne Francesca di ser Giuliano Lanfredini, che pure morì senza progenie, una terza con Margherita di Francesco di Jacopo di Guglielmo (1500), che gli diede finalmente sei figli; altri sei li ebbe dal quarto e ultimo matrimonio con Lucrezia Cortigiani.",
		"Il Rinascimento si sviluppò in Italia tra la fine del Medioevo e l'inizio dell'Età Moderna in un arco di tempo che va dall'inizio del quindicesimo secolo, fino alla fine del sedicesimo secolo. I suoi limiti cronologici conoscono ampie differenze tra discipline ed aree geografiche.",
		"Vissuto dalla maggior parte dei suoi protagonisti come un'età di cambiamento, maturò un nuovo modo di concepire il mondo e se stessi, sviluppando le idee dell'umanesimo, nato in ambito letterario nel quattordicesimo secolo per il rinato interesse degli studi classici, per opera soprattutto di Francesco Petrarca[3], e portandolo a influenzare per la prima volta anche le arti figurative e la mentalità corrente.",
		"«Fu tanto raro e universale, che dalla natura per suo miracolo esser produtto dire si puote: la quale non solo della bellezza del corpo, che molto bene gli concedette, volse dotarlo, ma di molte rare virtù volse anchora farlo maestro. Assai valse in matematica et in prospettiva non meno, et operò di scultura, et in disegno passò di gran lunga tutti li altri. Hebbe bellissime inventioni, ma non colorì molte cose, perché si dice mai a sé medesimo avere satisfatto, et però sono tante rare le opere sue. Fu nel parlare eloquentissimo et raro sonatore di lira [...] et fu valentissimo in tirari et in edifizi d'acque, et altri ghiribizzi, né mai co l'animo suo si quietava, ma sempre con l'ingegno fabricava cose nuove.»"
	],
	"dut": [
		"Apple overweegt om voor 1 miljard een U.K. startup te kopen",
		"In de 17e eeuw (circa 1630 - 1637) ontstond er in de Republiek der Zeven Verenigde Nederlanden rond de tulpenbol een bizarre tulpenmanie, ook wel \"tulpenrage\", \"tulpengekte\", \"tulpomanie\" of \"bollengekte\" genoemd: plotseling werden tulpenbollen speculatieve handelswaar. De gekte dreef de prijzen op tot exorbitante hoogte, zelfs tot de bol zijn gewicht in goud waard was. Er werden tulpen gekweekt in allerlei kleuren en door kunstschilders, zoals Nicolaes van Veerendael, op stillevens uitgebeeld. In deze periode zijn ook veel tulpentekeningen gemaakt.",
		"De aankoopcontracten, genoteerd op briefjes, werden voor grof geld doorverkocht. De prijs die uiteindelijk voor een bol betaald moest worden, werd doorgaans berekend naar het gewicht bij het rooien. Dit was de 'azenhandel'; een aas was een onder goudhandelaars gebruikte gewichtsmaat (1 aas = 0,048 gram). Deze handel was illegaal; de Staten van Holland verboden de verkoop van zaken die men zelf niet bezat. Naast de azenhandel in de colleges vonden ook openbare veilingen plaats van 'pondsgoed', waardeloze tulpen zonder fraaie kleurpatronen, die per pond verkocht werden aan argeloze kopers, voor extreme geldbedragen.",
		"Hij las veel in het Frans, onder meer Les temps difficiles (Parijs, 1869) door Charles Dickens, L'Imitation de Jésus Christ van Thomas a Kempis, William Shakespeare (Parijs, 1864) door Victor Hugo; in het Engels las hij The Pilgrim's Progress (Londen, 1877) door John Bunyan en Uncle Tom's Cabin (Londen, 1852) door Harriet Beecher Stowe. Dergelijke lectuur toont duidelijk aan dat hij intellectueel op een hoog peil stond.",
		"Behalve het grote aantal werken dat Johanna van Gogh bezat, hadden de volgende familieleden van Vincent werk in hun bezit: E.H. du Quesne-van Gogh tien stuks, Willemien van Gogh zeven stuks, Cornelia van Gogh-Carbentus één, Anna van Gogh-Carbentus drie en Andries Bonger (broer van Johanna) vijf stuks.",
	],
	"prt": [
		"Apple está querendo comprar uma startup do Reino Unido por 100 milhões de dólares.",
		"Fernão de Magalhães(Paço Vedro de Magalhães, Ponte da Barca, Portugal, Primavera de 1480 — Mactan, Cebu, Visayas Centrais, Filipinas, 27 de abril de 1521) foi um navegador português que se notabilizou por ter encabeçado a primeira viagem de circum-navegação ao globo de 1519 até 1522, ao serviço da Coroa de Castela. A expedição espanhola Magalhães-Elcano.",
		"Seu pai, Rui de Magalhães, foi Cavaleiro Fidalgo da Casa de D. Afonso, 1.º Conde de Faro, 2.º Conde de Odemira jure uxoris, 5.º Senhor de Mortágua jure uxoris, Senhor de Aveiro e Alcaide-Mor do Castelo de Estremoz. Rui de Magalhães terá sido Alcaide-Mor do Castelo de Aveiro onde está documentado em 1486. Entre junho de 1472 e junho de 1488 está documentado no Porto onde exerce os cargos de Juiz Ordinário, Procurador da Câmara e Vereador.",
		" \"(...) Vede também tantas ilhas, situadas no meio desse grande pego do oceano, as quais descobriram e povoaram, esses reinos de Angola e de Congo, ilhas do Cabo Verde e de S. Tomé, esta grande terra do Brasil; de modo que aos nossos portugueses se pode, com razão, atribuir (nas muitas conquistas que fizeram por mar e terra) o verdadeiro nome de Hércules e de Argonautas.\" ",
		" A importância económica do Brasil para Portugal, teria levado D. João IV a referir-se ao Brasil como a \"vaca leiteira do Reino\".",
	],
	"ara": [
		"كان سيغموند فرويد طبيب أعصاب نمساويًا ومؤسس التحليل النفسي ، وهو أسلوب سريري لعلاج الأمراض النفسية من خلال الحوار بين المريض والمحلل النفسي. ولد فرويد لوالدين يهوديين من غاليسيا في بلدة فرايبرغ المورافيا في الإمبراطورية النمساوية. تأهل كطبيب في الطب عام 1881 في جامعة فيينا. عاش فرويد وعمل في فيينا ، بعد أن أسس ممارسته السريرية هناك عام 1886. في عام 1938 ، غادر فرويد النمسا هربًا من الاضطهاد النازي. توفي في المنفى في المملكة المتحدة عام 1939.",
		"باراك حسين أوباما الثاني سياسي ومحامي أمريكي شغل منصب الرئيس الرابع والأربعين للولايات المتحدة من عام 2009 إلى عام 2017. كان أوباما عضوًا في الحزب الديمقراطي ، وكان أول رئيس أمريكي من أصل أفريقي للولايات المتحدة. شغل سابقًا منصب عضو مجلس الشيوخ الأمريكي عن ولاية إلينوي من عام 2005 إلى عام 2008 وعضو مجلس الشيوخ عن ولاية إلينوي من عام 1997 إلى عام 2004. ",
        "مقتل عضو من هيئة علماء المسلمين خلال اقتحام القوات الاميركية منزله في بغداد (25/12/2004) بغداد (اف ب) قتل عضو من هيئة علماء المسلمين ابرز هيئة دينية للطائفة السنية خلال اقتحام القوات الاميركية الجمعة منزله في بغداد كما اكدت الهيئة في بيان اصدرته السبت.",
		"هذا المشروع العظيم في تاريخ الترجمة البشرية ، حتى لو كانت الإنجازات المجيدة للحضارة الكلاسيكية البشرية موروثة في العصور الوسطى ، فقد أرسى أساسًا متينًا لتطور الثقافة العربية. كان الأوروبيون قادرين على فهم أفكار أسلافهم من خلال ترجمة هذه الترجمات العربية ، ثم بدأوا نهضتهم. يمكن القول أنه بدون العرب والبيزنطيين الذين يرثون ويحافظون على الثقافة الكلاسيكية الغربية ، فإن عصر النهضة الغربية لا أساس له على الإطلاق.",
		"في بداية القرن التاسع ، شجعت الخلافة العباسية ونظمت أنشطة ترجمة واسعة النطاق للفلسفة اليونانية الكلاسيكية. يوجد في \"مدينة الحكمة\" في بغداد عدد كبير من المترجمين المتخصصين. يقال إن أجر الترجمة يدفع بالذهب مساوٍ لوزن الترجمة. جمع أفلاطون وأرسطو وإقليدس وبطليموس وجالينوس وأبقراط والعديد من اليونانيين والهنود والفرس ترجمات الكلاسيكيات في الفلسفة والعلوم والطب."
	],
	"rus": [
		"Apple рассматривает возможность покупки стартапа из Соединённого Королевства за $1 млрд.",
		"Беспилотные автомобили перекладывают страховую ответственность на производителя.",
		"В Сан-Франциско рассматривается возможность запрета роботов-курьеров, которые перемещаются по тротуару.",
		"Лондон — это большой город в Соединённом Королевстве.",
		"Да, нет, наверное!"
	]
}

function clearResults(){
	$("#result").html( "" );
}


/**
 * @abstract change the example options based on the updated language options
 * @param {string} lang a kind of langage in string
 * @yield {NULL}
 */
function fillExampleSelectField(lang) {
	$("#example").empty();
	selectField = document.getElementById("example");
	textField = document.getElementById("text");
	idx = 0;
	for (var example in xel_examples[lang]) {
		var opt = document.createElement("option");
		opt.value=idx;
		opt.innerHTML = xel_examples[lang][idx].substring(0,50)+"..."; 
		selectField.appendChild(opt);
		idx += 1;
	}	
	selectField.value = "0";
	textField.value = xel_examples[lang][0];
	clearResults();
}

/**
 * @abstract load the language options in the field
 * @yield {NULL}
 */
function fillLanguageSelectField() {
	selectField = document.getElementById("lang");
	textField = document.getElementById("text");
	for (var key in xel_langs) {
		if (xel_langs.hasOwnProperty(key)) {           
			var opt = document.createElement("option");
			opt.value=key;
			opt.innerHTML = xel_langs[key];
			selectField.appendChild(opt);
		}
	}	
	selectField.value = "eng";
	fillExampleSelectField(selectField.value)
}

/**
 * @abstract fill in the text field given a lang and a example chosen
 * @yield {NULL}
 */
function newExampleSelect() {
	langSelectField = document.getElementById("lang");
	lang = langSelectField.value;
	exampleSelectField = document.getElementById("example");
	example = exampleSelectField.value;
	textField = document.getElementById("text");
	textField.value = xel_examples[lang][example]; 
	clearResults();
}

/**
 * @abstract update the examples when a new language is chosen
 * @yield {NULL}
 */
function newLanguageSelect() {
	langSelectField = document.getElementById("lang");
    lang = langSelectField.value;
	fillExampleSelectField(lang);
}

/**
 * @abstract helper function to deliver the post request
 * @yield {NULL}
 */
async function postData(url, data_json={}, pfunction) {
    console.log("input: " + JSON.stringify(data_json))
    fetch(url, {
        method: 'POST',
        cache: 'no-cache',
        headers: {
            'Accept': "application/json, text/plain, */*",
            'Content-Type': "application/json;charset=utf-8"
        },
        //mode: 'no-cors',
        body: JSON.stringify(data_json)
	}).then(resp => resp.json())
		.then(json_output => {pfunction(json_output)}
	);
}

/**
 * @abstract generate the output in the HTML document
 * @yield {NULL}
 */
function outputXEL(json) {
	result = document.getElementById("result")
	json_string = JSON.stringify(json)
	console.log(json_string)
	result.innerHTML +=	json_string.substring(1, json_string.length - 1).replaceAll('\\"', '"')
}

/**
 * @abstract send the post request with data, please modify if your service requires other variables 
 * @yield {NULL}
 */
function runAnnotation() {
	fLang = document.getElementById("lang").value;
	valid_languages = ['eng', 'cmn', 'spa', 'jpn', 'fre', 'ger', 'ita', 'dut','prt', 'ara', 'rus']
	url_tokenize = "./process"

    if (!valid_languages.includes(fLang)) {
        alert('Sorry! Invalid language...');
        langSelectField = document.getElementById("lang");
        langSelectField.value = 'eng';
        fillExampleSelectField('eng');
        return;
    }

    fText = document.getElementById("text").value;
	chosen = []
	packages = document.getElementsByTagName("input");
	for(var i = 0; i < packages.length; i++) {
		if(packages[i].type == "checkbox") {
			if(packages[i].checked == true) {
				chosen.push(packages[i].id);
			} 
		}  
	}

	data = { "text" : fText , "lang" : fLang, "packages": chosen };
	postData(url_tokenize, data, outputXEL);
}

/**
 * @abstract submit the form
 * @yield {boolean} false
 */
function formSubmit() {
	clearResults();
	runAnnotation();
	return false;
}
