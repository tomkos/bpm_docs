# Example: Java API Context

```
P8ConnectionCache connCache = new SimpleP8ConnectionCache();
    Connection conn = connCache.getP8Connection(CE\_URI);
    Subject subject = 
        UserContext.createSubject(conn, USER\_NAME, 
                                  PASSWORD, "FileNetP8WSI");
    UserContext uc = UserContext.get();
    uc.pushSubject(subject);
    Locale origLocale = uc.getLocale();
    uc.setLocale(1);
    CaseMgmtContext origCmctx = 
        CaseMgmtContext.set(
            new CaseMgmtContext(
                new SimpleVWSessionCache(), connCache()
            )
        );
    try {
        // Code that calls the Case Java API or 
        // directly calls the CE Java API
        ...
    }
    finally {
        CaseMgmtContext.set(origCmctx);
        uc.setLocale(origLocale);
        uc.popSubject();
    }
```

```
HttpServletRequest request;
    P8ConnectionCache connCache = 
        new HttpP8ConnectionCache(request);
    VWSessionCache vwSessCache = 
        new HttpVWSessionCache(request);
    UserContext origUc = UserContext.get();
    UserContext uc = new UserContext();
    uc.setLocale(request.getLocale());
    UserContext.set(uc);
    CaseMgmtContext origCmctx = 
        CaseMgmtContext.set(
            new CaseMgmtContext(vwSessCache, connCache)
        );
    try {
        // Code that calls the Case Java API or 
        // directly calls the CE Java API
        ...
    }
    finally {
        CaseMgmtContext.set(origCmctx);
        UserContext.set(origUc);
    }

    public class HttpP8ConnectionCache 
        implements P8ConnectionCache {
        // A custom implementation of P8ConnectionCache 
        // that caches Connection objects
        // in the HttpSession of the HttpServletRequest
    }

    public class HttpVWSessionCache implements VWSessionCache {
        // A custom implementation of VWSessionCache 
        // that caches VWSession objects in the HttpSession
        // of the HttpServletRequest
    }
```