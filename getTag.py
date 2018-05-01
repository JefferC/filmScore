# coding:utf-8

import re

a = '''<a href="javascript:" class="tab-i ckc" data-value="117">轻改</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="81">萌系</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="70">搞笑</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="20">热血</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="104">催泪</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="5">后宫</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="105">机战</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="82">基腐</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="110">恋爱</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="6">百合</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="125">伪娘</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="71">科幻</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="115">乙女</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="57">奇幻</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="124">推理</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="72">音乐</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="93">校园</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="121">偶像</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="127">社团</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="23">运动</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="9">少女</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="94">装逼</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="103">智斗</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="95">战斗</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="16">日常</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="122">魔法</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="21">治愈</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="98">声控</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="44">泡面</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="67">历史</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="87">猎奇</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="22">致郁</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="88">时泪</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="106">美食</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="24">少儿</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="138">励志</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="140">职场</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="139">神魔</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="135">漫改</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="137">原创</a>

                                    <a href="javascript:" class="tab-i ckc" data-value="136">游戏改</a>'''

a = a.replace(" ","").replace("\n\n","\n").split("\n")
r = re.compile(r".+?data-value=\"(\d+)\"\>(.+?)\</a>")

def getTag():
    dic = {}
    for i in a:
        x,y = r.findall(i)[0]
        dic[x] = y
    return dic
