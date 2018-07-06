templatedir = './templates/'
outputdir = './output/'

def copytemplate(input,output):
    with open( input, 'r') as originalfile:
        content = originalfile.readlines()
    with open( output, 'a') as mytexfile:
        for item in content:
            mytexfile.write(item)

def insert(ques):
    with open( outputdir + 'automated.tex' , 'a') as mytexfile:
        for item in ques:
            print(item)
            mytexfile.write(item)

if __name__ == "__main__":
    copytemplate(templatedir + 'document_begin.tex', outputdir + 'automated.tex')

    content = r''' \item{Welches Molekül sehen sie hier? Wofür braucht es der Körper?}
    \begin{flushright}
    \scalebox{1.7}{
    \begin{tabular}{|m{0.5cm}|m{0.5cm}|}
	\hline
    90 &  23 \\
	\hline
	\end{tabular}}
    \end{flushright}
    \begin{flushleft}
    \includegraphics[height=5cm]{Adenosintriphosphat.jpg}
    \end{flushleft}
    '''
    insert(content)

    copytemplate(templatedir + 'document_end.tex', outputdir + 'automated.tex')
