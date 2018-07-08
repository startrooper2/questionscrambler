from random import randint

templatedir = './templates/'
outputdir = './output/'
questiondir = './'


class FrageAntwort():
    # def __init__(self, question=None,answer=None,pic = None):
    question = None
    pic = None
    answer = None
    points = None


def readfile():
    with open(questiondir + 'testfragen.md', 'r') as originalfile:
        content = originalfile.read()
        blocks = content.split('\n\n')
        questionlist = []
        totalpoints = 0
        for part in blocks:
            obj = FrageAntwort()
            for line in part.split('\n'):
                if line.startswith('F: '):
                    obj.question = line[3:]
                elif line.startswith('A: '):
                    obj.answer = line[3:]
                elif line.startswith('B: '):
                    obj.pic = line[3:]
                elif line.startswith('P: '):
                    obj.points = line[3:]
                    totalpoints += int(obj.points)
            questionlist.append(obj)
        return questionlist, totalpoints


def copytemplate(input, output):
    with open(input, 'r') as originalfile:
        content = originalfile.readlines()
    with open(output, 'a') as mytexfile:
        for item in content:
            mytexfile.write(item)


def insert(ques):
    with open(outputdir + 'automated.tex', 'a') as mytexfile:
        for item in ques:
            #  print(item)
            mytexfile.write(item)

def mixer(liste):
    scrambled = []
    while len(liste) > 0:
        ind = randint(0, len(liste) - 1)
       # print(ind)
        scrambled.append(liste[ind])
        del liste[ind]
    return scrambled


if __name__ == "__main__":

    questionlist,totalpoints = readfile()
    print('Totalpoints = ' + str(totalpoints))
    scrambledlist = mixer(questionlist)

    copytemplate(templatedir + 'document_begin.tex', outputdir + 'automated.tex')

    for questionanwer in scrambledlist:
        question = "\item{%s}\n\\begin{flushright}\n" \
                   "\\scalebox{1.7}{\n" \
                   "\\begin{tabular}{|m{0.5cm}|m{0.5cm}|}\n" \
                   "\\hline\n" \
                   "\ %s &  \\\ \n " \
                   "\\hline\n" \
                   "\\end{tabular}}\n" \
                   "\\end{flushright}\n" % (questionanwer.question, questionanwer.points)

        if questionanwer.pic is not None:
            question = question +\
                       "\\begin{flushleft}\n" \
                       "\includegraphics[height=5cm]{europe.jpg}\n" \
                       "\end{flushleft}\n"\
        insert(question)

        # testseperator
        insert('\\afterpage{\\blankpage}')

    copytemplate(templatedir + 'document_end.tex', outputdir + 'automated.tex')
