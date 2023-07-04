from rcube.move_interpreter import Interpreter


def test_init():
    intp = Interpreter()
    assert type(intp) is Interpreter
