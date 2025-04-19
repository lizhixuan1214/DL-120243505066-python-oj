height, weight = map(int, input().split())

standard = height - 110

if weight > standard + 5:
    print("fat")
elif weight < standard - 5:
    print("thin")
else:
    print("standard")
