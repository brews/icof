from html.parser import HTMLParser
import urllib.request


class _BodyHeadParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_body = False
        self.in_h1 = False
        self.data = None

    def _body_or_head_switch_to(self, tag, switch_to=True):
        if tag == "body":
            self.in_body = switch_to
        elif tag == "h1":
            self.in_h1 = switch_to

    def handle_starttag(self, tag, attrs):
        self._body_or_head_switch_to(tag, True)

    def handle_endtag(self, tag):
        self._body_or_head_switch_to(tag, False)

    def handle_data(self, data):
        if self.in_body and self.in_h1:
            self.data = data


def is_california_on_fire(html=None):
    """Returns 'yes' or 'no'
    """
    target = "http://iscaliforniaonfire.com/"
    if html is None:
        with urllib.request.urlopen(target) as response:
            html = response.read().decode("utf-8")
    parser = _BodyHeadParser()
    parser.feed(html)
    return parser.data
