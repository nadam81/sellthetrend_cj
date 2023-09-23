.PHONY: clean
.SILENT: clean


clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.ipynb_checkpoints' -exec rm -fr {} +
	rm -rf out.csv
	find . -name '*_pretty.html' -exec rm -f {} +

jupyter:
	export WORKDIR=$(shell pwd) && jupyter lab --allow-root