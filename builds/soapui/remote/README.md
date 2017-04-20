Image that allows pre built SoapUI projects to be run via a REST API call. Simply POST the SoupUI saved project XML file to the exposed port and it will respond with the result. Make sure you point this at 1180 inside the container, to test (localProject.xml available at the source repo):

Also after testing with some more advanced examples I discovered that it is best to compress as well as post and receive in base64, I have updated the example to reflect this.

$ docker run --name=soapui --rm -p 1880:1880 thechane/soapui:5.3.0
$ gzip localProject.xml
$ base64 localProject.xml.gz > localProject.gz.base64
$ curl -H "Content-Type: text/xml" -d @localProject.gz.base64 -X POST http://127.0.0.1:1880/soapuiproject | base64 -d

<?xml version="1.0" encoding="UTF-8"?>
<con:testCaseRunLog testCase="localTestCase" timeTaken="51" status="FINISHED" timeStamp="2017-04-16 02:05:32" xmlns:con="http://eviware.com/soapui/config"><con:testCaseRunLogTestStep name="Hello - Request 1" timeTaken="51" status="OK" timestamp="2017-04-16 02:05:32" endpoint="http://127.0.0.1:1880/hello" httpStatus="200" contentLength="5" readTime="4" totalTime="50" dnsTime="0" connectTime="29" timeToFirstByte="17" httpMethod="GET" ipAddress="127.0.0.1"/></con:testCaseRunLog>


This was written to facilitate the testing of Docker (swarm mode) services. 
