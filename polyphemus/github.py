"""The plugin to enable github functionality.

This module is available as an polyphemus plugin by the name ``polyphemus.github``.

BaTLaB Plugin API
=================
"""
from __future__ import print_function
import sys

from .plugins import Plugin

if sys.version_info[0] >= 3:
    basestring = str

class PolyphemusPlugin(Plugin):
    """This class enables all github functionality."""

    requires = ('polyphemus.githubhook',)