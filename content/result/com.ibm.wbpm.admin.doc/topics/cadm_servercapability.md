# Server capability

## Considerations for server registration

When you add a new server, it must be registered with the playback server. The registration
process checks to see whether the capability on the new server matches the capability of the
playback server; if it matches, registration succeeds. If the capabilities are out of sync between
the two servers, the new server is not registered with the playback server.

## Considerations for process applications

In order to import or test a snapshot on the playback server or deploy it on a production server,
the target server must support all of the functionality in the process application. For example, you cannot import a process application with Service Component
Architecture (SCA) modules  unless the playback server is running in an Advanced deployment
environment.