.PHONY: run test install

run:
	python3 count.py

test:
	python3 -m unittest discover -p 'count_test.py'

install:
	pip install -r requirements.txt