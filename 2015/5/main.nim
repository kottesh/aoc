import std/[re, strutils, sets]

let D = readAll(stdin)
        .strip()
        .split("\n")

proc containsAny[T](s: string, elems: openArray[T]): bool =
    when T is char:
        var cnt: int = 0
        for c in s:
            if elems.contains(c):
                inc(cnt)
                if cnt >= 3:
                    return true
        return false
    else:
        for e in elems:
            if s.contains(e):
                return true
        return false

proc partOne(): int =
    for str in D:
        if 
            str.containsAny(['a', 'e', 'i', 'o', 'u']) and
            str.contains(re"(.)\1") and
            not str.containsAny(["ab", "cd", "pq", "xy"]):
                echo str
                inc(result)

proc partTwo(): int =
    for str in D:
        if str.contains(re"([a-z]{2}).*\1") and str.contains(re"([a-z]).\1"):
            inc(result)

when isMainModule:
    echo partOne()
    echo partTwo()