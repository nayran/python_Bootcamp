class Evaluator:
    @classmethod
    def zip_evaluate(self, coefs=[], words=[]):
        if len(coefs) != len(words):
            return -1
        final = 0
        x = zip(words, coefs)
        for i in x:
            final += len(i[0]) * i[1]
        print(final)
        return x

    @classmethod
    def enumerate_evaluate(self, coefs=[], words=[]):
        if len(coefs) != len(words):
            return -1
        final = 0
        for i, word in enumerate(words):
            final += len(word) * coefs[i]
        print(final)
        return final


words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, 1.0, -12.0, 0.0, 42.42]
Evaluator.enumerate_evaluate(coefs, words)

words = ['Le', 'Lorem', 'Ipsum', 'est', 'simple']
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.zip_evaluate(coefs, words)
