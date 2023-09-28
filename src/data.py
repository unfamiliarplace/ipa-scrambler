from lib import Place as p
from lib import Manner as m
from lib import Voice as v

from lib import Rounding as r
from lib import Height as h
from lib import Frontness as f

from lib import Phoneme as P
from lib import Vowel as V
from lib import Consonant as C

# Data

cs = [
    C('p', p.bilabial, m.plosive, v.voiced),
    C('b', p.bilabial, m.plosive, v.unvoiced),
    C('m', p.bilabial, m.nasal, v.voiced),
    C('ʙ', p.bilabial, m.trill, v.voiced),
    C('ɸ', p.bilabial, m.fricative, v.unvoiced),
    C('β', p.bilabial, m.fricative, v.voiced),
    C('ɱ', p.labiodental, m.nasal, v.voiced),
    C('f', p.labiodental, m.fricative, v.unvoiced),
    C('v', p.labiodental, m. fricative, v.unvoiced),
    C('n', p.alveolar, m.nasal, v.voiced),
    C('t', p.alveolar, m.plosive, v.unvoiced),
    C('d', p.alveolar, m.plosive, v.voiced),
    C('s', p.alveolar, m.fricative, v.unvoiced),
    C('z', p.alveolar, m.fricative, v.voiced),
    C('ɹ', p.alveolar, m.approximant, v.voiced),
    C('ɾ', p.alveolar, m.tap, v.voiced),
    C('r', p.alveolar, m.trill, v.voiced),
    C('θ', p.dental, m.fricative, v.unvoiced),
    C('ð', p.dental, m.fricative, v.voiced),
    C('ɬ', p.alveolar, m.lateral_fricative, v.unvoiced),
    C('ɮ', p.alveolar, m.lateral_fricative, v.voiced),
    C('l', p.alveolar, m.lateral_approximant, v.voiced),
    C('ʃ', p.alveopalatal, m.fricative, v.unvoiced),
    C('ʒ', p. alveopalatal, m.fricative, v.voiced),
    C('ɲ', p.palatal, m.nasal, v.voiced),
    C('c', p.alveopalatal, m.plosive, v.unvoiced),
    C('ɟ', p.alveopalatal, m.plosive, v.voiced),
    C('ɕ', p.alveopalatal, m.fricative, v.unvoiced),
    C('ʑ', p.alveopalatal, m.fricative, v.unvoiced),
    C('j', p.palatal, m.approximant, v.voiced),
    C('ŋ', p.velar, m.nasal, v.voiced),
    C('k', p.velar, m.plosive, v.unvoiced),
    C('ɡ', p.velar, m.plosive, v.voiced),
    C('x', p.velar, m.fricative, v.unvoiced),
    C('ɣ', p.velar, m.fricative, v.voiced),
    C('ɴ', p.uvular, m.nasal, v.voiced),
    C('q', p.uvular, m.plosive, v.unvoiced),
    C('ɢ', p.uvular, m.plosive, v.voiced),
    C('χ', p.uvular, m.fricative, v.unvoiced),
    C('ʁ', p.uvular, m.fricative, v.voiced),
    C('ʀ', p.uvular, m.trill, v.voiced),
    C('ʔ', p.glottal, m.plosive, v.unvoiced),
    C('ʕ', p.pharyngeal, m.plosive, v.voiced),
    C('h', p.glottal, m.fricative, v.voiced),
]

vs = [
    V('i', r.unrounded, h.close, f.front),
    V('y', r.rounded, h.close, f.front),
    V('ɪ', r.unrounded, h.near_close, f.front),
    V('ʏ', r.rounded, h.near_close, f.front),
    V('e', r.unrounded, h.close_mid, f.front),
    V('ø', r.rounded, h.close_mid, f.front),
    V('ɛ', r.unrounded, h.open_mid, f.front),
    V('œ', r.rounded, h.open_mid, f.front),
    V('æ', r.unrounded, h.near_open, f.front),
    V('a', r.unrounded, h.open, f.front),
    V('œ', r.rounded, h.open, f.front),
    V('ɨ', r.unrounded, h.close, f.central),
    V('ʉ', r.rounded, h.close, f.central),
    V('ɘ', r.unrounded, h.close_mid, f.central),
    V('ɵ', r.rounded, h.close_mid, f.central),
    V('ə', r.unrounded, h.mid, f.central),
    V('ɜ', r.unrounded, h.open_mid, f.central),
    V('ɞ', r.rounded, h.open_mid, f.central),
    V('ɐ', r.unrounded, h.near_open, f.central),
    V('ɯ', r.unrounded, h.close, f.back),
    V('u', r.rounded, h.close, f.back),
    V('ʊ', r.rounded, h.near_close, f.back),
    V('ɤ', r.unrounded, h.close_mid, f.back),
    V('o', r.rounded, h.close_mid, f.back),
    V('ʌ', r.unrounded, h.open_mid, f.back),
    V('ɔ', r.rounded, h.open_mid, f.back),
    V('ɑ', r.unrounded, h.open, f.back),
    V('ɒ', r.rounded, h.open, f.back)
]

ps = cs + vs
