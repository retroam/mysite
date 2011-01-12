from pybtex.database.input import bibtex
from pybtex.style.formatting import custom
from pybtex.backends import html, plaintext
from django.utils.safestring import mark_safe
from StringIO import StringIO

def parse(bib):
    parser = bibtex.Parser()
    return parser.parse_stream(StringIO(bib))

def citekeys(bib):
    return parse(bib).entries.keys()

def format(bib, backend):
    style = custom.Style()
    return [ 
        formatted_entry.text.render(backend) for formatted_entry in 
        style.format_entries(parse(bib).entries) ]

def format_as_html(bib):
    return mark_safe(u'<br>'.join(format(bib, html.Backend())))

def format_as_text(bib):
    return u'\n'.join(format(bib, plaintext.Backend()))

