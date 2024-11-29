# Setting environment variables

## About this task

To set environment variables:

## Procedure

1. Open the appropriate process application or toolkit in the designer and click Environment
Variables.
2. Click + to add a new variable. 

Tip: To copy a variable from other process application or toolkits, click Import an environment
variable. This is an easy way to add environment variables that are referred to by
artifacts copied or moved from other process application or toolkits.
3. Click the <NEW VARBL> placeholder in the Key cell, type the name
of the new environment variable, and press Enter.  Environment variable names must be
valid JavaScript identifiers (they must begin with a letter or a '\_' and can
contain only letters, digits or the '\_' character). The following examples are all
valid names: ecmsystem\_port , ecmSystem\_port, and
ecm\_system\_port.
4. Click the Default cell for the newly entered variable, type in a value, and press Enter. 
If you know the value for the Development, Test, Staging, or Production environment, click the
appropriate cell, type in the value, and press Enter. If you do not know the appropriate value for
each environment, you can leave the setting blank and an administrator can provide the correct value
after installation. If you do not provide a value for an environment and an administrator does not
provide a value after installation, the default is used.
5. To use one of the preceding variables in a script in the current process application, you can use the variable
key preceded by tw.env. For example, to set the value of a process variable to an
environment variable in a JavaScript, you can type: tw.local.port =
tw.env.ecmsystem\_port. If the environment variable you want to use in your script is in a
toolkit, you can precede the variable key with tw.env.toolkit.[toolkit\_acronym].
So, to use the same environment variable from a toolkit with an acronym of BA, you can type:
tw.local.port = tw.env.toolkit.BA.ecmsystem\_port
6. To remove an environment variable, click the cell of the variable and then
X.