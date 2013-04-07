# coding=utf-8
"""Entry point of PurpleNumber app.

@author: Dustin Tseng
"""
import jinja2
import os
import webapp2
import model
from model import CHINESE

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/template'))

class Empty():
    pass

def num_to_chinese(number, length=None):
    assert isinstance(number, int)
    assert (length is None) or isinstance(length, int)
    if number in CHINESE:
        chinese = CHINESE[number]
    else:
        chinese = CHINESE[number % 10]
        while number >= 10:
            number /= 10
            chinese = CHINESE[number % 10] + chinese
    if length is None:
        return chinese
    else:
        return chinese.rjust(length, CHINESE[" "])


def board_context(board):
    assert isinstance(board, model.Board)
    greeting1 = Empty()
    greeting2 = Empty()
    greeting1.author = "dustin"
    greeting1.content = "hi ho"
    greeting2.author = "robert"
    greeting2.content = "fee fie"
    person = board.person
    values = {
        "greetings": [greeting1, greeting2],
        "url": "http://hi",
        "url_linktext": "hi",
        "board": board,
        "chinese": CHINESE,
    }
    values["solar_birthday"] = u"陽曆%s　%s　%s" % (
        num_to_chinese(person.year, 4),
        num_to_chinese(person.month_of_year, 2),
        num_to_chinese(person.day_of_month, 2),
    )
    values["birthday"] = u"　　　　　　年　　月　　日%s時生" % (
        CHINESE[person.time_di_zhi],
    )
    values["lunar_birthday"] = u"陰曆　%s%s　　%s　%s" % (
        CHINESE[person.year_tian_gan],
        CHINESE[person.year_di_zhi],
        num_to_chinese(person.lunar_month_of_year, 2),
        num_to_chinese(person.lunar_day_of_month, 2),
    )
    return values

class MainPage(webapp2.RequestHandler):
    def get(self):
        board_template = jinja_environment.get_template('board.html')
        self.response.headers['Content-Type'] = (
            "Content-Type: text/html; charset=utf-8")
        self.response.out.write(board_template.render(board_context(model.SAMPLE)))

class RobertPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = (
            "Content-Type: text/html; charset=utf-8")
        self.response.write('Booraga! Bonjour, 曾冠傑!')

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/robert', RobertPage)],
                              debug=True)
