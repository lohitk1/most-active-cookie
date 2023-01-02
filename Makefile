
CC=python3
CC_EXE=pyinstaller
C_EXEFLAGS=--name=most_active_cookie --onefile --distpath=./ --clean
SRC=src/main
UTILS=src/main/utils
TEST=src/unittest
TESTFLAGS=-m


MAIN_PYTHON=most_active_cookie.py

output: $(SRC)/most_active_cookie.py $(UTILS)/calculations.py $(UTILS)/displays.py $(UTILS)/validations.py
	$(CC) $(TESTFLAGS) unittest $(TEST)/calculations_tests.py
	$(CC) $(TESTFLAGS) unittest $(TEST)/displays_tests.py
	$(CC) $(TESTFLAGS) unittest $(TEST)/calculations_tests.py
	$(CC_EXE) $(C_EXEFLAGS) ./$(SRC)/$(MAIN_PYTHON)

