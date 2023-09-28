class Place:
    bilabial = 'bilabial'
    labiodental = 'labiodental'
    dental = 'dental'
    alveolar = 'alveolar'
    alveopalatal = 'alveopalatal'
    retroflex = 'retroflex'
    palatal = 'palatal'
    velar = 'velar'
    uvular = 'uvular'
    pharyngeal = 'pharyngeal'
    glottal = 'glottal'

class Manner:
    plosive = 'plosive'
    nasal = 'nasal'
    trill = 'trill'
    tap = 'tap'
    fricative = 'fricative'
    lateral_fricative = 'lateral fricative'
    approximant = 'approximant'
    lateral_approximant = 'lateral approximant'

class Voice:
    voiced = 'voiced'
    unvoiced = 'unvoiced'

class Rounding:
    rounded = 'rounded'
    unrounded = 'unrounded'

class Height:
    close = 'close'
    near_close = 'near-close'
    close_mid = 'close-mid'
    mid = 'mid'
    open_mid = 'open-mid'
    near_open = 'near-open'
    open = 'open'

class Frontness:
    front = 'front'
    central = 'central'
    back = 'back'

class Phoneme:

    def __init__(self, symbol: str) -> None:
        self.symbol = symbol

    def __repr__(self) -> str:
        return self.symbol

class Consonant(Phoneme):

    def __init__(self, symbol, place, manner, voice):
        super().__init__(symbol)
        self.place = place
        self.manner = manner
        self.voice = voice

    def description(self) -> str:
        return f'{self.voice} {self.place} {self.manner}'

class Vowel(Phoneme):

    def __init__(self, symbol, rounding, height, frontness):
        super().__init__(symbol)
        self.rounding = rounding
        self.height = height
        self.frontness = frontness

    def description(self) -> str:
        return f'{self.voice} {self.place} {self.manner}'
