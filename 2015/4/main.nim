import checksums/md5

let D = readLine(stdin)

proc partOne(): int =
    var num: int = 1
    while getMD5(D & $num)[0..4] != "00000":
        inc(num)
    
    return num
    

proc partTwo(): int =
    var num: int = 1
    while getMD5(D & $num)[0..<6] != "000000":
        inc(num)
    
    return num

when isMainModule:
    echo partOne()
    echo partTwo()
