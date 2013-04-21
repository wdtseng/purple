# coding=utf-8
"""Entry point of PurpleNumber app.

@author: Dustin Tseng
"""
import jinja2
import os
import webapp2
from gen_board import generate_board
import model
import model_util
from model_data import CHINESE
from model_data import SAMPLE_PERSON
from google.appengine.api import users

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/template'))
EMAIL_WHITELIST = frozenset(["wdtseng@gmail.com",
                             "kcrtseng@gmail.com",
                             "hcctai@gmail.com"])

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
    person = board.person
    values = {
        "board": board,
        "chinese": CHINESE,
        "model_util": model_util
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

def is_current_user_whitelisted():
    """Checks whether the currently signed in user is whitelisted.
    Returns:
        True if and only if a user is signed in, and is in the whitelist.
    """
    current_user = users.get_current_user()
    print "current user: user_id=%s, email=%s" % (current_user.user_id(),
                                                  current_user.email())
    return (current_user
            and current_user.user_id() is not None
            and current_user.email() in EMAIL_WHITELIST)

class MainPage(webapp2.RequestHandler):
    def get(self):
        if is_current_user_whitelisted():
            board_template = jinja_environment.get_template("board.html")
            person = SAMPLE_PERSON
            board = generate_board(person)
            self.response.headers["Content-Type"] = "text/html; charset=utf-8"
            self.response.out.write(board_template.render(board_context(board)))
        else:
            self.response.status = "403 Forbidden"

class RobertPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html; charset=utf-8"
        self.response.write("Booraga, 曾冠傑!")

app = webapp2.WSGIApplication([("/", MainPage),
                               ("/robert", RobertPage)],
                              debug=True)
