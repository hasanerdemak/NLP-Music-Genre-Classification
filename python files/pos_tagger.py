from jpype import JClass, getDefaultJVMPath, shutdownJVM, startJVM, isJVMStarted, java
from enum import Enum

class POSTag(Enum):
    Noun = 1  # Noun
    Adj = 2  # Adjective
    Adv = 3  # Adverb
    Conj = 4  # Conjunction
    Interj = 5  # Interjection
    Verb = 6  # Verb
    Pron = 7  # Pronoun
    Num = 8  # Numeral
    Det = 9  # Determiner
    Postp = 10  # PostPositive
    Ques = 11  # Question
    Dup = 12  # Duplicator
    Punc = 13  # Punctution
    Unk = 14  # Unknown

ZEMBEREK_PATH = r'../libraries/zemberek-full.jar'
if not isJVMStarted():
    startJVM(getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

TurkishMorphology = JClass('zemberek.morphology.TurkishMorphology')
morphology = TurkishMorphology.createWithDefaults()

def get_pos_tags(sentence):
    analysis: java.util.ArrayList = (morphology.analyzeAndDisambiguate(sentence).bestAnalysis())

    pos_list = []
    for i, analysis in enumerate(analysis, start=1):
        #pos.append(f'\nAnalysis {i}: {analysis}')# + f'\nPrimary POS {i}: {analysis.getPos()}' + f'\nPrimary POS (Short Form) {i}: {analysis.getPos().shortForm}')
        pos_list.append(analysis.getPos().shortForm)
    
    return pos_list

def get_words_and_pos_tag_tuples(sentence):
    analysis: java.util.ArrayList = (morphology.analyzeAndDisambiguate(sentence).bestAnalysis())

    word_pos_tuples_list = []
    for i, analysis in enumerate(analysis, start=1):
        #pos.append(f'\nAnalysis {i}: {analysis}')# + f'\nPrimary POS {i}: {analysis.getPos()}' + f'\nPrimary POS (Short Form) {i}: {analysis.getPos().shortForm}')
        word_pos_tuples_list.append((f'{analysis.surfaceForm()}', f'{analysis.getPos().shortForm}'))
    
    return word_pos_tuples_list