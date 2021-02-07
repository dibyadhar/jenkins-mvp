# Install and Run Jenkins as standalone application

 Jenkins uses an embedded application server (Jetty) and can be invoked from the command line

1. [Download Jenkins](https://www.jenkins.io/download/).

2. Open up a terminal in the download directory.

3. Run `java -jar jenkins.war --httpPort=8080`.

4. Browse to http://localhost:8080.

----

# Advanced Configurations 

* Anatomy of the jenkins run command (Runtime requirement => Java 8/11) 
 
   [Refer Java requirements for jenkins](https://www.jenkins.io/doc/administration/requirements/java/)

  ```
  $ java ${JAVA_OPTS} -jar jenkins.war ${JENKINS_OPTS}
  ```


* Options configured by startup flags (JENKINS_OPTS):


   |  Flag | Description | Default
   |---|---| --- |
   |  --prefix $PREFIX | Runs Jenkins to include the $PREFIX at the end of the URL  | (default: /) |
   | --httpPort $PORT  |  Jenkins listens on $PORT port  | (default: 8080) |
   | --httpListenAddress $HTTP_HOST | Binds Jenkins to the IP address represented by $HTTP_HOST |  (default: 0.0.0.0) |
   | --logfile $LOGFILE  |  write to $LOGFILE instead of stdout |  (default: stdout) 


* Advanced runtime configuration example:

  ```
   java -jar jenkins.war --httpPort=8081 --prefix=/ci --httpListenAddress=127.0.0.1
  ```

* [Jenkins command line arguemnets reference](https://www.jenkins.io/doc/book/installing/initial-settings/#networking-parameters).

