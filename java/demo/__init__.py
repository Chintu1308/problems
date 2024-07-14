import check50

@check50.check()
def exists():
    """demo.java exists"""
    check50.exists("demo.java")
    check50.include("../../demo/Ram_input.txt", "../../demo/Charan_output.txt")
    check50.include("../../demo/Charan_input.txt", "../../demo/Charan_output.txt")

@check50.check(exists)
def compiles():
    """demo.java compiles"""
    check50.run("javac demo.java").exit(0)


@check50.check(compiles)
def demo_2_3():
    """demo_2_3"""
    test_input_output("Ram_input.txt", "Ram_output.txt")


@check50.check(compiles)
def demo_20_22():
    """demo_20_22"""
    test_input_output("Charan_input.txt", "Charan_output.txt")


# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "java demo"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()
