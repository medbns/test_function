import io
import pytest
from user_registration import *  # Adjust import as per your file structure

def test_user_name_empty(monkeypatch):
    # Mock user input for an empty username
    monkeypatch.setattr('builtins.input', lambda _: '')  # Mock input to return empty string
    assert get_user_name_from_input() is None


def test_user_name_with_spaces(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('my user name'))
    assert get_user_name_from_input() is None


def test_user_name_valid(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('valid_username'))
    assert get_user_name_from_input() == 'valid_username'


def test_password_too_short(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Abc1!'))
    assert get_password_from_input() is None


def test_password_no_special_character(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Abc12345'))
    assert get_password_from_input() is None


def test_password_no_number(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Abcdefgh!'))
    assert get_password_from_input() is None


def test_password_no_letter(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('12345678!'))
    assert get_password_from_input() is None


def test_password_valid(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Abc12345!'))
    assert get_password_from_input() == 'Abc12345!'


def test_email_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None


def test_email_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None


def test_email_valid(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'


def test_all_valid_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('valid_username\nAbc12345!\npetra@adaltas.com'))
    assert get_user_name_from_input() == 'valid_username'
    assert get_password_from_input() == 'Abc12345!'
    assert get_email_from_input() == 'petra@adaltas.com'
