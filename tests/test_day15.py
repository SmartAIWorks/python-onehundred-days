import importlib
import importlib.util
import os
import sys


def reload_day15():
    module = importlib.import_module('day15.day15_project')
    importlib.reload(module)
    return module


def test_validate_resources_enough():
    m = reload_day15()
    # Ensure resources are high enough
    m.resources.update({"water": 300, "milk": 200, "coffee": 100})
    product = {"ingredients": {"water": 50, "milk": 50, "coffee": 18}, "cost": 2.5}
    assert m.validate_resources(product) is True


def test_validate_resources_missing_water():
    m = reload_day15()
    m.resources.update({"water": 10, "milk": 200, "coffee": 100})
    product = {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5}
    assert m.validate_resources(product) is False


def test_validate_payment_insufficient():
    m = reload_day15()
    m.resources.update({"water": 300, "milk": 200, "coffee": 100})
    product = {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5}
    ok, change = m.validate(product, 1.0)
    assert ok is False
    assert change == 1.0


def test_validate_payment_sufficient_change():
    m = reload_day15()
    m.resources.update({"water": 300, "milk": 200, "coffee": 100})
    product = {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5}
    ok, change = m.validate(product, 2.0)
    assert ok is True
    assert change == 0.5


def test_update_resources_deducts_correctly():
    m = reload_day15()
    m.resources.update({"water": 100, "milk": 100, "coffee": 50})
    product = {"ingredients": {"water": 50, "milk": 20, "coffee": 10}, "cost": 2.0}
    m.update_resources(product)
    assert m.resources["water"] == 50
    assert m.resources["milk"] == 80
    assert m.resources["coffee"] == 40


