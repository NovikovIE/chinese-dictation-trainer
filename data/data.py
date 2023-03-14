import pandas as pd
import numpy as np


# to save as csv
def save_as_csv(dataset, name):
    npdataset = np.array(dataset)
    df = pd.DataFrame(npdataset)
    df.to_csv('data/' + name + '.csv')


numbers = [
    ['零', 'líng', 'ноль'],
    ['一', 'yī', 'один'],
    ['二', 'èr', 'два'],
    ['三', 'sān', 'три'],
    ['四', 'sì', 'четыре'],
    ['五', 'wǔ', 'пять'],
    ['六', 'liù', 'шесть'],
    ['七', 'qī', 'семь'],
    ['八', 'bā', 'восемь'],
    ['九', 'jiǔ', 'девять'],
    ['十', 'shí', 'десять'],
    ['百', 'bǎi', 'сто'],
    ['千', 'qiān', 'тысяча'],
    ['万', 'wàn', 'десять тысяч'],
    ['亿', 'yì', 'сто миллионов'],
]

words1 = [
    ['你', 'nǐ', 'ты, you (singular)'],
    ['我', 'wǒ', 'я, I, me'],
    ['好', 'hǎo', 'хороший, good'],
    ['你好!', 'nǐ hǎo', 'Привет!'],
    ['迪玛', 'Dímǎ', 'Дима'],
    ['玛莎', 'Mǎshā', 'Маша'],
    ['五', 'wǔ', '5'],
    ['八', 'bā', '8'],
    ['大', 'dà', 'большой, big'],
    ['猫', 'māo', 'кошка, кот'],
]

words2 = [
    ['猫', 'māo', 'кошка/кот, cat'],
    ['它', 'tā', 'он/она о животных, предметах, it'],
    ['很', 'hěn', 'очень/связка в предложениях с качественным сказуемым'],
    ['不', 'bù', 'не/нет, no, not'],
    ['饿', 'è', 'голодный, hungry'],
    ['可爱', 'kě’ài', 'милый, очаровательный, прелестный, cute'],
    ['对', 'duì', 'правильный, верный, верно!, right!'],
    ['爱', 'ài', 'любить, love'],
    ['的', 'de',
     'притяжательная частица (показывает принадлежность или свойство предмета, стоящего после '
     'нее)'],
    ['吗', 'ma', 'вопросительная частица (yes/no question particle)'],
    ['他', 'tā', 'он, he'],
    ['她', 'tā', 'она, she'],
    ['狗', 'gǒu', 'собака, пес'],
    ['暖', 'nuǎn', 'теплый, тепло'],
]

words3 = [
    ['他', 'tā', 'он, he'],
    ['她', 'tā', 'она, she'],
    ['姐姐', 'jiějie', 'старшая сестра, older sister'],
    ['爸爸', 'bàba', 'папа, dad'],
    ['U盘', 'U-pán', 'флэшка, flash drive'],
    ['也', 'yě', 'тоже, also'],
    ['没', 'méi',
     'не (иметь) отрицание для глагола обладания, not (have) negation for the verb of '
     'possession'],
    ['有', 'yǒu', 'иметь, have'],
    ['需要', 'xūyào', 'нуждаться; необходимо; требоваться, need.'],
    ['给', 'gěi', 'давать, give'],
    ['多', 'duō', 'много, many'],
    ['谢谢', 'xièxie', 'спасибо, thank you'],
    ['不客气', 'búkèqi', 'не за что'],
    ['妹妹', 'mèimei', 'младшая сестра, little sister'],
    ['哥哥', 'gēge', 'старший брат, older brother'],
    ['弟弟', 'dìdi', 'младший брат, little brother'],
    ['妈妈', 'māma', 'мама, mom'],
    ['我们', 'wǒmen', 'мы, we, us'],
    ['你们', 'nǐmen', 'вы, you (plural)'],
    ['他们', 'tāmen', 'они, they'],
    ['CD盘', 'CD-pán', 'CD-диск, CD'],
    ['光盘', 'guāngpán', 'лазерный диск, laser disc'],
    ['键盘', 'jiànpán', 'клавиатура, keyboard'],
    ['盘', 'pán', 'тарелка, блюдо, поднос, plate, tray'],
    ['一', 'yī', '1'],
    ['六', 'liù', '6'],
    ['七', 'qī', '7'],
    ['九', 'jiǔ', '9'],
    ['零', 'líng', '0'],
    ['请', 'qĭng', 'просить, пожалуйста, ask (for), please'],
    ['小', 'xiǎo', 'маленький, little, small'],
    ['东西', 'dōngxi', 'вещь, предмет, thing, something'],
    ['说', 'shuō', 'говорить, say, speak'],
    ['懂', 'dǒng', 'понимать, understand'],
]

words4 = [
    ['这', 'zhè', 'этот, это, this, it'],
    ['是', 'shì', 'быть, являться, be'],
    ['什么', 'shénme', 'что, какой, what'],
    ['大学', 'dàxué', 'университет, University'],
    ['网站', 'wǎngzhàn', 'сайт, website'],
    ['网', 'wǎng', 'сеть, Интернет, web, Internet'],
    ['站', 'zhàn', 'стоять, остановка, stand, station'],
    ['真', 'zhēn', 'так! истинный, действительно, real, really, true'],
    ['真的', 'zhēnde', 'правда, истинный, real, really, true'],
    ['网址', 'wǎngzhǐ', 'интернет-адрес, web-address, URL'],
    ['址', 'zhǐ', 'местоположение, address, site'],
    ['首页', 'shǒuyè', 'главная страница, Front page'],
    ['首', 'shǒu', 'глава, голова, главный, head, main'],
    ['页', 'yè', 'страница, page'],
    ['个人', 'gèrén', 'личность, личный, персональный, person, personal'],
    ['专区', 'zhuānqū', 'зона, район, zone'],
    ['个人专区', 'gèrén zhuānqū', 'личный кабинет, account'],
    ['当然', 'dāngrán', 'конечно, of course'],
    ['就', 'jiù', 'именно, вот, как раз, just'],
    ['这儿/这里', 'zhèr/zhèlǐ', 'здесь, here'],
    ['还', 'hái', 'еще, помимо этого, also'],
    ['可以', 'kěyǐ', 'можно, can'],
    ['切换', 'qiēhuàn', 'поменять, переключить, switch'],
    ['语言', 'yǔyán', 'язык, language'],
    ['网页', 'wǎngyè', 'веб-страница, web-page'],
    ['十', 'shí', '10'],
    ['那', 'nà', 'то, тот, that'],
    ['那儿/那里', 'nàr/nàlǐ', 'там, there'],
    ['哪儿/哪里', 'nǎr/nǎlǐ', 'где?, where'],
    ['谁', 'shéi (shuí)', 'кто?, who?'],
    ['用户', 'yònghù', 'пользователь, user'],
    ['用户名', 'yònghù míng', 'имя пользователя, логин, username, login'],
    ['密码', 'mìmǎ', 'пароль, password'],
    ['主人', 'zhǔrén', 'хозяин'],
    ['朋友', 'péngyou', 'друг'],
    ['吃', 'chī', 'есть, кушать'],
    ['还', 'hái', 'еще'],
    ['玩具', 'wánjù', 'игрушка'],
    ['电脑', 'diànnǎo', 'компьютер'],
    ['暖', 'nuǎn', 'теплый'],
    ['上', 'shàng', 'верх, сверху, залезать, подниматься'],
    ['网', 'wǎng', 'сеть'],
    ['上网', 'shàngwǎng', 'заходить в Интернет'],
    ['玩儿', 'wánr', 'играть, развлекаться'],
    ['睡觉', 'shuìjiào', 'спать'],
]

words5 = [
    ['早上', 'zǎoshang', 'утро'],
    ['叫', 'jiào', 'звать, называться'],
    ['名字', 'míngzi', 'имя, name'],
    ['张诚', 'Zhāng Chéng', 'Чжан Чэн (китайское имя)'],
    ['来自', 'láizì', 'происходить из, исходить из, come from'],
    ['哪里', 'nǎlǐ', 'где, куда, откуда, where'],
    ['俄罗斯', 'é luó sī', 'Россия, Russia'],
    ['中国', 'zhōngguó', 'Китай, China'],
    ['会', 'huì', 'уметь, can'],
    ['俄语', 'éyǔ', 'русский язык, Russian (lang)'],
    ['汉语', 'hànyǔ', 'китайский язык, Chinese (lang)'],
    ['一点点', 'yīdiǎndiǎn', 'немного, чуть-чуть, a little bit'],
    ['点', 'diǎn', 'капля, drop'],
    ['最近', 'zuìjìn', 'в последнее (ближайшее) время, recently'],
    ['在', 'zài', 'гл. находиться, be located somewhere, предлог в / на, at / in'],
    ['语法', 'yǔfǎ', 'грамматика, grammar'],
    ['最', 'zuì', 'самый, наиболее, the most…'],
    ['难', 'nán', 'трудный, difficult, hard'],
    ['错误', 'cuòwù', 'ошибка, mistake'],
    ['太', 'tài', 'слишком, too (much)'],
    ['了', 'le', 'модальная частица, modal partcle'],
    ['汉字', 'hànzì', 'китайские иероглифы, Chinese characters'],
    ['学(习)', 'xué(xí)', 'учить, учиться, learn, study'],
    ['哈哈', 'hāhā', 'ха-ха, звукоподражание, ha-ha'],
    ['得', 'děi', 'необходимо, должно, следует, must, have to'],
    ['上课', 'shàngkè', 'идти на урок, начинать урок, attend class, take class, begin the '
                        'lesson'],
    ['先', 'xiān', 'сначала, сейчас, first, firstly'],
    ['走', 'zǒu', 'идти (пешком), уходить, walk, go, leave'],
    ['啦', 'la', 'конечная частица, end particle'],
    ['再见', 'zàijiàn', 'до свидания, good bye'],
    ['拜拜', 'bàibai', 'пока-пока, bye-bye'],
    ['日本', 'rìběn', 'Япония, Japan'],
    ['西班牙', 'xībānyá', 'Испания, Spain'],
    ['德国', 'déguó', 'Германия, Germany'],
    ['英国', 'yīngguó', 'Англия, England'],
    ['法国', 'fǎguó', 'Франция, France'],
    ['美国', 'měiguó', 'Америка, America'],
    ['韩国', 'hánguó', 'Корея (южная), Korea (South)'],
    ['芬兰', 'fēnlán', 'Финляндия, Finland'],
    ['波兰', 'bōlán', 'Польша, Poland'],
    ['发音 ', 'fāyīn ', 'произношение , pronounciation'],
    ['二 ', 'èr ', '2'],
    ['三 ', 'sān ', '3'],
    ['四 ', 'sì ', '4'],
    ['亚里士多德', 'yàlǐshìduōdé', 'Аристотель'],
    ['古', 'gǔ', 'древний'],
    ['希腊', 'xīlà', 'Греция'],
    ['科学家', 'kēxuéjiā', 'ученый'],
    ['科学', 'kēxué', 'наука'],
    ['家', 'jiā', 'суффикс, обозначающий профессию'],
    ['小', 'xiǎo', 'маленький'],
    ['聪明', 'cōngmíng', 'умный'],
    ['所以', 'suǒyǐ', 'поэтому'],
    ['朋友', 'péngyou', 'друг'],
    ['好玩儿', 'hǎowánr', 'прикольный, интересно, весело'],
]

words6 = [
    ['手机', 'shǒujī', 'моб.телефон / mobile phone'],
    ['朋友', 'péngyou', 'друг'],
    ['触屏', 'chùpíng', 'сенсорный экран , touch screen'],
    ['就是', 'jiùshì', 'вот именно, точно так, exactly/am, is, are'],
    ['屏幕', 'píngmù', 'экран     screen'],
    ['种', 'zhǒng', 'вид, сорт    type/kind'],
    ['按键', 'ànjiàn', 'кнопка, клавиша      button'],
    ['啊', 'à', 'а (междометие)'],
    ['知道', 'zhīdào', 'знать понимать'],
    ['像', 'xiàng', 'быть похожим, подобно, как'],
    ['三星', 'sānxīng', 'Самсунг (букв. “три звезды”)'],
    ['或者', 'huòzhě', 'или (в утвердительных предложениях)'],
    ['苹果', 'píngguǒ', 'яблоко / Apple'],
    ['品牌', 'pǐnpái', 'марка, фирма, лэйбл'],
    ['样', 'yàng', 'образец, вид, образ'],
    ['谁', 'shéi', 'who'],
    ['谁的', 'shéide', 'whose'],
    ['电脑', 'diànnǎo', 'компьютер'],
    ['笔记本电脑', 'bǐjìběn diànnǎo', 'ноутбук'],
    ['平板电脑', 'píngbǎn diànnǎo', 'планшет'],
    ['按键手机', 'ànjiàn shǒujī', 'кнопочный телефон'],
]

words7a = [
    ['时间', 'shíjiān', 'время'],
    ['这么', 'zhème', 'настолько'],
    ['晚', 'wǎn', 'поздний, поздно'],
    ['了', 'le', 'модальная частица'],
    ['怎么', 'zěnme', 'как / почему?'],
    ['还', 'hái', 'еще'],
    ['睡觉', 'shuìjiào', 'спать'],
    ['明天', 'míngtiān', 'завтра'],
    ['测试', 'cèshì', 'тест'],
    ['物理学', 'wùlǐ xué', 'физика'],
    ['别', 'bié', 'отрицание'],
    ['担心', 'dānxīn', 'беспокоиться, волноваться'],
    ['聪明', 'cōngmíng', 'умный'],
    ['一定', 'yīdìng', 'обязательно'],
    ['会', 'huì', 'уметь / в будущем времени имеет значение возможности'],
    ['通过', 'tōngguò', 'пройти'],
    ['懂', 'dǒng', 'понимать'],
    ['解答', 'jiědá', 'решать'],
    ['问题', 'wèntí', 'задача, вопрос, проблема'],
    ['问', 'wèn', 'спрашивать'],
    ['所以', 'suǒyǐ', 'поэтому'],
    ['今天', 'jīntiān', 'сегодня'],
    ['晚上', 'wǎnshang', 'вечер'],
    ['准备', 'zhǔnbèi', 'готовить (подготавливать), готовиться'],
    ['一下', 'yīxià', 'разок'],
    ['加油', 'jiāyóu', 'удачи!'],
    ['加', 'jiā', 'добавить'],
    ['油', 'yóu', 'масло (жидкое)'],
    ['昨天', 'zuótiān', 'вчера'],
    ['今年', 'jīnnián', 'этот год'],
    ['明年', 'míngnián', 'следующий год'],
    ['去年', 'qùnián', 'прошлый год'],
    ['什么时候', 'shénme shíhou', 'когда?'],
    ['时候', 'shíhou', 'время/пора'],
    ['试题', 'shìtí', 'вопросы / задания в тесте'],
    ['书', 'shū', 'книга.'],
    ['记得', 'jìde', 'помнить'],
    ['做', 'zuò', 'делать (здесь: видеть)'],
    ['梦', 'mèng', 'сон / сновидение'],
    ['但是', 'dànshì', 'но, однако'],
    ['响', 'xiǎng', 'звенеть'],
    ['打电话', 'dǎ diànhuà', 'звонить по телефону'],
    ['解释', 'jiěshì', 'объяснять'],
    ['都', 'dōu', 'все'],
    ['应该', 'yīnggāi', 'должно, должно быть, следовало бы.'],
]

words7b = [
    ['醒', 'xǐng', 'просыпаться'],
    ['嗯', 'ǹg', 'угу (междометие)'],
    ['现在', 'xiànzài', 'сейчас'],
    ['几', 'jǐ', 'сколько? (до 10) несколько'],
    ['点', 'diǎn', 'точка, капля, сч. сл. “час” для называния времени по часам'],
    ['都', 'dōu', 'все / уже'],
    ['半', 'bàn', 'половина'],
    ['再', 'zài', 'снова, еще раз'],
    ['迟到', 'chídào', 'опоздать'],
    ['快', 'kuài', 'быстро, скоро'],
    ['起', 'qǐ', 'подниматься'],
    ['床', 'chuáng', 'кровать'],
    ['吧', 'ba', 'частица'],
    ['孩子', 'háizi', 'ребенок'],
    ['马上', 'mǎshàng', 'скоро, сразу'],
    ['差', 'chà', 'недоставать'],
    ['刻', 'kè', 'сч.сл. “четверть”'],
    ['昨天', 'zuótiān', 'вчера'],
    ['好像', 'hǎoxiàng', 'похоже, что'],
    ['左右', 'zuǒyòu', '“влево-вправо” / примерно'],
    ['左', 'zuǒ', 'лево'],
    ['右', 'yòu', 'право'],
    ['哎哟', 'āiyō', 'ого, ух ты (междометие)'],
    ['应该', 'yīnggāi', 'должно быть, следует'],
    ['分', 'fēn', 'часть, зд.: сч.сл. “минута”'],
    ['去', 'qù', 'идти, направляться, (англ. go)'],
    ['吃', 'chī', 'есть (кушать)'],
    ['早饭', 'zǎofàn', 'завтрак'],
    ['课间', 'kè jiān', 'перемена'],
    ['手表', 'shǒubiǎo', 'наручные часы'],
    ['钟', 'zhōng', 'часы башенные, настенные, настольные'],
    ['闹钟', 'nàozhōng', 'будильник'],
    ['中午', 'zhōngwǔ', 'полдень'],
    ['上午', 'shàngwǔ', 'первая половина дня (до полудня)'],
    ['下午', 'xiàwǔ', 'вторая половина дня (после полудня)'],
    ['歌', 'gē', 'песня'],
    ['刷牙', 'shuāyá', 'чистить зубы'],
    ['出发', 'chūfā', 'выходить, отправляться'],
    ['上学', 'shàngxué', 'ходить в школу, ходить на занятия'],
    ['午饭', 'wǔfàn', 'обед'],
    ['放学', 'fàngxué', 'заканчивать занятия (уроки)'],
    ['打', 'dǎ', 'бить, играть'],
    ['乒乓球', 'pīngpāngqiú', 'настольный теннис'],
    ['功课', 'ōngkè', 'домашнее задание, занятие (урок)'],
    ['晚饭', 'wǎnfàn', 'ужин'],
    ['聊天', 'liáotiān', 'болтать, разговаривать, chat'],
    ['洗澡', 'xǐzǎo', 'принимать ванну, мыться'],
    ['听', 'tīng', 'слышать, слушать'],
    ['音乐', 'yīnyuè', 'музыка'],
    ['晚安', 'wǎn’ān', 'спокойной ночи'],
    ['能', 'néng', 'мочь, уметь (физически, по обстоятельствам)'],
    ['叫醒', 'jiàoxǐng', 'будить'],
    ['着急', 'zháojí', 'волноваться'],
    ['的时候', 'de shíhòu', 'во время (чего-либо)'],
    ['考试', 'kǎoshì', '(名词) экзамен'],
    ['每天', 'měitiān', 'каждый день'],
    ['大声', 'dàshēng', 'громко'],
    ['让', 'ràng', 'позволить, разрешить'],
    ['喵', 'miāo', 'звукоподр. мяу!'],
]

words8_base = [
    ['双生', 'shuāngshēng', 'Близнецы'],
    ['超市', 'chāoshì', 'супермаркет'],
    ['超', 'chāo', 'превышать, превосходить, гипер-, super-'],
    ['市', 'shì (shìchǎng)', 'рынок (городская площадь)'],
    ['买', 'mǎi', 'покупать'],
    ['一些', 'yīxiē', 'несколько, немного'],
    ['东西', 'dōngxi', 'предмет, вещь'],
    ['后天', 'hòutiān', 'послезавтра'],
    ['联欢会', 'liánhuān huì', 'встреча, вечеринка'],
    ['记得', 'jìde', 'помнить'],
    ['可是', 'kěshì', 'но, однако'],
    ['已经', 'yǐjīng', 'уже'],
    ['个', 'ge', 'счетное слово (штука)'],
    ['关', 'guān', 'закрывать'],
    ['门', 'mén', 'дверь'],
    ['但是', 'dànshì', 'но, однако'],
    ['忙', 'máng', 'занятой, загруженный'],
    ['商店', 'shāngdiàn', 'магазин'],
    ['不但', 'búdàn', 'не только …'],
    ['各种', 'gè zhǒng', 'различный, разного рода'],
    ['零食', 'língshí', 'закуска, перекус'],
    ['和', 'hé', 'союз и'],
    ['饮料', 'yǐnliào', 'напиток'],
    ['而且', 'érqiě', 'к тому же, вдобавок'],
    ['包邮', 'bāo yóu', 'доставка включена в стоимость (бесплатная доставка)'],
    ['一般', 'yìbān', 'обычно, как правило'],
    ['实体', 'shítǐ', 'материальный, осязаемый'],
    ['购物', 'gòuwù', 'делать покупки'],
    ['简单', 'jiǎndān', 'простой, элементарный'],
    ['用', 'yòng', 'использовать, пользоваться'],
    ['谷歌', 'gǔgē', 'Google'],
    ['浏览器', 'liúlǎn qì', 'браузер'],
    ['搜索', 'sōusuǒ', 'искать, поиск'],
    ['然后', 'ránhòu', 'потом, затем, (англ. then/afterwards)'],
    ['后', 'hòu', 'после, за, вслед за'],
    ['打开', 'dǎkāi', 'открывать'],
    ['链接', 'liànjiē', 'ссылка, Link'],
    ['挑选', 'tiāoxuǎn', 'выбирать'],
    ['自己', 'zìjǐ', 'сам, себя (возвр. мест.)'],
    ['喜欢', 'xǐhuan', 'любить, нравиться, like'],
    ['商品', 'shāngpǐn', 'товар'],
    ['选择', 'xuǎnzé', 'выбирать'],
    ['付款', 'fùkuǎn', 'платить, оплата'],
    ['方式', 'fāngshì', 'способ, метод'],
    ['打', 'dǎ', 'бить, ударять, make'],
    ['电话', 'diànhuà', 'телефон'],
    ['打电话', 'dǎ diànhuà', 'звонить по телефону'],
    ['帮助', 'bāngzhù', 'помогать'],
    ['到', 'dào', 'прибывать, добираться, приходить'],
    ['号码', 'hàomǎ', 'номер'],
    ['多少', 'duōshǎo', 'сколько?'],
]

words8_extra = [
    ['银行卡支付', 'yínháng kǎ zhīfù', 'оплата банковской картой'],
    ['信用卡支付', 'xìnyòng kǎ zhīfù', 'оплата кредитной картой'],
    ['营业时间', 'yíngyè shíjiān', 'business hours'],
    ['特价', 'tèjià', '“специальная цена”, сниженная цена'],
    ['优惠', 'yōuhuì', 'скидка'],
    ['订购', 'dìnggòu', 'заказывать'],
    ['进口', 'jìnkǒu', 'импорт'],
    ['出口', 'chūkǒu', 'экспорт'],
    ['本', 'běn', '“корешок” (для книг, журналов, словарей)'],
    ['台', 'tái', '“подставка/башня” (для оргтехники)'],
    ['只', 'zhī', 'сч. сл. для зверей, птиц, одного предмета из пары (один глаз, одна рука, '
                  'одна тапочка), лодок.'],
    ['支', 'zhī', '“ветка” сч.сл. для предметов, похожих на палочки (ручки, кисти)'],
    ['瓶', 'píng', 'бутылка'],
    ['双', 'shuāng', '“пара” сч.сл. для предметов, составляющих пары (обувь, лыжи, перчатки…)'],
    ['食物', 'shíwù', 'продукты питания, еда'],
    ['开心', 'kāixīn', 'веселый, радостный'],
    ['挨饿', 'ái’è', 'терпеть (испытывать) голод, голодать'],
    ['带', 'dài', 'пояс, ремень; приносить, иметь при себе'],
    ['牛奶', 'niúnǎi', 'молоко (коровье)'],
    ['猫粮', 'māoliáng', 'кошачий корм'],
    ['这些', 'zhèxiē', 'эти'],
    ['便宜', 'piányí', 'удобный, выгодный, дешевый'],
    ['上床', 'shàngchuáng', 'ложиться в кровать'],
    ['大家', 'dàjiā', 'все'],
    ['网上购物', 'wǎng shàng gòuwù', 'онлайн шоппинг'],
    ['购物', 'gòuwù', 'делать покупки'],
    ['网购', 'wǎnggòu', 'покупка через Интернет, покупать через Интернет'],
    ['简单', 'jiǎndān', 'простой, примитивный'],
    ['安全', 'ānquán', 'безопасность, безопасный'],
    ['因为', 'yīnwèi', 'по причине..., потому что...'],
    ['自己', 'zìjǐ', 'сам, себя, собственный'],
    ['选择', 'xuǎnzé', 'выбор, выбирать'],
    ['支付', 'zhīfù', 'платить, уплачивать'],
    ['货到付款', 'huòdào fùkuǎn', 'оплата после доставки'],
    ['货到', 'huòdào', 'прибытие груза'],
    ['付款', 'fùkuǎn', 'производить платеж, оплачивать'],
    ['方法', 'fāngfǎ', 'метод'],
    ['方便', 'fāngbiàn', 'удобный'],
    ['经常', 'jīngcháng', 'ежедневный, повседневный, часто'],
    ['犯', 'fàn', 'совершать (преступление, ошибку), нарушать (правила)'],
    ['比如', 'bǐrú', 'например'],
    ['总是', 'zǒngshì', 'всегда, постоянно'],
    ['挑选', 'tiāoxuǎn', 'выбирать'],
    ['后来', 'hòulái', 'потом, в дальнейшем, впоследствии'],
    ['才', 'cái', 'только, только что (выражает запоздалость по срав. с 就)'],
    ['购物车', 'gòuwùchē', 'тележка, корзина для покупок'],
    ['车', 'chē', 'телега, повозка, машина'],
    ['地方', 'dìfang', 'место, местоположение'],
    ['点击', 'diǎnjī', 'кликать, щелкать (мышкой)'],
    ['添加', 'tiānjiā', 'добавлять'],
    ['出现在', 'chūxiàn zài', 'появиться в, возникнуть в'],
    ['里', 'lǐ', 'в, внутри'],
    ['取消', 'qǔxiāo', 'аннулировать, отменить, отмена (кнопка)'],
    ['消失', 'xiāoshī', 'исчезать, пропадать'],
    ['神奇', 'shénqí', 'удивительный, чудесный, волшебный'],
    ['次', 'cì', 'сч. сл. для раз'],
    ['台', 'tái', 'сч. сл. для техники (телевизор, компьютер и т.д.)'],
    ['收货', 'shōuhuò', 'получать заказанный товар, принимать поставку'],
    ['以后', 'yǐhòu', 'после, потом'],
    ['觉得', 'juéde', 'полагать, думать'],
    ['申请', 'shēnqǐng', 'подавать заявление'],
    ['退换货', 'tuìhuànhuò', 'возврат и замена (обмен) товара'],
    ['退货', 'tuìhuò', 'возвращать купленный товар'],
    ['退', 'tuì', 'возвращать, отдавать обратно'],
    ['换', 'huàn', 'менять, обменивать'],
    ['再次', 'zàicì', 'повторно, ещё раз'],
    ['下单', 'xiàdān', 'делать заказ'],
    ['包裹', 'bāoguǒ', 'упаковывать, посылка'],
    ['邮寄', 'yóujì', 'отправлять (почтой)'],
    ['длинный', 'cháng', 'длинный, долгий'],
    ['想', 'xiǎng', 'думать, размышлять, хотеть'],
    ['等', 'děng', 'ждать, ожидать'],
    ['订单', 'dìngdān', 'заказ (на покупку чего-либо)'],
    ['对了', 'duìle', 'да, так!, совершенно верно!, да, кстати ... (вводное слово)'],
    ['月', 'yuè', 'месяц'],
    ['写错', 'xiěcuò', 'написать неправильно'],
    ['收件', 'shōujiàn', 'входящие (напр. о почтовых сообщениях или смс)'],
    ['收件人', 'shōujiànrén', 'адресат, получатель (письма)'],
    ['唉', 'āi, ài', 'ай!, ах! (досада или сожаление), угу!, ага! (согласие)'],
    ['夸', 'kuā', 'хвалить'],
    ['笨', 'bèn', 'глупый'],
]
