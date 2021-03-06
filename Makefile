all: convert-to-tex render rename cleanup

convert-to-tex:
	python format.py; pandoc resume.formatted.md -o resume.tex --template=template.tex; python clean.py

render:
	xelatex output.tex

rename:
	mv output.pdf arnav_kumar.pdf

cleanup:
	rm output.log; rm resume.formatted.md
