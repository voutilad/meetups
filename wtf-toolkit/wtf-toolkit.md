%title: BTV Meetup -- The hidden programs in CPython
%author: dave@sisu.io
%date: 2017-10-04
%comment: view with textproc/mdp

-> The hidden programs in CPython <-
===

-> BTV Python Meetup <-
-> 4 October 2017 <-
---

-> Dave Voutila <-
-> dave@sisu.io <-
---

---

-> who am i ? <-
===

* *Independent Software Consultant*
  - Home office in Williston
  - Originally from north of Worcester, MA
^
* *Decade of Software Presales Engineering*
^
* Experienced with...
  - *Python* (you would hope)
  - *Java* (my day-to-day)
  - *C* (including interop with Python/Java)
^
* *Also talk to me about...*
  - Running long distances
  - [Operating Systems](http://pages.cs.wisc.edu/~remzi/OSTEP/)
  - [OpenBSD!](https://openbsd.org) - my other OS
^
* *But not...*
  - C++
  - the Red Sox

---
-> let's take a journey!  <-

* Have you ever spent time looking at CPython?
  - [CPython](https://github.com/python/cpython)
  - Seriously, go grab it when you can.
^
* Turns out you can learn a lot about Python's source
  - [datetime!](https://voutilad.github.io/meetups/datetime/datetime.pdf)
  - [weird int's](https://kate.io/blog/2017/08/22/weird-python-integers/)
^
* Aside: want to peg a CPU core?

```
    $ python -c 'print(1 << (1024 * 1024 * 1024))'
```

...that's been running 60m on my 2015 MacBook Pro, btw.


---
-> A rose by any other  `__name__`... <-

* Originally planned on talking about tools in *Python3*
^
  - `ensurepip` (recent addition)
  - `http.server` (formerly `SimpleHTTPServer`)
  - `pdb` (often overlooked)
  - `venv` (built-in virtual env support!)
^
* But, what others might there be?
  - *Assuming Python 3.6.3*
  - Counting just `.py` files...
^

```bash
$ find . -name '*.py' | grep -v test | wc -l
    900
```

* That's a lot of py files.


---
-> ...would run just as sweet <-

* Remember Python's faux "main" function.

```python
if __name__ == '__main__':
        print('how many have entry points like this?')
```
^

* Let's do some digging...
  - look for all non-test, non-"Tools" files
  - see if they've got some instance of `__main__`
^

```bash
#!/bin/sh
# dump.sh
PY=$(find ${1} -name '*.py' | grep -v -e test -e Tools)
for i in ${PY}
do
    cat ${i} | grep -i '__main__' |
        awk -v "i=${i}" '{ print i }' | sort -u
done
```
^

* Let's do a quick count...

```bash
$ ./dump.sh ~/src/python/cpython | wc -l
    192
```

---
-> just what are those files??? <-

* I'll point out some interesting ones tonight
  - but I really recommend poking around on your own!
  - lots of odd stuff in there
^
* Some highlights:
  - XML RPC client/server examples: `xml.{server/client}`
^
  - a text-based calendar printer: `calendar`
^
  - simple text tokenizer: `tokenize`
^
  - json validator/pretty printer: `json.tool`
^
  - an nntp client/newsreader: `nntp`
^
  - telnet client: `telnetlib`
^
  - zip/gzip/tar clients
^
  - super awesome obfuscation: `encodings.rot_13`
* ...and many more...
^
* To run any, make sure you have python3 and do:

```bash
$ python3.6 -m calendar
```

---
-> a few demos! <-

* secret turtles, secret games...
  - `$ python3 -m turtledemo.nim`
^
* a clock?!
  - `$ python3 -m turtledemo.clock`
^
* a curses demo
  - `$ python3 -m curses.textpad`
^
* the nntp client to read the python mailing list
  - `$ python3 -m nntp`

---
-> that was strange wasn't it? <-

* Some take aways...
  - poke around in source code!
  - python shouldn't be trusted too much :-/
^
* Read source code.
  - Read source code?
  - Read source code!

```bash
$ git clone https://github.com/python/cpython
```

---
-> The End! <-
===

-> Thanks for playing! <-
---



-> Slides made using [mdp](https://github.com/visit1985/mdp) <-
