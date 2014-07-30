import sys
import json
from collections import Counter


def process_hashtags(tweet_file):
    hashtag_dict = {}
    my_counter = Counter()
    for line in tweet_file:
        tweet = json.loads(line)
        if "entities" in tweet:
            hashtags = tweet["entities"]["hashtags"]
            for i in hashtags:
                if "text" in i:
                    hashtag_text = i["text"]
                    my_counter[hashtag_text] += 1
    return my_counter


def main():
    tweet_file = open(sys.argv[1])
    my_counter = process_hashtags(tweet_file)
    for hashtag,count in my_counter.most_common(10):
        print hashtag + " " + str(count)


if __name__ == '__main__':
    main()