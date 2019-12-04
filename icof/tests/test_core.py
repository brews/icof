import pytest
import icof


@pytest.fixture
def fake_html():
    out = """
        <html>
        <head>
        <title>Is California On Fire?</title>
        </head>
        <body>
        <h1>Yes</h1>
        updated: Mon Nov 18 11:22:53 2019 PST
        </body>
        </html>
        """
    return out


def test_icof_online():
    answer = icof.is_california_on_fire()
    assert answer.lower() in ('yes', 'no')


def test_icof_offline(fake_html):
    answer = icof.is_california_on_fire(html=fake_html)
    goal = 'Yes'
    assert answer == goal
