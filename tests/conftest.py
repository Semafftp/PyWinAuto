import pytest
from pywinauto import Application


@pytest.fixture()
def app():
    app = Application(backend="uia").start(fr"calc.exe", timeout=20000)
    app.connect(best_match="Калькулятор", timeout=5)
    yield app
    app.kill(soft=True)

