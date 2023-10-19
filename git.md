## Git compiling and tricks

### Compiling 
To compile git I just follow the steps in https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

```
$ tar -zxf git-2.0.0.tar.gz
$ cd git-2.0.0
$ make configure
$ ./configure --prefix=/usr
$ make all doc info
$ sudo make install install-doc install-html install-info
```

### Useful commands

#### Check the commit between a previous commit and the HEAD of the current branch.

```$ git log --pretty=format:"%h; date: %ci; subject:%s" 3f7f5ec24d06942d50115ab1c001573427adaf29...HEAD```

#### Disabling git auto crlf
Git by default map the line endings to the one in the system that we are working. This is not nice most of the time. So always disable it.

To check how is the status of that var:
```git config --global core.autocrlf```

To set it false:
```git config --global core.autocrlf false ```
