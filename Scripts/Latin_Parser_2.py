import sys

theTypes = ["noun", "verb", "part", "adj", "adv", "prep", "pron", "conj", "partic", "article", "irreg", "exclam"]
theNums = ["sg", "pl", "dual"]
theGens = ["fem", "masc", "neut"]
theCases = ["nom", "voc", "acc", "gen", "dat"]
thePersons = ["1st", "2nd", "3rd"]
theTenses = ["pres", "fut", "imperf", "perf", "plup", "futperf", "aor"]
theMoods = ["subj", "ind", "imperat", "inf", "opt"]
theVoices = ["act", "pass", "mp"]

def main():
	input = sys.argv[1].decode('utf-8')
	L = input.split(' : ')
	query = L[0]
	lemma = L[1]
	defin = L[2]
	parse = L[3]
	parsings = parse.split(' ')
	for i in parsings:
		if i in theTypes:
			type = i
		elif i in theNums:
			num = i
		elif i in theGens:
			gen = i
		elif i in theCases:
			case = i
		elif i in thePersons:
			pers = i
		elif i in theTenses:
			tense = i 
		elif i in theMoods:
			mood = i
		elif i in theVoices:
			voice = i
	if not 'num' in locals():
		num = None
	if not 'gen' in locals():
		gen = None
	if not 'case' in locals():
		case = None
	if not 'pers' in locals():
		pers = None
	if not 'tense' in locals():
		tense = None
	if not 'mood' in locals():
		mood = None
	if not 'voice' in locals():
		voice = None
	
	final_txt = query + '\n\n'
	if type == 'noun':
		final_txt += 'Case: \t\t' + case + '\nNumber: \t\t' + num + '\nGender: \t\t' + gen + '\n\nTranslation: \t' + defin + '\nLemma: \t\t' + lemma + '\n\nSyntax: \t\t' + type
	elif type == 'verb':
		if mood == 'inf':
			final_txt += 'Tense: \t\t' + tense + '\nMood: \t\t' + mood + '\nVoice: \t\t' + voice + '\n\nTranslation: \t' + defin + '\nLemma: \t\t' + lemma + '\n\nSyntax: \t\t' + type
		else:
			final_txt += 'Person: \t\t' + pers + '\nNumber: \t\t' + num + '\nTense: \t\t' + tense + '\nMood: \t\t' + mood + '\nVoice: \t\t' + voice + '\n\nTranslation: \t' + defin + '\nLemma: \t\t' + lemma + '\n\nSyntax: \t\t' + type
	elif type == 'part':
		type = 'ppl'
		final_txt += 'Case: \t\t' + case + '\nNumber: \t\t' + num + '\nGender: \t\t' + gen + 'Tense: \t\t' + tense + '\nMood: \t\t' + mood + '\nVoice: \t\t' + voice + '\n\nTranslation: \t' + defin + '\nLemma: \t\t' + lemma + '\n\nSyntax: \t\t' + type
	elif type == 'adj':
		final_txt += 'Case: \t\t' + case + '\nNumber: \t\t' + num + '\nGender: \t\t' + gen + '\n\nTranslation: \t' + defin + '\nLemma: \t\t' + lemma + '\n\nSyntax: \t\t' + type
	elif type == 'adv':	
		final_txt += 'Translation: \t' + defin + '\nLemma: \t\t' + lemma + '\n\nSyntax: \t\t' + type
	elif type == 'prep':
		final_txt += 'Translation: \t' + defin + '\nLemma: \t\t' + lemma + '\n\nSyntax: \t\t' + type
	elif type == 'pron':
		final_txt += 'Case: \t\t' + case + '\nNumber: \t\t' + num + '\nGender: \t\t' + gen + '\n\nTranslation: \t' + defin + '\nLemma: \t\t' + lemma + '\n\nSyntax: \t\t' + type
	elif type == 'conj':
		final_txt += 'Translation: \t' + defin + '\nLemma: \t\t' + lemma + '\n\nSyntax: \t\t' + type
	elif type == 'irreg':
		final_txt += 'Translation: \t' + defin + '\nLemma: \t\t' + lemma + '\n\nSyntax: \t\t' + type
	elif type == 'exclam':
		final_txt += 'Translation: \t' + defin + '\nLemma: \t\t' + lemma + '\n\nSyntax: \t\t' + type
	print final_txt.encode('utf-8')
		
		
		


if __name__ == '__main__':
    main()