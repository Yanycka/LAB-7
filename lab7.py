class lecture(str):
    def _init(self, word: str):
        self.word = str(word)

    def find_min_tree_symbols(self, word: str):
        self.word = str(word)
        size = len(word)

        if size < 4:
            return False

        for i in range(size - 3):
            three_symbs_word = word[i] + word[i+1] + word[i+2]

            for y in range(i+1, size - 2):
                compare_next_three_symbs = word[y] + word[y+1] + word[y+2]

                if three_symbs_word == compare_next_three_symbs:
                    return True

        return False


    def palindrom(self, word: str):
        self.word = str(word)

        if word == "":
            return True

        word = "".join(char for char in word if char.isalnum())
        
        size = len(word)
        for i in range(size):
            if word[i] != word[size-i-1]:
                return False
        return True


lecture_six = lecture()

word = input("Your word: ")
print(lecture_six.find_min_tree_symbols(word))
print(lecture_six.palindrom(word))