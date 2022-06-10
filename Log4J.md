## Log4J 

Yeah, we all know log4j, but here I pretend to document something really usefull that Log4J have called MDC (Mapped diagnostic contexts). 

As is writen here (https://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/MDC.html) 

> It provides mapped diagnostic contexts. A Mapped Diagnostic Context, or MDC in short, is an instrument for distinguishing interleaved log output from different sources. Log output is typically interleaved when a server handles multiple clients near-simultaneously.

In other words, a mechanism that allows you to save among your logs identifier or info that is common to a transactional thread, like a random uuid, origin ip, etc.

