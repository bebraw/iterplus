Developer's Guide
=================

As you might have figured out, the library relies quite heavily on Sphinx documentation tool. It is in fact used to test it. Provided you have installed Sphinx (via easy_install, pip or something), you can use "make doctest" at the docs directory to run doctests. This probably needs a nice setup.py alias but I haven't gotten around implementing that...

It is possible to generate the documentation via setup.py, though. You can do this simply via "build_sphinx" parameter (ie. setup.py build_sphinx). There's also an untested "upload_sphinx" that's supposed to upload the project documentation to the right place.

