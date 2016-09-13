from nltk.corpus import wordnet as wn

print wn.synset('tree.n.01').part_meronyms()
print wn.synset('tree.n.01').substance_meronyms()
print wn.synset('tree.n.01').member_holonyms()

## ------- MINT -------
for synset in wn.synsets('mint', wn.NOUN):
    ##must use () at end of synset.name and synset.definition
    print synset.name() + ':', synset.definition()

## ------- ENTAILMENTS AND ANTONYMS -------
print wn.synset('walk.v.01').entailments()
print wn.synset('eat.v.01').entailments()
print wn.synset('tease.v.03').entailments()

print wn.lemma('supply.n.02.supply').antonyms()
print wn.lemma('rush.v.01.rush').antonyms()
print wn.lemma('horizontal.a.01.horizontal').antonyms()
print wn.lemma('staccato.r.01.staccato').antonyms()


print "LEXICAL RELATIONS AND OTHERS METHODS DEFINED FOR THIS SYNSET"
print dir(wn.synset('harmony.n.02'))

print "*SEMANTIC SIMILARITY* "
print "LOWEST COMMON HYPERNYMS (CLOSELY RELATED)"
right = wn.synset('right_whale.n.01')
orca = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
tortoise = wn.synset('tortoise.n.01')
novel = wn.synset('novel.n.01')
print right.lowest_common_hypernyms(orca)
print right.lowest_common_hypernyms(tortoise)
print right.lowest_common_hypernyms(novel)

print wn.synset('baleen_whale.n.01').min_depth()
print wn.synset('whale.n.02').min_depth()
print wn.synset('vertebrate.n.01').min_depth()
print wn.synset('entity.n.01').min_depth()

##path_similarity assigns a score in the range 0-1 based on shortest path
##that connects the concepts in the hypernym hierarchy (-1 if path not found)

ps_minke = right.path_similarity(minke)
ps_orca = right.path_similarity(orca)
ps_tortoise = right.path_similarity(tortoise)
ps_novel = right.path_similarity(novel)

print ps_minke
print ps_orca
print ps_tortoise
print ps_novel

##USE HELP(WN) FOR MORE INFO ON SIMILARITY MEASURES
