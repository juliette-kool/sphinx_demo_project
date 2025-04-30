Writing and Documenting Python Modules
======================================

This page explains how to structure Python modules and document them in a way that integrates cleanly with Sphinx and supports long-term readability, usability, and collaboration.

It uses Google-style docstrings and is aligned with SYSTEMIQ's internal standards and the Furo theme.

---

Module Structure
----------------

Each Python module should:

- Do **one thing well** (single-responsibility principle)
- Include a **top-level module docstring** that briefly describes its purpose
- Contain **well-named functions or classes** with clear inputs/outputs
- Be placed in the `src/` folder

Example:

.. code-block:: python

    """
    src/example_module.py

    Utilities for loading and analyzing raster data from cloud storage.
    """

    def load_config(path: str) -> dict:
        """Load a YAML configuration file.

        Args:
            path (str): Path to the config file.

        Returns:
            dict: Parsed configuration as a dictionary.
        """
        ...


    def compute_summary(data: np.ndarray) -> dict:
        """Compute mean, min, max from a 2D NumPy array.

        Args:
            data (np.ndarray): Input raster data.

        Returns:
            dict: Dictionary with 'mean', 'min', and 'max' values.
        """
        ...

---

Docstring Style
---------------

We use the **Google style** for clarity and compatibility with Sphinx + Napoleon.

Key components:

1. **One-line summary**: Short and descriptive.
2. **Args**: List input parameters with types and explanations.
3. **Returns**: Describe the return value and its type.
4. **Raises** (optional): Mention specific errors your function may raise.

Example:

.. code-block:: python

    def calculate_area(width: float, height: float) -> float:
        """Calculate the area of a rectangle.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.

        Returns:
            float: The computed area.
        """

---

Best Practices
--------------

- ✘ Avoid vague names like `process()` or `do_stuff()`
- ✔ Use meaningful verbs: `load_config()`, `compute_area()`, `clip_raster()`
- ✔ Always document what the function **expects** and what it **returns**
- ✔ Keep docstrings short and focused — use full documentation pages for deep explanations

---

Next Steps
----------

After documenting your module:

1. Add a corresponding `.rst` file in `docs/source/api/`
2. Use `automodule` to pull in your docstrings:

.. code-block:: rst

    .. automodule:: src.example_module
        :members:
        :undoc-members:
        :show-inheritance:

3. Add your `.rst` file to `index.rst` under a `.. toctree::`

---