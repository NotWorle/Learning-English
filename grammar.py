class BaseGrammar:
    def __init__(self):
        self.s = 'S'
        self.v = 'V'
        self.o = 'O'

    def set_s(self, s):
        self.s = s
    def set_v(self, v):
        self.v = v
    def set_o(self, o):
        self.o = o

    def __str__(self):
        return f'{self.s} + {self.v} + {self.o}'

class BaseAffirmative(BaseGrammar):
    def __init__(self):
        BaseGrammar.__init__(self)

class BaseNegative(BaseGrammar):
    def __init__(self):
        BaseGrammar.__init__(self)
        self.no = 'not'

    def set_no(self, no):
        self.no = no

    def __str__(self):
        return f'{self.s} + {self.v} + {self.no} + {self.o}'

class BaseQuestionAffirmative(BaseAffirmative):
    def __init__(self):
        BaseGrammar.__init__(self)

    def __str__(self):
        return f'{self.v} + {self.s} + {self.o}'

class BaseQuestionNegative(BaseNegative):
    def __init__(self):
        BaseNegative.__init__(self)

    def __str__(self):
        return f'{self.v} + {self.no} + {self.s} + {self.o}'

class FutureInPast(BaseGrammar):
    def __init__(self):
        BaseGrammar.__init__(self)



base = BaseGrammar()
affirmative = BaseAffirmative()
negative = BaseNegative()
question_affir = BaseQuestionAffirmative()
question_negative = BaseQuestionNegative()
print(base)
print(affirmative)
print(negative)
print(question_affir)
print(question_negative)