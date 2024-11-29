# Verifying that the web service is working

## About this task

These steps let you determine if you have a proper, working
URL containing the expected WSDL file.

You can see the following
steps with screen captures from a previous version in this technote.

## Procedure

1. Verify that you have a live WSDL URL.
2. Paste the URL into a browser window. You may need to add
?WSDL to the end or your URL. If the URL is not working, you are likely
lacking the correct network configuration to access the web service.
3. Install soapUI using the default configuration.
4. Right-click Projects and click New
soapUI Project.
5. Paste your WSDL URL into the box labeled Initial
WSDL/WADL. Do not change the other values and options
and click OK.   You should now have a sample
call for your web service where you can make sample calls based on
XML input.
6. Test the web service by replacing question marks with actual
data inputs and press Play. There are hints
that are provided by soapUI in places where repeated entries or optional
entries exist. For these entries, deleting items should not be a problem.