def ONSquareTime(n):
    iterations = 0
    for i in range(n):
        for j in range(n):
            iterations += 1
            print(f"Iteration {iterations}: (i={i},j={j})")
    print("Total iterarions done:", iterations, "\n")

ONSquareTime(3)
ONSquareTime(4)
ONSquareTime(5)