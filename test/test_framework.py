from test.TestingFramework import TestingFramework

if __name__ == "__main__":
    # cmd = """echo hello | cat | grep "aa"; sort aa < "First: `ls ./`" | head -r '1.txt' > 1"""
    cmd = "cat < test_framework.py"
    tf = TestingFramework(cmd)
