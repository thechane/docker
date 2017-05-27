#!/usr/bin/env python

import sys, base64, gzip, os
from StringIO import StringIO
from subprocess import check_output, CalledProcessError

try:
    os.remove("/tmp/go.xml")
except OSError:
    pass

fileString = ''.join(sys.argv[1:])
endpoint = None
if '*' in file:
    splitFile = fileString.split('*')
    endpoint = splitFile.pop()
    #add more here if needed later
    fileString = ''.join(splitFile)
goXML = open("/tmp/go.xml", "w")
goXML.write(gzip.GzipFile(fileobj=StringIO(base64.b64decode(fileString))).read())
goXML.close()

try:
    if endpoint is None or endpoint == "null":
        print check_output(["testrunner.sh", "-Djava.awt.headless=true", "-f", "/tmp", "-M", "/tmp/go.xml"], stderr=sys.stdout.fileno())
    else:
        print check_output(["testrunner.sh", "-Djava.awt.headless=true", "-f", "/tmp", "-M", "-e", endpoint, "/tmp/go.xml"], stderr=sys.stdout.fileno())
except CalledProcessError, e:
    resXML = open("/tmp/test_case_run_log_report.xml", "w")
    resXML.write("CalledProcessError during execution : " + str(e))
    resXML.close()

