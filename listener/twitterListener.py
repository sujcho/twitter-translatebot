"""
Author - Anu Vaidya, Sujin Emily Cho
date: Mar 12, 2017
Get Streaming tweets for a specific user
"""
import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream

import json

import sys
sys.path.append('..')
from dbConnect import connect_to_DB
from dbAssembler import *

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, user_list):
        print("init")
        self.__this_id = user_list

    def on_data(self, data):

        all_data = json.loads(data)
        tweet_obj={}
        author = all_data['user']['id_str']

        if(author in self.__this_id) :
            print("same?")
            tweet_obj['text'] = all_data['text']
            tweet_obj['lang'] = all_data['lang']
            print (tweet_obj['text'])
        return tweet_obj

    def on_error(self,status):
        print(status)


class TwitterListener:

    def __read_cfg_from_DB(self):
        cfg = {}
        with open("cfg.txt", "r") as f:
            for line in f:
                # we have to retrieve the correct key for listener.
                key, value = line.strip().split(':')
                cfg[key] = value
                print("cfg " + cfg[key])
        return cfg

    def __get_userlist(self):
        #list of users to follow. Added value has to be "id" not username.
        #reading from DB
        user_list = ['25073877','838107760721985536']
        return user_list

    def __init__(self):
        self.metaData= connect_to_DB()
        self.cfg = self.__read_cfg_from_DB()
        self.user_list = self.__get_userlist()

    #athenticated and get twitter handle
    def get_authenticated(self):

        if self.cfg is not None:
            auth = tweepy.OAuthHandler(self.cfg['consumer_key'], self.cfg['consumer_secret'])
            auth.set_access_token(self.cfg['access_token'], self.cfg['access_token_secret'])
            return tweepy.API(auth)

        else:
            print ("%s: %s at %s" % ('Error','config data is null',__file__))


    def main(self):

        api = self.get_authenticated()
        self.myStreamListener =  MyStreamListener(self.user_list);

    #    my_stream_listener = MyStreamListener();
    #Do we also need depenedcy injection for stream instance?
        my_stream = tweepy.Stream(auth = api.auth,listener=self.myStreamListener)
        my_stream.filter(follow= self.user_list, async=True)


if __name__ == "__main__":

    MyTwitterListener = TwitterListener()
    MyTwitterListener.main()
    myDB = SQLAssembler(DB_model="sqlite3", database="test.db")
