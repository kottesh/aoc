import std/[sets]

let D = readAll(stdin)

type
    Pos = tuple[x, y: int]

proc mover(x: var int, y: var int, dir: char): void =
    case dir
    of '^': inc(y)
    of 'v': dec(y)
    of '>': inc(x)
    of '<': dec(x)
    else: discard

proc partOne(): int =
    var visited = initHashSet[Pos]()
    var x, y: int
    x = 0
    y = 0

    visited.incl (x, y)

    for dir in D:
        mover(x, y, dir)
        visited.incl (x, y)
    
    visited.len

proc partTwo(): int =
    var visited = initHashSet[Pos]()
    var 
        x1, y1, x2, y2: int
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    for idx, dir in D:
        if idx mod 2 == 0: 
            mover(x1, y1, dir)
            visited.incl (x1, y1)
        else:
            mover(x2, y2, dir)
            visited.incl (x2, y2)

    visited.len

when isMainModule:
    echo partOne()
    echo partTwo()
