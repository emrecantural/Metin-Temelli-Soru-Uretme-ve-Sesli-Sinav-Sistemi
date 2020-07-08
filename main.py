import textAnalysis
#text analysis

# Main Function
def main():
    # Create AQG object
    aqg = textAnalysis.AutomaticQuestionGenerator() #fonksiyonun classı

    inputTextPath = "C:/Users/emrec/Desktop/Question-Generator/texts/input.txt"
    readFile = open(inputTextPath, 'r+', encoding="utf8")
    #readFile = open(inputTextPath, 'r+', encoding="utf8", errors = 'ignore')
    inputText = readFile.read()
    #inputText = '''I am Dipta. I love codding. I build my carrier with this.'''
    print ("input: ", inputText)
    questionList = aqg.aqgParse(inputText) #clasın fonksiyonu
    aqg.display(questionList)

    #aqg.DisNormal(questionList)

    return 0


# Call Main Function
if __name__ == "__main__":
    main()