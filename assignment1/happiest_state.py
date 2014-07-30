import sys
import json
from collections import Counter


def process_tweets(in_file,in_dict):
    processed_tweets = []
    for line in in_file:
        tweet = json.loads(line)
        if "text" in tweet:
            if "lang" in tweet:
                if tweet["lang"] == "en":
                    simple_tweet = {}
                    word_list = tweet["text"].split()
                    score = score_tweet(word_list,in_dict)
                    simple_tweet["tweet_id"] = tweet["id_str"]
                    simple_tweet["score"] = score
                    simple_tweet["user_location"] = tweet["user"]["location"].upper()
                    simple_tweet["coordinates"] = tweet["coordinates"]
                    processed_tweets.append(simple_tweet)
    return processed_tweets


def build_sent_dict(read_file):
  scores = {}
  for line in read_file:
    term, score = line.split("\t")
    scores[term] = int(score)
  return scores

def score_tweet(in_list,in_dict):
  score = 0
  for word in in_list:
    if word in in_dict:
      score = score + in_dict[word]
  return score


def get_state(simple_tweet):
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    rev_states = {}
    for state in states:
        rev_states[states[state].upper()] = state
    tweet_state = []
    state_set = set(states.keys())
    rev_state_set = set(rev_states.keys())
    location_words = simple_tweet["user_location"].split()
    location_set = set(location_words)
    for x in location_set.intersection(state_set):
        tweet_state.append(x)
    for x in location_set.intersection(rev_state_set):
        tweet_state.append(rev_states[x])
    return tweet_state


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dict = build_sent_dict(sent_file)
    tweets = process_tweets(tweet_file,sent_dict)
    state_cnt = Counter()
    state_sum = Counter()
    state_avg = Counter()
    for tweet in tweets:
        tweet_state = get_state(tweet)
        for x in tweet_state:
            state_cnt[x] += 1
            state_sum[x] += tweet["score"]
    for state in state_sum:
        state_avg[state] = float(state_sum[state])/float(state_cnt[state])
        #print state + " " + str(state_avg[state])
    print state_avg.most_common(1)[0][0]


if __name__ == '__main__':
    main()