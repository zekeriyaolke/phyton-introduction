class HangMan:
    def __init__(self):
        self.errorCount = 0
        self.maxErrorCount = 5
        self.usersAnswer = ""
        self.currentAnswerIndex = 0

    def start(self):
        print("Soruyu Giriniz!:")
        self.question = self.validateQuestion(input())
        print("Cevabı Giriniz!:")
        self.answer = self.validateAnswer(input())
        print("\n\n\n\n\nOyun başladı!\n")
        print("Soru: " + self.question)

    def validateQuestion(self, question):
        if len(question) > 1:
            return question
        raise ValueError("Soruyu giriniz!")

    def validateAnswer(self, answer):
        if len(answer) > 1:
            return answer
        raise ValueError("Cevabı giriniz!")

    def getRemainingError(self):
        return self.maxErrorCount - self.errorCount

    def addAnswerChar(self, answerPart):
        self.usersAnswer += answerPart
        return self.usersAnswer == self.answer

    def validateAnswerChar(self, answerPart):
        return len(answerPart) == 1

    def end(self):
        print("Tebrikler cevabı bildiniz!!\n " + hangman.usersAnswer)

try:
    hangman = HangMan()
    hangman.start()

    while hangman.usersAnswer != hangman.answer:
        answerPart = input("Cevabın " + str(hangman.currentAnswerIndex + 1) + " harfini giriniz: \n")
        if hangman.validateAnswerChar(answerPart) == False:
            print("Lütfen tek karakter giriniz!")
            continue

        if hangman.answer[hangman.currentAnswerIndex] != answerPart:
            hangman.errorCount += 1
            if hangman.errorCount == hangman.maxErrorCount:
                print("Kaybettiniz!")
                break
            else:
                print(str(hangman.getRemainingError()) + " yanlış hakkınız kaldı.")
        else:
            if hangman.addAnswerChar(answerPart):
                hangman.end()
            hangman.currentAnswerIndex += 1

except ValueError as error:
    print('Hata: ' + repr(error))
# except Exception as other:
#         print("Bilinmeyen hata oluştu: " + repr(other))
