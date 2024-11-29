# Installing a snapshot fails when single sign-on has been configured

If you receive a message similar to the
following one in your Workflow Center systemOut.log
file after installing a snapshot then it is an indication that your
single sign-on configuration needs to be updated.

```
8/29/12 2:35:14:235 EDT] 00001a91 HttpMethodBas W org.apache.commons.httpclient.HttpMethodBase processCookieHeaders 
Cookie rejected: "$Version=0; LtpaToken=Mj0K0SVfNfOK6r6+Oy6sDNAeIw0IKn5ghkYNA8KFUZuTy2SuI3bgE/EmquYoznVI3SakYJ9J3QfyqLR80/b9k46hioz/
qBRGZgh7ZpMv7GE5DCKjuSkHganqoZKvIBseI222h6zDC8Ea0jelJWAc7IQEqH0Pgpg5hJOmdt258llWxuSL9scuz+leejgDnSJE3kzThjSMvBlxYbk6J7DF8OiTHguxSwl
NS25Deud11mN3MI1L1O7vFx3FzEQ6PLdKi+4d8HYQ48755KjzNO1f4Q1/MywQWRCvXQszugmid/5batRcpgS998Hhe44OuibLeElViY+jsYQ31u/qpIB9s8yni7fx8c/k; 
$Path=/; $Domain=.ibm.com". Domain attribute ".ibm.com" violates RFC 2109: host minus domain may not contain any dots 
[8/29/12 2:35:14:237 EDT] 00001a91 AbstractSuppo I CWLLG0154I: v1 of the clone Remote login succeeded. 
[8/29/12 2:35:14:248 EDT] 00001a91 AbstractSuppo I CWLLG0714I: v1 of the clone Sending export. 
[8/29/12 2:35:14:950 EDT] 00001a91 AbstractSuppo E CWLLG0155E: v1 of the clone Installation failed. 
[8/29/12 2:35:15:005 EDT] 00001a91 GovernanceSer E com.lombardisoftware.server.ejb.governance.GovernanceEventServiceCore deploySnapshotFromGovernance 
CWLLG3512E: Governance service 'Install Snapshot' failed due the following error: 'CWLLG0155E:The install failed. Check server logs on APSEN01 for more information.'
```

To
correct the problem, fully qualify the domain name in your single
sign-on configuration on WebSphere Application Server. For example,
instead of using mycorporation.com as the domain, use rtp.raleigh.mycorporation.com.

If Lightweight Third-Party Authentication (LTPA) is being
used, you may also want to re-import the LTPA keys into WebSphere
Application Server.