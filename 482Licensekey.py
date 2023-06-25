def lk(s, k):
    s = s.replace("-", "").upper()[::-1]
    st = ""
    for i in range(0, len(s), k):
        st += s[i : i + k] + "-"
    st = st[::-1]
    st = st.replace("-", "", 1)
    return st


s = "2-5g-3-J"
k = 2
print(lk(s, k))
