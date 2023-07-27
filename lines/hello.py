"""
Docstring processing tools will strip a uniform amount of indentation from the second and further lines of
the docstring, equal to the minimum indentation of all non-blank lines after the first line.
Any indentation in the first line of the docstring (i.e., up to the first newline) is insignificant
and removed. Relative indentation of later lines in the docstring is retained.
Blank lines should be removed from the beginning and end of the docstring.
Since code is much more precise than words, here is an implementation of the algorithm:
"""
def trim(docstring):
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxsize
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxsize:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)