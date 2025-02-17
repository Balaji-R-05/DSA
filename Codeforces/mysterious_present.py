def max_envelope_chain(n, w, h, envelopes):
    # Step 1: Filter envelopes that can fit the card
    valid_envelopes = [(wi, hi, i + 1) for i, (wi, hi) in enumerate(envelopes) if wi > w and hi > h]
    
    if not valid_envelopes:
        print(0)
        return
 
    # Step 2: Sort envelopes by width (asc) and by height (desc) if widths are the same
    valid_envelopes.sort(key=lambda x: (x[0], -x[1]))
 
    # Step 3: Find LIS based on height
    from bisect import bisect_left
    
    dp = []  # Stores the height values in LIS order
    parent = [-1] * len(valid_envelopes)  # To reconstruct path
    pos = [-1] * len(valid_envelopes)  # Stores position of elements in dp
 
    for i, (wi, hi, idx) in enumerate(valid_envelopes):
        loc = bisect_left(dp, hi)  # Find the position in LIS
        
        if loc == len(dp):
            dp.append(hi)  # Extend LIS
            pos[loc] = i  # Store index of this element
        else:
            dp[loc] = hi  # Replace element in LIS
            pos[loc] = i
 
        # Track parent for backtracking
        if loc > 0:
            parent[i] = pos[loc - 1]
    
    # Step 4: Backtrack to reconstruct the sequence
    lis_length = len(dp)
    chain = []
    last = pos[lis_length - 1]  # Last index in LIS
    
    while last != -1:
        chain.append(valid_envelopes[last][2])  # Store envelope index
        last = parent[last]
 
    chain.reverse()  # Reverse to get order
 
    # Step 5: Output the result
    print(lis_length)
    print(" ".join(map(str, chain)))
 
 
 
n, w, h = map(int, input().split())
envelopes = [tuple(map(int, input().split())) for _ in range(n)]
 
max_envelope_chain(n, w, h, envelopes)