import vk
import time
import statistics

def vk_iD2(vk_Id):

    v = "5.131"  # это версия апи,ее нужно обновлять
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
    return vk_Id
def vk_info(vk_Id):
    ville = "не найдено"
    v = "5.131"  # это версия апи,ее нужно обновлять
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
    f_to_analis = 1000
    friends = list()
    count = 0
    for i in f_list["items"]:
        friends.append(i)
    sitys = list()
    shools = list()

    vuses = list()
    time.sleep(0.18)
    friends = api.users.get(user_id=friends, v=5.131, fields={"city", "schools", "education"})
    for friend in range(len(friends)):
        count += 1
        if count > f_to_analis:
            break
        sity = friends[friend]

        try:
            sitys.append(sity["city"]["title"])
        except:
            pass
        try:
            if sity['university_name'] != "":
                vuses.append(sity['university_name'])
        except:
            pass
        try:
            sitys.append(sity["city"]["title"])
        except:
            pass
        try:
            shools.append(sity["schools"][0]["name"])
        except:
            pass
        try:
            shools.append(sity["schools"][0]["name"])
        except:
            pass

    proc_shool = len(shools) / 100
    proc_city = len(sitys) / 100
    proc_vuses = len(vuses) / 100
    shool = "не найдено"
    shool_p = "Na"
    if len(shools) != 0:
        shool_p = shools.count(statistics.mode(shools)) // proc_shool
        shool = statistics.mode(shools)

    vile = "не найдено"
    vile_p = "Na"
    if len(sitys) != 0:
        vile_p = sitys.count(statistics.mode(sitys)) // proc_city
        vile = statistics.mode(sitys)
    vuse = "не найдено"
    vuse_p = "Na"
    if len(sitys) != 0:
        vuse_p = vuses.count(statistics.mode(vuses)) // proc_vuses
        vuse = statistics.mode(vuses)
    return (shool, shool_p, vile, vile_p, vuse, vuse_p)
