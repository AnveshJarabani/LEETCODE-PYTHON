def mergetrees(r1, r2):
    if r1 is None and r2 is None:
        return None
    r1.val = r1.val if r1 else 0
    r2.val = r2.val if r2 else 0
    r3 = r1.val + r2.val
    r3.left = mergetreees(r1.left if r1 else None, r2.left if r2 else None)
    return r3
