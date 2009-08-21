### Copyright (C) 2008-2009 Antonio Valentino <a_valentino@users.sf.net>

### This file is part of GSDView.

### GSDView is free software; you can redistribute it and/or modify
### it under the terms of the GNU General Public License as published by
### the Free Software Foundation; either version 2 of the License, or
### (at your option) any later version.

### GSDView is distributed in the hope that it will be useful,
### but WITHOUT ANY WARRANTY; without even the implied warranty of
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
### GNU General Public License for more details.

### You should have received a copy of the GNU General Public License
### along with GSDView; if not, write to the Free Software
### Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA.

# -*- coding: UTF8 -*-

'''Utility functions and classes for GSDView.'''

__author__   = '$Author$'
__date__     = '$Date$'
__revision__ = '$Revision$'

__all__ = ['getresource']

import os
import sys

try:
    import pkg_resources
except ImportError:
    import logging
    logging.getLogger('gsdview').debug('"pkg_resources" not found.')

from gsdview import appsite

def default_workdir():
    if sys.platform[:3] == 'win':
        return 'C:\\'
    else:
        return os.path.expanduser('~')

def _getresource(resource, package):
    try:
        return pkg_resources.resource_filename(package, resource)
    except NameError:
        # pkg_resources not available
        if '.' in package:
            fromlist = package.split('.')[:-1]
            m = __import__(package, fromlist=fromlist)
        else:
            m = __import__(package)
        datadir = os.path.dirname(os.path.abspath(m.__file__))
        return os.path.join(datadir, resource)

def getresource(resource, package=None):
    '''Return the resurce path.

    If `package` is specified (usually passing `__name__` of the called
    modile) the package resource name is returned.

    If no `package` is specified then it is assumed that resource is
    located in the common resource directory (e.g.
    `/usr/share/<PROJECTNAME>` on UNIX-like systems.

    .. note:: it is safe to use this function also if the package is
              distributed as a compressed *egg* or as standalon package
              generated using `pyinstaller <http://www.pyinstaller.org>`_.

    '''

    if package:
        if not hasattr(sys, 'frozen'):   # not packed
            return _getresource(resource, package)
        else:
            m = __import__(package)
            #if '.pyz' not in m.__file__:
            if os.path.exists(m.__file__):
                return _getresource(resource, package)
            else:
                datadir = appsite.DATADIR
    else:
        datadir = appsite.DATADIR

    return os.path.join(datadir, resource)
