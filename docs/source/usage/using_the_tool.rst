Using the Tool
==============

This section describes how to use the core functionality of the project after setup.

Typical Workflow
----------------

1. **Load your data**
   Describe how a user should prepare or load data into the tool.

2. **Run the main function**
   Explain the primary function or command to execute the tool’s core functionality.

   Example:
   ::
      python -m src.main --config config.yaml

3. **Interpret the output**
   Describe what the user should expect in terms of outputs, and where they’ll be stored.

Configuration
-------------

If the tool uses a configuration file (e.g. `config.yaml`), describe:

- Required and optional parameters
- File structure
- Example configuration block

   Example:
   ::
      input_path: data/input/
      output_path: data/output/
      mode: "fast"

Tips
----

- Use relative paths when possible.
- Review logs for errors or warnings.
- Run with `--debug` flag to get more verbose output.