
class mcqs:

        def __init__(self, file_path):
                self.path = file_path
                with open(self.path, 'r+') as f:
                        text = f.readlines()
                        print(text)

        def makeQns():
            pass
