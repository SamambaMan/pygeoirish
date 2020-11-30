format:
	flake8 . --ignore=E402 --exclude=src/pygeoirish/itm2utm.py,geocode.py

test:
	PYTHONPATH=src pytest -s -vv
