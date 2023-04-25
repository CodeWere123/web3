def nerfed_search(vk_Id, vk_Id2):
    import vk
    import time

    api = vk.API(access_token="ab605a86ab605a86ab605a869fab1d5c5daab60ab605a86c9c8fb310fd87b6364fd592b", v="5.131")
    if "m." in vk_Id:
        vk_Id = vk_Id.replace("m.", "")
    if "http:" in vk_Id:
        vk_Id = vk_Id.replace("http:", "https:")
    if "https://vk.com/id" in vk_Id:  # тут выделение из ссылки на вк айди пользователя
        vk_Id = vk_Id[17:]
    elif "vk.com/id" in vk_Id:
        vk_Id = vk_Id[9:]
    elif "https://vk.com/" in vk_Id:
        vk_Id = vk_Id[15:]
        vk_Id = api.utils.resolveScreenName(screen_name=vk_Id, v=5.131)["object_id"]
    else:
        vk_Id = vk_Id[7:]
        vk_Id = api.utils.resolveScreenName(screen_name=vk_Id, v=5.131)["object_id"]
    f_list = api.friends.get(user_id=vk_Id, v=5.131)
    f1 = f_list["items"]
    f1_copy = f1
    time.sleep(0.017)
    removals1 = list()
    friends = api.users.get(user_id=f1, v=5.131)

    for i in friends:
        if i['is_closed']:
            removals1.append(i["id"])
    for i in f1:
        for j in removals1:
            if i == j:
                f1.remove(j)
    f1 = f1[:35]
    if "m." in vk_Id2:
        vk_Id2 = vk_Id2.replace("m.", "")
    if "http:" in vk_Id2:
        vk_Id2 = vk_Id2.replace("http:", "https:")
    if "https://vk.com/id" in vk_Id2:  # тут выделение из ссылки на вк айди пользователя
        vk_Id2 = vk_Id2[17:]
    elif "vk.com/id" in vk_Id2:
        vk_Id2 = vk_Id2[9:]
    elif "https://vk.com/" in vk_Id2:
        vk_Id2 = vk_Id2[15:]
        vk_Id2 = api.utils.resolveScreenName(screen_name=vk_Id2, v=5.131)["object_id"]
    else:
        vk_Id2 = vk_Id2[7:]
        vk_Id2 = api.utils.resolveScreenName(screen_name=vk_Id2, v=5.131)["object_id"]
    time.sleep(0.017)
    f_list2 = api.friends.get(user_id=vk_Id2, v=5.131)
    f2 = f_list2["items"]
    f2_copy = f2
    time.sleep(0.4)
    removals2 = list()

    friends2 = api.users.get(user_id=f2, v=5.131)
    for i in friends2:
        if i['is_closed']:
            removals2.append(i["id"])
    for i in f2:
        for j in removals2:
            if i == j:
                f2.remove(j)

    f2 = f2[:115]

    f1_list = list()
    for i in f1:
        time.sleep(0.017)
        try:
            f1_list.extend(api.friends.get(user_id=i, v=5.131)["items"])

        except:
            pass

    f1_list = set(f1_list)
    for i in f2:
        time.sleep(0.005)
        try:
            f2_list = set(api.friends.get(user_id=i, v=5.131)["items"])
            c = f1_list.intersection(f2_list)

            if c:
                for i in c:
                    try:
                        time.sleep(0.005)
                        f3 = api.friends.get(user_id=i, v=5.131)["items"]
                        FIRST = set(f3).intersection(set(f1_copy))
                        LAST = set(f3).intersection(set(f2_copy))

                        res = f"""

🍀Старт страница vk.com/id{vk_Id}🍀

vk.com/id{list(FIRST)[0]} --> vk.com/id{i} --> vk.com/id{list(LAST)[0]}

🍀Целевая страница vk.com/id{vk_Id2}🍀
"""
                        return res
                    except:
                        pass

        except:
            pass
    return "К сожалению связи не найдены."


def prem_search(vk_Id, vk_Id2, token):
    import vk
    import time

    api = vk.API(access_token=token, v="5.131")
    if "m." in vk_Id:
        vk_Id = vk_Id.replace("m.", "")
    if "http:" in vk_Id:
        vk_Id = vk_Id.replace("http:", "https:")
    if "https://vk.com/id" in vk_Id:  # тут выделение из ссылки на вк айди пользователя
        vk_Id = vk_Id[17:]
    elif "vk.com/id" in vk_Id:
        vk_Id = vk_Id[9:]
    elif "https://vk.com/" in vk_Id:
        vk_Id = vk_Id[15:]
        vk_Id = api.utils.resolveScreenName(screen_name=vk_Id, v=5.131)["object_id"]
    else:
        vk_Id = vk_Id[7:]
        vk_Id = api.utils.resolveScreenName(screen_name=vk_Id, v=5.131)["object_id"]
    time.sleep(0.02)
    f_list = api.friends.get(user_id=vk_Id, v=5.131)
    f1 = f_list["items"]
    f1_copy = f1
    time.sleep(0.02)
    removals1 = list()
    friends = api.users.get(user_id=f1, v=5.131)

    for i in friends:
        if i['is_closed']:
            removals1.append(i["id"])
    for i in f1:
        for j in removals1:
            if i == j:
                f1.remove(j)
    f1 = f1[:40]
    if "m." in vk_Id2:
        vk_Id2 = vk_Id2.replace("m.", "")
    if "http:" in vk_Id2:
        vk_Id2 = vk_Id2.replace("http:", "https:")
    if "https://vk.com/id" in vk_Id2:  # тут выделение из ссылки на вк айди пользователя
        vk_Id2 = vk_Id2[17:]
    elif "vk.com/id" in vk_Id2:
        vk_Id2 = vk_Id2[9:]
    elif "https://vk.com/" in vk_Id2:
        vk_Id2 = vk_Id2[15:]
        vk_Id2 = api.utils.resolveScreenName(screen_name=vk_Id2, v=5.131)["object_id"]
    else:
        vk_Id2 = vk_Id2[7:]
        vk_Id2 = api.utils.resolveScreenName(screen_name=vk_Id2, v=5.131)["object_id"]
    time.sleep(0.02)
    f_list2 = api.friends.get(user_id=vk_Id2, v=5.131)
    f2 = f_list2["items"]
    f2_copy = f2
    time.sleep(0.7)
    removals2 = list()
    friends2 = api.users.get(user_id=f2, v=5.131)
    for i in friends2:
        if i['is_closed']:
            removals2.append(i["id"])
    for i in f2:
        for j in removals2:
            if i == j:
                f2.remove(j)
    f2 = f2[:115]
    f1_list = list()
    for i in f1:
        time.sleep(0.017)
        try:
            f1_list.extend(api.friends.get(user_id=i, v=5.131)["items"])
        except:
            pass
    f2_list = list()
    for i in f2:
        time.sleep(0.005)
        try:
            f2_list.extend(api.friends.get(user_id=i, v=5.131)["items"])

        except:
            pass

    f1_list = set(f1_list)
    f2_list = set(f2_list)
    c = f1_list.intersection(f2_list)

    if len(c) != 0:
        c = list(c)
        time.sleep(0.9)
        f3 = api.users.get(user_id=c, v=5.131)
        removals3 = list()
        for i in f3:
            if i['is_closed']:
                removals3.append(i["id"])
        for i in c:
            for j in removals3:
                if i == j:
                    c.remove(j)
        chains = """
"""

        try:
            c = c[:4]
        except:
            pass

        for i in c:
            time.sleep(0.05)
            MIDDLE = i
            f3 = api.friends.get(user_id=MIDDLE, v=5.131)["items"]
            FIRST = set(f3).intersection(set(f1_copy))
            LAST = set(f3).intersection(set(f2_copy))
            chains += f"🍀🍀🍀🍀Цепочка:  vk.com/id{list(FIRST)[0]} --> vk.com/id{MIDDLE} --> vk.com/id{list(LAST)[0]}🍀🍀🍀🍀\n"

        res = f"""
    ⛵Ваша страница: vk.com/id{vk_Id}
{chains}
    ⛺Целевая страница vk.com/id{vk_Id2}
"""
        return res
    else:
        res = "Цепочка отстутвует!"
    return res
