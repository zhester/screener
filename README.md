screener
========

Python Code Screening Tools

Purpose
-------

This project is intended to provide a set of tools to automate basic code
screening of Python files.

Problem
-------

I have been teaching a basic programming course, and I find myself in need of
some basic automation when evaluating a large number of code samples spread
across many files.  I can easily distill exactly what I need to identify into
a few rules, and almost get a "score" for any Python source file that
satisfies the basic requirements (interfaces, parameter lists, return types,
etc.).

I'd also like to eventually integrate more aggressive code checking (such as
`pylint`), but for now, I just want a few simple things that I can use to
build one-off scripts without re-inventing the common stuff every time.

Components
----------

### Arbitrary Importing

A simple function to safely (re)import any module given a path to a Python
script.  This is not without its pitfalls and edge cases, so I just wanted one
function to take care of everything for me.

### Function Interface Checking

A common screening task for me is to make sure a piece of code has even
implemented the functions as requested.  This component uses a rule-based
system to test 1) if the functions are available in a module/object, and 2) if
the functions support a minimal interface.

### Unit Testing Automation

I haven't decided how far to take this yet, but I'd like to build a system
that gives me the shortest path to writing very short unit test cases and stub
functions around the `unittest` module.  These are not intended to be
industrial-grade unit tests, but enough for me to tell that there is some
implementation behind a particular interface before I need to dig deeper into
the code for manual inspection.

