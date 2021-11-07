def solve(givenStr, wantStr):
    gs = givenStr
    ws = wantStr
    StepCounter = 0
    ReplaceCounter = 0
    RemoveCounter = 0
    AddCounter = 0
    if len(givenStr) == len(wantStr):
        for i in range(len(gs)):
            if(gs[i]!=ws[i]):
                ReplaceCounter += 1
    elif( len(givenStr) < len(wantStr)):
        
        
        StepCounter = ReplaceCounter + RemoveCounter + AddCounter
    return StepCounter  




if __name__ == "__main__":
    givenStr = input()
    wantStr = input()
    val = solve(givenStr, wantStr)
    print(val)