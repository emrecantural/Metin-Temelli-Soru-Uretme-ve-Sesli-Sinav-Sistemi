import nltk
import idCard

#get_chunk
def combineChunk (chunked):
    sentence= ""
    for j in range(len(chunked)):
        sentence += (chunked[j][0]+ " ")
        return sentence
#what_whom1    
def module1(subsections, num, tagged):
    tokenize = nltk.word_tokenize(subsections[num])
    tag = nltk.pos_tag(tokenize)
    grammar = r"""chunk:{<TO>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|VBG|DT|POS|CD|VBN>+}"""
    chunkparser = nltk.RegexpParser(grammar)
    chunked = chunkparser.parse(tag)

    list1 = idCard.chunkSearch(subsections[num], chunked)
    s = []

    if len(list1) != 0:
        for j in range(len(chunked)):
            sentence1 = ""
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
                    sentence2 = "to whom "
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
                                sentence2 = "to what"

                sentence4 = sentence1 + sentence2 + sentence3
                for k in range(len(subsections)):
                    if k != num:
                        sentence4 += ("," + subsections[k])
                sentence4 += '?'
                sentence4= idCard.lastStep(sentence4)
                # str4 = 'Q.' + str4
                s.append(sentence4)
    return s
#what_whom2
def module2(subsections, num, tagged):
    tok = nltk.word_tokenize(subsections[num])
    tag = nltk.pos_tag(tok)
    gram = r"""chunk:{<IN>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|POS|VBG|DT|CD|VBN>+}"""
    chunkparser = nltk.RegexpParser(gram)
    chunked = chunkparser.parse(tag)
    list1 = idCard.chunkSearch(subsections[num], chunked)
    s = []

    if len(list1) != 0:
        for j in range(len(chunked)):
            sentence1 = ""
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
                                sentence2 = " " + chunked[j][0][0] + "whom "
                            elif tagged[x1][1] == "LOC" or tagged[x1][1] == "ORG" or tagged[x1][1] == "GPE":
                                sentence2 = " where "
                            elif tagged[x1][1] == "TIME" or tagged[x1][1] == "DATE":
                                sentence2 = " when "
                            else:
                                sentence2 = " " + chunked[j][0][0] + " what"

                sentence4 = sentence1 + sentence2 + sentence3
                for k in range(len(subsections)):
                    if k != num:
                        sentence4 += ("," + subsections[k])
                sentence4 += '?'
                sentence4 = idCard.lastStep(sentence4)
                # str4 = 'Q.' + str4
                s.append(sentence4)
    return s

#whose
def module3(subsections, num, tagged):
    tokenize = nltk.word_tokenize(subsections[num])
    tag = nltk.pos_tag(tokenize)
    grammar = r"""chunk:{<NN.?>*<PRP\$|POS>+<RB.?>*<JJ.?>*<NN.?|VBG|VBN>+}"""
    chunkparser = nltk.RegexpParser(grammar)
    chunked = chunkparser.parse(tag)

    list1 = idCard.chunkSearch(subsections[num], chunked)
    s = []

    if len(list1) != 0:
        for j in range(len(chunked)):
            sentence1 = ""
            sentence3 = ""
            sentence2 = " whose "
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
                if chunked[j][1][1] == 'POS':
                    for k in range(2, len(chunked[j])):
                        sentence2 += (chunked[j][k][0] + " ")
                else:
                    for k in range(1, len(chunked[j])):
                        sentence2 += (chunked[j][k][0] + " ")

                sentence4 = sentence1 + sentence2 + sentence3
                for k in range(len(subsections)):
                    if k != num:
                        sentence4 += ("," + subsections[k])
                sentence4 += '?'
                sentence4 = idCard.lastStep(sentence4)
                # str4 = 'Q.' + str4
                s.append(sentence4)
    return s

#howmany
def module4(subsections, num, tagged):
    tokenize = nltk.word_tokenize(subsections[num])
    tag = nltk.pos_tag(tokenize)
    grammar = r"""chunk:{<DT>?<CD>+<RB>?<JJ|JJR|JJS>?<NN|NNS|NNP|NNPS|VBG>+}"""
    chunkparser = nltk.RegexpParser(grammar)
    chunked = chunkparser.parse(tag)

    list1 = idCard.chunkSearch(subsections[num], chunked)
    s = []

    if len(list1) != 0:
        for j in range(len(chunked)):
            sentence1 = ""
            sentence3 = ""
            sentence2 = " how many "
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

                subText = combineChunk(chunked[j])
                tokenize = nltk.word_tokenize(subText)
                tag = nltk.pos_tag(tokenize)
                grammar = r"""chunk:{<RB>?<JJ|JJR|JJS>?<NN|NNS|NNP|NNPS|VBG>+}"""
                chunkparser = nltk.RegexpParser(grammar)
                chunked1 = chunkparser.parse(tag)

                list2 = idCard.chunkSearch(subText, chunked1)
                sentence5 = ""

                for k in range(len(chunked1)):
                    if k in list2:
                        sentence5 += combineChunk(chunked1[k])

                sentence4 = sentence1 + sentence2 + sentence5 + sentence3
                for k in range(len(subsections)):
                    if k != num:
                        sentence4 += ("," + subsections[k])
                sentence4 += '?'
                sentence4 = idCard.lastStep(sentence4)
                # str4 = 'Q.' + str4
                s.append(sentence4)
    return s

#howmuch_1
def module5(subsections, num, tagged):
    tokenize = nltk.word_tokenize(subsections[num])
    tag = nltk.pos_tag(tokenize)
    grammar = r"""chunk:{<IN>+<\$>?<CD>+}"""
    chunkparser = nltk.RegexpParser(grammar)
    chunked = chunkparser.parse(tag)

    list1 = idCard.chunkSearch(subsections[num], chunked)
    s = []

    if len(list1) != 0:
        for j in range(len(chunked)):
            sentence1 = ""
            sentence3 = ""
            sentence2 = " how much "
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

                sentence2 = chunked[j][0][0] + sentence2
                sentence4 = sentence1 + sentence2 + sentence3
                for k in range(len(subsections)):
                    if k != num:
                        sentence4 += ("," + subsections[k])
                sentence4 += '?'
                sentence4 = idCard.lastStep(sentence4)
                # str4 = 'Q.' + str4
                s.append(sentence4)
    return s