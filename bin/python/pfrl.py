#! /usr/bin/python3

# Should implement this in lua instead
# From https://stackoverflow.com/questions/40993488/convert-markdown-links-to-html-with-pandoc

import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Link) and ".md" in elem.url:
        print(elem.url) if "readme" in elem.url else None
        if elem.url.endswith('.md'):
            elem.url = elem.url[:-3] + '.pdf'
        elem.url.replace(".md#", ".pdf#")
        return elem

if __name__ == '__main__':
    pf.run_filter(action)
