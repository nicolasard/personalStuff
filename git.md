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
