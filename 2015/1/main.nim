import std/[strutils] 

let D = readAll(stdin).strip()


proc partOne(): int =
    for idx, step in D:
        if step == '(': result += 1
        else: result -= 1 

proc partTwo(): int =
    for idx, step in D:
        if step == '(': result += 1
        else: result -= 1 

        if result == -1: return idx + 1

when isMainModule:
    echo partOne()
    echo partTwo()
