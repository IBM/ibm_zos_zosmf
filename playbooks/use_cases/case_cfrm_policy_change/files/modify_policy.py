# Copyright (c) IBM Corporation 2020
# Apache License, Version 2.0 (see https://opensource.org/licenses/Apache-2.0)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import sys
import json
import re

in_file_path = sys.argv[1]
out_file_path = sys.argv[2]
change_file_path = sys.argv[3]

f_read = open(in_file_path, 'r')
f_write = open(out_file_path, 'w')

with open(change_file_path, 'r') as c_read:
    policy_change_json = json.load(c_read)

f_write.writelines('DATA TYPE(CFRM) REPORT(YES)' + '\n')

find_policy = False
remove_next = False
policy_start = 'DEFINE POLICY NAME(' + policy_change_json['policy_name'] + ')'

for res in f_read:
    if res.find('1ADMINISTRATIVE') == -1 and res.find('+__________') == -1:
        if res.find('1ADMINISTRATIVE') == -1 and res.find('+__________') == -1:
            if res.find('DEFINE POLICY NAME(') > -1:
                if res.find(policy_start) > -1:
                    find_policy = True
                    f_write.writelines(res.replace('\n', '') + ' REPLACE(YES)' + '\n')
                else:
                    find_policy = False
            elif find_policy and res.find('STRUCTURE NAME(') > -1:
                find_str = False
                for str_k, str_v in policy_change_json['changed_structures'].items():
                    if res.find('(' + str_k + ')') > -1:
                        find_str = True
                        res_new = res.replace('\n', '')
                        if str_v['SIZE']:
                            res_new = re.sub(r'SIZE\((.*)\)', 'SIZE(' + str_v['SIZE'] + ')', res_new)
                        if str_v['INITSIZE']:
                            res_new = res_new + ' INITSIZE(' + str_v['INITSIZE'] + ')'
                            remove_next = True
                        f_write.writelines(res_new + '\n')
                if not find_str:
                    f_write.writelines(res)
            elif find_policy:
                if remove_next:
                    remove_next = False
                    if res.find('INITSIZE') == -1:
                        f_write.writelines(res)
                else:
                    f_write.writelines(res)

f_read.close()
f_write.close()
