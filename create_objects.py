import pprint

# dir = '/home/adi/Dokumente/Unterricht/Physiologie/'
dir = './'


class FrageAntwort():
    #def __init__(self, question=None,answer=None,pic = None):
    question = None
    pic = None
    answer = None


def readfile():
    with open(dir + 'testfragen.md', 'r') as originalfile:
        content = originalfile.read()
        blocks = content.split('\n\n')
        questionlist = []
        for part in blocks:
            print(part)
            obj = FrageAntwort()
            for line in part.split('\n'):
                if line.startswith('F: '):
                    obj.question = line[3:]
                elif line.startswith('A: '):
                    obj.answer = line[3:]
                elif line.startswith('B: '):
                    obj.pic = line[3:]
            questionlist.append(obj)
        return questionlist

# def writefile(records):
#     with open(dir + 'prüfungsfragen.tex', 'w') as mytxtfile:
#         for item in records:
#             mytxtfile.write(item)

if __name__ == "__main__":
    questionlist = readfile()
   # pprint.pprint(questionlist)
    print(questionlist[0].question)
    print(questionlist[1].question)
    print(questionlist[2].question)
    print(questionlist[3].question)
