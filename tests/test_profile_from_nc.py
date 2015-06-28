#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

from argo.argo import profile_from_nc

def validate_profile(p):
    assert hasattr(p, 'keys')
    assert hasattr(p, 'attributes')
    assert 'datetime' in p.attributes

def test_extract_1_profile():
    pp = profile_from_nc('test_data/20150127_prof.nc', 0)
    assert len(pp) == 1
    for p in pp:
        validate_profile(p)

def test_extract_list_profiles():
    pp = profile_from_nc('test_data/20150127_prof.nc', [0, 2, 5])
    assert len(pp) == 3
    for p in pp:
        validate_profile(p)

def test_extract_all_profiles():
    pp = profile_from_nc('test_data/20150127_prof.nc')
    assert len(pp) > 1
    for p in pp:
        validate_profile(p)
