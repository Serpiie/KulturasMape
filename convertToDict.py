import csv
import string

input_file = csv.DictReader(open("MS2020.csv", encoding="utf8"))

# for row in input_file:
#     print(row)
#     print(',')
import string
import re

a = '''
{'Objekta nosaukums': '"Liepāja okupāciju režīmos"', 'Adrese': 'Klāva Ukstiņa iela 7/9, Liepāja, LV-3401'}
,
{'Objekta nosaukums': '1991. gada barikāžu muzejs', 'Adrese': 'Krāmu iela 3, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Ādolfa Alunāna memoriālais muzejs', 'Adrese': 'Filozofu iela 3, Jelgava, LV-3001'}
,
{'Objekta nosaukums': 'Ainažu jūrskolas muzejs', 'Adrese': 'Valdemāra iela 47, Ainaži, Limbažu nov., LV-4035'}
,
{'Objekta nosaukums': 'Ainažu Ugunsdzēsības muzejs', 'Adrese': 'Valdemāra iela 69, Ainaži, Limbažu nov., LV-4035'}
,
{'Objekta nosaukums': 'Aizkraukles vēstures un mākslas muzejs', 'Adrese': '"Kalna Ziedi", Aizkraukle, Aizkraukles nov., LV-5101'}
,
{'Objekta nosaukums': 'Aizputes novadpētniecības muzejs - tūrisma informācijas punkts', 'Adrese': 'Skolas iela 1, Aizpute, Dienvidkurzemes nov., LV-3456'}
,
{'Objekta nosaukums': 'Aknīstes Novadpētniecības muzejs', 'Adrese': 'Miera iela 1, Aknīste, Jēkabpils nov., LV-5208'}
,
{'Objekta nosaukums': 'Aktieru Amtmaņu muzejs', 'Adrese': '"Zvanītāju Bukas", Valle, Valles pag., Bauskas nov., LV-5106'}
,
{'Objekta nosaukums': 'Aleksandra Čaka muzejs', 'Adrese': 'Lāčplēša iela 48 - 8, Rīga, LV-1011'}
,
{'Objekta nosaukums': 'Alojas Novadpētniecības centrs', 'Adrese': 'Ausekļa iela 1, Aloja, Limbažu nov., LV-4064'}
,
{'Objekta nosaukums': 'Alsungas Tūrisma informācijas un vēsturiskā mantojuma centrs', 'Adrese': 'Skolas iela 11A, Alsunga, Alsungas pag., Kuldīgas nov., LV-3306'}
,
{'Objekta nosaukums': 'Alūksnes muzejs', 'Adrese': 'Pils iela 74, Alūksne, Alūksnes nov., LV-4301'}
,
{'Objekta nosaukums': 'Andreja Pumpura Lielvārdes muzejs', 'Adrese': 'Edgara Kauliņa aleja 20, Lielvārde, Ogres nov., LV-5070'}
,
{'Objekta nosaukums': 'Andreja Upīša memoriālais muzejs', 'Adrese': 'Brīvības iela 38-4, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Andreja Upīša memoriālmāja', 'Adrese': 'Daugavas iela 58, Skrīveri, Skrīveru pag., Aizkraukles nov., LV-5125'}
,
{'Objekta nosaukums': 'Andrupenes lauku sēta', 'Adrese': 'Skolas iela 5, Andrupene, Andrupenes pag., Krāslavas nov., LV-5687'}
,
{'Objekta nosaukums': 'Antona Austriņa memoriālais muzejs "Kaikaši"', 'Adrese': '"Kaikaši", Vecpiebalga, Vecpiebalgas pag., Cēsu nov., LV-4122'}
,
{'Objekta nosaukums': 'Antona Rupaiņa muzejs', 'Adrese': 'Rītupes iela 34, Bērzgale, Bērzgales pag., Rēzeknes nov., LV-4612'}
,
{'Objekta nosaukums': 'Apriķu  muzejs', 'Adrese': '"Apriķu skola", Apriķi, Lažas pag., Dienvidkurzemes nov., LV-3455'}
,
{'Objekta nosaukums': 'Āraišu ezerpils Arheoloģiskais parks', 'Adrese': '"Āraišu ezerpils", Drabešu pag., Cēsu nov., LV-4101'}
,
{'Objekta nosaukums': 'Aspazijas māja', 'Adrese': 'Zigfrīda Meierovica prospekts 20, Jūrmala, LV-2015'}
,
{'Objekta nosaukums': 'Baldones muzejs', 'Adrese': '"Mercendarbes muiža", Baldones pag., Ķekavas nov., LV-2125'}
,
{'Objekta nosaukums': 'Baltinavas  muzejs', 'Adrese': 'Tilžas iela 7, Baltinava, Baltinavas pag., Balvu nov., LV-4594'}
,
{'Objekta nosaukums': 'Balvu Novada muzejs', 'Adrese': 'Brīvības iela 46, Balvi, Balvu nov., LV-4501'}
,
{'Objekta nosaukums': 'Bārdu dzimtas memoriālais muzejs "Rumbiņi"', 'Adrese': '"Rumbiņi", Katvaru pag., Limbažu nov., LV-4061'}
,
{'Objekta nosaukums': 'Bārtas  muzejs', 'Adrese': '"Bārtas muzejs", Bārta, Bārtas pag., Dienvidkurzemes nov., LV-3482'}
,
{'Objekta nosaukums': 'Bauskas muzejs', 'Adrese': 'Kalna iela 6, Bauska, Bauskas nov., LV-3901'}
,
{'Objekta nosaukums': 'Bauskas pils muzejs', 'Adrese': '"Pilskalns", Bauska, Bauskas nov., LV-3901'}
,
{'Objekta nosaukums': 'Brāļu Jurjānu memoriālais muzejs "Meņģeļi"', 'Adrese': '"Meņģeļi", Ērgļu pag., Madonas nov., LV-4840'}
,
{'Objekta nosaukums': 'Brāļu Kaudzīšu memoriālais muzejs "Kalna Kaibēni"', 'Adrese': '"Kalna Kaibēni", Vecpiebalgas pag., Cēsu nov., LV-4122'}
,
{'Objekta nosaukums': 'Bulduru Izstāžu nams', 'Adrese': 'Muižas iela 6, Jūrmala, LV-2010'}
,
{'Objekta nosaukums': 'Cēsu Vēstures un mākslas muzejs', 'Adrese': 'Pils laukums 9, Cēsis, Cēsu nov., LV-4101'}
,
{'Objekta nosaukums': 'Daugavas muzejs', 'Adrese': '"Jaundoles", Salaspils pag., Salaspils nov., LV-2121'}
,
{'Objekta nosaukums': 'Daugavpils Novadpētniecības un mākslas muzejs', 'Adrese': 'Rīgas iela 8, Daugavpils, LV-5401'}
,
{'Objekta nosaukums': 'Dekoratīvās mākslas un dizaina muzejs', 'Adrese': 'Skārņu iela 10, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Dobeles novada grāmatnieku muzejs "Ķipi"', 'Adrese': '"Ķipi", Tērvetes pag., Dobeles nov., LV-3730'}
,
{'Objekta nosaukums': 'Dobeles novada muzejs', 'Adrese': 'Brīvības iela 7, Dobele, Dobeles nov., LV-3701'}
,
{'Objekta nosaukums': 'Drustu novadpētniecības muzejs', 'Adrese': 'Palsas iela 20, Drusti, Drustu pag., Smiltenes nov., LV-4132'}
,
{'Objekta nosaukums': 'Druvienas Vecā skola - muzejs', 'Adrese': '"Vecā skola", Druvienas pag., Gulbenes nov., LV-4426'}
,
{'Objekta nosaukums': 'E.Dārziņa un J.Sudrabkalna memoriālais muzejs "Jāņaskola"', 'Adrese': '"Jāņa skola", Jaunpiebalgas pag., Cēsu nov., LV-4125'}
,
{'Objekta nosaukums': "Eduarda Veidenbauma memoriālais muzejs ''Kalāči''", 'Adrese': '"Kalāči", Liepas pag., Cēsu nov., LV-4128'}
,
{'Objekta nosaukums': 'Farmācijas muzejs', 'Adrese': 'Riharda Vāgnera iela 13, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Franča Trasuna muzejs "Kolnasāta"', 'Adrese': 'Kalna iela 3, Sakstagals, Sakstagala pag., Rēzeknes nov., LV-4638'}
,
{'Objekta nosaukums': 'Gulbenes novada vēstures un mākslas muzejs', 'Adrese': 'Pils iela, Gulbene, Gulbenes nov.'}
,
{'Objekta nosaukums': 'Ģ.Eliasa Jelgavas vēstures un mākslas muzejs', 'Adrese': 'Akadēmijas iela 10, Jelgava, LV-3001'}
,
{'Objekta nosaukums': 'Imanta Ziedoņa muzejs', 'Adrese': '"Dzirnakmeņi", Krimuldas pag., Siguldas nov., LV-2142'}
,
{'Objekta nosaukums': 'Jāņa Akuratera muzejs', 'Adrese': 'Ojāra Vācieša iela 6A, Rīga, LV-1004'}
,
{'Objekta nosaukums': 'Jāņa Jaunsudrabiņa muzejs "Riekstiņi"', 'Adrese': '"Riekstiņi", Neretas pag., Aizkraukles nov., LV-5118'}
,
{'Objekta nosaukums': 'Jaņa Rozentāla Saldus vēstures un mākslas muzejs', 'Adrese': 'Striķu iela 22, Saldus, Saldus nov., LV-3801'}
,
{'Objekta nosaukums': 'Jaņa Rozentāla un Rūdolfa Blaumaņa muzejs', 'Adrese': 'Alberta iela 12 - 9, Rīga, LV-1010'}
,
{'Objekta nosaukums': 'Jaunlaicenes muižas muzejs', 'Adrese': '"Dravnieki", Jaunlaicene, Jaunlaicenes pag., Alūksnes nov., LV-4336'}
,
{'Objekta nosaukums': 'Jaunmoku pils muzejs', 'Adrese': '"Jaunmoku pils", Tumes pag., Tukuma nov., LV-3139'}
,
{'Objekta nosaukums': 'Jaunpils muzejs', 'Adrese': '"Pils", Jaunpils, Jaunpils pag., Tukuma nov., LV-3145'}
,
{'Objekta nosaukums': 'Jāzepa Vītola memoriālais muzejs "Anniņas"', 'Adrese': '"Anniņas", Gaujiena, Gaujienas pag., Smiltenes nov., LV-4339'}
,
{'Objekta nosaukums': 'Jēkabpils Vēstures muzeja brīvdabas nodaļa "Sēļu sēta"', 'Adrese': 'Filozofu iela 6, Jēkabpils, Jēkabpils nov., LV-5201'}
,
{'Objekta nosaukums': 'Jēkabpils Vēstures muzejs', 'Adrese': 'Rīgas iela 216B, Jēkabpils, Jēkabpils nov., LV-5202'}
,
{'Objekta nosaukums': 'Jūrmalas Brīvdabas muzejs', 'Adrese': 'Tīklu iela 1A, Jūrmala, LV-2010'}
,
{'Objekta nosaukums': 'Jūrmalas muzejs', 'Adrese': 'Tirgoņu iela 29, Jūrmala, LV-2015'}
,
{'Objekta nosaukums': 'Kalncempju pagasta Viktora Ķirpa Ates muzejs', 'Adrese': '"Atte", Annas pag., Alūksnes nov., LV-4341'}
,
{'Objekta nosaukums': 'Kandavas novada muzejs', 'Adrese': 'Talsu iela 11, Kandava, Tukuma nov., LV-3120'}
,
{'Objekta nosaukums': "Kārļa Skalbes memoriālais muzejs ''Saulrieti''", 'Adrese': '"Saulrieti", Vecpiebalgas pag., Cēsu nov., LV-4122'}
,
{'Objekta nosaukums': 'Kārļa Ulmaņa piemiņas muzejs "Pikšas"', 'Adrese': '"Pikšu muzejs", Bērzes pag., Dobeles nov., LV-3732'}
,
{'Objekta nosaukums': 'Kazdangas muzejs', 'Adrese': 'Jaunatnes gatve 1, Kazdanga, Kazdangas pag., Dienvidkurzemes nov., LV-3457'}
,
{'Objekta nosaukums': 'Krāslavas Vēstures un mākslas muzejs', 'Adrese': 'Pils iela 8, Krāslava, Krāslavas nov., LV-5601'}
,
{'Objekta nosaukums': 'Krišjāņa Barona muzejs', 'Adrese': 'Krišjāņa Barona iela 3 - 5, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Kubalu skola - muzejs', 'Adrese': '"Kubalu skola", Saustere, Dundagas pag., Talsu nov., LV-3270'}
,
{'Objekta nosaukums': 'Kuldīgas novada pašvaldības iestāde "Kuldīgas novada muzejs"', 'Adrese': 'Pils iela 5, Kuldīga, Kuldīgas nov., LV-3301'}
,
{'Objekta nosaukums': 'Ķekavas novadpētniecības muzejs', 'Adrese': 'Rīgas iela 26, Ķekava, Ķekavas pag., Ķekavas nov., LV-2123'}
,
{'Objekta nosaukums': 'Lapmežciema pagasta muzejs', 'Adrese': 'Liepu iela 4, Lapmežciems, Lapmežciema pag., Tukuma nov., LV-3118'}
,
{'Objekta nosaukums': 'Latgales Kultūrvēstures muzejs', 'Adrese': 'Atbrīvošanas aleja 102, Rēzekne, LV-4601'}
,
{'Objekta nosaukums': 'Latvenergo koncerna Enerģētikas muzeja ekspozīcija Pļaviņu HES', 'Adrese': 'Enerģētiķu iela 2, Aizkraukle, Aizkraukles nov., LV-5101'}
,
{'Objekta nosaukums': 'Latvenergo koncerna Enerģētikas muzejs', 'Adrese': 'Ķeguma prospekts 7/9, Ķegums, Ogres nov., LV-5020'}
,
{'Objekta nosaukums': 'Latvieši pasaulē – muzejs un pētniecības centrs', 'Adrese': 'Mūkusalas iela 3, Rīga, LV-1048'}
,
{'Objekta nosaukums': 'Latvijas Arhitektūras muzejs', 'Adrese': 'Mazā Pils iela 19, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Latvijas Ceļu muzejs', 'Adrese': '"Šlokenbekas muižas ansamblis", Milzkalne, Smārdes pag., Tukuma nov., LV-3148'}
,
{'Objekta nosaukums': 'Latvijas dzelzceļa vēstures muzejs', 'Adrese': 'Uzvaras bulvāris 2A, Rīga, LV-1048'}
,
{'Objekta nosaukums': 'Latvijas Etnogrāfiskā brīvdabas muzeja ekspozīcija zvejnieka - zemnieka sēta "Vītolnieki"', 'Adrese': '"Vītolnieki", Pape, Rucavas pag., Dienvidkurzemes nov., LV-3477'}
,
{'Objekta nosaukums': 'Latvijas Etnogrāfiskā brīvdabas muzeja lauku ekspozīcija "Vēveri"', 'Adrese': '"Vēveri", Vecpiebalgas pag., Cēsu nov., LV-4122'}
,
{'Objekta nosaukums': 'Latvijas Etnogrāfiskais brīvdabas muzejs', 'Adrese': 'Bonaventuras iela 10, Rīga, LV-1024'}
,
{'Objekta nosaukums': 'Latvijas Fotogrāfijas muzejs', 'Adrese': 'Mārstaļu iela 8, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Latvijas Kara muzeja nodaļa "O. Kalpaka muzejs un piemiņas vieta "Airītes""', 'Adrese': '"O. Kalpaka muzejs", Zirņu pag., Saldus nov., LV-3853'}    
,
{'Objekta nosaukums': 'Latvijas Kara muzeja nodaļa "Ziemassvētku kauju muzejs"', 'Adrese': '"Mangaļi", Valgundes pag., Jelgavas nov., LV-3017'}
,
{'Objekta nosaukums': 'Latvijas Kara muzejs', 'Adrese': 'Smilšu iela 20, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Latvijas Kultūras akadēmijas Eduarda Smiļģa Teātra muzejs', 'Adrese': 'Eduarda Smiļģa iela 37, Rīga, LV-1002'}
,
{'Objekta nosaukums': 'Latvijas Lauksaimniecības muzejs', 'Adrese': 'Celtnieku iela 12, Talsi, Talsu nov., LV-3201'}
,
{'Objekta nosaukums': 'Latvijas Mākslinieku savienības muzejs', 'Adrese': '11. novembra krastmala 35, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Latvijas Nacionālā vēstures muzeja nodaļa "Dauderi"', 'Adrese': 'Zāģeru iela 7, Rīga, LV-1005'}
,
{'Objekta nosaukums': 'Latvijas Nacionālā vēstures muzeja nodaļa "Tautas frontes muzejs"', 'Adrese': 'Vecpilsētas iela 13/15, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Latvijas Nacionālais dabas muzejs', 'Adrese': 'Krišjāņa Barona iela 4, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Latvijas Nacionālais mākslas muzejs', 'Adrese': 'Jaņa Rozentāla laukums 1, Rīga, LV-1010'}
,
{'Objekta nosaukums': 'Latvijas Nacionālais vēstures muzejs', 'Adrese': 'Pulka iela 8, Rīga, LV-1007'}
,
{'Objekta nosaukums': 'Latvijas Naivās mākslas muzejs', 'Adrese': 'AB dambis 2, Rīga, LV 1048'}
,
{'Objekta nosaukums': 'Latvijas Okupācijas muzejs', 'Adrese': 'Latviešu strēlnieku laukums 1, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Latvijas Sporta muzejs', 'Adrese': 'Alksnāja iela 9, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Latvijas Ugunsdzēsības muzejs', 'Adrese': 'Hanzas iela 5, Rīga, LV-1045'}
,
{'Objekta nosaukums': 'Liepājas Muzejs', 'Adrese': 'Kūrmājas prospekts 16, Liepāja, LV-3401'}
,
{'Objekta nosaukums': 'Limbažu muzejs', 'Adrese': 'Burtnieku iela 7, Limbaži, Limbažu nov., LV-4001'}
,
{'Objekta nosaukums': 'LKA Rīgas Kino muzejs', 'Adrese': 'Peitavas iela 10, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'LNMM izstāžu zāle "Arsenāls"', 'Adrese': 'Torņa iela 1, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Ludzas Novadpētniecības muzejs', 'Adrese': 'Kuļņeva iela 2, Ludza, Ludzas nov., LV-5701'}
,
{'Objekta nosaukums': 'Madonas novadpētniecības un mākslas muzejs', 'Adrese': 'Skolas iela 12, Madona, Madonas nov., LV-4801'}
,
{'Objekta nosaukums': 'Mākslas muzejs "Rīgas Birža"', 'Adrese': 'Doma laukums 6, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Maltas vēstures muzejs', 'Adrese': 'Parka iela 8, Malta, Maltas pag., Rēzeknes nov., LV-4630'}
,
{'Objekta nosaukums': 'Mazsalacas  muzejs', 'Adrese': 'Parka iela 31, Mazsalaca, Valmieras nov., LV-4215'}
,
{'Objekta nosaukums': 'Memoriālo muzeju apvienība', 'Adrese': 'Kaļķu iela 24, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Mencendorfa nams. Rīdzinieku 17.-18.gs. māja-muzejs.', 'Adrese': 'Grēcinieku iela 18, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Muzejs "Ebreji Latvijā"', 'Adrese': 'Skolas iela 6, Rīga, LV-1010'}
,
{'Objekta nosaukums': 'Muzejs "Rīgas Jūgendstila centrs"', 'Adrese': 'Alberta iela 12, Rīga, LV-1010'}
,
{'Objekta nosaukums': 'Naujenes Novadpētniecības muzejs', 'Adrese': 'Skolas iela 1, Naujene, Naujenes pag., Augšdaugavas nov., LV-5462'}
,
{'Objekta nosaukums': 'Naukšēnu Cilvēkmuzejs', 'Adrese': '"Doktorāts", Naukšēni, Naukšēnu pag., Valmieras nov., LV-4244'}
,
{'Objekta nosaukums': 'Ogres Vēstures un mākslas muzejs', 'Adrese': 'Brīvības iela 36, Ogre, Ogres nov., LV-5001'}
,
{'Objekta nosaukums': 'Ojāra Vācieša muzejs', 'Adrese': 'Ojāra Vācieša iela 19, Rīga, LV-1004'}
,
{'Objekta nosaukums': 'Olaines Vēstures un mākslas muzejs', 'Adrese': 'Jelgavas iela 9 - 37, Olaine, Olaines nov., LV-2114'}
,
{'Objekta nosaukums': 'Pāles novadpētniecības muzejs', 'Adrese': 'Pāle, Pāles pag., Limbažu nov.'}
,
{'Objekta nosaukums': 'Paula Stradiņa Medicīnas vēstures muzejs', 'Adrese': 'Antonijas iela 1, Rīga, LV-1010'}
,
{'Objekta nosaukums': 'Pāvilostas novadpētniecības muzejs', 'Adrese': 'Dzintaru iela 1, Pāvilosta, Dienvidkurzemes nov., LV-3466'}
,
{'Objekta nosaukums': 'Pētera Upīša Dārzkopības muzejs', 'Adrese': 'Ceriņi, Krimūnu pag., Dobeles nov.'}
,
{'Objekta nosaukums': 'Piebalgas muzeju apvienība "Orisāre"', 'Adrese': '"Norkalni 2", Vecpiebalga, Vecpiebalgas pag., Cēsu nov., LV-4122'}
,
{'Objekta nosaukums': 'Preiļu vēstures un lietišķās mākslas muzejs', 'Adrese': 'Raiņa bulvāris 28, Preiļi, Preiļu nov., LV-5301'}
,
{'Objekta nosaukums': 'Profesora Aleksandra Bieziņa muzejs', 'Adrese': '"Jaundilmaņi", Sarkaņu pag., Madonas nov., LV-4870'}
,
{'Objekta nosaukums': 'Raiņa māja Berķenelē', 'Adrese': '"Raiņa mājas", Birkineļi, Kalkūnes pag., Augšdaugavas nov., LV-5449'}
,
{'Objekta nosaukums': 'Raiņa muzejs "Jasmuiža"', 'Adrese': '"Jasmuiža", Aizkalne, Aizkalnes pag., Preiļu nov., LV-5305'}
,
{'Objekta nosaukums': 'Raiņa muzejs "Tadenava"', 'Adrese': '"Tadenavas muzejs", Dunavas pag., Jēkabpils nov., LV-5216'}
,
{'Objekta nosaukums': 'Raiņa un Aspazijas māja', 'Adrese': 'Baznīcas iela 30, Rīga, LV-1010'}
,
{'Objekta nosaukums': 'Raiņa un Aspazijas muzejs (apvienība)', 'Adrese': 'Baznīcas iela 30, Rīga, LV-1010'}
,
{'Objekta nosaukums': 'Raiņa un Aspazijas vasarnīca', 'Adrese': 'Jāņa Pliekšāna iela 5/7, Jūrmala, LV-2015'}
,
{'Objekta nosaukums': 'Rakstniecības un mūzikas muzejs', 'Adrese': 'Pulka iela 8, Rīga, LV-1007'}
,
{'Objekta nosaukums': 'Retro auto muzejs', 'Adrese': 'Kantora iela 22A, Rīga, LV-1002'}
,
{'Objekta nosaukums': 'Rīgas Motormuzejs', 'Adrese': 'Sergeja Eizenšteina iela 8, Rīga, LV-1079'}
,
{'Objekta nosaukums': 'Rīgas pašvaldības kultūras iestāžu apvienības Rīgas Porcelāna muzejs', 'Adrese': 'Kalēju iela 9/11, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Rīgas Stradiņa universitātes Anatomijas muzejs', 'Adrese': 'Kronvalda bulvāris 9, Rīga, LV-1010'}
,
{'Objekta nosaukums': 'Rīgas Stradiņa universitātes muzejs', 'Adrese': 'Dzirciema iela 16, Rīga, LV-1007'}
,
{'Objekta nosaukums': 'Rīgas vēstures un kuģniecības muzejs', 'Adrese': 'Palasta iela 4, Rīga, LV-1050'}
,
{'Objekta nosaukums': 'Roberta Mūka muzejs Galēnos', 'Adrese': 'Skolas iela 11C, Galēni, Galēnu pag., Preiļu nov., LV-5311'}
,
{'Objekta nosaukums': 'Rojas Jūras zvejniecības muzejs', 'Adrese': 'Selgas iela 33, Roja, Rojas pag., Talsu nov., LV-3264'}
,
{'Objekta nosaukums': 'Romana Sutas un Aleksandras Beļcovas muzejs', 'Adrese': 'Elizabetes iela 57A - 26, Rīga, LV-1050'}
,
{'Objekta nosaukums': "Rūdolfa Blaumaņa memoriālais muzejs ''Braki''", 'Adrese': '"Braki", Ērgļu pag., Madonas nov., LV-4840'}
,
{'Objekta nosaukums': 'Rundāles pils muzejs', 'Adrese': '"Rundāles pils", Pilsrundāle, Rundāles pag., Bauskas nov., LV-3921'}
,
{'Objekta nosaukums': 'Rundāles ūdensdzirnavu muzejs', 'Adrese': '"Rundāles ūdensdzirnavas", Pilsrundāle, Rundāles pag., Rundāles nov., LV-3921'}
,
{'Objekta nosaukums': 'Salacgrīvas  muzejs', 'Adrese': 'Sila iela 2, Salacgrīva, Limbažu nov., LV-4033'}
,
{'Objekta nosaukums': 'Salaspils memoriāls', 'Adrese': '"Salaspils memoriāls", Salaspils pag., Salaspils nov., LV-2121'}
,
{'Objekta nosaukums': 'Skrindu dzimtas muzejs', 'Adrese': 'Vabole, Vaboles pag., Augšdaugavas nov.'}
,
{'Objekta nosaukums': 'Smiltenes novada muzejs', 'Adrese': '"Mēru muiža", Mēri, Bilskas pag., Smiltenes nov., LV-4706'}
,
{'Objekta nosaukums': 'Staiceles lībiešu muzejs "Pivālind"', 'Adrese': 'Lielā iela 14, Staicele, Limbažu nov., LV-4043'}
,
{'Objekta nosaukums': 'Talsu novada muzejs', 'Adrese': 'Kārļa Mīlenbaha iela 19, Talsi, Talsu nov., LV-3201'}
,
{'Objekta nosaukums': 'Tēlnieka Voldemāra Jākobsona memoriālā māja', 'Adrese': '"Galdiņi", Vecbebri, Bebru pag., Aizkraukles nov., LV-5135'}
,
{'Objekta nosaukums': 'Tukuma muzejs', 'Adrese': 'Harmonijas iela 7, Tukums, Tukuma nov., LV-3101'}
,
{'Objekta nosaukums': 'Tukuma muzejs - Durbes pils', 'Adrese': 'M. Parka iela 7, Tukums, Tukuma nov., LV-3101'}
,
{'Objekta nosaukums': 'Tukuma muzejs - Džūkstes Pasaku muzejs', 'Adrese': '"Lanciņu skola", Lancenieki, Džūkstes pag., Tukuma nov., LV-3147'}
,
{'Objekta nosaukums': 'Tukuma muzejs - Mākslas galerija "Durvis"', 'Adrese': 'Brīvības laukums 21, Tukums, Tukuma nov., LV-3101'}
,
{'Objekta nosaukums': 'Tukuma muzejs - Pastariņa muzejs', 'Adrese': '"Bisnieki", Zentenes pag., Tukuma nov., LV-3123'}
,
{'Objekta nosaukums': 'Tukuma muzejs - Tukuma Audēju darbnīca', 'Adrese': 'Tidaholmas iela 3, Tukums, Tukuma nov., LV-3101'}
,
{'Objekta nosaukums': 'Tukuma muzejs - Tukuma Mākslas muzejs', 'Adrese': 'Harmonijas iela 7, Tukums, Tukuma nov., LV-3101'}
,
{'Objekta nosaukums': 'Tukuma muzejs - Tukuma pilsētas vēstures muzejs "Pils tornis"', 'Adrese': 'Brīvības laukums 19A, Tukums, Tukuma nov., LV-3101'}
,
{'Objekta nosaukums': 'Turaidas muzejrezervāts', 'Adrese': 'Turaidas iela 10, Sigulda, Siguldas nov., LV-2150'}
,
{'Objekta nosaukums': 'Upītes kultūrvēstures muzejs', 'Adrese': 'Akas laukums 1, Upīte, Šķilbēnu pag., Balvu nov., LV-4587'}
,
{'Objekta nosaukums': 'Valkas novadpētniecības muzejs', 'Adrese': 'Rīgas iela 64, Valka, Valkas nov., LV-4701'}
,
{'Objekta nosaukums': 'Valmieras muzejs', 'Adrese': 'Bruņinieku iela 3, Valmiera, Valmieras nov., LV-4201'}
,
{'Objekta nosaukums': 'Varakļānu Novada muzejs', 'Adrese': 'Pils iela 29, Varakļāni, Varakļānu nov., LV-4838'}
,
{'Objekta nosaukums': 'Vārkavas novadpētniecības muzejs - tūrisma informācijas centrs', 'Adrese': 'Kovaļevsku iela 4, Vārkava, Vārkavas pag., Preiļu nov., LV-5337'}       
,
{'Objekta nosaukums': 'Ventspils muzejs. Herberta Dorbes muzejs "Senču putekļi"', 'Adrese': 'Ērgļu iela 1, Ventspils, LV-3601'}
,
{'Objekta nosaukums': 'Ventspils muzejs. Livonijas ordeņa pils', 'Adrese': 'Jāņa iela 17, Ventspils, LV-3601'}
,
{'Objekta nosaukums': 'Ventspils muzejs. Piejūras brīvdabas muzejs', 'Adrese': 'Riņķa iela 2, Ventspils, LV-3601'}
,
{'Objekta nosaukums': 'Ventspils muzejs. Ziemeļkurzemes amatniecības centrs "Amatu māja"', 'Adrese': 'Skolas iela 3, Ventspils, LV-3601'}
,
{'Objekta nosaukums': 'Vērgales pagasta muzejs', 'Adrese': '"Dīķnieki", Vērgale, Vērgales pag., Dienvidkurzemes nov., LV-3463'}
,
{'Objekta nosaukums': 'Vēstures ekspozīcija "Sirdsapziņas ugunskurs"', 'Adrese': 'Pils iela 12, Cēsis, Cēsu nov., LV-4101'}
,
{'Objekta nosaukums': 'Viesītes muzejs "Sēlija"', 'Adrese': 'Kaļķu iela 1, Viesīte, Jēkabpils nov., LV-5237'}
,
{'Objekta nosaukums': 'Viļa Plūdoņa muzejs', 'Adrese': '"Lejenieki", Ceraukstes pag., Bauskas nov., LV-3901'}
,
{'Objekta nosaukums': 'Viļakas muzejs', 'Adrese': 'Balvu iela 13, Viļaka, Balvu nov., LV-4583'}
,
{'Objekta nosaukums': 'Viļānu Novadpētniecības  muzejs', 'Adrese': 'Kultūras laukums 2, Viļāni, Rēzeknes nov., LV-4650'}
,
{'Objekta nosaukums': 'Žaņa Lipkes memoriāls', 'Adrese': 'Mazais Balasta dambis 9, Rīga, LV-1048'}
'''

re.sub("'","\"",a)
a.replace("'",'"')

print(a)