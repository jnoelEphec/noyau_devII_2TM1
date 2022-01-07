#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Ce fichier contient une classe représentant un utilisateur.
    ----- CODE DE LA CLASSE A IMPLEMENTER -----
"""


class User:
    def __init__(self, uid, pseudo, current_user: bool):
        """a new user is created"""
        """
        PRE : uid and pseudo are strings, current_user is a boolean
        POST : a new User object is created
        """
        self.uid = uid
        self.pseudo = pseudo
        self.is_current_user = current_user
