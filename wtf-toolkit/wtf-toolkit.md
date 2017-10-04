%title: BTV Meetup -- The hidden programs in CPython
%author: dave@sisu.io
%date: 2017-10-04
%comment: view with textproc/mdp

-> The hidden programs in CPython <-
===

-> BTV Python Meetup <-
---

-> Dave Voutila <-
---

---

-> who am i ? <-
===

* *Independent Software Consultant*
  - Home office in Williston
  - Originally from north of Worcester, MA
* *Decade of Software Presales Engineering*
* Experienced with...
  - *Python* (you would hope)
  - *Java*
  - *C* (<3)
* *Talk to me about...*
  - Running long distances
  - Operating Systems!
  - [OpenBSD](https://openbsd.org)

---
-> let's take a journey  <-

* Have you ever spent time looking at CPython?
  - [CPython](https://github.com/python/cpython)
  - Seriously, go grab it when you can.
* Turns out you can learn a lot about Python's source
  - [datetime!](https://voutilad.github.io/meetups/datetime/datetime.pdf)
  - [weird int's](https://kate.io/blog/2017/08/22/weird-python-integers/)
* Aside: want to peg a CPU core?

```
    $ python -c 'print(1 << (1024 * 1024 * 1024))'
```

...that's been running 30m on my 2015 MacBook Pro, btw.


---
-> A rose by any other  `__name__`... <-

* Originally planned on talking about tools in *Python3*
  - `ensurepip` (recent addition)
  - `http.server` (formerly `SimpleHTTPServer`)
  - `pdb` (often overlooked)
* But, what others might there be?
  - *Assuming Python 3.6.3*
  - Counting just `.py` files...

```bash
$ find . -name '*.py' | grep -v test | wc -l
    900
```

* That's a lot of py files.

---
-> ...would run just as sweet <-

```python
if __name__ == '__main__':
        print('how many have entry points like this?')
```

* Let's do some digging...
  - look for all non-test, non-"Tools" files
  - see if they've got some instance of `__main__`


```bash
#!/bin/sh

PY=$(find ${1} -name '*.py' | grep -v -e test -e Tools)
for i in ${PY}
do
    cat ${i} | grep -i '__main__' |
        awk -v "i=${i}" '{ print i }' | sort -u
done
```

* Let's do a quick count...

```
$ ./dump.sh ~/src/python/cpython | wc -l
    192
```

---
-> just what are those files??? <-

* I'll point out some interesting ones tonight
  - but I really recommend poking around on your own!
  - lots of odd stuff in there
* 
