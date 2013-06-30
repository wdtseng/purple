# coding=utf-8
"""protorpc service definitions of 紫微斗數 命盤.

@author: Dustin Tseng
"""
from protorpc import message_types
from protorpc import messages
from protorpc import remote
from model import DiZhi
from model import TianGan
from model_data import CHINESE


class Chinese(messages.Message):
    """Just a series of Chinese string literals."""
    tian_gan = messages.StringField(1)
    tian_gans = messages.StringField(2, repeated=True)
    di_zhi = messages.StringField(3)
    di_zhis = messages.StringField(4, repeated=True)

class PurpleService(remote.Service):
    """Service to retrieve various Chinese string literals."""
    @remote.method(message_types.VoidMessage, Chinese)
    def get_chinese(self, request):
        chinese = Chinese()
        chinese.tian_gan = u"天干"
        chinese.tian_gans = [CHINESE[tian_gan] for tian_gan in TianGan]
        chinese.di_zhi = u"地支"
        chinese.di_zhis = [CHINESE[di_zhi] for di_zhi in DiZhi]
        return chinese

    




