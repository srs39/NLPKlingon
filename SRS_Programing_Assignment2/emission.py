#Samantha Shoecraft
#7/26/17
import nltk
import operator

myfile = open('Klingon_Train.txt', 'r')
words = myfile.read().split()
tuples = [nltk.tag.str2tuple(word) for word in words]

dict = {}
for t in tuples:
	if t[0] in dict:
		dict.get(t[0])[t[1]] = dict.get(t[0]).get(t[1]) + 1
	else:
		dict[t[0]] = {'N' : 0, 'V' : 0, 'PRO' : 0, 'CONJ' : 0}
		dict[t[0]][t[1]] = 1;

for key in dict:
	times = 0;
	dict2 = dict.get(key);
	for tag in dict2:
		times += dict2.get(tag)
	for tag in dict2:
		dict2[tag] = (dict2[tag] / times) + 0.1
myfile.close()
