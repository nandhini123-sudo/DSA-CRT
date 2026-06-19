nums=2
if nums%2==0 and nums>1:
    print("even positive")
    if 100%nums==0:
        print("super number")
elif nums%2==0 and nums<0:
    print("even negative")
elif nums%2==1 and nums<0:
    print("odd positive")
elif nums%2==1 and nums>1:
    print("odd negative")
