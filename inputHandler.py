class InputHandler:
    def __init__(self):
        self.inputs = {}
    
    def add_question(self, label, q):
        inp = input(f'{q}? ')
        self.inputs[label] = inp
    
    def add_n_question(self, label, q, n=None, nq=None):
        if n and not nq:
            inp_res = []
            for i in range(0, n):
                inp_res.append(input(f'{q} {i} ? '))
            self.inputs[label] = inp_res
        elif not n and nq:
            n_q = input(f'{nq}? ')
            inp_res = []
            for i in range(0,int(n_q)):
                inp_res.append(input(f'{q} {i} ? '))
            self.inputs[label] = inp_res
        return
    
    def get_inputs(self):
        return self.inputs

if __name__ == '__main__':
    ih = InputHandler()
    ih.add_question('name', 'What is your name')
    ih.add_question('age', 'What is your age')
    ih.add_n_question('sports', 'Name your three favorite sports', n=3)
    ih.add_n_question('morning', 'What is your morning routine', nq='How many steps are there in your morning routine')
    final = ih.get_inputs()
    print(final)