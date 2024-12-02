from src.decorators import log


def test_log(capsys):
    @log()
    def my_function_for_test(x, y):
        return x + y

    my_function_for_test(1, 2)

    captured = capsys.readouterr()
    assert "my_function_for_test ok" in captured.out
    assert "Time to complete the function:" in captured.out


def test_log_er(capsys):
    @log()
    def my_function_for_test(a, b):
        return a + b

    my_function_for_test(1, "2")

    captured = capsys.readouterr()
    assert (
            captured.out == "my_function_for_test error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}\n"
    )

def test_log_func():
    @log("logs\logs.txt")
    def my_function_for_test(a, b):
        return a + b

    assert my_function_for_test(1, 2) == 3
    assert my_function_for_test("a", 2) == 'ValueError'