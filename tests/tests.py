#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import unittest
from persona_test_user.persona_test_user import PersonaTestUser


class TestPersonaUser(unittest.TestCase):

    def test_basic_user(self):
        user = PersonaTestUser().create_user()

        assert type(user) is dict
        assert type(user['email']) is unicode
        assert type(user['pass']) is unicode
        assert user['env'] == 'prod'


if __name__ == '__main__':
    unittest.main()
