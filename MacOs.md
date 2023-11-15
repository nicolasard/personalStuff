### MacOs
My personal notes about using Macbook devices.

##### Execute stuff downloaded from the internet
Might be very stupid, but, by default, when downloading stuff from the internet in MacOS that's not executable as is flagged with an attribute `com.apple.quarantine`.

To remove that attribute from a folder and all its content. Run the following command

```
sudo xattr -r -d com.apple.quarantine ./jdk-17.0.9.jdk#
```

##### The mac setEnv.
This is my old knowed setEnv.sh/bat adapted for the Mac that I'm using.

```
!/bin/bash

export JAVA_JDK=/Users/nicolas.ardisonfiserv.com/tools/jdk-17.0.9.jdk/Contents/Home

export PATH=$JAVA_JDK/bin:$PATH
```
