# Cannot open Workplace

## Symptoms

If the workflow desktop URL
does not use the HTTPS protocol, your browser session is invalidated when you attempt to open
Workplace. You get a message
that the session is expired and that you must log in again.

## Resolving the problem

To accept the self-signed certificate, access the workflow server by using the URL of the
Workflow dashboard origin and context root, for example,
https://server:9443/teamworks. When you are prompted, accept the
certificate.

Ensure that you log in to the workflow desktop with a URL that uses https
instead of http.