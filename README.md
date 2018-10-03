# kattispy
This is a tool to run sample data from kattis problems. You can use this tool to help verify if your solution is correct before submitting.

At the moment only python and go are supported languages. Please keep in mind that you need to have the language installed to actually run it.

## How to use
kattispy requires at least three and up to five arguments.

```bash
$ git clone https://github.com/4ever2/kattispy.git
$ cd kattispy
$ python Main.py -prog programfile -test testdirectory -lang programlanguage
```

Required:

* -lang [specify the language of the program]
* -prog [path of file you want to test] 
* -test [path of folder containing answers]

Optional:

* -mem [maximum memory usable by the program in bytes]
* -time [maximum execution time of your program in seconds]

Sample test data can be downloaded from the kattis page for each problem



## TODO
* Add tests
* Help argument
* Handle floats properly
* Check for compile and runtime errors
* Make code modular
* Add support for more languages
  * ~~Go~~
  * ~~Python 3~~
  * Python 2
  * Node.js
  * PHP
  * Java
  * C
  * C++
  * C#
  * Haskel
  * SpiderMonkey
  * Kotlin
  * Objective-C
  * Pascal
  * Prolog
  * Ruby
  * Scala
* ~~Add documentation to README~~
* Linux support
* Add automated tests
* ~~Find sample data and load it~~
* ~~Run program and collect output~~
* ~~Verify result~~
* ~~CPU time limit~~
* ~~Memory limit~~

## Contribute
Contributions are always welcome!
