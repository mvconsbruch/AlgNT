# solutions.py

MOD = 27

# Use a,b,c in place of a',b',c'.
def f(a,b,c,m):
    return ( a*a*a + m*b*b*b + m*m*c*c*c - 3*m*a*b*c ) % MOD

solutions_found = False 
for a in range(MOD):
    for b in range(MOD):
        for c in range(MOD):
            # skip pairs with everything divisible by 3 
            if a % 3 == 0 and b%3 == 0 and c%3 == 0: 
                continue

            for m in range(MOD):
                # skip pairs with m == +-1 mod 9
                # or 3|m.
                if (m+1)%9 == 0 or (m-1)%9 == 0 or m%3 == 0:
                    continue

                if f(a,b,c,m) == 0:
                    solutions_found = True
                    print(f"Solution found! (a,b,c,m) = ({a},{b},{c},{m})")

if solutions_found == False:
    print("There are no solutions.")
