import sys
import json


def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))


def build_sent_dict(read_file):
    scores = {}
    pos_words = []
    neg_words = []
    for line in read_file:
        term, score = line.split("\t")
        scores[term] = int(score)
        if int(score) > 0:
            pos_words.append(unicode(term, errors='replace'))
            #print "pos word: " + term
        else:
            neg_words.append(unicode(term, errors='replace'))
            #print "neg word: " + term
    return scores, pos_words, neg_words


def get_tweet_words(in_file, pos_words, neg_words):
    word_list = []
    tweets = []
    for line in in_file:
        tweet = json.loads(line)
        if "text" in tweet:
            word_list.extend(tweet["text"].split())
            score = 0
            for x in pos_words:
                if x in tweet["text"]:
                    score = score + 1
            for y in neg_words:
                if y in tweet["text"]:
                    score = score - 1
            tweets.append({'id': tweet["id"], 'text': tweet["text"],'score':score})
            #print str(score) + ": " + tweet["text"]
    uniq_words = uniq(word_list, pos_words, neg_words)
    for z in uniq_words:
        new_score = 0
        for i in tweets:
            if z in i["text"].split():
                new_score = new_score + i["score"]
        print z + "\t" + str(new_score)
    return uniq_words, tweets


def uniq(input_list, pos_words, neg_words):
    output = []
    for x in input_list:
        if x not in output and x not in pos_words and x not in neg_words:
            output.append(x)
            #print x
    return output


def main():
    sent_file = open(sys.argv[1])
    sent_dict, pos_words, neg_words = build_sent_dict(sent_file)
    tweet_file = open(sys.argv[2])
    tweet_word_list, tweets = get_tweet_words(tweet_file, pos_words, neg_words)
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
