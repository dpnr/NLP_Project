Midpoint Project Evaluation

a) Citations and Resources
	1) scikit-learn to train a SVM for Incident http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html, Library - http://scikit-learn.org
	2) WordNet, PorterStemmer, stopwords, PunktTokenizer, RegexParser  from NLTK  Library - http://www.nltk.org/
	3) NER tagger - Stanford Core NLP - https://stanfordnlp.github.io/CoreNLP/

b) Time Estimate
	1)It takes 40 sec to process 1 document. 
	2) In the nlp_Project.py, Commenting out the Perpetrator Organization increases the speed significantly. Almost makes it process 1 Dcoument in 1 sec. Feel free to Comment it out if it is taking too long to run.

c) Contribution
	1)Akshay Khatwani - Incident Extraction, Victim Extraction, Targets Extraction(not in working condition)
	2)Pranavnath Dommata - 	ID Extraction, Weapon Extraction, Perp Organization Extraction, Perp Individual Extraction

d) Limitations
	1)Before Running the shell script, Please type bash in terminal. The script written is for Bash.
	2)There could be possibility of limited disk space owing to downloading of the Stanford Library(Clearing trash worked for us).
	3)We get Deprecation warnings on the Console which doesn't affect the output file(used for checking the Accuracy).
