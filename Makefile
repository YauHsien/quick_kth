.PHONY: start halt test

start:
	@cmd /k "env\Scripts\activate.bat"

halt:
	@cmd /k "env\Scripts\deactivate.bat"

test:

	python seesaw_median_test.py
