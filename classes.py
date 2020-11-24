class Homework:
    def __init__(self,deadline="not set yet",exerc="not set yet",submit="not set yet"):
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
        if id:
            self.id = id

class Subject:
    def __init__(self,name="not set yet",hws=[],test="not set yet",exam="not set yet"):
        self.name = name
        self.hws = []
        self.test = test
        self.exam = exam


