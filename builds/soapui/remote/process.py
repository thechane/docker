#!/usr/bin/env python

import sys, base64, gzip, os
from StringIO import StringIO
from subprocess import check_output, CalledProcessError

try:
    os.remove("/tmp/go.xml")
except OSError:
    pass

file = ' '.join(sys.argv[1:])
splitFile = file.split('*')
endpoint = splitFile.pop()
goXML = open("/tmp/go.xml", "w")
goXML.write(gzip.GzipFile(fileobj=StringIO(base64.b64decode(''.join(splitFile)))).read())
goXML.close()

try:
    if endpoint == "null":
        print check_output(["testrunner.sh", "-f", "/tmp", "-M", "/tmp/go.xml"], stderr=sys.stdout.fileno())
    else:
        print check_output(["testrunner.sh", "-f", "/tmp", "-M", "-e", endpoint, "/tmp/go.xml"], stderr=sys.stdout.fileno())
except CalledProcessError, e:
    resXML = open("/tmp/test_case_run_log_report.xml", "w")
    resXML.write("CalledProcessError during execution : " + str(e))
    resXML.close()

