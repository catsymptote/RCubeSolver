from src.move_interpreter import Interpreter


def test_init():
    intp = Interpreter()
    assert type(intp) is Interpreter
