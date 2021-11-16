import pytest

from evalme.image.object_detection import KeyPointsEvalItem, keypoints_distance, PolygonObjectDetectionEvalItem, OCREvalItem


def test_keypoints_matching():
    '''
    Matching with almost 1 distance
    '''
    test_data = [
        [{
            "id": "S6oszbKrqK",
            "type": "keypointlabels",
            "value": {
                "x": 35.111111,
                "y": 65.41666666666667,
                "width": 0.625,
                "keypointlabels": ["Engine"]
            },
            "to_name": "image",
            "from_name": "label",
            "image_rotation": 0,
            "original_width": 320,
            "original_height": 240
        }],
        [{
            "id": "S6oszbKrqK",
            "type": "keypointlabels",
            "value": {
                "x": 34.222222,
                "y": 64.4167,
                "width": 0.625,
                "keypointlabels": ["Engine"]
            },
            "to_name": "image",
            "from_name": "label",
            "image_rotation": 0,
            "original_width": 320,
            "original_height": 240
        }]
    ]
    assert keypoints_distance(test_data[0], test_data[1], label_weights={}) == 1


def test_keypoints_matching_per_label():
    '''
    Matching with almost 1 distance per label
    '''
    test_data = [
        [{
            "id": "S6oszbKrqK",
            "type": "keypointlabels",
            "value": {
                "x": 35.111111,
                "y": 65.41666666666667,
                "width": 0.625,
                "keypointlabels": ["Engine"]
            },
            "to_name": "image",
            "from_name": "label",
            "image_rotation": 0,
            "original_width": 320,
            "original_height": 240
        }],
        [{
            "id": "S6oszbKrqK",
            "type": "keypointlabels",
            "value": {
                "x": 34.222222,
                "y": 64.4167,
                "width": 0.625,
                "keypointlabels": ["Engine"]
            },
            "to_name": "image",
            "from_name": "label",
            "image_rotation": 0,
            "original_width": 320,
            "original_height": 240
        }]
    ]
    assert keypoints_distance(test_data[0], test_data[1], label_weights={}, per_label=True) == {"Engine": 1}


def test_keypoints_not_matching():
    '''
    Not Matching with almost 1 distance
    '''
    test_data = [
        [{
            "id": "S6oszbKrqK",
            "type": "keypointlabels",
            "value": {
                "x": 35.333333,
                "y": 65.41666666666667,
                "width": 0.625,
                "keypointlabels": ["Engine"]
            },
            "to_name": "image",
            "from_name": "label",
            "image_rotation": 0,
            "original_width": 320,
            "original_height": 240
        }],
        [{
            "id": "S6oszbKrqK",
            "type": "keypointlabels",
            "value": {
                "x": 34.222222,
                "y": 64.4165,
                "width": 0.625,
                "keypointlabels": ["Engine"]
            },
            "to_name": "image",
            "from_name": "label",
            "image_rotation": 0,
            "original_width": 320,
            "original_height": 240
        }]
    ]

    assert keypoints_distance(test_data[0], test_data[1], label_weights={}) == 0


def test_keypoints_not_matching_label():
    '''
    Not Matching label
    '''
    test_data = [
        [{
            "id": "S6oszbKrqK",
            "type": "keypointlabels",
            "value": {
                "x": 34.0,
                "y": 64.0,
                "width": 0.625,
                "keypointlabels": ["Engine"]
            },
            "to_name": "image",
            "from_name": "label",
            "image_rotation": 0,
            "original_width": 320,
            "original_height": 240
        }],
        [{
            "id": "S6oszbKrqK",
            "type": "keypointlabels",
            "value": {
                "x": 34.0,
                "y": 64.0,
                "width": 0.625,
                "keypointlabels": ["Engine1"]
            },
            "to_name": "image",
            "from_name": "label",
            "image_rotation": 0,
            "original_width": 320,
            "original_height": 240
        }]
    ]
    assert keypoints_distance(test_data[0], test_data[1], label_weights={}) == 0


def test_keypoints_not_matching_per_label():
    '''
    Not Matching with almost 1 distance per label
    '''
    test_data = [
        [{
            "id": "S6oszbKrqK",
            "type": "keypointlabels",
            "value": {
                "x": 35.333333,
                "y": 65.41666666666667,
                "width": 0.625,
                "keypointlabels": ["Engine"]
            },
            "to_name": "image",
            "from_name": "label",
            "image_rotation": 0,
            "original_width": 320,
            "original_height": 240
        }],
        [{
            "id": "S6oszbKrqK",
            "type": "keypointlabels",
            "value": {
                "x": 34.222222,
                "y": 64.4165,
                "width": 0.625,
                "keypointlabels": ["Engine"]
            },
            "to_name": "image",
            "from_name": "label",
            "image_rotation": 0,
            "original_width": 320,
            "original_height": 240
        }]
    ]
    assert keypoints_distance(test_data[0], test_data[1], label_weights={}, per_label=True) =={"Engine": 0}


def test_object_detection_fixing_polygon():
    points = [[37.5, 23.046875], [36.328125, 23.828125], [35.15625, 25.0], [37.109375, 23.4375], [38.671875, 23.046875], [41.015625, 25.390625], [41.015625, 26.953125], [40.625, 34.375], [40.234375, 37.890625], [41.40625, 39.453125], [41.796875, 40.625], [42.1875, 41.796875], [42.96875, 42.96875], [39.453125, 43.359375], [39.453125, 41.796875], [38.28125, 41.015625], [39.0625, 42.1875], [38.28125, 44.140625], [36.71875, 43.359375], [37.109375, 41.796875], [36.71875, 40.625], [37.5, 39.453125], [36.328125, 38.28125], [35.15625, 39.0625], [34.765625, 40.234375], [34.375, 41.40625], [33.984375, 42.96875], [33.203125, 44.140625], [32.8125, 45.3125], [32.421875, 46.484375], [31.640625, 47.65625], [31.25, 48.828125], [31.25, 50.390625], [30.859375, 51.5625], [30.078125, 52.734375], [29.6875, 53.90625], [29.296875, 55.078125], [28.90625, 56.25], [29.296875, 57.8125], [38.28125, 57.8125], [42.96875, 58.203125], [56.25, 57.8125], [59.765625, 58.203125], [60.9375, 57.421875], [60.546875, 55.859375], [60.15625, 54.296875], [59.765625, 53.125], [59.765625, 48.828125], [59.375, 46.875], [58.984375, 44.921875], [58.203125, 43.75], [57.8125, 42.578125], [57.421875, 41.40625], [57.421875, 37.890625], [57.03125, 35.9375], [56.640625, 34.765625], [56.25, 31.640625], [55.859375, 29.6875], [55.46875, 27.734375], [54.6875, 26.5625], [55.46875, 25.390625], [53.90625, 25.0], [52.734375, 25.390625], [51.5625, 25.0], [50.390625, 24.21875], [48.828125, 23.828125], [47.65625, 24.21875], [46.484375, 23.4375], [45.3125, 24.21875], [46.09375, 26.953125], [44.921875, 27.34375], [43.359375, 26.171875], [41.40625, 24.609375], [40.234375, 23.046875]]
    p = PolygonObjectDetectionEvalItem(raw_data=None)
    polygon = p._try_build_poly(points)
    assert polygon.is_valid


def test_object_detection_fixing_polygon():
    """
    Test for checking building invalid polygons with loops
    """
    p = PolygonObjectDetectionEvalItem(raw_data=None)

    points1 = [[71.24548999277505, 36.442868897058716], [71.31558790201544, 37.70463126338564], [71.45578372049621, 39.49212794901545], [71.52588162973657, 41.17447777078468], [71.52588162973657, 42.96197445641448], [71.42744842558623, 45.27520546134716], [71.32230156172567, 47.30468799946319], [71.21044103815485, 49.42850658383994], [70.96509835581352, 52.00460474842407], [70.78985358271255, 54.265262321426476], [70.54451090037121, 56.57849332635916], [70.34093083236029, 58.807458774596476], [70.26411926340965, 60.258633561479336], [70.16568605925933, 61.90929125848349], [70.09558815001893, 63.61252238741793], [70.01877658106832, 64.41193468397212], [70.33421717265004, 66.04171107381104], [70.509461945751, 67.77663432751056], [70.58627351470162, 69.20692780722821], [70.69142037856221, 70.85758550423236], [70.8176953255995, 72.64508218986217], [70.90171410628336, 74.46427100025706], [71.01406818187716, 76.74580988042466], [71.03519626505388, 78.39646757742882], [71.10529417429427, 79.92109710340716], [71.18210574324492, 81.5299921860809], [71.21044103815485, 82.23432810833987], [71.07695887938432, 82.67579687094738], [70.93004940119332, 82.9177827234336], [70.54451090037121, 82.97035615536389], [70.18878835052809, 82.60086147578286], [69.97227451511971, 81.78767704949077], [69.97048961465292, 80.90606805814588], [69.86484919876933, 80.43068618666975], [69.52679986794186, 80.20884131331421], [69.2098786202911, 79.92361219042854], [68.70280462404989, 79.701767317073], [68.17460254463198, 79.54330669324763], [67.68865663156748, 79.63838306754286], [67.0970703026194, 79.76515156660317], [66.48435589049461, 80.08207281425392], [65.74487297930952, 80.39899406190467], [64.8363654027107, 80.71591530955543], [63.69648963582931, 80.99337713085148], [62.70240761490822, 81.38157207973887], [61.784075352967555, 81.83738885841124], [60.605850385566455, 81.87386039550947], [59.65999873999142, 81.79340974568201], [58.73492518962879, 81.67225917510848], [57.85780403220267, 81.63517862484865], [57.43529069195391, 81.71175837580526], [56.75889812040099, 82.25500990165214], [56.37309564523462, 82.40121795693683], [56.03277336117247, 82.45725418825431], [55.7151554112775, 82.26999733190546], [55.326917291475496, 81.88653465985347], [55.058061904904946, 81.36917038099757], [54.81980387642082, 80.68320401905817], [54.658559177049796, 79.8972182739836], [54.57795248388386, 79.21247101818575], [54.58786254237386, 78.31563727052497], [54.65744788021747, 77.32990585050003], [54.83977505252922, 74.792935976939], [55.17620037056849, 72.30473837034044], [55.3583293680495, 70.7532969148149], [55.60257456419653, 69.70893636699515], [55.783799901722084, 68.33456897337967], [55.85825286218083, 67.08414411711703], [55.93177037724768, 65.76804422219723], [55.94015426181347, 64.30099510919057], [55.94832194493592, 62.86909389643798], [55.96427935908149, 62.098023087460696], [56.615029525666664, 61.002802357662496], [57.02527568231736, 61.29596595758693], [57.46273366498702, 61.83028687299975], [58.07050051782664, 62.25380786427346], [58.50389989802015, 62.5171573413049], [58.91879381577917, 62.999267914918605], [59.268562115515415, 63.06605068811326], [59.76005622645524, 63.11999279809634], [60.66139312484395, 63.515046526694505], [61.35051604759635, 63.423340732929645], [61.808574623067514, 63.106240060787805], [62.30432304818241, 62.54327537914041], [62.539587740692454, 62.325116299571405], [62.701051475838895, 62.13850046431015], [63.14586691284543, 61.85717292059291], [63.202574327194625, 61.54864449551725], [63.11650219433461, 61.264041361548685], [63.274309291605334, 61.22151134316702], [63.582222682455466, 61.2478114045958], [63.75181297117496, 61.20139237851563], [63.857191244642124, 60.970382934677055], [63.91814492387204, 60.7641684432282], [63.92312129493989, 60.59745156025348], [65.0463149189407, 61.25941764845373], [65.26880983467146, 61.19402295639785], [65.46676384125016, 61.012843304807575], [65.6123736498138, 60.67692773078017], [65.59604489008994, 60.35646600722881], [65.41896154775907, 60.023177806943735], [64.77191598191997, 59.41690925218269], [64.1102731388132, 58.84895732540074], [62.981803205149085, 58.06039045019356], [62.27164004306869, 57.527117916145414], [61.67247382657756, 56.90039294960442], [61.799599957596286, 56.67646440884397], [61.94017088193441, 56.455007201204374], [62.45993772054322, 56.04610401425424], [62.89643561187592, 55.644356500727994], [63.26697706818597, 55.17486124375921], [63.494035357433795, 54.2992312297473], [63.50053269403326, 53.62317766665219], [63.37350720761441, 53.33902533686241], [63.155714962569014, 53.28547820194824], [62.93646558232525, 53.467955360686666], [62.75750778876408, 53.84796659605624], [62.51358363920958, 54.20704608897229], [62.19592381110928, 54.42049191776855], [61.86510534683914, 54.76663160134683], [61.5584376140037, 55.02540945221735], [61.23542311979876, 55.38703932414456], [61.008044494654534, 55.53373279178538], [60.77725906662706, 55.69279453789216], [60.582252028989245, 56.01155377925047], [60.22746959329231, 56.352486418021705], [59.89775460423932, 56.70636858783149], [59.68277910344004, 57.17862985566916], [59.44928001985543, 57.3149276037563], [59.36463419352438, 57.567519400805146], [58.987793860548834, 57.854797289506095], [58.52559786339017, 58.07313198091575], [58.24434785689984, 58.19215402593864], [58.077723717313056, 58.121470940970845], [57.89359234179078, 58.1606992666703], [57.67251611790723, 58.23713702708523], [57.84937591912521, 57.961590785049204], [58.06187606719222, 57.56530903495161], [58.21133943908635, 57.07174404340931], [58.29430454972359, 56.32974077406917], [58.31969169477289, 55.02957071624504], [58.435808363835285, 53.697081552322054], [58.649470464180425, 52.61819639193315], [58.89781449260207, 51.53422336516053], [59.06282111541507, 50.82814637206523], [59.28767650641035, 50.31260035578549], [59.4313703272291, 49.900796984713594], [59.474775368756816, 48.96510288587076], [59.403972830570574, 47.52965772633963], [59.23276525734068, 45.796951211939245], [59.171278783971104, 45.077484253139055], [59.082753938223746, 44.388948899918795], [58.966611547569435, 43.28526667806965], [58.912438598470956, 41.91598270138615], [58.8987991918453, 40.56595175598115], [58.87839066486148, 39.953793495574956], [58.96645332254199, 38.071295960351215], [59.04503499682862, 36.49942433070164], [59.384522359533335, 35.64443640738881], [59.74517246454507, 34.448201172071], [59.87982738580833, 34.08344698503056], [59.893086405566386, 33.87428634636171], [60.6808904611383, 31.940211162639486], [61.605356522644634, 29.677699633344925], [62.34241758643345, 27.893863288378906], [60.952549423160285, 29.34680069116033], [55.76160558614943, 35.32618023397065], [55.605506396023245, 35.42073813617422], [55.32715112944967, 35.73508199284892], [54.97103071960984, 36.25797742952729], [54.633528241537626, 36.9843285912676], [54.26807096343351, 37.497235560356465], [53.83217258093989, 38.17825775749258], [53.50162649038513, 38.82396866456495], [53.06786127867833, 40.601739955066876], [52.84196368499808, 42.274530364303985], [52.783383655409835, 43.50938477202643], [52.50839748642768, 44.888336083281494], [52.27768684320113, 46.18629756025955], [52.08641844032083, 47.37588014112915], [51.89566214915828, 48.73266925030944], [51.767322528757404, 50.556542209518994], [51.736372698058275, 51.54206297327813], [51.573990445706315, 52.63373910051626], [51.460791538415, 52.80725375510232], [51.18430899498759, 53.32131252483345], [51.151662652699535, 54.10159729440949], [51.03533729809058, 54.37210075071141], [51.01499813520173, 55.17663231836683], [50.76725409047201, 55.70161729889367], [50.58968379533592, 56.46000611085433], [50.46707739306644, 57.722815377595246], [50.27082356745067, 57.89138016219952], [50.13187687357528, 58.137339781228505], [50.0505686270744, 58.49945538885535], [50.14341425874418, 59.16469263980238], [49.90914966679136, 59.847920599849765], [49.788683653097344, 60.07596583726081], [49.49172086583298, 60.84586996559508], [49.342901624433125, 62.06998842588095], [49.44041859346952, 63.165749955028346], [49.668574290179805, 64.25848784417997], [49.928395850437056, 64.84305279936005], [50.045011644085044, 65.77996047111341], [50.23549100699365, 66.31095971614643], [50.47181880846324, 66.7936169724774], [50.58996806612921, 67.40380181374151], [50.86712300509155, 68.23554400882216], [51.59897199956446, 68.14526579162069], [51.95153704809118, 67.66791136732252], [52.358679530540996, 67.16988440595944], [54.16704190258511, 64.94553664502024], [52.83206973286896, 66.54983768172292], [52.532778438919806, 67.08044997450287], [51.903247322225354, 68.06972794484054], [51.50610560216469, 69.05767590607314], [50.9763233009358, 70.27166785402501], [50.643172261999155, 71.47216701540958], [50.326294994272324, 72.8395583813219], [50.03638925654642, 74.14605788254052], [49.71391643855616, 75.58382795671191], [49.28807344733942, 77.21490358075039], [48.929120399392765, 79.09330268348658], [48.66901680622432, 80.20108084054931], [48.398138379146346, 81.50535576181836], [48.25063589117616, 83.05711020633949], [48.06391298950883, 84.79611358302171], [47.94539885735842, 86.1971092057169], [48.053392825320884, 86.43685855038606], [48.27501899364376, 86.78694831748697], [48.51450477872317, 87.00091570116585], [48.765382164740195, 86.99654280439964], [48.963754939739204, 86.90510968569275], [49.33711718690008, 86.41847473794789], [49.623338541643015, 85.87302289375616], [49.90191566957567, 85.12933633620422], [50.165129293348876, 84.15921547587293], [50.53503291688815, 82.95540932606576], [50.8425972664721, 81.68713373626564], [51.448810109552355, 79.28079697536243], [52.01489270758875, 77.25119324876009], [52.397596113371925, 75.53728494854272], [52.84880150303474, 73.60041029173141], [53.200356278734176, 72.25757073582841], [53.55414118029318, 70.56654297468714], [54.09316588867561, 68.66701901873371], [54.49009452250821, 67.13851701864796], [54.765570133787854, 65.95636820582571], [54.988354931064855, 65.45988879571682], [55.20746733105245, 65.06114792853795], [55.35881698296463, 64.56310037826378], [55.52796053323985, 63.4684275275065], [55.65506462817371, 62.66928007195139], [54.970870757233286, 56.976136683492406], [54.81722694678211, 56.486161932449185], [54.534615960529436, 55.5960275401542], [54.20026803388244, 54.473773490150734], [53.81265797615115, 53.10707703191306], [53.53970603636695, 52.16462875865812], [53.40800663144548, 51.37397226079495], [53.40600958902171, 50.54830848080784], [53.39971745622639, 49.740420779485895], [53.42019042398491, 48.985118280857606], [53.555862382265154, 48.04355632801825], [53.69391853898538, 48.04536749780579], [53.82490938412744, 47.40243294385485], [54.29413081269998, 45.89443917195816], [54.69197287851976, 44.57950920119552], [55.00946162616242, 43.57893556516054], [55.13387583055568, 42.67917658806935], [55.325327441870236, 40.59723983750328], [55.623374845658255, 38.212844537177176], [55.71981824562783, 36.588936573240204], [55.78559152860122, 35.332379462641015], [62.699666338793875, 26.8117100745742], [62.936586468431884, 27.045428761365315], [63.843428465370565, 27.33794376174733], [65.75375388377067, 28.362506138960082], [66.36252637750958, 28.331606991988995], [67.59390862819974, 28.27529080240259], [68.61872688988996, 28.609172524220007], [69.64706780180786, 29.766475576045952], [70.50000726932018, 31.827931997229065], [70.99035785108931, 34.144349909489875]]
    polygon1 = p._try_build_poly(points1)

    points2 = [[37.5, 23.046875], [36.328125, 23.828125], [35.15625, 25.0], [37.109375, 23.4375], [38.671875, 23.046875], [41.015625, 25.390625], [41.015625, 26.953125], [40.625, 34.375], [40.234375, 37.890625], [41.40625, 39.453125], [41.796875, 40.625], [42.1875, 41.796875], [42.96875, 42.96875], [39.453125, 43.359375], [39.453125, 41.796875], [38.28125, 41.015625], [39.0625, 42.1875], [38.28125, 44.140625], [36.71875, 43.359375], [37.109375, 41.796875], [36.71875, 40.625], [37.5, 39.453125], [36.328125, 38.28125], [35.15625, 39.0625], [34.765625, 40.234375], [34.375, 41.40625], [33.984375, 42.96875], [33.203125, 44.140625], [32.8125, 45.3125], [32.421875, 46.484375], [31.640625, 47.65625], [31.25, 48.828125], [31.25, 50.390625], [30.859375, 51.5625], [30.078125, 52.734375], [29.6875, 53.90625], [29.296875, 55.078125], [28.90625, 56.25], [29.296875, 57.8125], [38.28125, 57.8125], [42.96875, 58.203125], [56.25, 57.8125], [59.765625, 58.203125], [60.9375, 57.421875], [60.546875, 55.859375], [60.15625, 54.296875], [59.765625, 53.125], [59.765625, 48.828125], [59.375, 46.875], [58.984375, 44.921875], [58.203125, 43.75], [57.8125, 42.578125], [57.421875, 41.40625], [57.421875, 37.890625], [57.03125, 35.9375], [56.640625, 34.765625], [56.25, 31.640625], [55.859375, 29.6875], [55.46875, 27.734375], [54.6875, 26.5625], [55.46875, 25.390625], [53.90625, 25.0], [52.734375, 25.390625], [51.5625, 25.0], [50.390625, 24.21875], [48.828125, 23.828125], [47.65625, 24.21875], [46.484375, 23.4375], [45.3125, 24.21875], [46.09375, 26.953125], [44.921875, 27.34375], [43.359375, 26.171875], [41.40625, 24.609375], [40.234375, 23.046875]]
    polygon2 = p._try_build_poly(points2)

    a = polygon1.intersection(polygon2).area
    b = p._iou({'points': points1}, {'points': points2})

    assert a > 184
    assert b > 0.17

    
def test_OCR_matching_function():
    res1 = [{
            "id": "rSbk_pk1g-",
            "type": "rectangle",
            "value": {
                "x": 35.273972602739725,
                "y": 6.481481481481482,
                "width": 37.157534246575345,
                "height": 17.12962962962963,
                "rotation": 0
            },
            "to_name": "image",
            "from_name": "bbox",
            "image_rotation": 0,
            "original_width": 584,
            "original_height": 216
        }, {
            "id": "rSbk_pk1g-",
            "type": "labels",
            "value": {
                "x": 35.273972602739725,
                "y": 6.481481481481482,
                "width": 37.157534246575345,
                "height": 17.12962962962963,
                "labels": ["Text"],
                "rotation": 0
            },
            "to_name": "image",
            "from_name": "label",
            "image_rotation": 0,
            "original_width": 584,
            "original_height": 216
        }, {
            "id": "rSbk_pk1g-",
            "type": "textarea",
            "value": {
                "x": 35.273972602739725,
                "y": 6.481481481481482,
                "text": ["oh no"],
                "width": 37.157534246575345,
                "height": 17.12962962962963,
                "rotation": 0
            },
            "to_name": "image",
            "from_name": "transcription",
            "image_rotation": 0,
            "original_width": 584,
            "original_height": 216
        }
        ]

    obj1 = OCREvalItem(res1)
    obj2 = OCREvalItem(res1)

    assert obj1.compare(obj2) == 1


def test_OCR_matching_function_no_rectangle():
    res1 = [{
            "id": "rSbk_pk1g-",
            "type": "rectangle",
            "value": {
                "x": 35.273972602739725,
                "y": 6.481481481481482,
                "width": 37.157534246575345,
                "height": 17.12962962962963,
                "rotation": 0
            },
            "to_name": "image",
            "from_name": "bbox",
            "image_rotation": 0,
            "original_width": 584,
            "original_height": 216
        }, {
            "id": "rSbk_pk1g-",
            "type": "labels",
            "value": {
                "x": 35.273972602739725,
                "y": 6.481481481481482,
                "width": 37.157534246575345,
                "height": 17.12962962962963,
                "labels": ["Text"],
                "rotation": 0
            },
            "to_name": "image",
            "from_name": "label",
            "image_rotation": 0,
            "original_width": 584,
            "original_height": 216
        }, {
            "id": "rSbk_pk1g-",
            "type": "textarea",
            "value": {
                "x": 35.273972602739725,
                "y": 6.481481481481482,
                "text": ["oh no"],
                "width": 37.157534246575345,
                "height": 17.12962962962963,
                "rotation": 0
            },
            "to_name": "image",
            "from_name": "transcription",
            "image_rotation": 0,
            "original_width": 584,
            "original_height": 216
        }
        ]
    res2 = [ {
            "id": "rSbk_pk1g",
            "type": "labels",
            "value": {
                "x": 35.273972602739725,
                "y": 6.481481481481482,
                "width": 37.157534246575345,
                "height": 17.12962962962963,
                "labels": ["Text"],
                "rotation": 0
            },
            "to_name": "image",
            "from_name": "label",
            "image_rotation": 0,
            "original_width": 584,
            "original_height": 216
        }, {
            "id": "rSbk_pk1g",
            "type": "textarea",
            "value": {
                "x": 35.273972602739725,
                "y": 6.481481481481482,
                "text": ["oh no"],
                "width": 37.157534246575345,
                "height": 17.12962962962963,
                "rotation": 0
            },
            "to_name": "image",
            "from_name": "transcription",
            "image_rotation": 0,
            "original_width": 584,
            "original_height": 216
        }
        ]

    obj1 = OCREvalItem(res1)
    obj2 = OCREvalItem(res2)

    assert obj1.compare(obj2) == 0


def test_OCR_matching_function_not_matching_text():
    res1 = [{
            "id": "rSbk_pk1g-",
            "type": "rectangle",
            "value": {
                "x": 35.273972602739725,
                "y": 6.481481481481482,
                "width": 37.157534246575345,
                "height": 17.12962962962963,
                "rotation": 0
            },
            "to_name": "image",
            "from_name": "bbox",
            "image_rotation": 0,
            "original_width": 584,
            "original_height": 216
        }, {
            "id": "rSbk_pk1g-",
            "type": "labels",
            "value": {
                "x": 35.273972602739725,
                "y": 6.481481481481482,
                "width": 37.157534246575345,
                "height": 17.12962962962963,
                "labels": ["Text"],
                "rotation": 0
            },
            "to_name": "image",
            "from_name": "label",
            "image_rotation": 0,
            "original_width": 584,
            "original_height": 216
        }, {
            "id": "rSbk_pk1g-",
            "type": "textarea",
            "value": {
                "x": 35.273972602739725,
                "y": 6.481481481481482,
                "text": ["oh no"],
                "width": 37.157534246575345,
                "height": 17.12962962962963,
                "rotation": 0
            },
            "to_name": "image",
            "from_name": "transcription",
            "image_rotation": 0,
            "original_width": 584,
            "original_height": 216
        }
        ]
    res2 = [{
        "id": "rSbk_pk1g",
        "type": "rectangle",
        "value": {
            "x": 35.273972602739725,
            "y": 6.481481481481482,
            "width": 37.157534246575345,
            "height": 17.12962962962963,
            "rotation": 0
        },
        "to_name": "image",
        "from_name": "bbox",
        "image_rotation": 0,
        "original_width": 584,
        "original_height": 216
    }, {
        "id": "rSbk_pk1g",
        "type": "labels",
        "value": {
            "x": 35.273972602739725,
            "y": 6.481481481481482,
            "width": 37.157534246575345,
            "height": 17.12962962962963,
            "labels": ["Text"],
            "rotation": 0
        },
        "to_name": "image",
        "from_name": "label",
        "image_rotation": 0,
        "original_width": 584,
        "original_height": 216
    }, {
        "id": "rSbk_pk1g",
        "type": "textarea",
        "value": {
            "x": 35.273972602739725,
            "y": 6.481481481481482,
            "text": ["ayyes"],
            "width": 37.157534246575345,
            "height": 17.12962962962963,
            "rotation": 0
        },
        "to_name": "image",
        "from_name": "transcription",
        "image_rotation": 0,
        "original_width": 584,
        "original_height": 216
    }
    ]
    obj1 = OCREvalItem(res1)
    obj2 = OCREvalItem(res2)

    assert obj1.compare(obj2) == 0


def test_simple_OCR_matching():
    from evalme.metrics import Metrics
    ann1 = [{'original_width': 768, 'original_height': 576, 'image_rotation': 0, 'value': {'x': 64.53333333333333, 'y': 59.502664298401434, 'width': 19.19999999999997, 'height': 12.07815275310836, 'rotation': 0}, 'id': '9VXbGdgh0T', 'from_name': 'bbox', 'to_name': 'image', 'type': 'rectangle', 'origin': 'manual'}, {'original_width': 768, 'original_height': 576, 'image_rotation': 0, 'value': {'x': 64.53333333333333, 'y': 59.502664298401434, 'width': 19.19999999999997, 'height': 12.07815275310836, 'rotation': 0, 'labels': ['Text']}, 'id': '9VXbGdgh0T', 'from_name': 'label', 'to_name': 'image', 'type': 'labels', 'origin': 'manual'}, {'original_width': 768, 'original_height': 576, 'image_rotation': 0, 'value': {'x': 64.53333333333333, 'y': 59.502664298401434, 'width': 19.19999999999997, 'height': 12.07815275310836, 'rotation': 0, 'text': ['17-RX-RR']}, 'id': '9VXbGdgh0T', 'from_name': 'transcription', 'to_name': 'image', 'type': 'textarea', 'origin': 'manual'}]
    ann2 = [{'id': 'buquXLcKOL', 'type': 'rectangle', 'value': {'x': 63.6, 'y': 60.92362344582593, 'width': 20.666666666666668, 'height': 10.8348134991119, 'rotation': 0}, 'origin': 'manual', 'to_name': 'image', 'from_name': 'bbox', 'image_rotation': 0, 'original_width': 768, 'original_height': 576}, {'id': 'buquXLcKOL', 'type': 'labels', 'value': {'x': 63.6, 'y': 60.92362344582593, 'width': 20.666666666666668, 'height': 10.8348134991119, 'labels': ['Text'], 'rotation': 0}, 'origin': 'manual', 'to_name': 'image', 'from_name': 'label', 'image_rotation': 0, 'original_width': 768, 'original_height': 576}, {'id': 'buquXLcKOL', 'type': 'textarea', 'value': {'x': 63.6, 'y': 60.92362344582593, 'text': ['17-RX-RR'], 'width': 20.666666666666668, 'height': 10.8348134991119, 'rotation': 0}, 'origin': 'manual', 'to_name': 'image', 'from_name': 'transcription', 'image_rotation': 0, 'original_width': 768, 'original_height': 576}]
    score = Metrics.apply({}, ann1, ann2, metric_name='OCR')
    assert score > 0
