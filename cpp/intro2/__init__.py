import check50

@check50.check()
def exists():
    """intro2.cpp exists"""
    check50.exists("intro2.cpp")
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
    """intro2.cpp compiles"""
    check50.run("check50.run("g++ -std=c++11 demo.cpp -o demo").exit(0)").exit(0)

@check50.check(compiles)
def demo_1():
    """demo_1"""
    test_input_output("1.in", "1.out")

@check50.check(compiles)
def demo_2():
    """demo_2"""
    test_input_output("2.in", "2.out")

@check50.check(compiles)
def demo_3():
    """demo_3"""
    test_input_output("3.in", "3.out")

@check50.check(compiles)
def demo_4():
    """demo_4"""
    test_input_output("4.in", "4.out")

@check50.check(compiles)
def demo_5():
    """demo_5"""
    test_input_output("5.in", "5.out")

@check50.check(compiles)
def demo_6():
    """demo_6"""
    test_input_output("6.in", "6.out")

@check50.check(compiles)
def demo_7():
    """demo_7"""
    test_input_output("7.in", "7.out")

@check50.check(compiles)
def demo_8():
    """demo_8"""
    test_input_output("8.in", "8.out")

@check50.check(compiles)
def demo_9():
    """demo_9"""
    test_input_output("9.in", "9.out")

@check50.check(compiles)
def demo_10():
    """demo_10"""
    test_input_output("10.in", "10.out")

@check50.check(compiles)
def demo_11():
    """demo_11"""
    test_input_output("11.in", "11.out")

@check50.check(compiles)
def demo_12():
    """demo_12"""
    test_input_output("12.in", "12.out")

@check50.check(compiles)
def demo_13():
    """demo_13"""
    test_input_output("13.in", "13.out")

@check50.check(compiles)
def demo_14():
    """demo_14"""
    test_input_output("14.in", "14.out")

# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "./demo"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()
