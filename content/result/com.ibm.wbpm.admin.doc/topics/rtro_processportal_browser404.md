# Process Portal:
404 Not found error

## Overview

Some browsers use a small icon
(favicon.ico) to enhance the display of address
bar information. When a user logs in to Process Portal, the
browser tries to locate the favicon.ico file.

If
the file cannot be found, users receive an HTTP 404 "Not found" message
indicating that the favicon.ico URL could not
be found on the server.

## Resolving the problem

1. Create a favicon.ico file.
2. Depending on your environment, complete one of the following steps:

- For environments without a reverse proxy server, put the favicon.ico file
in the web server's root directory.
- For
environments where a reverse proxy server, such as IBM® Security Access
Manager WebSEAL, is connected to the web
server, create a /favicon.ico junction from the reverse proxy server to the web
server, and put the favicon.ico file in the junction-root
directory.