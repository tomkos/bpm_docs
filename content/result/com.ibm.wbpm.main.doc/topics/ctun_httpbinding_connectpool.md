<!-- image -->

# HTTP binding connection pool tuning

Connection pooling improves performance by avoiding the increased processor usage of creating and
disconnecting connections. The connection pool contains outbound connection objects for reuse. When
an application starts a web service over an HTTP transport, the HTTP outbound connector for the web
service locates and uses an existing connection from a pool of connections. When the response is
received, the connector returns the connection to the connection pool for reuse. The increased
processor usage needed to create and disconnect the connection is avoided. The
HTTPConnection object represents an outbound connection from the HTTP client. A
background daemon thread cleans up the closed and expired outbound connection objects in the
connection pool.

To view connection pool statistics, set a trace of
SCA.Binding.HTTPBinding=finest, which writes the HTTP binding connection pool
statistics into the trace file during each HTTP binding call.

- com.ibm.websphere.sca.http.pc.connectionKeepAlive
- com.ibm.websphere.sca.http.pc.maxConnection
- com.ibm.websphere.sca.http.pc.connectionTimeout
- com.ibm.websphere.sca.http.pc.connectionPoolCleanUpTime
- com.ibm.websphere.sca.http.pc.connectionIdleTimeout

## com.ibm.websphere.sca.http.pc.connectionKeepAlive

The property key for the keep-alive setting on the HTTP connection. This property is a switch to
enable or disable the connection pool. Set the value as true to enable and
false to disable. The default is true.

## com.ibm.websphere.sca.http.pc.maxConnection

Property to indicate the maximum size of the HTTP outbound connection pool. The default value is
50. Increase this value if many threads call the HTTP binding import
frequently.

## com.ibm.websphere.sca.http.pc.connectionTimeout

Property to indicate the connection wait timeout. If the connection pool is full and all the
connections are in use, the current thread must wait for an available connection. This property
indicates the timeout for the wait. The default value is 300 (seconds).

## com.ibm.websphere.sca.http.pc.connectionPoolCleanUpTime

Property to indicate the reap time for the clean-up thread. The default value is
180 (seconds), which means that the clean-up thread cleans up the closed and
expired outbound connection objects in the connection pool every 180 seconds.

## com.ibm.websphere.sca.http.pc.connectionIdleTimeout

Property to indicate the timeout value for an idle connection. The default value is
5 (seconds), which means that the connection object expires if it is not used for 5
seconds.