def perms(nums):
    perms = [[]]
    for n in nums:
        new_perm = []
        for perm in perms:
            for i in range(len(perm) + 1):
                new_perm.append(perm[:i] + [n] + perm[i:])
                # handle duplication
                if i < len(perm) and perm[i] == n:
                    break
        perms = new_perm
    return perms
