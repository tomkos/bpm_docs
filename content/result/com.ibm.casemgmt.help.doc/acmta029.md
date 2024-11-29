# Unreadable characters for non-English locales in the Case configuration tool on AIX

## Symptoms

## Resolving the problem

```
export LC\_ALL=locale
export LANG=locale
```

You can get a list of available locales on your system by running the following command:
locale -a.

```
export LC\_ALL=FR\_FR.UTF-8
export LANG=FR\_FR.UTF-8
```

For a list of the common locales that can be used with Case configuration tool on AIX, see Supported languages and locales.