#!/usr/bin/python3
#-*-coding:utf-8-*-


def pig_it(text):
    word_list = text.split(" ")
    new_list = []
    for w in word_list:
        if len(w) == 1:
            new_list.append(w)
            continue
        tmp = w[0]
        w = w.replace(w[0], "")
        new_list.append(w + tmp + "ay") 
    return " ".join(new_list)


def test():
    print(pig_it("Pig latin is cool"))
    print(pig_it("Hello World !"))



if __name__ == "__main__":
    test()
