import std/[strutils, sequtils, algorithm]

let D = 
    readAll(stdin)
    .strip()
    .split("\n")
    .map(
        proc (item: string): seq[int] =
            item.split("x").map(parseInt).sorted()
    )

proc partOne(): int =
    for dim in D:
        let
            l = dim[0]
            w = dim[1]
            h = dim[2]
            side1 = l * w
            side2 = w * h
            side3 = h * l
            smallest = min([side1, side2, side3])

        result += smallest + 2 * (side1 + side2 + side3)

proc partTwo(): int =
    for dim in D:
        let
            P = 2 * dim[0] + 2 * dim[1]
            V = dim[0] * dim[1] * dim[2]

        result += P + V

when isMainModule:
    echo partOne() 
    echo partTwo() 