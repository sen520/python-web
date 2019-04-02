# coding=utf-8

#加载省信息
def get_provinces():
    with open('assets/province.json') as fr:
        raw_content = fr.read()
        # print eval(raw_content)
    return eval(raw_content)

#根据省id查找所有的市信息
def get_citys_by_provinceid(provinceid):
    with open('assets/city.json') as fr:
        raw_content = fr.read()
    citys = eval(raw_content)
    return citys[provinceid]

#根据市id查找所有的区信息
def get_areas_by_cityid(cityid):
    with open('assets/area.json') as fr:
        raw_content = fr.read()
    areas=eval(raw_content)
    return areas[cityid]

#根据省id查找所有城市/区信息
def get_citys_areas_by_provinceid(provinceid):
    citys = get_citys_by_provinceid(provinceid)
    city_id = citys[0]['id']
    areas = get_areas_by_cityid(city_id)
    return citys,areas
