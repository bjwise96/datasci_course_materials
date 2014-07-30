import sys
import json


def get_tweet_words(in_file):
    word_list = []
    tweets = []
    for line in in_file:
        tweet = json.loads(line)
        if "text" in tweet:
            word_list.extend(tweet["text"].split())
    uniq_words = uniq(word_list)
    all_cnt = len(word_list)
    for i in uniq_words:
        print i + "\t" + str(float(word_list.count(i))/float(all_cnt))

def uniq(input_list):
    output = []
    for x in input_list:
        if x not in output:
            output.append(x)
            #print x
    return output

def main():
    tweet_file = open(sys.argv[1])
    get_tweet_words(tweet_file)

if __name__ == '__main__':
    main()