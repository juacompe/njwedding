from feed.tests.regex_test_content import raw_content
import re

regex_text='id="photo-display" src="(?P<src>.+?)"'

def get_image_url_from_raw_html( content ):
    regex = re.compile( regex_text )
    r = regex.search( content )
    if not r:
        return None

    #list of group found
    found = r.groups()
    if found:
        return found[0]
    return None