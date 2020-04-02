# tupleinator

update your std.debug.warn addiction with ease

zig made a large (only if you're an std.debug.warn/print-debugging addict
like me) breaking change that removed varargs and replaced them by tuples
throughout all of std.fmt

```zig
// old
warn("test {} {} {}", a, b, c);

// new
warn("test {} {} {}", .{a, b, c});
```

it might be ok for 3 warns in a bit of code but then you look at me writing a
toy compiler and you have as many warns as there are instructions in x86

 - python 3
 - very bad code, unmaintainable code, to the public domain, for everyone
 - this won't work throughout the entirety of a source file,
    manual tinkering required
 - generated code needs a zig fmt pass

## how use

```bash
python3 ./tupleinator.py path/to/unenlightened/code.zig > enlightened_code.zig

# profit
mv enlightened_code.zig path/to/unenlightened/code.zig
```
