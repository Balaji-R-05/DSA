def study_schedule(d, sumTime, limits):
    minTotal = sum(minTime for minTime, maxTime in limits)
    maxTotal = sum(maxTime for minTime, maxTime in limits)
 
    if sumTime < minTotal or sumTime > maxTotal:
        print("NO")
        return
 
    schedule = [minTime for minTime, maxTime in limits]
    remaining = sumTime - minTotal 
 
    for i in range(d):
        minTime, maxTime = limits[i]
        extra = min(maxTime - minTime, remaining)  # How much we can increase
        schedule[i] += extra
        remaining -= extra
        if remaining == 0:
            break
 
    print("YES")
    print(" ".join(map(str, schedule)))
 
d, sumTime = map(int, input().split())
limits = [tuple(map(int, input().split())) for _ in range(d)]
 
 
study_schedule(d, sumTime, limits)