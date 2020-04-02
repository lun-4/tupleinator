# tupleinator

have a lot of zig code that's still in 0.5.0-land, are you sure you're ready
for 0.6.0? have you done your research and found out how energy intensitve
it is to replace every warn() call? have i got the tool for you!

zig made a large (only if you're an std.debug.warn/print-debugging addict
like me) breaking change that removed varargs and replaced them by tuples
throughout all of std.fmt some time ago between 0.5 and 0.6, and i got too
lazy to fix every instance of warn(), so i made a tool for it

```zig
// old (0.5.0)
warn("test {} {} {}", a, b, c);

// new (0.6.0)
warn("test {} {} {}", .{a, b, c});
```

it might be ok for 3 warns in a bit of code but then you look at me writing a
toy compiler and you have as many warns as there are instructions in x86

selling points:
 - python 3
 - very bad code, unmaintainable code, to the public domain, for everyone
 - this won't get all warn calls. manual tinkering required
 - generated code needs a zig fmt pass

## how use

```bash
python3 ./tupleinator.py path/to/unenlightened/code.zig > enlightened_code.zig

# profit
mv enlightened_code.zig path/to/unenlightened/code.zig
```
