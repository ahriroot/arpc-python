# -*- coding: utf-8 -*-
# Generated by arpc-python at Tue Nov 22 01:57:53 2022
# Path: ./arpc_file/test/test.arpc
# package: test

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
    """
    This class is a Procedure class for arpc.
    """

    @abc.abstractmethod
    def get_user_v1(self, request: RequestV1) -> ResponseV1: pass

    @abc.abstractmethod
    def post_user_v1(self, request: ResponseV1) -> RequestV1: pass

    def register(self, server):
        server.register('arpc2.0', lambda request, _: self.get_user_v1(
            RequestV1.deserialize(request)).serialize())
        server.register('arpc2.1', lambda request, _: self.post_user_v1(
            ResponseV1.deserialize(request)).serialize())


class Client:

    def get_user_v1(self):
        pass

    def post_user_v1(self):
        pass

