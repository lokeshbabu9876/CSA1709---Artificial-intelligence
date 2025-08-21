import itertools

# Crypt-Arithmetic Problem: SEND + MORE = MONEY
def solve_cryptarithm():
    letters = ('S','E','N','D','M','O','R','Y')
    digits = range(10)
    
    for perm in itertools.permutations(digits, len(letters)):
        assign = dict(zip(letters, perm))
        
        # Skip if S or M is 0 (leading digit cannot be zero)
        if assign['S'] == 0 or assign['M'] == 0:
            continue
        
        # Construct numbers
        send = assign['S']*1000 + assign['E']*100 + assign['N']*10 + assign['D']
        more = assign['M']*1000 + assign['O']*100 + assign['R']*10 + assign['E']
        money = assign['M']*10000 + assign['O']*1000 + assign['N']*100 + assign['E']*10 + assign['Y']
        
        if send + more == money:
            print("Solution Found:")
            print(f"SEND  = {send}")
            print(f"MORE  = {more}")
            print(f"MONEY = {money}")
            print("Mapping:", assign)
            return
    
    print("No solution exists")

# Run the solver
solve_cryptarithm()
