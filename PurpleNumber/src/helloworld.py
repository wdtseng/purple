# coding=utf-8
import jinja2
import os
import webapp2
import model
from model import CHINESE

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/template'))

CHINESE_SPACE = u"　";

class Empty():
    pass

def num_to_chinese(number, length=0):
    assert isinstance(number, int)
    NUMBERS = u"零一二三四五六七八九十"
    if number == 0:
        chinese = NUMBERS[0]
    else:
        chinese = u""
        while number > 0:
            chinese = NUMBERS[number % 10] + chinese
            number /= 10
    if length == 0:
        return chinese
    else:
        return chinese.rjust(length, CHINESE_SPACE)


def board_template_value(board):
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
        self.response.out.write(board_template.render(board_template_value(model.SAMPLE)))

class RobertPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Booraga! Bonjour, 曾冠傑!')

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/robert', RobertPage)],
                              debug=True)
