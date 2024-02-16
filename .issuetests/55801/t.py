from contextlib import redirect_stdout, redirect_stderr
import warnings


def test1():
    warnings.warn("test1")
    print(f"registry on exiting fun1: \n    {__warningregistry__}")


def test2():
    print(f"registry on entering fun2: \n    {__warningregistry__}")
    warnings.warn("test2")
    print(f"registry on exiting fun2: \n    {__warningregistry__}")


def test3():
    print(f"registry before entering fun3: \n    {__warningregistry__}")
    with warnings.catch_warnings():
        print(f"registry in catch_warnings(): \n    {__warningregistry__}")
        warnings.warn("test3")
    print(f"registry after exiting fun3: \n    {__warningregistry__}")


with open("t.txt", "w") as f:
    with redirect_stdout(f), redirect_stderr(f):
        test1()
        test1()
        test2()
        test2()
        test3()
        test1()
        test2()
