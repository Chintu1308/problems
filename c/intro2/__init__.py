import check50

@check50.check()
def exists():
    """intro2.c exists"""
    check50.exists("intro2.c")
    check50.include("../../intro2/1.in", "../../intro2/1.out")
    check50.include("../../intro2/2.in", "../../intro2/2.out")
    check50.include("../../intro2/3.in", "../../intro2/3.out")
    check50.include("../../intro2/4.in", "../../intro2/4.out")
    check50.include("../../intro2/5.in", "../../intro2/5.out")
    check50.include("../../intro2/6.in", "../../intro2/6.out")
    check50.include("../../intro2/7.in", "../../intro2/7.out")
    check50.include("../../intro2/8.in", "../../intro2/8.out")
    check50.include("../../intro2/9.in", "../../intro2/9.out")
    check50.include("../../intro2/10.in", "../../intro2/10.out")
    check50.include("../../intro2/11.in", "../../intro2/11.out")
    check50.include("../../intro2/12.in", "../../intro2/12.out")
    check50.include("../../intro2/13.in", "../../intro2/13.out")
    check50.include("../../intro2/14.in", "../../intro2/14.out")

@check50.check(exists)
def compiles():
    """intro2.c compiles"""
    check50.c.compile('intro2.c', lcs50=False)

@check50.check(compiles)
def test_1():
    """Test 1"""
    test_input_output("1.in", "1.out")

@check50.check(compiles)
def test_2():
    """Test 2"""
    test_input_output("2.in", "2.out")

@check50.check(compiles)
def test_3():
    """Test 3"""
    test_input_output("3.in", "3.out")

@check50.check(compiles)
def test_4():
    """Test 4"""
    test_input_output("4.in", "4.out")

@check50.check(compiles)
def test_5():
    """Test 5"""
    test_input_output("5.in", "5.out")

@check50.check(compiles)
def test_6():
    """Test 6"""
    test_input_output("6.in", "6.out")

@check50.check(compiles)
def test_7():
    """Test 7"""
    test_input_output("7.in", "7.out")

@check50.check(compiles)
def test_8():
    """Test 8"""
    test_input_output("8.in", "8.out")

@check50.check(compiles)
def test_9():
    """Test 9"""
    test_input_output("9.in", "9.out")

@check50.check(compiles)
def test_10():
    """Test 10"""
    test_input_output("10.in", "10.out")

@check50.check(compiles)
def test_11():
    """Test 11"""
    test_input_output("11.in", "11.out")

@check50.check(compiles)
def test_12():
    """Test 12"""
    test_input_output("12.in", "12.out")

@check50.check(compiles)
def test_13():
    """Test 13"""
    test_input_output("13.in", "13.out")

@check50.check(compiles)
def test_14():
    """Test 14"""
    test_input_output("14.in", "14.out")

# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    check50.run("./intro2").stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()
