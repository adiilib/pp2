d = {
    "ZER":"0","ONE":"1","TWO":"2","THR":"3","FOU":"4",
    "FIV":"5","SIX":"6","SEV":"7","EIG":"8","NIN":"9"
}
r = {v:k for k,v in d.items()}

s = input()

for op in "+-*":
    if op in s:
        a, b = s.split(op)

        x = int("".join(d[a[i:i+3]] for i in range(0,len(a),3)))
        y = int("".join(d[b[i:i+3]] for i in range(0,len(b),3)))

        ans = eval(f"{x}{op}{y}")

        print("".join(r[c] for c in str(ans)))
        break
