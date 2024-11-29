<!-- image -->

# Additional servlet tasks

The URL for access to the servlet follows this pattern:

```
http://hostname:port/TestProjectNameWeb/TestServlet
```

A
GET or a POST performs the same job. The servlet name is always TestServlet.
The servlet class is com.ibm.wbit.comptest.ct.TestServlet.

For
each test project, the set of test suites that reside in the test
project can be queried. To query the test suites, the servlet requires
a parameter named action and a value of getSuites.
This returns all the test suites in a comma delimited string.

```
http://myHost:9080/MyTestWeb/TestServlet?action=getSuites
```

Test
suites can be invoked all at once, one at a time, you can invoke a
particular test case for each test suite. To invoke all the test suites
at once, simply call the servlet with no parameters. This invokes
all the test cases in each test suite based on their order as defined
in the deployment descriptor.

```
http://myHost:9080/MyTestWeb/TestServlet
```

```
http://hostname:port/VersionTestProjectNameWeb/TestServlet
```

To
invoke a particular test suite, the servlet requires a parameter called suite with
the name of the test suite as the value. This will run the
entire list of test cases in this particular test suite.

```
http://myHost:9080/MyTestWeb/TestServlet?suite=myTestSuite
```

To
invoke only a subset of the test cases defined in a particular test
suite, the servlet requires two parameters. The first is a suite parameter
with the name of the test suite as the value. The other parameter
is called testcases with a comma separated list of
all the test cases to run as the value. Only those test cases named
in the list will be run. There can only be one value for the suite
parameter, because multiple values will cause this parameter to be
ignored and all test suites will be run instead.

```
http://myHost:9080/MyTestWeb/TestServlet?suite=MyTestSuite&testcases=testcase1,testcase2
```

The
results of the runs are returned in an XML string.

To query
for test cases, the servlet requires the action parameter to have
a value of getTestcases, and the suite parameter
to have the name of the test suite. Multiple values for suite are
allowed. This returns the test cases for all the test suites requested
in the suite parameter.

```
http://myHost:9080/MyTestWeb/TestServlet?action=getTestcases&suite=Suite1&suite=Suite2
```

If
no value is provided for the suite parameter, or no suite parameter
is found, the entire list of test cases for all the test suites is
returned.

```
http://myHost:9080/MyTestWeb/TestServlet?action=getTestcases
```

```
testsuiteName1{testcase1,testcase2,…},testsuiteName2{testcase1,…},…
```

If
you have referenced some proprietary environment variables in the
test suite editor for a component test project, test suite, or test
case, and you want to define the environment variables in the servlet
URL, you can use the following syntax:

```
http://localhost:9080/OrderTestWeb/TestServlet?DRUG=drug%20claim&AMOUNT=100&DATE=2011-07-05
```

In
the example, there are three environment variable definitions
appended to the end of the URL. Each definition must be separated
by an ampersand (&) character. In the URL, the escape code %20 is
used to encode a space because the URL does not allow certain ASCII
characters.

In the example, the three environment variables
that are defined are:

- DRUG: "drug claim"
- AMOUNT: 100
- DATE: 2011-07-05