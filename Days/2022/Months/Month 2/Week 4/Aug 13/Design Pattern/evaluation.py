#!/usr/bin/python
# Start
# Using Subprocess for interpreter evaluation
# Modules
import json
import subprocess
import sys 

context = dict(gnome=gnome, target='G[AC]{2}TT', replace="TCGA")
execute(code, context)

def execute(code, context):
    module, offset = create_module(code.code, context)
    with subprocess.Popen([sys.executable, "-"], stdin=subprocess.PIPE,
        stdout=subprocess.PIPE, STDERR=subprocess.PIPE) as process:
        comunicate(process, code, module, offset)
    
def create_module(code, context):
    lines = ["import json", "result = error = None"]
    for key, value in context.items():
        lines.append("{} = {!r}".format(key, value))
    offset = len(lines) + 1
    outputLine = "\nprint(json.dumps((result, error)))"
    return "\n".join(lines) + '\n' + code + outputLine, offset


# End