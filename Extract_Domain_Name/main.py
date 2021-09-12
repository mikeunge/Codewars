#!/usr/bin/python3
# -*-coding:utf-8-*-


def domain_name(url):
    url_arr = url.split(".")
    if url_arr[0] == "http://www" or url_arr[0] == "https://www" or url_arr[0] == "www":
        return url_arr[1]
    no_www = url_arr[0].split("//")
    if len(no_www) > 1:
        return no_www[1]
    else:
        return no_www[0]


# This is so genius I can-
def domain_name_best_solution(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


def run_test():
    print(domain_name("http://www.google.com"))
    print(domain_name("http://google.com"))
    print(domain_name("http://google.co.jp"))
    print(domain_name("https://github.com/mikeunge/"))
    print(domain_name("www.xakep.ru"))
    print(domain_name("https://youtube.com"))

if __name__ == "__main__":
    run_test()
