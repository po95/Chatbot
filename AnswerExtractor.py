

output = open('Answers.txt', 'w', encoding='utf-8')
input = open('Questions.txt', 'r', encoding='utf-8')

class QA:
    def __init__(self):
        f = open('corpus.txt', encoding='utf-8').read()
        self.corpus = []
        s = []
        for ch in f:
            if ord(ch) == 2404:
                self.corpus.append(''.join(s))
                s = []
            else:
                s.append(ch)
        self.qwords = []
        f = open('QWords.txt', encoding='utf-8')
        for line in f.readlines():
            self.qwords.append(line)
    
    def answer(self, q):
        tmp = []
        for ch in q:
            if ord(ch) == 63:
                continue
            tmp.append(ch)
        q = ''.join(tmp)
        words = q.split()
        q = []
        for word in words:
            f = 1
            for qw in self.qwords:
                if word in qw:
                    f = 0
                    break
            if f == 1:
                q.append(word)
        candidate = []
        for sent in self.corpus:
            cnt = 0
            for w in q:
                if w in sent:
                    cnt += 1
            if cnt > 0:
                candidate.append((sent, cnt))
        candidate = sorted(candidate, key= lambda x: x[1], reverse=True)
        return candidate[0][0].strip()

qa = QA()
for q in input.readlines():
    ans = qa.answer(q)
    print(q + "উঃ-" + ans, file = output)

output.close()
input.close()
