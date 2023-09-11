import time

from pywinauto import Application

app = Application(backend="uia").start(fr'calc.exe')

app.connect(best_match="Калькулятор", timeout=5)

time.sleep(2)

numbut = app.top_window().child_window(class_name="NamedContainerAutomationPeer", found_index=4)
numbut.draw_outline()
time.sleep(3)
app.kill()
