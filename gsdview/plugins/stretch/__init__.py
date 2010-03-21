# -*- coding: utf-8 -*-

### Copyright (C) 2008-2010 Antonio Valentino <a_valentino@users.sf.net>

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


'''Image stretch control for GSDView.'''

__author__   = 'Antonio Valentino <a_valentino@users.sf.net>'
__date__     = '$Date: 2010/02/14 22:02:21 $'
__revision__ = '$Revision: 36b7b35ff3b6 $'
__requires__ = []       # @TODO: move to the info file

__all__ = ['init', 'close', 'WorldmapPanel',
           'name','version', 'short_description','description',
           'author', 'author_email', 'copyright', 'license_type',
           'website', 'website_label',
]

from stretch.info import *

_controller = None

def init(mainwin):
    from PyQt4 import QtGui
    from stretch.core import StretchController

    global _controller
    _controller = StretchController(mainwin)

    mainwin.imagemenu.addSeparator()
    mainwin.imagemenu.addAction(_controller.action)

    toolbar = QtGui.QToolBar(mainwin.tr('Stretching Toolbar'))
    toolbar.setObjectName('stretchingToolbar')
    toolbar.addAction(_controller.action)
    mainwin.addToolBar(toolbar)

def close(mainwin):
    saveSettings(mainwin.settings)

def loadSettings(settings):
    pass

def saveSettings(settings):
    pass
