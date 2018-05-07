# coding:utf-8
import nltk,urllib2,os#,time,pandas
import BeautifulSoup as bs
#import jieba.posseg as pseg



#Page = [str(p) for p in xrange(Page_limt)]


url_source = "http://www.dilidili.wang/tvdh/"
html_dir = r"D:\Study\Python_St\filmScore\Data\\dilidili.html"

text_dir = r"D:\Study\Python_St\filmScore\Data\dilidili.txt"

get_ornot = False
exec_html_ornot = True

_animes =[]

def get_data(url,num_dir):
    try:
        dl = urllib2.Request(url)
        dl.add_header("User-Agent","Mozilla/5.0")
        dilidili = urllib2.urlopen(dl)
        clean_it(num_dir)
        html_file = open(num_dir,'w')
        html_file.write(dilidili.read())
        return True
    except Exception as e:
        print e
        return False
    finally:
        if "dilidili" in vars():
            dilidili.close()
        if "html_file" in vars():
            html_file.close()

def Exec_Html(html_file,text_file):
    html_file_ob = open(html_file,'r')
    txt_file = html_file_ob.read()
    html_file_ob.close()
    dili = bs.BeautifulSoup(txt_file)
    anime_div = dili.findAll("div",attrs={'class':'anime_list'})[0]
    dl = anime_div.findAll("dl")
    anime_list = []
    anime_str = ""
    lt = []
    for one in dl:
        if one.find('h3').find('a').contents == []: continue
        name = one.find('h3').find('a').contents[0]
        info = one.findAll('div',attrs={'class':'d_label'})
        #print info
        location = info[0].contents[1] if len(info[0].contents)==2 else ""
        if location == u"日本":
            location = 'jp'
        elif location == u'中国':
            location = 'ca'
        else:
            continue
        age = info[1].contents[1] if len(info[1].contents)==2 else ""
        if location not in lt:lt.append(location)
        if age[:4] == '':
            age = None
        else:
            try:
                age = int(age[:4])
            except:
                age = None
        if age < 2014:
            continue
        tags = info[2].contents[1] if len(info[2].contents)==2 else ""
        played = info[3].contents[1] if len(info[3].contents)==2 else ""
        if played.isdigit():
            played = str(int(float(played)/300000))
        else:
            played = '0'
        anime_dict = {'name':name
                      ,'location':location
                      ,'age':age
                      ,'tags':tags.split('|')[0].split('/')[0].split(u'丨')[0]
                      ,'count':played}
        anime_list.append(anime_dict)
        anime_str += anime_dict['name'] + "\t" + anime_dict['location'] + "\t" + str(anime_dict['age']) + '\t'\
                     + anime_dict['tags'] + '\t' + str(anime_dict['count']) + "\n"
    _animes = anime_list
    w = open(text_file,'w')
    w.write(anime_str.encode('utf8'))
    w.close()
    return _animes

def clean_it(the_dir):
    if os.path.exists(the_dir):
        os.remove(the_dir)


# NLTK
def Nltk_get_feature(_animes):
    try:
        if _animes == {}: return False
        anime_list = []
        for e in _animes:
            nm = e.pop('name')
            ct = e.pop('count')
            #ag = e.pop('age')
            #tg = e.pop('tags')
            tune = (e,ct)
            anime_list.append(tune)
        train_set, test_set = anime_list[20:], anime_list[:20]
        # training
        classifier = nltk.NaiveBayesClassifier.train(train_set)
        print nltk.classify.accuracy(classifier, test_set)
        #print classifier.classify({'location': '中国','age':2018,'tags':'搞笑'})

        for i in [u'游戏改',u'轻小说',u'游戏',u'青春',u'小说改编',u'热血']:
            print i + u'  中国'
            print classifier.classify({'location': 'ca', 'age': 2017, 'tags':i})
            print i + u"  日本"
            print classifier.classify({'location': 'jp', 'age': 2017, 'tags':i})

        '''
        print classifier.classify({'location': 'ca'})
        print classifier.classify({'location': 'jp'})
        '''
    except Exception as e:
        print e
        return False


def main():
    if get_ornot:
        if get_data(url_source,html_dir):
            print "Get Data Done"
        else:
            print "Get Data Failed"
            exit(12)
    if exec_html_ornot:
        _animes =  Exec_Html(html_dir,text_dir)
        if _animes:
            print "Exec Html Done"
        else:
            print "Exec Html Failed"
    Nltk_get_feature(_animes)


if __name__ == "__main__":
    main()