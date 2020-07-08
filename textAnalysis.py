import spacy
import clause
import nounClause
import idCard
import en_core_web_sm
import validation
   

def wordTagging(nlp, tokenize):  
    nlp = en_core_web_sm.load() #gerek yok aslında
    doc = nlp(tokenize)
    finalList = []
    array = [[]]
    for word in doc:
        array[0] = 0
        for ner in doc.ents:
            if (ner.text == word.text):
                finalList.append((word.text, ner.label_))
                array[0] = 1
        if (array[0] == 0):
            finalList.append((word.text, 'O'))
    return finalList




class AutomaticQuestionGenerator():
        
    def aqgParse(self, sentence): #text = girilen metin
        nlp=en_core_web_sm.load()
        
        sentences =sentence.split(".") #metni cümlelerine ayırdık ve  (sentences)
        questionsList =[] #üretilen sorular
        print ("sentences: ", sentences)

        if len(sentences) != 0: #text uzunluğu 0 değil ise
            for i in range (len(sentences)): #cümle sayısı kadar uygula
                #segmentSets = subsections
                subsections = sentences[i].split(",") #cümlenin virgülle ayrılmış alt cümlecikleri
                tagged = wordTagging(nlp, sentences[i])
                print ("tagged: ", tagged)
                print ("subsections: ", subsections)


                if (len(subsections)) != 0:
                    for j in range(len(subsections)):
                        try:
                            questionsList += clause.module7(subsections, j, tagged)
                        except Exception:
                            pass

                        if idCard.clause_identify(subsections[j]) == 1:
                            try:
                                questionsList += clause.module1(subsections, j, tagged)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.module2(subsections, j, tagged)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.module3(subsections, j, tagged)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.module4(subsections, j, tagged)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.module5(subsections, j, tagged)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.module6(subsections, j, tagged)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.module8(subsections, j, tagged)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.module9(subsections, j, tagged)
                            except Exception:
                                pass


                            else:
                                try:
                                    s = idCard.subjectphrase_search(subsections, j)
                                except Exception:
                                    pass

                                if len(s) != 0:
                                    subsections[j] = s + subsections[j]
                                    try:
                                        questionsList += clause.module1(subsections, j, tagged)
                                    except Exception:
                                        pass
                                    try:
                                        questionsList += clause.module2(subsections, j, tagged)
                                    except Exception:
                                        pass
                                    try:
                                        questionsList += clause.module3(subsections, j, tagged)
                                    except Exception:
                                        pass
                                    try:
                                        questionsList += clause.module4(subsections, j, tagged)
                                    except Exception:
                                        pass
                                    try:
                                        questionsList += clause.module5(subsections, j, tagged)
                                    except Exception:
                                        pass
                                    try:
                                        questionsList += clause.module6(subsections, j, tagged)
                                    except Exception:
                                        pass

                                    else:
                                        try:
                                            questionsList += nounClause.module1(subsections, j, tagged)
                                        except Exception:
                                            pass
                                        try:
                                            questionsList += nounClause.module2(subsections, j, tagged)
                                        except Exception:
                                            pass
                                        try:
                                            questionsList += nounClause.module3(subsections, j, tagged)
                                        except Exception:
                                            pass
                                        try:
                                            questionsList += nounClause.module4(subsections, j, tagged)
                                        except Exception:
                                            pass
                                        try:
                                            questionsList += nounClause.module5(subsections, j, tagged)
                                        except Exception:
                                            pass

                questionsList.append('\n')
        return questionsList



   
    
    # AQG Display the Generated Question
    def display(self, str):
        print("\n")
        print("------------")
        print("Sorular:\n")
        #print("jhkjnl : "+str[0][:-1])

        count = 0
        out = ""
        for i in range(len(str)):
            if (len(str[i]) >= 3):
                if (validation.hNvalidation(str[i]) == 1):
                    if ((str[i][0] == 'W' and str[i][1] == 'h') or (str[i][0] == 'H' and str[i][1] == 'o') or (
                            str[i][0] == 'H' and str[i][1] == 'a')):
                        WH = str[i].split(',')
                        #print("WDGHJ : "+WH[0]) #BURASI SORULAR TEKER TEKER ALINIYOR.
                        if (len(WH) == 1):
                            #segmentsets deki 3 n den dolayı temizle sonuna ? koy.
                            str[i] = str[i][:-1]
                            str[i] = str[i][:-1]
                            str[i] = str[i][:-1]
                            str[i] = str[i] + "?"
                            count = count + 1

                            if (count < 10):
                                soru = "Q-0%d: %s" % (count, str[i])
                                print(soru)
                                #soruList = ""
                                #soruList += "Q-0" + count.__str__() + ": " + str[i] + "\n"
                                out += ("Q-0" + count.__str__() + ": " + str[i] + "\n")
                                
                            else:
                                print("Q-%d: %s" % (count, str[i]))
                                out += "Q-" + count.__str__() + ": " + str[i] + "\n"
                                
                            
        print("")
        print("Soruların Bitimi")
        print("----------\n\n")
        """
        output = "C:/Users/onur/Desktop/Automatic-Question-Generator-master/AutomaticQuestionGenerator/DB/output.txt"
        w = open(output, 'w+', encoding="utf8")
        w.write(out)
        w.close()
        """
        return out