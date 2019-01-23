#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 11:46:42 2018
@author: m.yama
"""

import os, site, requests, shutil
from glob import glob

def build_antlr():
    def wget(url):
        with requests.get(url) as r:
            if r.status_code == 404:
                raise RuntimeError("Code 404 Error")
            with open(os.path.basename(url), "w") as w:
                w.write(r.read())

    builddir = os.path.join(os.environ["TEMP"], "pytsql.tmp")
    os.chdir(builddir)
    wget("https://www.antlr.org/download/antlr-4.7.2-complete.jar")
    wget("https://raw.githubusercontent.com/antlr/grammars-v4/master/tsql/TSqlLexer.g4")
    wget("https://raw.githubusercontent.com/antlr/grammars-v4/master/tsql/TSqlParser.g4")
    os.system("java -Xmx500M -cp antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 TSqlLexer.g4")
    os.system("java -Xmx500M -cp antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 TSqlParser.g4")
    libdir = site.getsitepackages()[0]
    instdir = os.path.join(libdir, "pytsql")
    os.mkdir(instdir)
    for x in glob("TSql*.py"):
        shutil.copy(x, instdir)
    shutil.rmtree(builddir, True) 
    with open(instdir + "/__init__.py", "w") as w:
        w.write("from antlr4 import *\n")
        w.write("from .TSqlParser import TSqlParser\n")
        w.write("from .TSqlLexer import *\n")
        w.write("from .TSqlParserListener import TSqlParserListener\n")

if __name__ == "__main__":
    build_antlr()