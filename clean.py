lines = open('resume.tex').read().splitlines()
result = []
should_keep = False

for line in lines:
	if line.find('{document}') > -1:
		should_keep = not should_keep
		continue

	if should_keep:
		result.append(line)

open('resume.tex', 'w').write(("\n".join(result)))

# pandoc resume.md -o resume.tex --template=foo.tex; python clean.py;
