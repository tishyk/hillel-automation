rm -rf playwright_venv ||true; python3 -m virtualenv playwright_venv || true; \
	. playwright_venv/bin/activate \
	&& pip install -e . \
	&& pip install -e src/ \
	&& python -m playwright install