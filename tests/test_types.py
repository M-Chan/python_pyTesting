from filesToTest import typesOfVariables


def testType_python1():
    assert isinstance(
        typesOfVariables.python1, int
    )  # should fail as python1 is a string


def testType_python2():
    assert isinstance(typesOfVariables.python2, int)  # should pass


def testType_python3():
    assert isinstance(
        typesOfVariables.python3, int
    )  # should fail as python3 is a float
