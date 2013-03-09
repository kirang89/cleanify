#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Cleanify main script
#

import sys
import tidylib as tidy
from concurrent.futures import ThreadPoolExecutor
import os

try:
    import jsbeautifier
except ImportError:
    print "Js Beautifier module not installed."
    print "Run script install_jsbeautifier first."
    sys.exit(1)

try:
    import cssutils
except ImportError:
    print "cssutils not installed."
    sys.exit(1)

tidy.BASE_OPTIONS = {}
tidy_options = {
    "indent": 1,
    "wrap": 0,
    "output-xhtml": 0,
    "tidy-mark": 0,
    "clean": 0,
    "output-html": 1,
    "char-encoding": "utf8"
}


class Cleanify():
    def __init__(self, directory):
        self.target = directory
        self.dirstats = {}
        self.htmlfiles = []
        self.jsfiles = []
        self.cssfiles = []

    def scan(self):
        os.chdir(self.target)
        for root, dirs, files in os.walk('./'):
            for file in files:
                if file.endswith('.html'):
                    self.htmlfiles.append(os.path.join(root, file))
                elif file.endswith('.js'):
                    self.jsfiles.append(os.path.join(root, file))
                elif file.endswith('.css'):
                    self.cssfiles.append(os.path.join(root, file))
                else:
                    pass

    def clean_html(self, htmlfile):
        try:
            reader = open(htmlfile, 'r')
            content = reader.read()
            reader.close()
            document, errors = tidy.tidy_document(content, options=tidy_options)
            if document:
                writer = open(htmlfile, 'w')
                writer.write(document)
                writer.close()
            print "Cleaned", htmlfile
        except Exception, e:
            print e

    def clean_js(self, jsfile):
        try:
            res = jsbeautifier.beautify_file(jsfile)
            if res:
                fileWriter = open(jsfile, 'w')
                fileWriter.write(res)
                fileWriter.close()
            print "Cleaned", jsfile
        except Exception, e:
            print e

    def clean_css(self, cssfile):
        try:
            content = cssutils.parseFile(cssfile)
            if content:
                writer = open(cssfile, 'w')
                writer.write(content)
                writer.close()
            print "Cleaned", cssfile
        except Exception, e:
            print e

    def clean(self):
        self.scan()
        hlen = len(self.htmlfiles)
        jlen = len(self.jsfiles)
        clen = len(self.cssfiles)
        hc = 0
        jc = 0
        cc = 0
        print self.htmlfiles
        if hlen > 0 or jlen > 0 or clen > 0:
            print "we've got some files"
            workers = 5
            print workers, " workers created"
            with ThreadPoolExecutor(max_workers=workers) as executor:
                for hfile in self.htmlfiles:
                    executor.submit(self.clean_html, hfile)
                    hc += 1
                for jfile in self.jsfiles:
                    executor.submit(self.clean_js, jfile)
                    jc += 1
                for cfile in self.cssfiles:
                    executor.submit(self.clean_css, cfile)
                    cc += 1
                executor.shutdown()
            print "Cleaning completed."
            print "Cleaned ", hc, " html files, ", jc, " js files and ", cc, " css files"
        else:
            print "No html, js or css files found."
            sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.isdir(sys.argv[1]):
            project_dir = sys.argv[1]
            cleanify = Cleanify(project_dir)
            cleanify.clean()
        else:
            print "Invalid directory"
            sys.exit(1)
