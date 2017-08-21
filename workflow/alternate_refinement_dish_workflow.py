import re,sys

# @BEGIN Alternative_Clean_Dish
# @IN name @URI file:Dish.csv.tsv
# @IN pass_thru_cols @URI file:Dish.csv.tsv
# @OUT alternate_clean_Dish.tsv @URI file:alternate_clean_Dish.tsv

#Global data structures
translated_unigram_mapping = dict()
translated_dish_name_mapping = dict()
COL_NAME = 1

def isAscii(unigram):
	try:
		unigram.decode('ascii')
		return True
	except UnicodeDecodeError:
		return False

def google_translate(unigram):
	#TODO Implement call to legit Google Translate API here
	return unigram

def main(argv):
	
	# @BEGIN get_non_english_unigram
	# @IN name
	# @OUT non_eng_unigram
	# @END get_non_english_unigram
	fr = open('Dish-csv.tsv', 'r')
	for line in fr:
		s = line.split('\t')
		dish_name = s[COL_NAME]
		for unigram in dish_name.split(' '):
			if not isAscii(unigram):
				#Put unigram to be translated in dictionary
				translated_unigram_mapping[unigram] = ''
				#Put dish name to be translated in dictionary
				translated_dish_name_mapping[unigram] = ''
	fr.close()

	# @BEGIN google_translate
	# @IN non_eng_unigram
	# @OUT translated_unigram
	# @END google_translate
	for unigram in translated_unigram_mapping:
		translated_unigram_mapping[unigram] = google_translate(unigram)

	# @BEGIN put_together_translated_dish_name
	# @IN name
	# @IN translated_unigram
	# @OUT translated_dish_name
	# @END put_together_translated_dish_name
	for dish_name in translated_dish_name_mapping:
		eng_dish_name = ''
		for unigram in dish_name.split(' '):
			if unigram in translated_unigram_mapping:
				eng_dish_name+=' '+translated_unigram_mapping[unigram]
			else:
				eng_dish_name+=' '+unigram
		translated_dish_name_mapping[dish_name] = re.sub('^ ', '' , eng_dish_name)


	# @BEGIN export
	# @IN translated_dish_name
	# @IN pass_thru_cols
	# @OUT alternate_clean_Dish.tsv @URI alternate_clean_Dish.tsv
	# @END export
	fw = open('alternate_clean_Dish.tsv', 'w')
	fr = open('Dish-csv.tsv', 'r')
	for line in fr:
		new_line = ''
		s = line.split('\t')
		for i in range(0,len(s)):
			if i==1:
				dish_name = s[i]
				if dish_name in translated_dish_name_mapping:
					new_line+='\t'+dish_name+'\t'+translated_dish_name_mapping[dish_name]
				else:
					new_line+='\t'+dish_name+'\t'+dish_name
			else:
				new_line+='\t'+s[i]
		fw.write(re.sub('^\t', '', new_line))
	fw.close()
	fr.close()
	
# @END Alternative_Clean_Dish

if __name__ == "__main__":
	main(sys.argv)
