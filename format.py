lines = open('resume.md').read().splitlines()
result = []
should_keep = False

for line in lines:
	result.append(line.replace("---", "\hfill"))

open('resume.formatted.md', 'w').write(("\n".join(result)))

# pandoc resume.md -o resume.tex --template=foo.tex; python clean.py;
