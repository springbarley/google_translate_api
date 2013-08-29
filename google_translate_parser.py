#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class TreeNode(object):
    '''build a left child, right brother tree

    parser like a hierarchical auto state machine'''
    def __init__(self):
        self.child = None
        self.brother = None
        self.value = None
        self.already_has_node = False
        self.value = ""

    '''if high level node doesn't has a child, than add a child,
        else add the brother of the child of the high level node'''
    def add_child_or_brother_of_child(self,node):
        if not self.already_has_node:
            return self.add_a_child(node)
        else:
            return self.child.get_right_most_brother().add_a_brother(node)

    def add_a_child(self, node):
        assert self.already_has_node == False
        self.child = node
        self.already_has_node = True
        return node

    def add_a_brother(self, brother_node):
        self.brother = brother_node
        return brother_node

    def get_right_most_brother(self):
        right_brother_node = self
        while(right_brother_node.brother != None):
            right_brother_node = right_brother_node.brother
        return right_brother_node
    def add_chara_to_value(self, chara):
        self.value += chara

    def get_child(self):
        return self.child
    def get_brother(self):
        return self.brother
    def has_brother(self):
        if not self.brother:
            return self.brothe
        return None
class ParserTree(object):
    def __init__(self):
        self.root_node = TreeNode()
        self.stack = []
        self.stack.append(self.root_node)

    def do_parse(self, json_result):
        '''parse the json_result to get a parse tree,

        when meet the '[', push a node in stack
        when meet the ']', pop a node in stack
        else append the string as the value of current node of stack'''
        for chara in json_result:
            if chara == '[':
                new_node = TreeNode()
                self.stack[len(self.stack) - 1].add_child_or_brother_of_child(new_node)
                self.stack.append(new_node)
            elif chara == ']':
                self.stack.pop()
            else:
                self.stack[len(self.stack) - 1].add_chara_to_value(chara)
        if len(self.stack) == 1:
            print("syntax right")
        else:
            print("syntax error")
        print("parser done")

    '''todo
        print the tree style in console'''
    def show_parser_tree(self):
        root_node = self.root_node
        pass

    def fetch_best_result(self):
        node_value_result = []
        now_node = self.root_node.child.child.child
        node_value_result.append(now_node.value)

        while now_node != None:
            node_value_result.append(now_node.value)
            now_node = now_node.get_brother()

        '''collect the result beside description items in node_value[0] to get translate result'''
        result = [item[item.find("\""):item.find(",") - 1] for item in node_value_result]
        return result

if __name__ == "__main__":
    parser = ParserTree()
    json_result = r'''[[["GOMEとアプライアンスです\n","国美和家电都是","Gome to apuraiansudesu","Guóměi hé jiādiàn dōu shì"],["コンピュータ\n","电脑","Konpyūta","Diànnǎo"],["また\n","还有","Mata","Hái yǒu"],["この\n","这个","Kono","Zhège"],["この爬虫類はそれを遅く","这个爬虫太慢了吧","Kono hachūrui wa sore o osoku","Zhège páchóng tài mànle ba"]],,"zh-CN",,[["GOME",[4],0,0,961,0,1,0],["と",[5],0,0,460,1,2,0],["アプライアンスです",[6],0,0,460,2,4,0],["\n",,0,0,0,0,0,0],["コンピュータ",[15],0,0,537,0,1,1],["\n",,0,0,0,0,0,0],["また",[27],0,0,965,0,1,1],["\n",,0,0,0,0,0,0],["この",[42],0,0,850,0,1,1],["\n",,0,0,0,0,0,0],["この",[60],0,0,1000,0,1,1],["爬虫類",[61],0,0,998,1,2,1],["はそれを",[62],0,0,387,2,5,1],["遅く",[63],0,0,277,5,6,1]],[["国",4,[["GOME",961,0,0],["国美",38,0,0],["込め",0,0,0],["Gomeは",0,0,0],["GOMEの",0,0,0]],[[0,1]],"国美和家电都是"],["和",5,[["と",460,0,0],["や",44,0,0],["および",34,0,0],["及び",20,0,0],["し",0,0,0]],[[2,3]],""],
    ["家电 都是",6,[["アプライアンスです",460,0,0],["アプライアンスは",0,0,0],["アプライアンスが",0,0,0],["アプライアンスには",0,0,0]],[[3,7]],""],["电脑",15,[["コンピュータ",537,0,0],["コンピューター",462,0,0],["のコンピュータ",0,0,0],["コンピュータの",0,0,0]],[[0,2]],"电脑"],["还有",27,[["また",965,0,0],["さらに",34,0,0],["も",0,0,0]],[[0,2]],"还有"],["这个",42,[["この",850,0,0],["これ",149,0,0],["本",0,0,0],["これは",0,0,0]],[[0,2]],"这个"],["这个",60,[["この",1000,0,0],["これ",0,0,0],["これは",0,0,0],["本",0,0,0]],[[0,2]],"这个爬虫太慢了吧"],["爬虫",61,[["爬虫類",998,0,0],
    ["は虫類",0,0,0],["ハ虫類",0,0,0],["ハ虫",0,0,0],["レプタイル",0,0,0]],[[2,4]],""],["爬虫 吧",62,[["はそれを",387,0,0],["がそれを",36,0,0],["それを",0,0,0],["これを",0,0,0]],[[2,4],[7,8]],""],["太慢",63,[["遅く",277,0,0],["遅らせる",137,0,0],["遅くなる",0,0,0],["鈍化",0,0,0],["遅くする",0,0,0]],[[4,6]],""]],,,[["zh-CN"]],29]'''
    json_result.replace('\n', '')
    parser.do_parse(json_result)
    result = parser.fetch_best_result()
    result = [item.decode() for item in result]
    print("".join(result))