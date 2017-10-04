# I don't know what I'm doing...
#  ...more than half of the time.
OUTPUT	= hidden.xml slides.xml slides.html

all: $(OUTPUT)

hidden.xml:
	( \
		printf '<?xml version="1.0" encoding="UTF-8" ?>\n'; \
		printf '<article data-sblg-article="1">\n'; \
	        grep -v '%' hidden.md | lowdown; \
		printf '</article>'; \
	) > $@

slides.xml:
	cp template.xml slides.xml

slides.html: hidden.xml slides.xml
	sblg -o slides.html -t slides.xml hidden.xml

clean:
	rm -f $(OUTPUT)
