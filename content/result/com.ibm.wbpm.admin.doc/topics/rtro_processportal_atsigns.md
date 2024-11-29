# Process Portal stream comments do not allow
at characters (@) that are not enclosed in double quotes or followed by a user name

## Symptom and cause

```
00000231 wle  E   CWLLG2229E: An exception occurred in an EJB call.  Error: PreparedStatementCallback; 
SQL [select t0.USER\_ID,t0.USER\_NAME,t0.FULL\_NAME,t0.PROVIDER,t0.USER\_STATE,t0.LAST\_STATE\_MODIFIED from LSW\_USR\_XREF t0 where 
UPPER(USER\_NAME) = UPPER(?)]; DB2 SQL Error: SQLCODE=-302, SQLSTATE=22001, SQLERRMC=null, DRIVER=4.21.29; nested exception is 
com.ibm.db2.jcc.am.SqlDataException: DB2 SQL Error: SQLCODE=-302, SQLSTATE=22001, SQLERRMC=null, DRIVER=4.21.29 
       com.lombardisoftware.client.delegate.BusinessDelegateException: PreparedStatementCallback; 
SQL [select t0.USER\_ID,t0.USER\_NAME,t0.FULL\_NAME,t0.PROVIDER,t0.USER\_STATE,t0.LAST\_STATE\_MODIFIED from LSW\_USR\_XREF t0 where 
UPPER(USER\_NAME) = UPPER(?)]; DB2 SQL Error: SQLCODE=-302, SQLSTATE=22001, SQLERRMC=null, DRIVER=4.21.29; nested exception is 
com.ibm.db2.jcc.am.SqlDataException: DB2 SQL Error: SQLCODE=-302, SQLSTATE=22001, SQLERRMC=null, DRIVER=4.21.29 
at com.lombardisoftware.client.delegate.BusinessDelegateException.asBusinessDelegateException(BusinessDelegateException.java:46) 
at com.lombardisoftware.client.delegate.UserGroupAPIFacadeDelegateDefault.findUserByName(UserGroupAPIFacadeDelegateDefault.java:134) 
at com.lombardisoftware.server.ejb.api.BPDInstanceCommentAPICore.findTaggedUsers(BPDInstanceCommentAPICore.java:354) 
at com.lombardisoftware.server.ejb.api.BPDInstanceCommentAPICore.parseUsersTaggedInComments(BPDInstanceCommentAPICore.java:327) 
at com.lombardisoftware.server.ejb.api.BPDInstanceCommentAPICore.addComment(BPDInstanceCommentAPICore.java:105) 
at com.lombardisoftware.server.ejb.api.BPDInstanceCommentAPICore.addComment(BPDInstanceCommentAPICore.java:95) 
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) 
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:90) 
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:55) 
at java.lang.reflect.Method.invoke(Method.java:508)
```

Most of the strings that get posted include the double-quoted at character "@",
or an @ character that is followed by a user name, as part of an email exchange
between users. The unquoted @ character is expected to be followed by a user name, and triggers a
user lookup. If no user name is provided, an error might occur.

Process Portal uses the
<taggedUser></taggedUser> markup for every @ sign mentioned in a comment, and
therefore does not prompt you to select a user name from a drop-down list. Instead, it allows you to
enter the user name after the @ character.

## Resolving the problem

This is expected behavior in Process Portal, and
no workaround is available.