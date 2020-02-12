from stringUtil import *


class Parser:
    # This method return a variation of string a list of
    # [original length, original word, snake case of the word, splits after split by _, initials of the splits]
    def parse(self, input_str):

        original_length = len(input_str)
        original_str = input_str

        input_str = to_snake_case(input_str)
        variations = [original_length, original_str, input_str]

        splits = input_str.split('_')
        if len(splits) > 1:
            variations = variations + splits

            initial = ""
            for sub_str in splits:
                if len(sub_str) > 0:
                    initial = initial + sub_str[0]

            if initial != "":
                variations = variations + [initial]

        # print(variations)
        return variations


if __name__ == '__main__':
    word = "Article_Title"
    obj = Parser()
    print(obj.parse(word))
