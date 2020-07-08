import nltk
def chunkSearch (subsections, chunked):
    m = len(chunked)
    list1 = []
    for j in range(m):
        if (len(chunked[j]) > 2 or len(chunked[j]) == 1):
            list1.append(j)
        if (len(chunked[j]) == 2):
            try:
                str1 = chunked[j][0][0] + " " + chunked[j][1][0]
            except Exception:
                pass
            else:
                if (str1 in subsections) == True:
                    list1.append(j)
    return list1

#verbphrase_identify
def verbSentence (clause):
    tokenize = nltk.word_tokenize(clause)
    tag = nltk.pos_tag(tokenize)
    grammar = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
    chunkparser = nltk.RegexpParser(grammar)
    chunked = chunkparser.parse(tag)
    sentence1 = ""
    sentence2 = ""
    sentence3 = ""
    list1 = chunkSearch(clause, chunked)
    if len(list1) != 0:
        m = list1[len(list1) - 1]
        for j in range(len(chunked[m])):
            sentence1 += chunked[m][j][0]
            sentence1 += " "

    tokenize2 = nltk.word_tokenize(sentence1)
    tag2 = nltk.pos_tag(tokenize2)
    grammar2 = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*}"""
    chunkparser2 = nltk.RegexpParser(grammar2)
    chunked2 = chunkparser2.parse(tag2)

    list2 = chunkSearch(sentence1, chunked2)
    if len(list2) != 0:

        m = list2[0]
        for j in range(len(chunked2[m])):
            sentence2 += (chunked2[m][j][0] + " ")
            
    #burası yukarıdakiyle aynı
    tokenize2 = nltk.word_tokenize(sentence1)
    tag2 = nltk.pos_tag(tokenize2)
    grammar2 = r"""chunk:{<VB.?|MD|RP>+}"""
    chunkparser1 = nltk.RegexpParser(grammar2)
    #chunked 2 normali
    chunked3 = chunkparser1.parse(tag2)

    list3 = chunkSearch(sentence1, chunked3)
    if len(list3) != 0:

        m = list3[0]
        for j in range(len(chunked3[m])):
            sentence3 += (chunked3[m][j][0] + " ")

    X = ""
    #str4
    sentence4 = ""
    #st
    subTokenize = nltk.word_tokenize(sentence3)
    if len(subTokenize) > 1:
        X = subTokenize[0]
        #s
        subSentence = ""
        for k in range(1, len(subTokenize)):
            subSentence += subTokenize[k]
            subSentence += " "
        sentence3 = subSentence
        sentence4 = X + " " + sentence2 + sentence3

    if len(subTokenize) == 1:
        #tag1 yukarıdaki ile alakası var mı bilmiyorum
        tag2 = nltk.pos_tag(subTokenize)
        if tag2[0][0] != 'are' and tag2[0][0] != 'were' and tag2[0][0] != 'is' and tag2[0][0] != 'am':
            if tag2[0][1] == 'VB' or tag2[0][1] == 'VBP':
                X = 'do'
            if tag2[0][1] == 'VBD' or tag2[0][1] == 'VBN':
                X = 'did'
            if tag2[0][1] == 'VBZ':
                X = 'does'
            sentence4 = X + " " + sentence2 + sentence3
        if (tag2[0][0] == 'are' or tag2[0][0] == 'were' or tag2[0][0] == 'is' or tag2[0][0] == 'am'):
            sentence4 = tag2[0][0] + " " + sentence2

    return sentence4    


#postprocess
def lastStep (string):
    tokenize = nltk.word_tokenize(string)
    tag = nltk.pos_tag(tokenize)

    sentence = tokenize[0].capitalize()
    sentence += " "
    if len(tokenize) != 0:
        for i in range(1, len(tokenize)):
            if tag[i][1] == "NNP":
                sentence += tokenize[i].capitalize()
                sentence += " "
            else:
                sentence += tokenize[i].lower()
                sentence += " "
        tokenize = nltk.word_tokenize(sentence)
        sentence = ""
        for i in range(len(tokenize)):
            if tokenize[i] == "i" or tokenize[i] == "we":
                sentence += "you"
                sentence += " "
            elif tokenize[i] == "my" or tokenize[i] == "our":
                sentence += "your"
                sentence += " "
            elif tokenize[i] == "your":
                sentence += "my"
                sentence += " "
            elif tokenize[i] == "you":
                if i - 1 >= 0:
                    subTokenize = nltk.word_tokenize(tokenize[i - 1])
                    subTag = nltk.pos_tag(subTokenize)
                    # print ta
                    if subTag[0][1] == 'IN':
                        sentence += "me"
                        sentence += " "
                    else:
                        sentence += "i"
                        sentence += " "
                else:
                    sentence += "i "

            elif tokenize[i] == "am":
                sentence += "are"
                sentence += " "
            else:
                sentence += tokenize[i]
                sentence += " " 
    return sentence    

#clause_identify
def clauseId(subsection):
    tokenize = nltk.word_tokenize(subsection)
    tag = nltk.pos_tag(tokenize)
    grammar = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?|VB.?|MD|RP>+}"""
    chunkparser = nltk.RegexpParser(grammar)
    chunked = chunkparser.parse(tag)

    flag = 0
    for j in range(len(chunked)):
        if (len(chunked[j]) > 2):
            flag = 1
        if (len(chunked[j]) == 2):
            try:
                sentence = chunked[j][0][0] + " " + chunked[j][1][0]
            except Exception:
                pass
            else:
                if (sentence in subsection) == True:
                    flag = 1
        if flag == 1:
            break

    return flag
    
#subjectphrase_search
def subjectSearch( subsections,num):
    str2 = ""
    for j in range(num - 1, 0, -1):
        str1 = ""
        flag = 0
        tok = nltk.word_tokenize(subsections[j])
        tag = nltk.pos_tag(tok)
        gram = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
        chunkparser = nltk.RegexpParser(gram)
        chunked = chunkparser.parse(tag)

        list1 = chunkSearch(subsections[j], chunked)
        if len(list1) != 0:
            m = list1[len(list1) - 1]
            for j in range(len(chunked[m])):
                str1 += chunked[m][j][0]
                str1 += " "

            tok1 = nltk.word_tokenize(str1)
            tag1 = nltk.pos_tag(tok1)
            gram1 = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+}"""
            chunkparser1 = nltk.RegexpParser(gram1)
            chunked1 = chunkparser1.parse(tag1)

            list2 = chunkSearch(str1, chunked1)
            if len(list2) != 0:
                m = list2[len(list2) - 1]
                for j in range(len(chunked1[m])):
                    str2 += (chunked1[m][j][0] + " ")
                flag = 1

        if flag == 0:
            tok1 = nltk.word_tokenize(subsections[j])
            tag1 = nltk.pos_tag(tok1)
            gram1 = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+}"""
            chunkparser1 = nltk.RegexpParser(gram1)
            chunked1 = chunkparser1.parse(tag1)

            list2 = chunkSearch(str1, chunked1)
            st = nltk.word_tokenize(subsections[j])
            if len(chunked1[list2[0]]) == len(st):
                str2 = subsections[j]
                flag = 1

        if flag == 1:
            break

    return str2


#segment_identify = subsectionId
def subsectionId (sentence):
    sectionSet= sentence.split(",")
    return sectionSet

def chunk_search(segment, chunked):
    m = len(chunked)
    list1 = []
    for j in range(m):
        if (len(chunked[j]) > 2 or len(chunked[j]) == 1):
            list1.append(j)
        if (len(chunked[j]) == 2):
            try:
                str1 = chunked[j][0][0] + " " + chunked[j][1][0]
            except Exception:
                pass
            else:
                if (str1 in segment) == True:
                    list1.append(j)
    return list1

def segment_identify(sen):
    segment_set = sen.split(",")
    return segment_set


def clause_identify(segment):
    tok = nltk.word_tokenize(segment)
    tag = nltk.pos_tag(tok)
    gram = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?|VB.?|MD|RP>+}"""
    chunkparser = nltk.RegexpParser(gram)
    chunked = chunkparser.parse(tag)

    flag = 0
    for j in range(len(chunked)):
        if (len(chunked[j]) > 2):
            flag = 1
        if (len(chunked[j]) == 2):
            try:
                str1 = chunked[j][0][0] + " " + chunked[j][1][0]
            except Exception:
                pass
            else:
                if (str1 in segment) == True:
                    flag = 1
        if flag == 1:
            break

    return flag


def verbphrase_identify(clause):
    tok = nltk.word_tokenize(clause)
    tag = nltk.pos_tag(tok)
    gram = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
    chunkparser = nltk.RegexpParser(gram)
    chunked = chunkparser.parse(tag)
    str1 = ""
    str2 = ""
    str3 = ""
    list1 = chunk_search(clause, chunked)
    if len(list1) != 0:
        m = list1[len(list1) - 1]
        for j in range(len(chunked[m])):
            str1 += chunked[m][j][0]
            str1 += " "

    tok1 = nltk.word_tokenize(str1)
    tag1 = nltk.pos_tag(tok1)
    gram1 = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*}"""
    chunkparser1 = nltk.RegexpParser(gram1)
    chunked1 = chunkparser1.parse(tag1)

    list2 = chunk_search(str1, chunked1)
    if len(list2) != 0:

        m = list2[0]
        for j in range(len(chunked1[m])):
            str2 += (chunked1[m][j][0] + " ")

    tok1 = nltk.word_tokenize(str1)
    tag1 = nltk.pos_tag(tok1)
    gram1 = r"""chunk:{<VB.?|MD|RP>+}"""
    chunkparser1 = nltk.RegexpParser(gram1)
    chunked2 = chunkparser1.parse(tag1)

    list3 = chunk_search(str1, chunked2)
    if len(list3) != 0:

        m = list3[0]
        for j in range(len(chunked2[m])):
            str3 += (chunked2[m][j][0] + " ")

    X = ""
    str4 = ""
    st = nltk.word_tokenize(str3)
    if len(st) > 1:
        X = st[0]
        s = ""
        for k in range(1, len(st)):
            s += st[k]
            s += " "
        str3 = s
        str4 = X + " " + str2 + str3

    if len(st) == 1:
        tag1 = nltk.pos_tag(st)
        if tag1[0][0] != 'are' and tag1[0][0] != 'were' and tag1[0][0] != 'is' and tag1[0][0] != 'am':
            if tag1[0][1] == 'VB' or tag1[0][1] == 'VBP':
                X = 'do'
            if tag1[0][1] == 'VBD' or tag1[0][1] == 'VBN':
                X = 'did'
            if tag1[0][1] == 'VBZ':
                X = 'does'
            str4 = X + " " + str2 + str3
        if (tag1[0][0] == 'are' or tag1[0][0] == 'were' or tag1[0][0] == 'is' or tag1[0][0] == 'am'):
            str4 = tag1[0][0] + " " + str2

    return str4


def subjectphrase_search(segment_set, num):
    str2 = ""
    for j in range(num - 1, 0, -1):
        str1 = ""
        flag = 0
        tok = nltk.word_tokenize(segment_set[j])
        tag = nltk.pos_tag(tok)
        gram = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
        chunkparser = nltk.RegexpParser(gram)
        chunked = chunkparser.parse(tag)

        list1 = chunk_search(segment_set[j], chunked)
        if len(list1) != 0:
            m = list1[len(list1) - 1]
            for j in range(len(chunked[m])):
                str1 += chunked[m][j][0]
                str1 += " "

            tok1 = nltk.word_tokenize(str1)
            tag1 = nltk.pos_tag(tok1)
            gram1 = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+}"""
            chunkparser1 = nltk.RegexpParser(gram1)
            chunked1 = chunkparser1.parse(tag1)

            list2 = chunk_search(str1, chunked1)
            if len(list2) != 0:
                m = list2[len(list2) - 1]
                for j in range(len(chunked1[m])):
                    str2 += (chunked1[m][j][0] + " ")
                flag = 1

        if flag == 0:
            tok1 = nltk.word_tokenize(segment_set[j])
            tag1 = nltk.pos_tag(tok1)
            gram1 = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+}"""
            chunkparser1 = nltk.RegexpParser(gram1)
            chunked1 = chunkparser1.parse(tag1)

            list2 = chunk_search(str1, chunked1)
            st = nltk.word_tokenize(segment_set[j])
            if len(chunked1[list2[0]]) == len(st):
                str2 = segment_set[j]
                flag = 1

        if flag == 1:
            break

    return str2


def postprocess(string):
    tok = nltk.word_tokenize(string)
    tag = nltk.pos_tag(tok)

    str1 = tok[0].capitalize()
    str1 += " "
    if len(tok) != 0:
        for i in range(1, len(tok)):
            if tag[i][1] == "NNP":
                str1 += tok[i].capitalize()
                str1 += " "
            else:
                str1 += tok[i].lower()
                str1 += " "
        tok = nltk.word_tokenize(str1)
        str1 = ""
        for i in range(len(tok)):
            if tok[i] == "i" or tok[i] == "we":
                str1 += "you"
                str1 += " "
            elif tok[i] == "my" or tok[i] == "our":
                str1 += "your"
                str1 += " "
            elif tok[i] == "your":
                str1 += "my"
                str1 += " "
            elif tok[i] == "you":
                if i - 1 >= 0:
                    to = nltk.word_tokenize(tok[i - 1])
                    ta = nltk.pos_tag(to)
                    # print ta
                    if ta[0][1] == 'IN':
                        str1 += "me"
                        str1 += " "
                    else:
                        str1 += "i"
                        str1 += " "
                else:
                    str1 += "i "

            elif tok[i] == "am":
                str1 += "are"
                str1 += " "
            else:
                str1 += tok[i]
                str1 += " "

    return str1
