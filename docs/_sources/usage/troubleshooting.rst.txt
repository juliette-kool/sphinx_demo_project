Troubleshooting
===============

Common issues and how to resolve them.

Installation Issues
-------------------

**Problem:** `ModuleNotFoundError` when running the tool
**Solution:**
Make sure dependencies are installed:

::

   pip install -r requirements.txt

---

**Problem:** Python version mismatch
**Solution:**
Check that you're using the recommended Python version:

::

   python --version

Runtime Errors
--------------

**Problem:** `FileNotFoundError` for config or input files
**Solution:**
Ensure the file paths are correct and exist relative to the root folder.

**Problem:** Output is empty or unexpected
**Solution:**
Check if inputs are valid and the correct configuration options were selected.

Logging and Debugging
---------------------

- Logs are saved to `logs/output.log` by default.
- Use `--debug` mode for detailed logs.
- You can also add print statements or use breakpoints when debugging in an IDE like VSCode.

Still Stuck?
------------

Reach out to the maintainer or open an issue in the GitHub repository with:

- What you tried
- Your config settings
- Console output / traceback