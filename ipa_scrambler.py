class Place:
    bilabial = 'bilabial'
    labiodental = 'labiodental'
    dental = 'dental'
    alveolar = 'alveolar'
    postalveolar = 'postalveolar'
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

class Consonant:
    def __init__(self, symbol, place, manner, voice):
        self.symbol = symbol
        self.name = name
        self.place = place
        self.manner = manner
        self.voice = voice

p = Place
m = Manner
v = Voice
c = Consonant

cs = [
    c('p', p.bilabial, m.plosive, v.voiced),
    c('b', p.bilabial, m.plosive, v.unvoiced),
    c('m', p.bilabial, m.nasal, v.voiced),
    c('ʙ', p.bilabial, m.trill, v.voiced),
    c('ɸ', p.bilabial, m.fricative, v.unvoiced),
    c('β', p.bilabial, m.fricative, v.voiced),
    c('ɱ', ),
    c('f', ),
    c('v', ),
    c('n', ),
    c('t', ),
    c('d', ),
    c('s', ),
    c('z', ),
    c('ɹ', ),
    c('ɾ', ),
    c('r', ),
    c('ɬ', ),
    c('ɮ', ),
    c('l', ),
    c('ʃ', ),
    c('ʒ', ),
    c('ɲ', ),
    c('c', ),
    c('ɟ', ),
    c('ɕ', ),
    c('ʑ', ),
    c('j', ),
    c('ŋ', ),
    c('k', ),
    c('ɡ', ),
    c('x', ),
    c('ɣ', ),
    c('ɴ', ),
    c('q', ),
    c('ɢ', ),
    c('χ', ),
    c('ʁ', ),
    c('ʀ', ),
    c('ʔ', ),
    c('ʕ', ),
    c('h', ),
]
