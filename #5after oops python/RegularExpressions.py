#Use of regular expressions in python
#importing re for helping as in regular expressions
import re

mystr = '''Shree Yash Pratishthan, Shreeyash Collage of engineering and Technology, Aurangabad(Sambhajinagar)
		--Computer Science and Engineering
		--(34.05 Percentile)Approx

5] Terna Public charitable Trust's Collage of Engineering. Osmanabad
		--Computer Science and Technology
		--(34.05 Percentile)Approx

6]Hi-Tech Institute of Technology, Aurangabad(Sambhaginagar)
		--Computer Science and Technology
		--(25.13 Percintile)Approx

7] Aurangabad Collage of Engineering, Naygaon Savangi, Aurangabad
		--Computer Science and Engineering 
		--(33.41 Percentile)

8] Gramin Collage of Engineering, Vishnupuri, Nanded
		--Computer Engineering 
		--(36.19 Percentile)

9]*Bharat Collage of Engineering, Kanher Badlapur(w)
		--Computer Engineering
		--(4.46 Percentile)Approx

9]*Bharat Collage of Engineering, Kanher Badlapur(w)
		--Computer Engineering
		--(4.46 Percentile)Approx

13]*Sanghavi Collage of Engineering , Varvandi, Nashik  cooo
		--Computer Engineering
		--(12.37 Percentile)Approx

18] *SKN sinhgad Institute of Technology & Science, Kusgaon(BK), Pune
		--Computer Engineering
		--(44.80 Percentile)Approx '''

#functions in regular expression:- findall, search, split, sub, finditer
 # For more inforamtion of regex you can read its document


#patt = re.compile(r'fass') # always using raw string in regular expressions
#patt = re.compile(r'.')   #dot means any charecter
#patt = re.compile(r'.*SKN')   #after dot means this charecter
#patt = re.compile(r'^shree')    # ^ it means string starts with
#patt = re.compile(r'ox$')      # $ it means string ends with  
#patt = re.compile(r'co*')       #thise will give how many c and as many o after c charecters * means all the charecters
#patt = re.compile(r'c*o')
#patt = re.compile(r'co{2}') #if we want any specific number of o after c '{}' thise is used
#patt = re.compile(r'{co}{2}') # making a group of these to
#patt = re.compile(r'Co{1}|t')  # using '|' thise as a 'oR' between co t

#special sequences
#patt = re.compile(r'\AShree')   #charecter or string starting with or not it will return if it is true
#patt = re.compile(r'19\b')    #ending with 19 or not

#finding a specific type of digits in string using its pattern
#\d means digits '{}' means exact no. of occurences
patt = re.compile(r'\d{2}.\d{2}')    

matches = patt.finditer(mystr)                                                          

for match in matches:
    print(match)
#    print(mystr[448:452])
