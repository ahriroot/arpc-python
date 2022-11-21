# -*- coding: utf-8 -*-
# Generated by arpc-python at Mon Nov 21 19:58:26 2022
# Path: ./arpc_file/api/api.arpc
# package: api

import abc
from arpc.utils import Base


class RequestV1(Base):
    """
    This class is a Param class for arpc.
    """

    def __init__(self, user_id):
        self.user_id = user_id


class ResponseV1(Base):
    """
    This class is a Param class for arpc.
    """

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username


class Arpc(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_user(self, request: RequestV1) -> ResponseV1: pass

    def register(self, server):
        server.register('arpc1.1', lambda request, _: self.get_user(RequestV1.deserialize(request)).serialize())


class Client(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_user(self):
        print('client ok')
