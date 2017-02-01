import  tweepy
import  config
import  schedule
dirpass = "/Users/takumi/PycharmProjects/schedule/"

# Setting
CONSUMER_KEY = 'JhlKQ1588Slr3TyvhQV3xORcZ'
CONSUMER_SECRET = 'hoBOVmcJ4FannA3KFj0mf6sbp0lGkZJlte9hccDKmQSMgOqVTJ'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = '732567257583226880-QRIIXEbcCCi3j5Axxap5li8GGAZFjbT'
ACCESS_SECRET = 'LBlxDWSfo8aFu3t6R4eA4EWeENuz8CPg6WPBFDRyKhNqz'
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

if config.title_num == 1:
    fr = open(dirpass + 'Schedule1.txt', 'r')
    content = fr.read()
    fr.close()
    api.update_status(status=content)
    # print(content)
elif config.title_num > 1:
    for i in range(config.title_num):
     fd = open(dirpass + 'Schedule'+str(i+1)+'.txt','r')
     contents = fd.read()
     api.update_status(status=contents)
     # print(contents)
    fd.close()

