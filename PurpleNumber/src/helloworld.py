# coding=utf-8
"""Entry point of PurpleNumber app.

@author: Dustin Tseng
"""
import jinja2
import os
import webapp2
import datetime
from gen_board import generate_board
import model
import model_util
from model_data import CHINESE
from model_data import SAMPLE_PERSON
from DataStore import PersonModel
from google.appengine.api import users
from lunardate import LunarDate

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/template'))
EMAIL_WHITELIST = frozenset(["wdtseng@gmail.com",
                             "kcrtseng@gmail.com",
                             "hcctai@gmail.com"])


def num_to_chinese(number, length=None):
    assert isinstance(number, (long, int))
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

def birthday_context(qry):
    values = {
        "chinese": CHINESE,
        "dizhi" : model.DiZhi,
        "sex" : model.Sex,
        "query" : qry
    }
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

class BoardPage(webapp2.RequestHandler):
    def post(self):
        # Check if we are getting someone from the datastore
        existing_person_name = self.request.get("existing")
        
        if len(existing_person_name) > 0:
            existing_person = PersonModel.query(PersonModel.person.name == existing_person_name).fetch(1)
            board = generate_board(existing_person[0].person)
        else:
            # Get the birthday data from the request
            bday = self.request.get("birthdate")
            btime = self.request.get("time")
            sex = self.request.get("sex")
            name = self.request.get("name")
    
            # Convert to metadata
            bdate = datetime.datetime.strptime(bday, "%Y-%m-%d")
            lunar_bdate = LunarDate.fromSolarDate(bdate.year, bdate.month, bdate.day)
            byear_tian_gan = model_util.get_year_tian_gan(lunar_bdate.year)
            byear_di_zhi = model_util.get_year_di_zhi(lunar_bdate.year)
            btime_di_zhi = model.DiZhi(int(btime))
    
            # Create the person
            p = model.Person(
                name=name,
                sex=model.Sex(int(sex)),
                year=bdate.year,
                month_of_year=bdate.month,
                day_of_month=bdate.day,
                year_tian_gan=byear_tian_gan,
                year_di_zhi=byear_di_zhi,
                lunar_month_of_year=lunar_bdate.month,
                lunar_day_of_month=lunar_bdate.day,
                time_di_zhi=btime_di_zhi,
            )
            board = generate_board(p)
    
            # Store the Person in the data store
            pModel = PersonModel(person=p)
            pModel.put()

        # generate the board
        board_template = jinja_environment.get_template("board.html")
        self.response.headers["Content-Type"] = "text/html; charset=utf-8"
        self.response.out.write(board_template.render(board_context(board)))

class BirthdayPage(webapp2.RequestHandler):
    def get(self):
        qry = PersonModel.query()

        board_template = jinja_environment.get_template("birthday.html")
        self.response.headers["Content-Type"] = "text/html; charset=utf-8"
        self.response.out.write(board_template.render(birthday_context(qry)))


app = webapp2.WSGIApplication([("/", MainPage),
                               ("/robert", RobertPage),
                               ("/birthday", BirthdayPage),
                               ("/board", BoardPage)],
                              debug=True)
