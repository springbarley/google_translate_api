#coding:utf-8
import httplib
import urllib
import urllib2
import sys
import socket

reload(sys)
sys.setdefaultencoding("utf-8")


socket.setdefaulttimeout(10)
urllib2.socket.setdefaulttimeout(10)

class google_translate_httpclient(object):
    def __init__(self, url):
        self.url = url
        self.request_header = {
                               'Host':"translate.google.cn",
                               'User-Agent': "Mozilla/5.0 (Windows NT 5.1; rv:23.0) Gecko/20100101 Firefox/23.0",
                               'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                               'Accept-Language': "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
                               'Accept-Encoding': "utf-8",
                               'Referer': "http://translate.google.cn/?hl=en",
                               'Cookie': "PREF=ID=e9d916e5c18989bf:U=65f53d5f8faf84ef:NW=1:TM=1374476960:LM=1375319033:S=Cz2f3vwhINJfOt2E; NID=67=fQHqTLOvGNeZSKU8YTVAZhPdfZXZzj310tE5gsHqCQvR9JV7wIafDMXM1aFOAGzBODIY6BKfrMLlZybQc7FbGLhFn5mHuumzVd7W4iXMmB528_ZOrIT411IUalx7UjQN",
                               'Connection': "keep-alive"
        }
        self.parameters = {'client':"t",
                            'sl':"zh-CN",
                            'tl':"ja",
                            'hl': "en",
                           'sc': "2",
                           'ie': "UTF-8",
                           'oe':"UTF-8",
                           'rom':"1",
                           'srcrom':"1",
                           'prev':"btn",
                           'ssel': "0",
                           'tsel': "4",
                           'q':"test",
                          }

    def set_language(self, in_language, out_language):
        self.parameters["s1"] = in_language
        self.parameters["tl"] = out_language

    def set_query_key_word(self, key_word):
        self.parameters["q"] = key_word

    def get_response(self):
        self.conn = httplib.HTTPConnection(self.url, 80)
        self.conn.request(method='GET', url =  '/translate_a/t?' + urllib.urlencode(self.parameters), headers=self.request_header)
        response = self.conn.getresponse()
        response_stream = open("D:/translate.txt", 'w')
        if response.status == 302:
            print(response.read())
        elif response.status == 404:
            print("page not found!")
        elif response.status == 403:
            print("something error!")
        else:
            response_stream.write(response.read())

        response_stream.close()

    def __del__(self):
        self.conn.close()

class google_translate_urllib2(object):
    def __init__(self, url):
        self.url = url
        self.request_header = {
                               'Host':"translate.google.cn",
                               'User-Agent': "Mozilla/5.0 (Windows NT 5.1; rv:23.0) Gecko/20100101 Firefox/23.0",
                               'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                               'Accept-Language': "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
                               'Accept-Encoding': "utf-8",
                               'Referer': "http://translate.google.cn/?hl=en",
                               'Cookie': "PREF=ID=e9d916e5c18989bf:U=65f53d5f8faf84ef:NW=1:TM=1374476960:LM=1375319033:S=Cz2f3vwhINJfOt2E; NID=67=fQHqTLOvGNeZSKU8YTVAZhPdfZXZzj310tE5gsHqCQvR9JV7wIafDMXM1aFOAGzBODIY6BKfrMLlZybQc7FbGLhFn5mHuumzVd7W4iXMmB528_ZOrIT411IUalx7UjQN",
                               'Connection': "keep-alive"
        }
        self.parameters = {'client':"t",
                          'sl':"zh-CN",
                           'tl':"ja",
                            'hl': "en",
                           'sc': "2",
                           'ie': "UTF-8",
                           'oe':"UTF-8",
                           'oc':"1",
                           'prev':"conf",
                           'psl':"zh-CN",
                           'ptl':"en",
                           'otf':"1",
                           'srcrom':"1",
                           'it':"sel.89531,tgtd.8774",
                           'ssel': "4",
                           'tsel': "4",
                           'q':"test",
                          }
    def set_language(self, in_language, out_language):
        self.parameters["s1"] = in_language
        self.parameters["tl"] = out_language

    def set_query_key_word(self, key_word):
        self.parameters["q"] = key_word

    def get_response(self):
        httpHandler = urllib2.HTTPHandler(debuglevel=1)
        httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
        opener = urllib2.build_opener(httpHandler, httpsHandler)
        urllib2.install_opener(opener)

        try:
            request = urllib2.Request('http://' + self.url + '/translate_a/t?'+ urllib.urlencode(self.parameters), headers = self.request_header)
            response = urllib2.urlopen(request)
            print(response.read())
            response_stream = open("D:/translate.txt", 'w')
        except urllib2.HTTPError, e:
            print(e.getcode())
            response_stream.write(response.read())


        response_stream.close()

if __name__ == "__main__":
    gl = google_translate_httpclient("translate.google.cn")
    gl.set_language("zh-CN", "ja")
    gl.set_query_key_word("美国")
    gl.get_response()
