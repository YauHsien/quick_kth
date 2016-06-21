.PHONY: start halt test

start:
	@cmd /k "env\Scripts\activate.bat"

halt:
	@cmd /k "env\Scripts\deactivate.bat"

test:
	python quick_kth_test.py
