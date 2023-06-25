def cookies(childs, cookies):
    childs.sort()
    cookies.sort()
    count = 0
    childs_ptr = len(childs) - 1
    cookies_ptr = len(cookies) - 1
    while childs_ptr >= 0 and cookies_ptr >= 0:
        if cookies[cookies_ptr] >= childs[childs_ptr]:
            count += 1
            cookies_ptr -= 1
            childs_ptr -= 1
        else:
            childs_ptr -= 1
    return count


print(cookies([10, 9, 8, 7], [5, 6, 7, 8]))
