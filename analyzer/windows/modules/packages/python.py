# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from lib.common.abstracts import Package

class Python(Package):
    """Python analysis package."""

    PATHS = [
        ("HomeDrive", "Python24", "python.exe"),
        ("HomeDrive", "Python25", "python.exe"),
        ("HomeDrive", "Python26", "python.exe"),
        ("HomeDrive", "Python27", "python.exe"),
        ("HomeDrive", "Python32", "python.exe"),
        ("HomeDrive", "Python33", "python.exe"),
        ("HomeDrive", "Python34", "python.exe"),
    ]

    def start(self, path):
        python = self.get_path("Python")
        arguments = self.options.get("arguments", "")
        return self.execute(python, "%s %s" % (path, arguments))
