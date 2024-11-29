# Trying to download a document might fail with a NullPointerException

You might see a stack similar to the following example:

[1/21/20 14:33:39:505 CST] 0000066c wle E CWLLG2229E: An exception occurred in an EJB
call. Error: nulljava.lang.NullPointerException at
com.lombardisoftware.server.ejb.api.BPDInstanceDocumentAPICore$6.setValues(BPDInstanceDocumentAPICore.java:966)
at org.springframework.jdbc.core.JdbcTemplate$2.doInPreparedStatement(JdbcTemplate.java:914) at
org.springframework.jdbc.core.JdbcTemplate$2.doInPreparedStatement(JdbcTemplate.java:909) at
org.springframework.jdbc.core.JdbcTemplate.execute(JdbcTemplate.java:644) at
org.springframework.jdbc.core.JdbcTemplate.update(JdbcTemplate.java:909) at
org.springframework.jdbc.core.JdbcTemplate.update(JdbcTemplate.java:970) at
com.lombardisoftware.utility.db.spring.BPMJdbcTemplate.update(BPMJdbcTemplate.java:851) at
com.lombardisoftware.server.ejb.api.BPDInstanceDocumentAPICore.insertDocument(BPDInstanceDocumentAPICore.java:947)
at
com.lombardisoftware.server.ejb.api.BPDInstanceDocumentAPICore.createDocumentInDB(BPDInstanceDocumentAPICore.java:365)
at
com.lombardisoftware.server.ejb.api.BPDInstanceDocumentAPICore.createDocument(BPDInstanceDocumentAPICore.java:343)
at sun.reflect.NativeMethodAccessorImpl.invoke0(NativeMethod) at
sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:90) at
sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:55)

## Cause

You receive this error because documents are currently stored in older tables and, therefore,
Business Automation Workflow tries to store documents in those older
tables.

## Resolving the problem

Run the startDocumentStoreMigration command. For more information, see startDocumentStoreMigration command. After document attachments are migrated, the error no longer
occurs.