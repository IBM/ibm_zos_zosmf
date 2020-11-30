# Copyright (c) IBM Corporation 2020
# Apache License, Version 2.0 (see https://opensource.org/licenses/Apache-2.0)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import sys
import os
import filecmp
import difflib


beforepath = sys.argv[1]
afterpath = sys.argv[2]
outputpath = sys.argv[3]
before = os.path.basename(beforepath)
after = os.path.basename(afterpath)
outputfile = ''
f_write = None
html_start = '<html>\n \
    <head>\n \
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n \
        <title>IPLINFO Compare Result</title>\n \
        <style type="text/css">\n \
            table.diff {font-family:Courier; border:medium;}\n \
            .diff_header {background-color:#e0e0e0}\n \
            td.diff_header {text-align:right}\n \
            .diff_next {background-color:#c0c0c0}\n \
            .diff_add {background-color:#aaffaa}\n \
            .diff_chg {background-color:#ffff77}\n \
            .diff_sub {background-color:#ffaaaa}\n \
        </style>\n \
    </head>\n \
    <body>\n \
        <h1>IPLINFO Compare Result</h1>\n \
        <h2>' + before + '    <---->    ' + after + '<h2>\n'
html_end = '</body></html>\n'


for pds in os.listdir(beforepath):
    if pds.find('RPT.SYSINFO') > -1:
        before_pds = beforepath + '/' + pds
        after_pds = afterpath + '/' + pds.replace('ONETIME', 'IPL')
        diff_list = filecmp.dircmp(before_pds, after_pds).diff_files
        if len(diff_list) == 0:
            if f_write is None:
                outputfile = outputpath + '/compare_result_' + before + '_vs_' + after + '.html'
                f_write = open(outputfile, 'w')
                f_write.writelines(html_start)
            f_write.writelines(
                '<h3 style="color: green">No difference found between PDS: ' + pds + '    <---->    ' + pds.replace('ONETIME', 'IPL') + '</h3>\n')
        else:
            if f_write is None:
                outputfile = outputpath + '/compare_result_' + before + '_vs_' + after + '.html'
                f_write = open(outputfile, 'w')
                f_write.writelines(html_start)
            f_write.writelines('<h3 style="color: green">Compare result for PDS: ' + pds + '    <---->    ' + pds.replace('ONETIME', 'IPL') + '</h3>\n')
            hd = difflib.HtmlDiff()
            for fname in diff_list:
                f1_read = open(before_pds + '/' + fname, 'r')
                f2_read = open(after_pds + '/' + fname, 'r')
                f1_temp = sorted(f1_read.readlines())
                f2_temp = sorted(f2_read.readlines())
                output = hd.make_file(f1_temp, f2_temp, context='false')
                output_list = output.split('\n')
                find_body = False
                for res in output_list:
                    if res.find('<body>') > -1:
                        find_body = True
                        f_write.writelines('<h4>Compare result for PDS member: ' + fname + '</h4>\n')
                        continue
                    if res.find('</body>') > -1:
                        find_body = False
                    if find_body:
                        f_write.writelines(res + '\n')
                f1_read.close()
                f2_read.close()
if f_write is not None:
    f_write.writelines(html_end)
    f_write.close()
    print(outputfile)
