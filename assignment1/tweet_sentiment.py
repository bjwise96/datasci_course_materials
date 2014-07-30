import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def build_sent_dict(read_file):
  scores = {}
  for line in read_file:
    term, score = line.split("\t")
    scores[term] = int(score)
  return scores


def process_tweets(in_file,in_dict):
    for line in in_file:
       tweet = json.loads(line)
       #print tweet.keys()
       if "text" in tweet:
           word_list = tweet["text"].split()
           score = score_tweet(word_list,in_dict)
           print score
    

def score_tweet(in_list,in_dict):
  score = 0
  for word in in_list:
    if word in in_dict:
      score = score + in_dict[word]        
  return score


def main():
    sent_file = open(sys.argv[1])
    sent_dict = build_sent_dict(sent_file)
    #print type(sent_dict)
    #print len(sent_dict)
    tweet_file = open(sys.argv[2])
    process_tweets(tweet_file,sent_dict)
      
    

if __name__ == '__main__':
    main()
