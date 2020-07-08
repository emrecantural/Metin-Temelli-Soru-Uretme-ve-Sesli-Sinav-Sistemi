# -*- coding: utf-8 -*-
import nltk
import idCard


#nounclause ta bulunan get_chunk yerine
def combineChunk (chunked):
    sentence= ""
    for j in range(len(chunked)):
        sentence += (chunked[j][0]+ " ")
        return sentence

#whom 1 modülü
def module1 (subsections, num, tagged):
    tokenize =nltk.word_tokenize (subsections[num]) #gönderilen aynı cümleyi tok ediyoruz
    tag= nltk.pos_tag(tokenize)
    grammar = r"""chunk:{<TO>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|VBG|DT|POS|CD|VBN>+}"""
    chunkparser =nltk.RegexpParser(grammar)
    chunked =chunkparser.parse (tag)
    #nltk ile etiketleme işlemi bitti
    
    list1 = idCard.chunkSearch(subsections[num],chunked) 
    list3= [] 
    if len (list1)!= 0: #dönen chunk uzunluğu 0 değil ise
        for j in range(len(chunked)):
            sentence1 = "" #str1
            sentence2 = "" #str2
            sentence3 = "" #str3
            if j in list1:
                for k in range(j):
                    if k in list1:
                        sentence1 += combineChunk(chunked[k])
                    else:
                        sentence1 += (chunked[k][0] + " ")

                for k in range(j + 1, len(chunked)):
                    if k in list1:
                        sentence3 += combineChunk(chunked[k])
                    else:
                        sentence3 += (chunked[k][0] + " ")

                if chunked[j][1][1] == 'PRP':
                    sentence2 = " to whom "
                else:
                    for x in range(len(chunked[j])):
                        if (chunked[j][x][1] == "NNP" or chunked[j][x][1] == "NNPS" or chunked[j][x][1] == "NNS" or
                                chunked[j][x][1] == "NN"):
                            break

                    for x1 in range(len(tagged)):

                        if tagged[x1][0] == chunked[j][x][0]:
                            if tagged[x1][1] == "PERSON":
                                sentence2 = " to whom "
                            elif tagged[x1][1] == "LOC" or tagged[x1][1] == "ORG" or tagged[x1][1] == "GPE":
                                sentence2 = " where "
                            elif tagged[x1][1] == "TIME" or tagged[x1][1] == "DATE":
                                sentence2 = " when "
                            else:
                                sentence2 = "to what "

                tokenize = nltk.word_tokenize(sentence1)
                tag = nltk.pos_tag(tokenize)
                grammar = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
                chunkparser = nltk.RegexpParser(grammar)
                chunked1 = chunkparser.parse(tag)
                list2 = idCard.chunkSearch(sentence1, chunked1)
                
                if len(list2) != 0:
                    m = list2[len(list2) - 1]
                
                    sentence4= combineChunk(chunked1[m]) #sentence4
                    
                    sentence4 = idCard.verbSentence(sentence4)
                    sentence5 = ""
                    sentence6 = ""

                    for k in range(m):
                        if k in list2:
                            sentence5 += combineChunk(chunked1[k])
                        else:
                            sentence5 += (chunked1[k][0] + " ")

                    for k in range(m + 1, len(chunked1)):
                        if k in list2:
                            sentence6 += combineChunk(chunked1[k])
                        else:
                            sentence6 += (chunked1[k][0] + " ")

                    subText = sentence5 + sentence2 + sentence4 + sentence6 + sentence3
                    for l in range(num + 1, len(subsections)):
                        subText += ("," + subsections[l])
                    subText += '?'
                    subText = idCard.lastStep(subText)
                    # st = 'Q.' + st
                    list3.append(subText)

    return list3    


#whom2 modülü
def module2 (subsections, num, tagged):
    tokenize = nltk.word_tokenize(subsections[num])
    tag = nltk.pos_tag(tokenize)
    grammar = r"""chunk:{<IN>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|POS|VBG|DT|CD|VBN>+}"""
    chunkparser = nltk.RegexpParser(grammar)
    chunked = chunkparser.parse(tag)

    list1 = idCard.chunkSearch(subsections[num], chunked)
    list3 = []

    if len(list1) != 0:
        for j in range(len(chunked)):
            sentence1 = ""
            sentence2 = ""
            sentence3 = ""
            if j in list1:
                for k in range(j):
                    if k in list1:
                        sentence1 += combineChunk(chunked[k])
                    else:
                        sentence1 += (chunked[k][0] + " ")

                for k in range(j + 1, len(chunked)):
                    if k in list1:
                        sentence3 += combineChunk(chunked[k])
                    else:
                        sentence3 += (chunked[k][0] + " ")

                if chunked[j][1][1] == 'PRP':
                    sentence2 = " " + chunked[j][0][0] + " whom "
                else:
                    for x in range(len(chunked[j])):
                        if (chunked[j][x][1] == "NNP" or chunked[j][x][1] == "NNPS" or chunked[j][x][1] == "NNS" or
                                chunked[j][x][1] == "NN"):
                            break

                    for x1 in range(len(tagged)):
                        if tagged[x1][0] == chunked[j][x][0]:
                            if tagged[x1][1] == "PERSON":
                                sentence2 = " " + chunked[j][0][0] + " whom "
                            elif tagged[x1][1] == "LOC" or tagged[x1][1] == "ORG" or tagged[x1][1] == "GPE":
                                sentence2 = " where "
                            elif tagged[x1][1] == "TIME" or tagged[x1][1] == "DATE":
                                sentence2 = " when "
                            else:
                                sentence2 = " " + chunked[j][0][0] + " what "

                tokenize = nltk.word_tokenize(sentence1)
                tag = nltk.pos_tag(tokenize)
                grammar = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
                chunkparser = nltk.RegexpParser(grammar)
                chunked1 = chunkparser.parse(tag)

                list2 = idCard.chunkSearch(sentence1, chunked1)
                if len(list2) != 0:
                    m = list2[len(list2) - 1]

                    sentence4 = combineChunk(chunked1[m])
                    sentence4 = idCard.verbSentence(sentence4)
                    sentence5 = ""
                    sentence6 = ""

                    for k in range(m):
                        if k in list2:
                            sentence5 += combineChunk(chunked1[k])
                        else:
                            sentence5 += (chunked1[k][0] + " ")

                    for k in range(m + 1, len(chunked1)):
                        if k in list2:
                            sentence6 += combineChunk(chunked1[k])
                        else:
                            sentence6 += (chunked1[k][0] + " ")

                    subText = sentence5 + sentence2 + sentence4 + sentence6 + sentence3
                    for l in range(num + 1, len(subsections)):
                        subText += ("," + subsections[l])
                    subText += '?'
                    subText = idCard.lastStep(subText)
                    # st = 'Q.' + st
                    list3.append(subText)

    return list3    


#whom_3 yerine yeni modül
def module3(subsections, num, tagged):
    tokenize = nltk.word_tokenize(subsections[num])
    tag = nltk.pos_tag(tokenize)
    grammar = r"""chunk:{<VB.?|MD|RP>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|POS|VBG|DT|CD|VBN>+}"""
    chunkparser = nltk.RegexpParser(grammar)
    chunked = chunkparser.parse(tag)

    list1 = idCard.chunkSearch(subsections[num], chunked)
    list3 = []

    if len(list1) != 0:
        for j in range(len(chunked)):
            sentence1 = ""
            sentence2 = ""
            sentence3 = ""
            if j in list1:
                for k in range(j):
                    if k in list1:
                        sentence1 += combineChunk(chunked[k])
                    else:
                        sentence1 += (chunked[k][0] + " ")

                for k in range(j + 1, len(chunked)):
                    if k in list1:
                        sentence3 += combineChunk(chunked[k])
                    else:
                        sentence3 += (chunked[k][0] + " ")

                if chunked[j][1][1] == 'PRP':
                    sentence2 = " whom "
                else:
                    for x in range(len(chunked[j])):
                        if (chunked[j][x][1] == "NNP" or chunked[j][x][1] == "NNPS" or chunked[j][x][1] == "NNS" or
                                chunked[j][x][1] == "NN"):
                            break

                    for x1 in range(len(tagged)):
                        if tagged[x1][0] == chunked[j][x][0]:
                            if tagged[x1][1] == "PERSON":
                                sentence2 = " whom "
                            elif tagged[x1][1] == "LOC" or tagged[x1][1] == "ORG" or tagged[x1][1] == "GPE":
                                sentence2 = " what "
                            elif tagged[x1][1] == "TIME" or tagged[x1][1] == "DATE":
                                sentence2 = " what time "
                            else:
                                sentence2 = " what "

                sentence0 = combineChunk(chunked[j])
                tokenize = nltk.word_tokenize(sentence0)
                tag = nltk.pos_tag(tokenize)
                grammar = r"""chunk:{<VB.?|MD>+}"""
                chunkparser = nltk.RegexpParser(grammar)
                chunked1 = chunkparser.parse(tag)

                sentence0 = combineChunk(chunked1[0])

                sentence1 += sentence0

                tokenize = nltk.word_tokenize(sentence1)
                tag = nltk.pos_tag(tokenize)
                grammar = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
                chunkparser = nltk.RegexpParser(grammar)
                chunked1 = chunkparser.parse(tag)

                list2 = idCard.chunkSearch(sentence1, chunked1)

                if len(list2) != 0:
                    m = list2[len(list2) - 1]

                    sentence4 = combineChunk(chunked1[m])
                    sentence4 = idCard.verbSentence(sentence4)
                    sentence5 = ""
                    sentence6 = ""

                    for k in range(m):
                        if k in list2:
                            sentence5 += combineChunk(chunked1[k])
                        else:
                            sentence5 += (chunked1[k][0] + " ")

                    for k in range(m + 1, len(chunked1)):
                        if k in list2:
                            sentence6 += combineChunk(chunked1[k])
                        else:
                            sentence6 += (chunked1[k][0] + " ")

                    subText = sentence5 + sentence2 + sentence4 + sentence6 + sentence3
                    for l in range(num + 1, len(subsections)):
                        subText += ("," + subsections[l])
                    subText += '?'
                    subText = idCard.lastStep(subText)
                    # st = 'Q.' + st
                    list3.append(subText)

    return list3


#whose
def module4(subsections, num, tagged):
    tokenize = nltk.word_tokenize(subsections[num])
    tag = nltk.pos_tag(tokenize)
    grammar = r"""chunk:{<DT|NN.?>*<PRP\$|POS>+<RB.?>*<JJ.?>*<NN.?|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
    chunkparser = nltk.RegexpParser(grammar)
    chunked = chunkparser.parse(tag)

    list1 = idCard.chunkSearch(subsections[num], chunked)
    list3 = []

    if len(list1) != 0:
        for i in range(len(chunked)):
            if i in list1:
                sentence1 = ""
                sentence2 = ""
                sentence3 = ""
                for k in range(i):
                    if k in list1:
                        sentence1 += combineChunk(chunked[k])
                    else:
                        sentence1 += (chunked[k][0] + " ")
                sentence1 += " whose "

                for k in range(i + 1, len(chunked)):
                    if k in list1:
                        sentence3 += combineChunk(chunked[k])
                    else:
                        sentence3 += (chunked[k][0] + " ")

                if chunked[i][1][1] == 'POS':
                    for k in range(2, len(chunked[i])):
                        sentence2 += (chunked[i][k][0] + " ")

                if chunked[i][0][1] == 'PRP$':
                    for k in range(1, len(chunked[i])):
                        sentence2 += (chunked[i][k][0] + " ")

                sentence2 = sentence1 + sentence2 + sentence3
                sentence4 = ""

                for l in range(0, len(subsections)):
                    if l < num:
                        sentence4 += (subsections[l] + ",")
                    if l > num:
                        sentence2 += ("," + subsections[l])
                sentence2 = sentence4 + sentence2
                sentence2 += '?'
                sentence2 = idCard.lastStep(sentence2)
                # str2 = 'Q.' + str2
                list3.append(sentence2)

    return list3

#what_to_do
def module5(subsections, num, tagged):
    tokenize = nltk.word_tokenize(subsections[num])
    tag = nltk.pos_tag(tokenize)
    grammar = r"""chunk:{<TO>+<VB|VBP|RP>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|POS|VBG|DT>*}"""
    chunkparser = nltk.RegexpParser(grammar)
    chunked = chunkparser.parse(tag)

    list1 = idCard.chunkSearch(subsections[num], chunked)
    list3 = []

    if len(list1) != 0:
        for j in range(len(chunked)):
            sentence1 = ""
            sentence2 = ""
            sentence3 = ""
            if j in list1:
                for k in range(j):
                    if k in list1:
                        sentence1 += combineChunk(chunked[k])
                    else:
                        sentence1 += (chunked[k][0] + " ")

                for k in range(j + 1, len(chunked)):
                    if k in list1:
                        sentence3 += combineChunk(chunked[k])
                    else:
                        sentence3 += (chunked[k][0] + " ")

                ls = combineChunk(chunked[j])
                tokenize = nltk.word_tokenize(ls)
                tag = nltk.pos_tag(tokenize)
                grammar = r"""chunk:{<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|POS|VBG|DT>+}"""
                chunkparser = nltk.RegexpParser(grammar)
                chunked2 = chunkparser.parse(tag)
                lis = idCard.chunkSearch(ls, chunked2)
                if len(lis) != 0:
                    x = lis[len(lis) - 1]
                    ls1 = combineChunk(chunked2[x])
                    index = ls.find(ls1)
                    sentence2 = " " + ls[0:index]
                else:
                    sentence2 = " to do "

                tokenize = nltk.word_tokenize(sentence1)
                tag = nltk.pos_tag(tokenize)
                grammar = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
                chunkparser = nltk.RegexpParser(grammar)
                chunked1 = chunkparser.parse(tag)

                list2 = idCard.chunkSearch(sentence1, chunked1)
                if len(list2) != 0:
                    m = list2[len(list2) - 1]

                    sentence4= combineChunk(chunked1[m])
                    sentence4 = idCard.verbSentence(sentence4)
                    sentence5 = ""
                    sentence6 = ""

                    for k in range(m):
                        if k in list2:
                            sentence5 += combineChunk(chunked1[k])
                        else:
                            sentence5 += (chunked1[k][0] + " ")

                    for k in range(m + 1, len(chunked1)):
                        if k in list2:
                            sentence6 += combineChunk(chunked1[k])
                        else:
                            sentence6 += (chunked1[k][0] + " ")

                    if chunked2[j][1][1] == 'PRP':
                        tr = " whom "
                    else:
                        for x in range(len(chunked[j])):
                            if (chunked[j][x][1] == "NNP" or chunked[j][x][1] == "NNPS" or chunked[j][x][1] == "NNS" or
                                    chunked[j][x][1] == "NN"):
                                break

                        for x1 in range(len(tagged)):
                            if tagged[x1][0] == chunked[j][x][0]:
                                if tagged[x1][1] == "PERSON":
                                    tr = " whom "
                                elif tagged[x1][1] == "LOC" or tagged[x1][1] == "ORG" or tagged[x1][1] == "GPE":
                                    tr = " where "
                                elif tagged[x1][1] == "TIME" or tagged[x1][1] == "DATE":
                                    tr = " when "
                                else:
                                    tr = " what "

                    subText = sentence5 + tr + sentence4 + sentence2 + sentence6 + sentence3
                    for l in range(num + 1, len(subsections)):
                        subText += ("," + subsections[l])
                    subText += '?'
                    subText = idCard.lastStep(subText)
                    # st = 'Q.' + st
                    list3.append(subText)

    return list3
#who
def module6(subsections, num, tagged):
    tokenize = nltk.word_tokenize(subsections[num])
    tag = nltk.pos_tag(tokenize)
    grammar = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
    chunkparser = nltk.RegexpParser(grammar)
    chunked = chunkparser.parse(tag)

    list1 = idCard.chunkSearch(subsections[num], chunked)
    list3 = []

    if len(list1) != 0:
        for j in range(len(list1)):
            m = list1[j]
            sentence1 = ""
            for k in range(m + 1, len(chunked)):
                if k in list1:
                    sentence1 += combineChunk(chunked[k])
                else:
                    sentence1 += (chunked[k][0] + " ")

            sentence2 = combineChunk(chunked[m])
            tokenize = nltk.word_tokenize(sentence2)
            tag = nltk.pos_tag(tokenize)

            for m11 in range(len(tag)):
                if tag[m11][1] == 'NNP' or tag[m11][1] == 'NNPS' or tag[m11][1] == 'NNS' or tag[m11][1] == 'NN':
                    break
            s11 = ' who '
            for m12 in range(len(tagged)):
                if tagged[m12][0] == tag[m11][0]:
                    if tagged[m12][1] == 'LOC':
                        s11 = ' which place '
                    elif tagged[m12][1] == 'ORG':
                        s11 = ' who '
                    elif tagged[m12][1] == 'DATE' or tagged[m12][1] == 'TIME':
                        s11 = ' what time '
                    else:
                        s11 = ' who '

            grammar = r"""chunk:{<RB.?>*<VB.?|MD|RP>+}"""
            chunkparser = nltk.RegexpParser(grammar)
            chunked1 = chunkparser.parse(tag)

            list2 = idCard.chunkSearch(sentence2, chunked1)
            if len(list2) != 0:
                sentence2 = combineChunk(chunked1[list2[0]])
                sentence2 = s11 + sentence2
                for k in range(list2[0] + 1, len(chunked1)):
                    if k in list2:
                        sentence2 += combineChunk(chunked[k])
                    else:
                        sentence2 += (chunked[k][0] + " ")
                sentence2 += (" " + sentence1)

                tok_1 = nltk.word_tokenize(sentence2)
                sentence2 = ""
                for h in range(len(tok_1)):
                    if tok_1[h] == "am":
                        sentence2 += " is "
                    else:
                        sentence2 += (tok_1[h] + " ")

                for l in range(num + 1, len(subsections)):
                    sentence2 += ("," + subsections[l])
                sentence2 += '?'

                sentence2 = idCard.lastStep(sentence2)
                # str2 = 'Q.' + str2
                list3.append(sentence2)

    return list3
#how_much2
def module7(subsections, num, tagged):
    tokenize = nltk.word_tokenize(subsections[num])
    tag = nltk.pos_tag(tokenize)
    grammar = r"""chunk:{<\$>*<CD>+<MD>?<VB|VBD|VBG|VBP|VBN|VBZ|RP>+}"""
    chunkparser = nltk.RegexpParser(grammar)
    chunked = chunkparser.parse(tag)

    list1 = idCard.chunkSearch(subsections[num], chunked)
    list3 = []

    if len(list1) != 0:
        for j in range(len(list1)):
            m = list1[j]
            sentence1 = ""
            for k in range(m + 1, len(chunked)):
                if k in list1:
                    sentence1 +=combineChunk(chunked[k])
                else:
                    sentence1 += (chunked[k][0] + " ")

            sentence2 = combineChunk(chunked[m])
            tokenize = nltk.word_tokenize(sentence2)
            tag = nltk.pos_tag(tokenize)
            grammar = r"""chunk:{<RB.?>*<VB.?|MD|RP>+}"""
            chunkparser = nltk.RegexpParser(grammar)
            chunked1 = chunkparser.parse(tag)
            s11 = ' how much '

            list2 = idCard.chunkSearch(sentence2, chunked1)
            if len(list2) != 0:
                sentence2 = combineChunk(chunked1[list2[0]])
                sentence2 = s11 + sentence2
                for k in range(list2[0] + 1, len(chunked1)):
                    if k in list2:
                        sentence2 += combineChunk(chunked[k])
                    else:
                        sentence2 += (chunked[k][0] + " ")
                sentence2 += (" " + sentence1)

                tokenize2 = nltk.word_tokenize(sentence2)
                sentence2 = ""
                for h in range(len(tokenize2)):
                    if tokenize2[h] == "am":
                        sentence2 += " is "
                    else:
                        sentence2 += (tokenize2[h] + " ")

                for l in range(num + 1, len(subsections)):
                    sentence2 += ("," + subsections[l])
                sentence2 += '?'

                sentence2 = idCard.lastStep(sentence2)
                # str2 = 'Q.' + str2
                list3.append(sentence2)

    return list3
#howmuch_1
def module8(subsections, num, tagged):
    tokenize = nltk.word_tokenize(subsections[num])
    tag = nltk.pos_tag(tokenize)
    grammar = r"""chunk:{<IN>+<\$>?<CD>+}"""
    chunkparser = nltk.RegexpParser(grammar)
    chunked = chunkparser.parse(tag)

    list1 = idCard.chunkSearch(subsections[num], chunked)
    list3 = []

    if len(list1) != 0:
        for j in range(len(chunked)):
            sentence1 = ""
            sentence2 = ""
            sentence3 = ""
            if j in list1:
                for k in range(j):
                    if k in list1:
                        sentence1 += combineChunk(chunked[k])
                    else:
                        sentence1 += (chunked[k][0] + " ")

                for k in range(j + 1, len(chunked)):
                    if k in list1:
                        sentence3 += combineChunk(chunked[k])
                    else:
                        sentence3 += (chunked[k][0] + " ")

                sentence2 = ' ' + chunked[j][0][0] + ' how much '

                tokenize = nltk.word_tokenize(sentence1)
                tag = nltk.pos_tag(tokenize)
                gram = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
                chunkparser = nltk.RegexpParser(gram)
                chunked1 = chunkparser.parse(tag)

                list2 = idCard.chunkSearch(sentence1, chunked1)
                if len(list2) != 0:
                    m = list2[len(list2) - 1]

                    sentence4 = combineChunk(chunked1[m])
                    sentence4 = idCard.verbSentence(sentence4)
                    sentence5 = ""
                    sentence6 = ""

                    for k in range(m):
                        if k in list2:
                            sentence5 += combineChunk(chunked1[k])
                        else:
                            sentence5 += (chunked1[k][0] + " ")

                    for k in range(m + 1, len(chunked1)):
                        if k in list2:
                            sentence6 += combineChunk(chunked1[k])
                        else:
                            sentence6 += (chunked1[k][0] + " ")

                    subText = sentence5 + sentence2 + sentence4 + sentence6 + sentence3
                    for l in range(num + 1, len(subsections)):
                        subText += ("," + subsections[l])
                    subText += '?'
                    subText = idCard.lastStep(subText)
                    # st = 'Q.' + st
                    list3.append(subText)

    return list3
#howmuch_3
def module9(subsections, num, tagged):
    tokenize = nltk.word_tokenize(subsections[num])
    tag = nltk.pos_tag(tokenize)
    grammar = r"""chunk:{<MD>?<VB|VBD|VBG|VBP|VBN|VBZ>+<IN|TO>?<PRP|PRP\$|NN.?>?<\$>*<CD>+}"""
    chunkparser = nltk.RegexpParser(grammar)
    chunked = chunkparser.parse(tag)

    list1 = idCard.chunkSearch(subsections[num], chunked)
    list3 = []

    if len(list1) != 0:
        for j in range(len(chunked)):
            sentence1 = ""
            sentence2 = ""
            sentence3 = ""
            if j in list1:
                for k in range(j):
                    if k in list1:
                        sentence1 += combineChunk(chunked[k])
                    else:
                        sentence1 += (chunked[k][0] + " ")

                for k in range(j + 1, len(chunked)):
                    if k in list1:
                        sentence3 +=combineChunk(chunked[k])
                    else:
                        sentence3 += (chunked[k][0] + " ")

                sentence0 =combineChunk(chunked[j])
                tokenize = nltk.word_tokenize(sentence0)
                tag = nltk.pos_tag(tokenize)
                grammar = r"""chunk:{<MD>?<VB|VBD|VBG|VBP|VBN|VBZ>+<IN|TO>?<PRP|PRP\$|NN.?>?}"""
                chunkparser = nltk.RegexpParser(grammar)
                chunked1 = chunkparser.parse(tag)

                sentence0 = combineChunk(chunked1[0])
                sentence1 += (" " + sentence0)

                sentence2 = ' how much '

                tokenize = nltk.word_tokenize(sentence1)
                tag = nltk.pos_tag(tokenize)
                grammar = r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
                chunkparser = nltk.RegexpParser(grammar)
                chunked1 = chunkparser.parse(tag)

                list2 = idCard.chunkSearch(sentence1, chunked1)

                if len(list2) != 0:
                    m = list2[len(list2) - 1]

                    sentence4 = combineChunk(chunked1[m])
                    sentence4 = idCard.verbSentence(sentence4)
                    sentence5 = ""
                    sentence6 = ""

                    for k in range(m):
                        if k in list2:
                            sentence5 += combineChunk(chunked1[k])
                        else:
                            sentence5 += (chunked1[k][0] + " ")

                    for k in range(m + 1, len(chunked1)):
                        if k in list2:
                            sentence6 += combineChunk(chunked1[k])
                        else:
                            sentence6 += (chunked1[k][0] + " ")

                    subText = sentence5 + sentence2 + sentence4 + sentence6 + sentence3

                    for l in range(num + 1, len(subsections)):
                        subText += ("," + subsections[l])
                    subText += '?'
                    subText = idCard.lastStep(subText)
                    # st = 'Q.' + st
                    list3.append(subText)

    return list3

