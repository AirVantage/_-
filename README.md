# _⚰

> Transitionning from `underscore` to `lodash`.

To do so we use [Grasp](http://www.graspjs.com/) to refactor using code
structure.

## How does it work?

### Prerequisites

```sh
$ npm install grasp -g
```

### Run

```sh
$ ./underscore_to_lodash --help
./underscore_to_lodash <folder with some js>
        Will run all transformations available in `rules`

```

Operates on a __single folder__ containing javascript code.
All code will be refactored following _conversions_ defined in `./rules`.

### Helper scripts

#### `capital.py`

Reads lines from _standard input_, then reports their occurrences.

```sh
$ cat sample
lapin
malin
lapin
$ cat sample | ./capital.py
1: malin
2: lapin
```
#### `install_lodash-migrate`

Straight forward name, it installs
 [lodash-migrate](https://github.com/lodash/lodash-migrate) in a project for
 __lodash →  lodash__ migrations gone bad.

 ```sh
$ ./install_lodash-migrate <where to install>
```

#### `lodash3_to_lodash4`

Draft of conversions for __lodash 3 → lodash 4__ migration.

> __Note:__ For hackers, not maintained, so far.

## Hack

You want to refactor some javascript, here is how.

### Conversions

It is just a rule enabling to change a Javascipt call to another using
[Grasp](http://www.graspjs.com/blog/2014/01/07/refactoring-javascript-with-grasp).
Once you make your rule:

1. Place it under `rules/`.
    * `$ touch rules/my/rule`
1. Make it executable.
    * `$ chmod u+x rules/my/rule`

🚀

### Checks

You might want to check that your conversion is complete.

That is why after all conversions, `underscore_to_lodash` runs some regexes to
ensure nothing is left.

You can add your regex at the end of `blacklist`.

### Limitations

So far, calls to `.chain` are handled __manually__.
