Getting Started
===============

Welcome to the full project guide.

This page provides detailed instructions on setting up and using the project locally.

Clone the Repository
--------------------

.. code-block:: bash

   git clone https://github.com/your-org/your-project.git
   cd your-project

Create and Activate a Virtual Environment
------------------------------------------

.. code-block:: bash

   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

Install Dependencies
---------------------

.. code-block:: bash

   pip install -r requirements.txt


Set Up Environment Variables
----------------------------

If your project uses a `.env` file:

.. code-block:: bash

   cp .env_template .env

Then edit `.env` to add your own keys or configurations.

Running Tests
-------------

We use `pytest` for running unit tests:

.. code-block:: bash

   pytest

Building the Documentation
---------------------------

This project uses `Sphinx` for documentation. To build the docs locally:

.. code-block:: bash

   cd docs
   make html
