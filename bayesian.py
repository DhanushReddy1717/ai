p_A0 = float(input("Enter P(A=0): "))
p_A1 = 1 - p_A0
print("\nEnter P(B=0 | A=0) and P(B=0 | A=1):")
b00 = float(input("P(B=0 | A=0): "))
b01 = float(input("P(B=0 | A=1): "))
b10 = 1 - b00
b11 = 1 - b01
print("\nEnter P(C=0 | B=0) and P(C=0 | B=1):")
c00 = float(input("P(C=0 | B=0): "))
c01 = float(input("P(C=0 | B=1): "))
c10 = 1 - c00
c11 = 1 - c01
P_A = [p_A0, p_A1]
P_B_given_A = [[b00, b01], [b10, b11]]
P_C_given_B = [[c00, c01], [c10, c11]]

def joint(a, b, c):
    return P_A[a] * P_B_given_A[b][a] * P_C_given_B[c][b]
print("\nJoint Probability Table:\n")
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            print(f"P(A={a}, B={b}, C={c}) = {joint(a,b,c):.4f}")
