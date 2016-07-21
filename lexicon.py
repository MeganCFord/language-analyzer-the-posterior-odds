lexicon = {
    "domain":
    {
      "financial": ["money", "cash", "dollar", "loan", "pay", "buy", "purchase", "get", "acquire",
        "sell", "sale", "trade", "rent", "mortgage", "rate", "invest", "devest", "lose", "gain",
        "total", "divide", "subtract", "add", "check", "bill", "debt", "landlord", "earn", "owe",
        "stock", "bond"],
      "behavioral": ["acting","behavior", "do","crazy","make", "made", "cook", "eat", "ate", "date", "go", "play", "see", "watch",
        "be", "relax", "sit", "run", "sick", "get", "plan", "day", "night", "sun", "moon", "goal", "reward",
        "punishment", "bad", "taste", "good", "done", "did", "prefer", "like", "hate", "loan", "pay",
        "buy", "desire", "want"],

      "scientific": ['animals', 'science', 'scientific','fact', 'biology','life', 'plants', 'frogs', 'aliens', 'planets', 'discect', 'living', 'matter', 'atoms', 'engineering', 'engineer', 'make', 'build', 'create', 'robot', 'function', 'machine', 'bits'],
      "educational": ['instruction', 'smart', 'learning','direction', 'mentor', 'learn', 'teach', 'study', 'knowledge', 'practice', 'skill', 'guidance', 'scholarship', 'improvement', 'enlightnement', 'coaching', 'nurture', 'lead', 'guide', 'discipline' ],
      "politics": ['people', 'leader', 'govern', 'law', 'policy', 'rights', 'protest', 'legal', 'candidate', 'election', 'republican', 'democtratic', 'justice', 'tax', 'taxes', 'debate', 'congress', 'political', 'president', 'rules'],
      "relationships": ['people', 'family', 'mother', 'father', 'dad', 'mom', 'brother', 'sister', 'cousin', 'relative', 'relational', 'friend', 'friendship', 'husband', 'wife', 'boyfriend', 'girlfriend','fiance', 'lover', 'colleague', 'enemies', 'enemy', 'talk', 'talking', 'converse', 'relate', 'meet', 'meeting', 'club', 'connection', 'connect', 'bridge', 'link']
    },
    "emotion":
    {
      "disgust": {
        "positive_words": ['eating', 'muscles', 'newborn', 'gas', 'sweat', 'cake', 'toothpaste', 'underwear', 'comedy', 'rain', 'hottubs', 'blood', 'toilet', 'crumbs', 'soda', 'jail', 'uncle', 'van', 'bugs', 'kissing', 'wrinkles', 'beans' ],
        "negative_words": ["idiot", "sick", "annoy", "bad", "gross", "disgust", "awful", "vomit",
          "cannibal", "carcass", "rot", "dislike", "hate", "worthless", "weird", "ugly", "trash",
          "toxic", "terrible", "vulgar"]
      },
      "fear": {
        "positive_words": ["alertness", "armed", "attorney", "birth", "cash", "cautious", "compassion",
        "defend", "destination", "flying", "holiness"],
        "negative_words": ["abandon", "abduction", "absence", "abyss", "accident", "afraid", "wrath",
        "victim", "unknown", "tyrant", "terrorize", "surveillance", "superstitious"]
      },
      "anger": {
        "positive_words": ["yell", "awful", "insult"],
        "negative_words": ["hate", "anger", "angry", "mad", "enemy", "yell", "scream", "wrong", "wreck", "awful",
          "terrible", "idiot", "stupid", "dumb", "hostile", "insult", "resent"]
      },
      "happy": {
        "positive_words": ['biscuit','flower','nice', 'blankets', 'shoes', 'air', 'toilet', 'machines', 'soap', 'canoe', 'beer', 'electricity', 'moonlight', 'sunshine', 'music', 'family', 'vacation', 'beach', 'trip', 'hike', 'love', 'like', 'partner', 'cheer', 'yum', 'drinks', 'food', 'happy', 'happiness', 'chocolate', 'dream', 'snuggle', 'money', 'new', 'puppy', 'baby', 'light', 'grass', 'magical', 'cheerful', 'content', 'delight', 'ecstatic', 'elated', 'glad', 'joyous', 'jubilant', 'lively', 'merry', 'overjoy', 'peaceful', 'pleased', 'thrilled', 'upbeat', 'blissful', 'blithe', 'captivated', 'chipper', 'chirper', 'content', 'convivial', 'content', 'exhultant', 'gay', 'gleeful', 'gratify', 'intoxicated', 'jolly', 'laughing', 'light', 'mirthful', 'peppy', 'perky', 'playful', 'sparkling', 'sunny', 'tickling', 'up', 'hopeful', 'mom', 'dad', 'candy', 'cake', 'jewelry', 'books', 'flips', 'teal', 'colors', 'soda', 'friends'],
        "negative_words": ['sympatheitc', 'food', 'overjoy', 'cake', 'candy', 'glitter', 'confetti', 'muscles', 'mother-in-law', 'tights', 'high-heels', 'hair-dye', 'gas', 'school', 'choker', 'peace-sign', 'pink', 'alcohol', 'drugs', 'buttons', 'hair', 'glasses', 'mountains', 'wheelchairs', 'exercise', 'halloween', 'cheese', 'meat', 'scissors', 'toothpicks', 'microwave', 'plastic', 'hottub', 'heat']
      },
      "sad": {
        "positive_words": ['ovation', 'overload', 'overwhelmed', 'hymns', 'prayer', 'instructions', 'oil', 'rain', 'sidewalk', 'moles', 'jeans', 'swimsuit', 'tears', 'rabbithole', 'cartoons', 'spanking', 'home', 'christmas', 'holidays', 'old', 'memory', 'memories', 'photos', 'relatives', 'capstone', 'jobs'],
        "negative_words": ['absent', 'abysmal', 'alienated', 'annulment', 'apthetic', 'badly', 'barren', 'bleak', 'boredom', 'cancel', 'chronic', 'clouded', 'crippled', 'cry', 'crying', 'cumbersome', 'damages', 'debt', 'deceased', 'defeated', 'defunct', 'delirious', 'denied', 'departed', 'depression', 'detention', 'difficulties', 'diminish', 'disability', 'disappointing', 'disapproval', 'discomfort', 'disconnected', 'disheartened', 'disheartening', 'dispel', 'disqualify', 'distraught', 'dreary', 'embarrass', 'embarrassed', 'error', 'evict', 'excluding', 'exhausting', 'exhausted', 'expire', 'extinct', 'faithless', 'fall', 'falling', 'famine', 'fatigued', 'fault', 'feeble', 'fell', 'flaw', 'forbid', 'forsake', 'fraility', 'frayed', 'frown', 'fruitless', 'funk', 'futile', 'geriatric', 'gloom', 'gloomy', 'glum', 'grief', 'handicap', 'hardship', 'heartache', 'heartless', 'hindering', 'hobo', 'hollow', 'homesick', 'impossible', 'imprudent', 'inability', 'inadequate', 'inefficient', 'infamy', 'inferior', 'infertility', 'inhospitable', 'interrupted', 'isolation', 'labored', 'late', 'lethargy', 'listless', 'lonesome', 'lost', 'lowest', 'lowly', 'meaningless', 'melancholic', 'melancholy', 'meltdown', 'miserably', 'misrepresent', 'mistake', 'monsoon','mourn', 'mourning', 'negative', 'nonsensical', 'nothingness', 'numbness', 'obituary', 'overload', 'overwhelmed', 'painfully', 'painful', 'perished', 'perplexity', 'pine', 'pointless', 'posthumous', 'rack', 'refused', 'regret', 'regrettable', 'regretted', 'regretting', 'remorse', 'repress', 'resigned', 'restrict', 'rue', 'rumor', 'runaway', 'sadly', 'sap', 'scarcely', 'secluded', 'sequestration', 'setback', 'shameful', 'shattered', 'sluggish', 'slump', 'sob', 'somber', 'sorely', 'sorrowful', 'splitting', 'spoiler', 'sprain', 'stagnant', 'sterile', 'stillborn', 'strip', 'subjected', 'surrendering', 'taint', 'tax', 'termination', 'tough', 'unable', 'unacceptable', 'uneducated', 'undesirable', 'undesired', 'uneducated', 'unfortunate', 'ungodly', 'unhappiness', 'unimportant', 'uninspired', 'uninterested', 'uninteresting', 'unrequited', 'unsuccesful', 'untitled', 'unwelcome', 'unwell']
      }
    }
  }

