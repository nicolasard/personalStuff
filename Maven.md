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

