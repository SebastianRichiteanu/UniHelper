class Homework:
    def __init__(self,deadline,exerc,submit):
        self.deadline = deadline
        self.exerc = exerc
        self.submit = submit
    def edit(self,dl,ex,sb):
        if dl:
            self.deadline = dl
        if ex:
            self.exerc = ex
        if sb:
            self.submit = sb
    def p(self):
        print(self.deadline+" "+self.exerc+" "+self.submit)

class Subject:
    def __init__(self,name,hws,test,exam):
        self.name = name
        self.hws = hws
        self.test = test
        self.exam = exam
    def p(self):
        for h in self.hws:
            h.p()
        print(self.test)
        print(self.exam)

