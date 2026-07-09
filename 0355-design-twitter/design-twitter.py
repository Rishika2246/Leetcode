from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)   # userId -> [(time, tweetId)]
        self.following = defaultdict(set) # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1  # newer tweets get smaller values for min-heap

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following[userId] | {userId}

        # Put each user's most recent tweet into the heap
        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]
                heapq.heappush(heap, (time, tweetId, user, index))

        feed = []

        # Merge tweet lists and take only the 10 newest tweets
        while heap and len(feed) < 10:
            time, tweetId, user, index = heapq.heappop(heap)
            feed.append(tweetId)

            if index > 0:
                prev_time, prev_tweet = self.tweets[user][index - 1]
                heapq.heappush(heap, (prev_time, prev_tweet, user, index - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)