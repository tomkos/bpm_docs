# Encrypting passwords for proxy settings

## Procedure

To encrypt passwords, complete the following steps:

1. From a command prompt, go to the install\_root/BPM/Lombardi/lib directory.
2. Run the java -cp utility.jar com.lombardisoftware.utility.EncryptPassword <password> command,
where <password> is the password that you want
to encrypt.   For example, run the following command:java -cp utility.jar com.lombardisoftware.utility.EncryptPassword JohnDoeThe
result is the following code:taVCmTLTWWgkTvfvavu/7g==:sROM4ZbvqRDFYMobWXqvwg==Important: If you are running the utility from a different directory,
replace utility.jar with the exact path to the utility.jar file.
3 If the utility fails with a ClassNotFoundException exception,set your Java home to the following directory before you run the utilityagain: install\_root /AppServer/java/bin/java For example:
    - java -cp install\_root/BPM/Lombardi/lib/utility.jar
com.lombardisoftware.utility.EncryptPassword JohnDoe
    - java -cp install\_root\BPM\Lombardi\lib\utility.jar
com.lombardisoftware.utility.EncryptPassword JohnDoe
4. Replace the existing encrypted password in your Business Automation Workflow configuration files as described in the topic
Configuring Proxy Settings. 

Restriction: You cannot use the EncryptPassword utility to decrypt passwords that are
already encrypted.