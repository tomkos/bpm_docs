# Verifying Process Portal in
federated environments

## Before you begin

## Procedure

1 Open the URL for the IBM® ProcessPortal verificationpage, and click Federation Verification . Table 1. Process Portal URLsfor HTTP and HTTPS Protocol Port Process Portal URL HTTP Default (80) http://BPM\_host /ProcessPortal/web\_test HTTP Non-default http://BPM\_host :port /ProcessPortal/web\_test HTTPS Default (443) https://BPM\_host /ProcessPortal/web\_test HTTPS Non-default https://BPM\_host :port /ProcessPortal/web\_test Where BPM\_host is the host name or IP addressof your Business Automation Workflow serveror routing server, and port is the port numberused for the Process Portal service. The validation checks the following configuration aspects:

| Protocol    | Port          | Process Portal URL                           |
|-------------|---------------|----------------------------------------------|
| HTTP        | Default (80)  | http://BPM\_host/ProcessPortal/web\_test       |
| HTTP        | Non-default   | http://BPM\_host:port/ProcessPortal/web\_test  |
| HTTPS       | Default (443) | https://BPM\_host/ProcessPortal/web\_test      |
| HTTPS       | Non-default   | https://BPM\_host:port/ProcessPortal/web\_test |

    - The Process Portal browser
has SSL certificates for each process federation server and federated Business Automation Workflow server
(or routing server) that it communicates with.
    - Single sign-on (SSO) is set up correctly for Process Portal.
    - A list of allowed origins exists that contains the URLs for each
process federation server and federated Business Automation Workflow server
(or routing server) that Process Portal communicates
with.
2. Follow the instructions that are displayed in the validation
page. If errors are found, you will be guided through the
steps to fix the problem.