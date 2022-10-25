# Test demo with Playwright framework 
# Install Guide
- `install.sh` can be used to install this repo in a one step.
- This repo a pip-installable package (should be installed in develop mode [-e]). `pip install -e . && pip install -e src/`
- It contains all the modules test needs in order to run this repo content.
- Playwright additional installation required for recording: `python -m playwright install`.

# Run Guide
- playwright record command example - `python -m playwright codegen src\data\runtime_data.html`
- pytest framework used to run this repo tests (Ex. `python -m pytest test` )
# Useful links
- Markdown cheatsheet(.md): https://www.markdownguide.org/cheat-sheet/ 
- Markdown cheatsheet(.rst): https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst
- Page Object Models: https://playwright.dev/python/docs/pom
- page.click(selector): https://playwright.dev/python/docs/actionability 
- playwright selectors: https://youtu.be/Iu04oCb_Vqw?t=146
- Pytest rootdir fixture: https://docs.pytest.org/en/6.2.x/reference.html#pytest.config.Config
- python timezone: https://docs.python.org/3/library/time.html
# Debug Option
- Use `PWDEBUG=1` Environment variable for playwright test debug

# Homework
# VirtualBox and  Oracle VM VirtualBox Extension Pack