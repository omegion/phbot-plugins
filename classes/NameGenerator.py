import random

LEFT = [
    'admiring',
    'adoring',
    'affectionate',
    'agitated',
    'amazing',
    'angry',
    'awesome',
    'blissful',
    'boring',
    'brave',
    'clever',
    'cocky',
    'compassionate',
    'competent',
    'condescending',
    'confident',
    'cranky',
    'dazzling',
    'determined',
    'distracted',
    'dreamy',
    'eager',
    'ecstatic',
    'elastic',
    'elated',
    'elegant',
    'eloquent',
    'epic',
    'fervent',
    'festive',
    'flamboyant',
    'focused',
    'friendly',
    'frosty',
    'gallant',
    'gifted',
    'goofy',
    'gracious',
    'happy',
    'hardcore',
    'heuristic',
    'hopeful',
    'hungry',
    'infallible',
    'inspiring',
    'jolly',
    'jovial',
    'keen',
    'kind',
    'laughing',
    'loving',
    'lucid',
    'mystifying',
    'modest',
    'musing',
    'naughty',
    'nervous',
    'nifty',
    'nostalgic',
    'objective',
    'optimistic',
    'peaceful',
    'pedantic',
    'pensive',
    'practical',
    'priceless',
    'quirky',
    'quizzical',
    'relaxed',
    'reverent',
    'romantic',
    'sad',
    'serene',
    'sharp',
    'silly',
    'sleepy',
    'stoic',
    'stupefied',
    'suspicious',
    'tender',
    'thirsty',
    'trusting',
    'unruffled',
    'upbeat',
    'vibrant',
    'vigilant',
    'vigorous',
    'wizardly',
    'wonderful',
    'xenodochial',
    'youthful',
    'zealous',
    'zen',
    'amaranth',
    'amber',
    'amethyst',
    'apricot',
    'aqua',
    'aquamarine',
    'azure',
    'beige',
    'black',
    'blue',
    'blush',
    'bronze',
    'brown',
    'chocolate',
    'coffee',
    'copper',
    'coral',
    'crimson',
    'cyan',
    'emerald',
    'fuchsia',
    'gold',
    'gray',
    'green',
    'harlequin',
    'indigo',
    'ivory',
    'jade',
    'lavender',
    'lime',
    'magenta',
    'maroon',
    'moccasin',
    'olive',
    'orange',
    'peach',
    'pink',
    'plum',
    'purple',
    'red',
    'rose',
    'salmon',
    'sapphire',
    'scarlet',
    'silver',
    'tan',
    'teal',
    'tomato',
    'turquoise',
    'violet',
    'white',
    'yellow',
    'average',
    'big',
    'colossal',
    'fat',
    'giant',
    'gigantic',
    'great',
    'huge',
    'immense',
    'large',
    'little',
    'long',
    'mammoth',
    'massive',
    'miniature',
    'petite',
    'puny',
    'short',
    'small',
    'tall',
    'tiny',
    'boiling',
    'breezy',
    'broken',
    'bumpy',
    'chilly',
    'cold',
    'cool',
    'creepy',
    'crooked',
    'cuddly',
    'curly',
    'damaged',
    'damp',
    'dirty',
    'dry',
    'dusty',
    'filthy',
    'flaky',
    'fluffy',
    'wet',
    'broad',
    'chubby',
    'crooked',
    'curved',
    'deep',
    'flat',
    'high',
    'hollow',
    'low',
    'narrow',
    'round',
    'shallow',
    'skinny',
    'square',
    'steep',
    'straight',
    'wide',
    'ancient',
    'brief',
    'early',
    'fast',
    'late',
    'long',
    'modern',
    'old',
    'quick',
    'rapid',
    'short',
    'slow',
    'swift',
    'young',
    'abundant',
    'empty',
    'few',
    'heavy',
    'light',
    'many',
    'numerous',
    'Sound',
    'cooing',
    'deafening',
    'faint',
    'harsh',
    'hissing',
    'hushed',
    'husky',
    'loud',
    'melodic',
    'moaning',
    'mute',
    'noisy',
    'purring',
    'quiet',
    'raspy',
    'resonant',
    'screeching',
    'shrill',
    'silent',
    'soft',
    'squealing',
    'thundering',
    'voiceless',
    'whispering',
    'bitter',
    'delicious',
    'fresh',
    'juicy',
    'ripe',
    'rotten',
    'salty',
    'sour',
    'spicy',
    'stale',
    'sticky',
    'strong',
    'sweet',
    'tasteless',
    'tasty',
    'thirsty',
    'fluttering',
    'fuzzy',
    'greasy',
    'grubby',
    'hard',
    'hot',
    'icy',
    'loose',
    'melted',
    'plastic',
    'prickly',
    'rainy',
    'rough',
    'scattered',
    'shaggy',
    'shaky',
    'sharp',
    'shivering',
    'silky',
    'slimy',
    'slippery',
    'smooth',
    'soft',
    'solid',
    'steady',
    'sticky',
    'tender',
    'tight',
    'uneven',
    'weak',
    'wet',
    'wooden',
    'afraid',
    'angry',
    'annoyed',
    'anxious',
    'arrogant',
    'ashamed',
    'awful',
    'bad',
    'bewildered',
    'bored',
    'combative',
    'condemned',
    'confused',
    'creepy',
    'cruel',
    'dangerous',
    'defeated',
    'defiant',
    'depressed',
    'disgusted',
    'disturbed',
    'eerie',
    'embarrassed',
    'envious',
    'evil',
    'fierce',
    'foolish',
    'frantic',
    'frightened',
    'grieving',
    'helpless',
    'homeless',
    'hungry',
    'hurt',
    'ill',
    'jealous',
    'lonely',
    'mysterious',
    'naughty',
    'nervous',
    'obnoxious',
    'outrageous',
    'panicky',
    'repulsive',
    'scary',
    'scornful',
    'selfish',
    'sore',
    'tense',
    'terrible',
    'thoughtless',
    'tired',
    'troubled',
    'upset',
    'uptight',
    'weary',
    'wicked',
    'worried',
    'agreeable',
    'amused',
    'brave',
    'calm',
    'charming',
    'cheerful',
    'comfortable',
    'cooperative',
    'courageous',
    'delightful',
    'determined',
    'eager',
    'elated',
    'enchanting',
    'encouraging',
    'energetic',
    'enthusiastic',
    'excited',
    'exuberant',
    'fair',
    'faithful',
    'fantastic',
    'fine',
    'friendly',
    'funny',
    'gentle',
    'glorious',
    'good',
    'happy',
    'healthy',
    'helpful',
    'hilarious',
    'jolly',
    'joyous',
    'kind',
    'lively',
    'lovely',
    'lucky',
    'obedient',
    'perfect',
    'pleasant',
    'proud',
    'relieved',
    'silly',
    'smiling',
    'splendid',
    'successful',
    'thoughtful',
    'victorious',
    'vivacious',
    'witty',
    'wonderful',
    'zealous',
    'zany',
    'other',
    'good',
    'new',
    'old',
    'great',
    'high',
    'small',
    'different',
    'large',
    'local',
    'social',
    'important',
    'long',
    'young',
    'national',
    'british',
    'right',
    'early',
    'possible',
    'big',
    'little',
    'political',
    'able',
    'late',
    'general',
    'full',
    'far',
    'low',
    'public',
    'available',
    'bad',
    'main',
    'sure',
    'clear',
    'major',
    'economic',
    'only',
    'likely',
    'real',
    'black',
    'particular',
    'international',
    'special',
    'difficult',
    'certain',
    'open',
    'whole',
    'white',
    'free',
    'short',
    'easy',
    'strong',
    'european',
    'central',
    'similar',
    'human',
    'common',
    'necessary',
    'single',
    'personal',
    'hard',
    'private',
    'poor',
    'financial',
    'wide',
    'foreign',
    'simple',
    'recent',
    'concerned',
    'american',
    'various',
    'close',
    'fine',
    'english',
    'wrong',
    'present',
    'royal',
    'natural',
    'individual',
    'nice',
    'french',
    'following',
    'current',
    'modern',
    'labour',
    'legal',
    'happy',
    'final',
    'red',
    'normal',
    'serious',
    'previous',
    'total',
    'prime',
    'significant',
    'industrial',
    'sorry',
    'dead',
    'specific',
    'appropriate',
    'top',
    'soviet',
    'basic',
    'military',
    'original',
    'successful',
    'aware',
    'hon',
    'popular',
    'heavy',
    'professional',
    'direct',
    'dark',
    'cold',
    'ready',
    'green',
    'useful',
    'effective',
    'western',
    'traditional',
    'scottish',
    'german',
    'independent',
    'deep',
    'interesting',
    'considerable',
    'involved',
    'physical',
    'left',
    'hot',
    'existing',
    'responsible',
    'complete',
    'medical',
    'blue',
    'extra',
    'past',
    'male',
    'interested',
    'fair',
    'essential',
    'beautiful',
    'civil',
    'primary',
    'obvious',
    'future',
    'environmental',
    'positive',
    'senior',
    'nuclear',
    'annual',
    'relevant',
    'huge',
    'rich',
    'commercial',
    'safe',
    'regional',
    'practical',
    'official',
    'separate',
    'key',
    'chief',
    'regular',
    'due',
    'additional',
    'active',
    'powerful',
    'complex',
    'standard',
    'impossible',
    'light',
    'warm',
    'middle',
    'fresh',
    'sexual',
    'front',
    'domestic',
    'actual',
    'united',
    'technical',
    'ordinary',
    'cheap',
    'strange',
    'internal',
    'excellent',
    'quiet',
    'soft',
    'potential',
    'northern',
    'religious',
    'quick',
    'very',
    'famous',
    'cultural',
    'proper',
    'broad',
    'joint',
    'formal',
    'limited',
    'conservative',
    'lovely',
    'usual',
    'ltd',
    'unable',
    'rural',
    'initial',
    'substantial',
    'christian',
    'bright',
    'average',
    'leading',
    'reasonable',
    'immediate',
    'suitable',
    'equal',
    'detailed',
    'working',
    'overall',
    'female',
    'afraid',
    'democratic',
    'growing',
    'sufficient',
    'scientific',
    'eastern',
    'correct',
    'inc',
    'irish',
    'expensive',
    'educational',
    'mental',
    'dangerous',
    'critical',
    'increased',
    'familiar',
    'unlikely',
    'double',
    'perfect',
    'slow',
    'tiny',
    'dry',
    'historical',
    'thin',
    'daily',
    'southern',
    'increasing',
    'wild',
    'alone',
    'urban',
    'empty',
    'married',
    'narrow',
    'liberal',
    'supposed',
    'upper',
    'apparent',
    'tall',
    'busy',
    'bloody',
    'prepared',
    'russian',
    'moral',
    'careful',
    'clean',
    'attractive',
    'japanese',
    'vital',
    'thick',
    'alternative',
    'fast',
    'ancient',
    'elderly',
    'rare',
    'external',
    'capable',
    'brief',
    'wonderful',
    'grand',
    'typical',
    'entire',
    'grey',
    'constant',
    'vast',
    'surprised',
    'ideal',
    'terrible',
    'academic',
    'funny',
    'minor',
    'pleased',
    'severe',
    'ill',
    'corporate',
    'negative',
    'permanent',
    'weak',
    'brown',
    'fundamental',
    'odd',
    'crucial',
    'inner',
    'used',
    'criminal',
    'contemporary',
    'sharp',
    'sick',
    'near',
    'roman',
    'massive',
    'unique',
    'secondary',
    'parliamentary',
    'african',
    'unknown',
    'subsequent',
    'angry',
    'alive',
    'guilty',
    'lucky',
    'enormous',
    'well',
    'communist',
    'yellow',
    'unusual',
    'net',
    'tough',
    'dear',
    'extensive',
    'glad',
    'remaining',
    'agricultural',
    'alright',
    'healthy',
    'italian',
    'principal',
    'tired',
    'efficient',
    'comfortable',
    'chinese',
    'relative',
    'friendly',
    'conventional',
    'willing',
    'sudden',
    'proposed',
    'voluntary',
    'slight',
    'valuable',
    'dramatic',
    'golden',
    'temporary',
    'federal',
    'keen',
    'flat',
    'silent',
    'indian',
    'worried',
    'pale',
    'statutory',
    'welsh',
    'dependent',
    'firm',
    'wet',
    'competitive',
    'armed',
    'radical',
    'outside',
    'acceptable',
    'sensitive',
    'living',
    'pure',
    'global',
    'emotional',
    'sad',
    'secret',
    'rapid',
    'adequate',
    'fixed',
    'sweet',
    'administrative',
    'wooden',
    'remarkable',
    'comprehensive',
    'surprising',
    'solid',
    'rough',
    'mere',
    'mass',
    'brilliant',
    'maximum',
    'absolute',
    'tory',
    'electronic',
    'visual',
    'electric',
    'cool',
    'spanish',
    'literary',
    'continuing',
    'supreme',
    'chemical',
    'genuine',
    'exciting',
    'written',
    'stupid',
    'advanced',
    'extreme',
    'classical',
    'fit',
    'favourite',
    'socialist',
    'widespread',
    'confident',
    'straight',
    'catholic',
    'proud',
    'numerous',
    'opposite',
    'distinct',
    'mad',
    'helpful',
    'given',
    'disabled',
    'consistent',
    'anxious',
    'nervous',
    'awful',
    'stable',
    'constitutional',
    'satisfied',
    'conscious',
    'developing',
    'strategic',
    'holy',
    'smooth',
    'dominant',
    'remote',
    'theoretical',
    'outstanding',
    'pink',
    'pretty',
    'clinical',
    'minimum',
    'honest',
    'impressive',
    'related',
    'residential',
    'extraordinary',
    'plain',
    'visible',
    'accurate',
    'distant',
    'still',
    'greek',
    'complicated',
    'musical',
    'precise',
    'gentle',
    'broken',
    'live',
    'silly',
    'fat',
    'tight',
    'monetary',
    'round',
    'psychological',
    'violent',
    'unemployed',
    'inevitable',
    'junior',
    'sensible',
    'grateful',
    'pleasant',
    'dirty',
    'structural',
    'welcome',
    'deaf',
    'above',
    'continuous',
    'blind',
    'overseas',
    'mean',
    'entitled',
    'delighted',
    'loose',
    'occasional',
    'evident',
    'desperate',
    'fellow',
    'universal',
    'square',
    'steady',
    'classic',
    'equivalent',
    'intellectual',
    'victorian',
    'level',
    'ultimate',
    'creative',
    'lost',
    'medieval',
    'clever',
    'linguistic',
    'convinced',
    'judicial',
    'raw',
    'sophisticated',
    'asleep',
    'vulnerable',
    'illegal',
    'outer',
    'revolutionary',
    'bitter',
    'changing',
    'australian',
    'native',
    'imperial',
    'strict',
    'wise',
    'informal',
    'flexible',
    'collective',
    'frequent',
    'experimental',
    'spiritual',
    'intense',
    'rational',
    'ethnic',
    'generous',
    'inadequate',
    'prominent',
    'logical',
    'bare',
    'historic',
    'modest',
    'dutch',
    'acute',
    'electrical',
    'valid',
    'weekly',
    'gross',
    'automatic',
    'loud',
    'reliable',
    'mutual',
    'liable',
    'multiple',
    'ruling',
    'curious',
    'arab',
    'sole',
    'jewish',
    'managing',
    'pregnant',
    'latin',
    'nearby',
    'exact',
    'underlying',
    'identical',
    'satisfactory',
    'marginal',
    'distinctive',
    'electoral',
    'urgent',
    'presidential',
    'controversial',
    'oral',
    'everyday',
    'encouraging',
    'organic',
    'continued',
    'expected',
    'statistical',
    'desirable',
    'innocent',
    'improved',
    'exclusive',
    'marked',
    'experienced',
    'unexpected',
    'superb',
    'sheer',
    'disappointed',
    'frightened',
    'gastric',
    'capitalist',
    'romantic',
    'naked',
    'reluctant',
    'magnificent',
    'convenient',
    'established',
    'closed',
    'uncertain',
    'artificial',
    'diplomatic',
    'tremendous',
    'marine',
    'mechanical',
    'retail',
    'institutional',
    'mixed',
    'required',
    'biological',
    'known',
    'functional',
    'straightforward',
    'superior',
    'digital',
    'spectacular',
    'unhappy',
    'confused',
    'unfair',
    'aggressive',
    'spare',
    'painful',
    'abstract',
    'asian',
    'associated',
    'legislative',
    'monthly',
    'intelligent',
    'hungry',
    'explicit',
    'nasty',
    'just',
    'faint',
    'coloured',
    'ridiculous',
    'amazing',
    'comparable',
    'successive',
    'realistic',
    'back',
    'decent',
    'unnecessary',
    'flying',
    'random',
    'influential',
    'dull',
    'genetic',
    'neat',
    'marvellous',
    'crazy',
    'damp',
    'giant',
    'secure',
    'bottom',
    'skilled',
    'subtle',
    'elegant',
    'brave',
    'lesser',
    'parallel',
    'steep',
    'intensive',
    'casual',
    'tropical',
    'lonely',
    'partial',
    'preliminary',
    'concrete',
    'alleged',
    'assistant',
    'vertical',
    'upset',
    'delicate',
    'mild',
    'occupational',
    'excessive',
    'progressive',
    'iraqi',
    'exceptional',
    'integrated',
    'striking',
    'continental',
    'okay',
    'harsh',
    'combined',
    'fierce',
    'handsome',
    'characteristic',
    'chronic',
    'compulsory',
    'interim',
    'objective',
    'splendid',
    'magic',
    'systematic',
    'obliged',
    'payable',
    'fun',
    'horrible',
    'primitive',
    'fascinating',
    'ideological',
    'metropolitan',
    'surrounding',
    'estimated',
    'peaceful',
    'premier',
    'operational',
    'technological',
    'kind',
    'advisory',
    'hostile',
    'precious',
    'gay',
    'accessible',
    'determined',
    'excited',
    'impressed',
    'provincial',
    'smart',
    'endless',
    'isolated',
    'drunk',
    'geographical',
    'like',
    'dynamic',
    'boring',
    'forthcoming',
    'unfortunate',
    'definite',
    'super',
    'notable',
    'indirect',
    'stiff',
    'wealthy',
    'awkward',
    'lively',
    'neutral',
    'artistic',
    'content',
    'mature',
    'colonial',
    'ambitious',
    'evil',
    'magnetic',
    'verbal',
    'legitimate',
    'sympathetic',
    'empirical',
    'head',
    'shallow',
    'vague',
    'naval',
    'depressed',
    'shared',
    'added',
    'shocked',
    'mid',
    'worthwhile',
    'qualified',
    'missing',
    'blank',
    'absent',
    'favourable',
    'polish',
    'israeli',
    'developed',
    'profound',
    'representative',
    'enthusiastic',
    'dreadful',
    'rigid',
    'reduced',
    'cruel',
    'coastal',
    'peculiar',
    'racial',
    'ugly',
    'swiss',
    'crude',
    'extended',
    'selected',
    'eager',
    'feminist',
    'canadian',
    'bold',
    'relaxed',
    'corresponding',
    'running',
    'planned',
    'applicable',
    'immense',
    'allied',
    'comparative',
    'uncomfortable',
    'conservation',
    'productive',
    'beneficial',
    'bored',
    'charming',
    'minimal',
    'mobile',
    'turkish',
    'orange',
    'rear',
    'passive',
    'suspicious',
    'overwhelming',
    'fatal',
    'resulting',
    'symbolic',
    'registered',
    'neighbouring',
    'calm',
    'irrelevant',
    'patient',
    'compact',
    'profitable',
    'rival',
    'loyal',
    'moderate',
    'distinguished',
    'interior',
    'noble',
    'insufficient',
    'eligible',
    'mysterious',
    'varying',
    'managerial',
    'molecular',
    'olympic',
    'linear',
    'prospective',
    'printed',
    'parental',
    'diverse',
    'elaborate',
    'furious',
    'fiscal',
    'burning',
    'useless',
    'semantic',
    'embarrassed',
    'inherent',
    'philosophical',
    'deliberate',
    'awake',
    'variable',
    'promising',
    'unpleasant',
    'varied',
    'sacred',
    'selective',
    'inclined',
    'tender',
    'hidden',
    'worthy',
    'intermediate',
    'sound',
    'protective',
    'fortunate',
    'slim',
    'islamic',
    'defensive',
    'divine',
    'stuck',
    'driving',
    'invisible',
    'misleading',
    'circular',
    'mathematical',
    'inappropriate',
    'liquid',
    'persistent',
    'solar',
    'doubtful',
    'manual',
    'architectural',
    'intact',
    'incredible',
    'devoted',
    'prior',
    'tragic',
    'respectable',
    'optimistic',
    'convincing',
    'unacceptable',
    'decisive',
    'competent',
    'spatial',
    'respective',
    'binding',
    'relieved',
    'nursing',
    'toxic',
    'select',
    'redundant',
    'integral',
    'then',
    'probable',
    'amateur',
    'fond',
    'passing',
    'specified',
    'territorial',
    'horizontal',
    'inland',
    'cognitive',
    'regulatory',
    'miserable',
    'resident',
    'polite',
    'scared',
    'marxist',
    'gothic',
    'civilian',
    'instant',
    'lengthy',
    'adverse',
    'korean',
    'unconscious',
    'anonymous',
    'aesthetic',
    'orthodox',
    'static',
    'unaware',
    'costly',
    'fantastic',
    'foolish',
    'fashionable',
    'causal',
    'compatible',
    'wee',
    'implicit',
    'dual',
    'ok',
    'cheerful',
    'subjective',
    'forward',
    'surviving',
    'exotic',
    'purple',
    'cautious',
    'visiting',
    'aggregate',
    'ethical',
    'protestant',
    'teenage',
    'dying',
    'disastrous',
    'delicious',
    'confidential',
    'underground',
    'thorough',
    'grim',
    'autonomous',
    'atomic',
    'frozen',
    'colourful',
    'injured',
    'uniform',
    'ashamed',
    'glorious',
    'wicked',
    'coherent',
    'rising',
    'shy',
    'novel',
    'balanced',
    'delightful',
    'arbitrary',
    'adjacent',
    'psychiatric',
    'worrying',
    'weird',
    'unchanged',
    'rolling',
    'evolutionary',
    'intimate',
    'sporting',
    'disciplinary',
    'formidable',
    'lexical',
    'noisy',
    'gradual',
    'accused',
    'homeless',
    'supporting',
    'coming',
    'renewed',
    'excess',
    'retired',
    'rubber',
    'chosen',
    'outdoor',
    'embarrassing',
    'preferred',
    'bizarre',
    'appalling',
    'agreed',
    'imaginative',
    'governing',
    'accepted',
    'vocational',
    'palestinian',
    'mighty',
    'puzzled',
    'worldwide',
    'handicapped',
    'organisational',
    'sunny',
    'eldest',
    'eventual',
    'spontaneous',
    'vivid',
    'rude',
    'faithful',
    'ministerial',
    'innovative',
    'controlled',
    'conceptual',
    'unwilling',
    'civic',
    'meaningful',
    'disturbing',
    'alive',
    'brainy',
    'breakable',
    'busy',
    'careful',
    'cautious',
    'clever',
    'concerned',
    'crazy',
    'curious',
    'dead',
    'different',
    'difficult',
    'doubtful',
    'easy',
    'famous',
    'fragile',
    'helpful',
    'helpless',
    'important',
    'impossible',
    'innocent',
    'inquisitive',
    'modern',
    'open',
    'outstanding',
    'poor',
    'powerful',
    'puzzled',
    'real',
    'rich',
    'shy',
    'sleepy',
    'stupid',
    'super',
    'tame',
    'uninterested',
    'wandering',
    'wild',
    'wrong',
    'adorable',
    'alert',
    'average',
    'beautiful',
    'blonde',
    'bloody',
    'blushing',
    'bright',
    'clean',
    'clear',
    'cloudy',
    'colorful',
    'crowded',
    'cute',
    'dark',
    'drab',
    'distinct',
    'dull',
    'elegant',
    'fancy',
    'filthy',
    'glamorous',
    'gleaming',
    'graceful',
    'grotesque',
    'homely',
    'light',
    'misty',
    'motionless',
    'muddy',
    'plain',
    'poised',
    'quaint',
    'shiny',
    'smoggy',
    'sparkling',
    'spotless',
    'stormy',
    'strange',
    'ugly',
    'unsightly',
    'unusual',
    'bad',
    'better',
    'beautiful',
    'big',
    'black',
    'blue',
    'bright',
    'clumsy',
    'crazy',
    'dizzy',
    'dull',
    'fat',
    'frail',
    'friendly',
    'funny',
    'great',
    'green',
    'gigantic',
    'gorgeous',
    'grumpy',
    'handsome',
    'happy',
    'horrible',
    'itchy',
    'jittery',
    'jolly',
    'kind',
    'long',
    'lazy',
    'magnificent',
    'magenta',
    'many',
    'mighty',
    'mushy',
    'nasty',
    'new',
    'nice',
    'nosy',
    'nutty',
    'nutritious',
    'odd',
    'orange',
    'ordinary',
    'pretty',
    'precious',
    'prickly',
    'purple',
    'quaint',
    'quiet',
    'quick',
    'quickest',
    'rainy',
    'rare',
    'ratty',
    'red',
    'roasted',
    'robust',
    'round',
    'sad',
    'scary',
    'scrawny',
    'short',
    'silly',
    'stingy',
    'strange',
    'striped',
    'spotty',
    'tart',
    'tall',
    'tame',
    'tan',
    'tender',
    'testy',
    'tricky',
    'tough',
    'ugly',
    'ugliest',
    'vast',
    'watery',
    'wasteful',
    'wonderful',
    'yellow',
    'yummy',
    'zany',
]

RIGHT = [
    'albattani',
    'allen',
    'almeida',
    'agnesi',
    'archimedes',
    'ardinghelli',
    'aryabhata',
    'austin',
    'babbage',
    'banach',
    'bardeen',
    'bartik',
    'bassi',
    'beaver',
    'bell',
    'benz',
    'bhabha',
    'bhaskara',
    'blackwell',
    'bohr',
    'booth',
    'borg',
    'bose',
    'boyd',
    'brahmagupta',
    'brattain',
    'brown',
    'carson',
    'chandrasekhar',
    'shannon',
    'clarke',
    'colden',
    'cori',
    'cray',
    'curran',
    'curie',
    'darwin',
    'davinci',
    'dijkstra',
    'dubinsky',
    'easley',
    'edison',
    'einstein',
    'elion',
    'engelbart',
    'euclid',
    'euler',
    'fermat',
    'fermi',
    'feynman',
    'franklin',
    'galileo',
    'gates',
    'goldberg',
    'goldstine',
    'goldwasser',
    'golick',
    'goodall',
    'haibt',
    'hamilton',
    'hawking',
    'heisenberg',
    'hermann',
    'heyrovsky',
    'hodgkin',
    'hoover',
    'hopper',
    'hugle',
    'hypatia',
    'jackson',
    'jang',
    'jennings',
    'jepsen',
    'johnson',
    'joliot',
    'jones',
    'kalam',
    'kare',
    'keller',
    'kepler',
    'khorana',
    'kilby',
    'kirch',
    'knuth',
    'kowalevski',
    'lalande',
    'lamarr',
    'lamport',
    'leakey',
    'leavitt',
    'lewin',
    'lichterman',
    'liskov',
    'lovelace',
    'lumiere',
    'mahavira',
    'mayer',
    'mccarthy',
    'mcclintock',
    'mclean',
    'mcnulty',
    'meitner',
    'meninsky',
    'mestorf',
    'minsky',
    'mirzakhani',
    'morse',
    'murdock',
    'neumann',
    'newton',
    'nightingale',
    'nobel',
    'noether',
    'northcutt',
    'noyce',
    'panini',
    'pare',
    'pasteur',
    'payne',
    'perlman',
    'pike',
    'poincare',
    'poitras',
    'ptolemy',
    'raman',
    'ramanujan',
    'ride',
    'montalcini',
    'ritchie',
    'roentgen',
    'rosalind',
    'saha',
    'sammet',
    'shaw',
    'shirley',
    'shockley',
    'sinoussi',
    'snyder',
    'spence',
    'stallman',
    'stonebraker',
    'swanson',
    'swartz',
    'swirles',
    'tesla',
    'thompson',
    'torvalds',
    'turing',
    'varahamihira',
    'visvesvaraya',
    'volhard',
    'wescoff',
    'wiles',
    'williams',
    'wilson',
    'wing',
    'wozniak',
    'wright',
    'yalow',
    'yonath',
    'canidae',
    'felidae',
    'cat',
    'cattle',
    'dog',
    'donkey',
    'goat',
    'horse',
    'pig',
    'rabbit',
    'aardvark',
    'aardwolf',
    'albatross',
    'alligator',
    'alpaca',
    'amphibian',
    'anaconda',
    'angelfish',
    'anglerfish',
    'ant',
    'anteater',
    'antelope',
    'antlion',
    'ape',
    'aphid',
    'armadillo',
    'asp',
    'baboon',
    'badger',
    'bandicoot',
    'barnacle',
    'barracuda',
    'basilisk',
    'bass',
    'bat',
    'bear',
    'beaver',
    'bedbug',
    'bee',
    'beetle',
    'bird',
    'bison',
    'blackbird',
    'boa',
    'boar',
    'bobcat',
    'bobolink',
    'bonobo',
    'booby',
    'bovid',
    'bug',
    'butterfly',
    'buzzard',
    'camel',
    'canid',
    'capybara',
    'cardinal',
    'caribou',
    'carp',
    'cat',
    'catshark',
    'caterpillar',
    'catfish',
    'cattle',
    'centipede',
    'cephalopod',
    'chameleon',
    'cheetah',
    'chickadee',
    'chicken',
    'chimpanzee',
    'chinchilla',
    'chipmunk',
    'clam',
    'clownfish',
    'cobra',
    'cockroach',
    'cod',
    'condor',
    'constrictor',
    'coral',
    'cougar',
    'cow',
    'coyote',
    'crab',
    'crane',
    'crawdad',
    'crayfish',
    'cricket',
    'crocodile',
    'crow',
    'cuckoo',
    'cicada',
    'damselfly',
    'deer',
    'dingo',
    'dinosaur',
    'dog',
    'dolphin',
    'donkey',
    'dormouse',
    'dove',
    'dragonfly',
    'dragon',
    'duck',
    'eagle',
    'earthworm',
    'earwig',
    'echidna',
    'eel',
    'egret',
    'elephant',
    'elk',
    'emu',
    'ermine',
    'falcon',
    'ferret',
    'finch',
    'firefly',
    'fish',
    'flamingo',
    'flea',
    'fly',
    'flyingfish',
    'fowl',
    'fox',
    'frog',
    'gamefowl',
    'galliform',
    'gazelle',
    'gecko',
    'gerbil',
    'gibbon',
    'giraffe',
    'goat',
    'goldfish',
    'goose',
    'gopher',
    'gorilla',
    'grasshopper',
    'grouse',
    'guan',
    'guanaco',
    'guineafowl',
    'gull',
    'guppy',
    'haddock',
    'halibut',
    'hamster',
    'hare',
    'harrier',
    'hawk',
    'hedgehog',
    'heron',
    'herring',
    'hippopotamus',
    'hookworm',
    'hornet',
    'horse',
    'hoverfly',
    'hummingbird',
    'hyena',
    'iguana',
    'impala',
    'jackal',
    'jaguar',
    'jay',
    'jellyfish',
    'junglefowl',
    'kangaroo',
    'kingfisher',
    'kite',
    'kiwi',
    'koala',
    'koi',
    'krill',
    'ladybug',
    'lamprey',
    'landfowl',
    'lark',
    'leech',
    'lemming',
    'lemur',
    'leopard',
    'leopon',
    'limpet',
    'lion',
    'lizard',
    'llama',
    'lobster',
    'locust',
    'loon',
    'louse',
    'lungfish',
    'lynx',
    'macaw',
    'mackerel',
    'magpie',
    'mammal',
    'manatee',
    'mandrill',
    'marlin',
    'marmoset',
    'marmot',
    'marsupial',
    'marten',
    'mastodon',
    'meadowlark',
    'meerkat',
    'mink',
    'minnow',
    'mite',
    'mockingbird',
    'mole',
    'mollusk',
    'mongoose',
    'monkey',
    'moose',
    'mosquito',
    'moth',
    'mouse',
    'mule',
    'muskox',
    'narwhal',
    'newt',
    'nightingale',
    'ocelot',
    'octopus',
    'opossum',
    'orangutan',
    'orca',
    'ostrich',
    'otter',
    'owl',
    'ox',
    'panda',
    'panther',
    'parakeet',
    'parrot',
    'parrotfish',
    'partridge',
    'peacock',
    'peafowl',
    'pelican',
    'penguin',
    'perch',
    'pheasant',
    'pig',
    'pigeon',
    'pike',
    'pinniped',
    'piranha',
    'planarian',
    'platypus',
    'pony',
    'porcupine',
    'porpoise',
    'possum',
    'prawn',
    'primate',
    'ptarmigan',
    'puffin',
    'puma',
    'python',
    'quail',
    'quelea',
    'quokka',
    'rabbit',
    'raccoon',
    'rat',
    'rattlesnake',
    'raven',
    'reindeer',
    'reptile',
    'rhinoceros',
    'roadrunner',
    'rodent',
    'rook',
    'rooster',
    'roundworm',
    'sailfish',
    'salamander',
    'salmon',
    'sawfish',
    'scallop',
    'scorpion',
    'seahorse',
    'shark',
    'sheep',
    'shrew',
    'shrimp',
    'silkworm',
    'silverfish',
    'skink',
    'skunk',
    'sloth',
    'slug',
    'smelt',
    'snail',
    'snake',
    'snipe',
    'sole',
    'sparrow',
    'spider',
    'spoonbill',
    'squid',
    'squirrel',
    'starfish',
    'stingray',
    'stoat',
    'stork',
    'sturgeon',
    'swallow',
    'swan',
    'swift',
    'swordfish',
    'swordtail',
    'tahr',
    'takin',
    'tapir',
    'tarantula',
    'tarsier',
    'termite',
    'tern',
    'thrush',
    'tick',
    'tiger',
    'tiglon',
    'toad',
    'tortoise',
    'toucan',
    'trout',
    'tuna',
    'turkey',
    'turtle',
    'tyrannosaurus',
    'urial',
    'vicuna',
    'viper',
    'vole',
    'vulture',
    'wallaby',
    'walrus',
    'wasp',
    'warbler',
    'weasel',
    'whale',
    'whippet',
    'whitefish',
    'wildcat',
    'wildebeest',
    'wildfowl',
    'wolf',
    'wolverine',
    'wombat',
    'woodpecker',
    'worm',
    'wren',
    'xerinae',
    'yak',
    'zebra',
    'alpaca',
    'cat',
    'cattle',
    'chicken',
    'dog',
    'donkey',
    'ferret',
    'gayal',
    'goldfish',
    'guppy',
    'horse',
    'koi',
    'llama',
    'sheep',
    'yak',
    'unicorn',
]


class NameGenerator(object):
    def __init__(self, sep=''):
        self.sep = sep
        self.length = 12

    def get(self, only_name=False):
        r = random.SystemRandom()

        left = ""
        if not only_name:
            left = r.choice(LEFT).title()

        right = r.choice(RIGHT).title()
        name = '%s%s%s' % (left, self.sep, right)
        return name[:self.length]
