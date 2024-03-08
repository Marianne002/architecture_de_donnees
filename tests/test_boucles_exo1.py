
from boucles_exo1 import guess_number


def test_guess_number_too_high(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "100")
    guess_number()
    captured = capsys.readouterr()
    assert "Le nombre mystère est plus petit." in captured.out


def test_guess_number_too_low(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    guess_number()
    captured = capsys.readouterr()
    assert "Le nombre mystère est plus grand." in captured.out


def test_guess_number_out_of_attemps(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    guess_number()
    captured = capsys.readouterr()
    assert "Dommage. Le nombre mystère était" in captured.out
