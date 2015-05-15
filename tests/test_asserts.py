#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest
from unittestzero import Assert


@pytest.mark.skip_selenium
@pytest.mark.nondestructive
class TestAsserts(object):

    def test_eq_native(self, mozwebqa):
        assert 'abc' == 'def'

    def test_eq_utz(self, mozwebqa):
        Assert.equal('abc', 'def')

    def test_neq_native(self, mozwebqa):
        assert 'abc' != 'abc'

    def test_neq_utz(self, mozwebqa):
        Assert.not_equal('abc', 'abc')

    def test_in_native(self, mozwebqa):
        assert 'abc' in 'ksjd shsy lsls'

    def test_in_utz(self, mozwebqa):
        Assert.contains('abc', 'ksjd shsy lsls')

