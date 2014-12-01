PYTHON=python3
all: new_latin_bible.txt
new_latin_bible.txt: bible.txt
	$(PYTHON) new_latin.py <$< >$@
clean: 
	rm -rf new_latin_bible.txt
