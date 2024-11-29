<!-- image -->

# HTTP bindings overview

## HTTP import bindings

The HTTP import binding
provides outbound connectivity from Service Component Architecture
(SCA) applications to an HTTP server or applications.

- The URL can be set dynamically in the HTTP headers by way of the
dynamic override URL.
- The URL can be set dynamically in the SMO target address element.
- The URL can be specified as a configuration property on the import.

Although
HTTP invocations are always request-reply, the HTTP import supports
both one-way and two-way operations and ignores the response in the
case of a one-way operation.

## HTTP export bindings

The HTTP export binding
provides inbound connectivity from HTTP applications to an SCA application.

A
URL is defined on the HTTP export. HTTP applications that want to
send request messages to the export use this URL to invoke the export.

The
HTTP export also supports pings.

## HTTP bindings at run time

Figure 1. Flow of a
request from the SCA application to the web application

<!-- image -->

Optionally, the import with the HTTP binding
can receive data back from the web application in a response to the
request.

Figure 2. Flow of a
request from the client application to the web service.

<!-- image -->

The web service is a web application
running on the server. The export is implemented in that web application
as a servlet so the client sends its request to a URL address. The
servlet passes the request to the SCA application in the runtime.

Optionally,
the export may send data to the client application in response to
the request.