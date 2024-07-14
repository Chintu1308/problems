
import check50
import check50.c

@check50.check()
def exists():
    """demo.c exists"""
    check50.exists("demo.c")
    check50.include("../../demo/Ram_input.txt", "../../demo/Ram_output.txt")
    check50.include("../../demo/Charan_input.txt", "../../demo/Charan_output.txt")

@check50.check(exists)
def compiles():
    """demo.c compiles"""
    check50.c.compile("demo.c", lcs50=False)


@check50.check(compiles)
def demo_2_3():
    """demo_Ram"""
    test_input_output("Ram_input.txt", "Ram_output.txt")


@check50.check(compiles)
def demo_10_20():
    """demo_Charan"""
    test_input_output("Charan_input.txt", "Charan_output.txt")


# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "./demo"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()
