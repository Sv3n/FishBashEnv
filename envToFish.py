#!/usr/bin/env python

import os
import subprocess

badKeys = ['HOME', 'PWD', 'USER', '_', 'OLDPWD', 'SHLVL']
with open('profile.fish', 'w') as f:
    for key, val in os.environ.items():
        if key in badKeys:
            continue
        if key == 'PATH':
            f.write("set -e PATH\n")
            pathUnique = set(val.split(':'))
            for elem in pathUnique:
                f.write("set -gx PATH $PATH %s\n" % elem)
        else:
            f.write("set -gx %s '%s'\n" % (key, val))
