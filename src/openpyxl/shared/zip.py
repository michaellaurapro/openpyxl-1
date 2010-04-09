'''
Copyright (c) 2010 openpyxl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

@license: http://www.opensource.org/licenses/mit-license.php
@author: Eric Gazoni
'''

from zipfile import ZipFile, ZIP_DEFLATED

class ZipArchive(object):

    PACKAGE_PROPS = 'docProps'

    ARC_CORE = PACKAGE_PROPS + '/core.xml'
    ARC_APP = PACKAGE_PROPS + '/app.xml'


    def __init__(self, filename, mode = 'r'):

        self._zipfile = ZipFile(file = filename,
                                mode = mode,
                                compression = ZIP_DEFLATED,
                                allowZip64 = False)


    def add_from_string(self, arc_name, content):

        self._zipfile.writestr(arc_name, content)

    def get_from_name(self, arc_name):

        return self._zipfile.read(arc_name)

    def close(self):

        self._zipfile.close()