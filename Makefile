
CC=python3
CC_EXE=PyInstaller
C_EXE_FLAGS=--name=most_active_cookie --onefile --distpath=./ --clean
SRC=src/main
UTILS=src/main/utils
TEST=src/unittest
PYTHON_FLAGS=-m


MAIN_PYTHON=most_active_cookie.py

output: $(SRC)/most_active_cookie.py $(UTILS)/calculations.py $(UTILS)/displays.py $(UTILS)/validations.py
	pip install pyinstaller
	$(CC) $(PYTHON_FLAGS) unittest $(TEST)/calculations_tests.py
	$(CC) $(PYTHON_FLAGS) unittest $(TEST)/displays_tests.py
	$(CC) $(PYTHON_FLAGS) unittest $(TEST)/calculations_tests.py
	$(CC) $(PYTHON_FLAGS) $(CC_EXE) $(C_EXE_FLAGS) ./$(SRC)/$(MAIN_PYTHON)

