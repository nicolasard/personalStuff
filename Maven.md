### Maven
This is my personal quick guide of how to use maven and what are my favourites plugin you can use.

#### Profiles 
https://maven.apache.org/guides/introduction/introduction-to-profiles.html

#### Properties
https://maven.apache.org/pom.html#properties

#### Spotless Plugin
This is a nice plugin to keep the code writen folloing the same code style (format) conventions. You can find the doc here.

This is a nice plugin config for your pom.xml

```
  <plugin>
    <groupId>com.diffplug.spotless</groupId>
    <artifactId>spotless-maven-plugin</artifactId>
		<version>2.28.0</version>
		  <configuration>
        <formats>
				  <format>
					  <includes>
						  <include>*.md</include>
						  <include>*.java</include>
						  <include>.gitignore</include>
					  </includes>
						<trimTrailingWhitespace/>
						<endWithNewline/>
						<indent>
						  <tabs>true</tabs>
						  <spacesPerTab>4</spacesPerTab>
						</indent>
					</format>
				</formats>
				<java>
				  <googleJavaFormat>
					<version>1.8</version>
					  <style>AOSP</style>
						<reflowLongStrings>true</reflowLongStrings>
					</googleJavaFormat>
				</java>
			</configuration>
			<executions>
			  <execution>
				  <goals>
					  <goal>check</goal>
					</goals>
				  <phase>compile</phase>
			  </execution>
		  </executions>
  </plugin>
```

#### Check dependency tree
This command will show the dependency tree for the project
```mvn dependency:tree ```


#### SQL-Scripts versioning with "Flyway DB"

Flyway DB is a great SQL script versioning system.

https://sajeerzeji44.medium.com/spring-boot-flyway-db-version-control-integration-1df2e90474e6

#### Debuging spring-boot apps 
Not sure if this is the best place to document this, but I don´t want to lose this command.

Note that the command could vary on the version of java running and the version of spring-boot.

```
Air-von-nico :: ~/workspaces/demo-project ‹master› » java --version
openjdk 17.0.8 2023-07-18
IBM Semeru Runtime Open Edition 17.0.8.0-m1 (build 17.0.8+5)
Eclipse OpenJ9 VM 17.0.8.0-m1 (build v0.40.0-release-b9cd65edd, JRE 17 Mac OS X amd64-64-Bit Compressed References 20230718_464 (JIT enabled, AOT enabled)
OpenJ9   - b9cd65edd
OMR      - 0e572348b
JCL      - 037408d4b91 based on jdk-17.0.8+5)
Air-von-nico :: ~/workspaces/demo-project ‹master› » mvn spring-boot:run -Dspring-boot.run.jvmArguments="-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=y,address=5005" 
[INFO] Scanning for projects...
[INFO] 
[INFO] ------------------------< ar.nic:demo-project >-------------------------
[INFO] Building demo-project 1.0-SNAPSHOT
[INFO]   from pom.xml
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] >>> spring-boot:3.0.6:run (default-cli) > test-compile @ demo-project >>>
[INFO] 
[INFO] --- resources:3.3.1:resources (default-resources) @ demo-project ---
[INFO] Copying 1 resource from src/main/resources to target/classes
[INFO] Copying 0 resource from src/main/resources to target/classes
[INFO] 
[INFO] --- compiler:3.10.1:compile (default-compile) @ demo-project ---
[INFO] Nothing to compile - all classes are up to date
[INFO] 
[INFO] --- resources:3.3.1:testResources (default-testResources) @ demo-project ---
[INFO] skip non existing resourceDirectory /Users/john.dietz/workspaces/demo-project/src/test/resources
[INFO] 
[INFO] --- compiler:3.10.1:testCompile (default-testCompile) @ demo-project ---
[INFO] No sources to compile
[INFO] 
[INFO] <<< spring-boot:3.0.6:run (default-cli) < test-compile @ demo-project <<<
[INFO] 
[INFO] 
[INFO] --- spring-boot:3.0.6:run (default-cli) @ demo-project ---
[INFO] Attaching agents: []
Listening for transport dt_socket at address: 5005
```

