from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):

        self.user_tweets = defaultdict(list[tuple[int, int]])
        self.following = defaultdict(set[int])
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.user_tweets[userId].append(
            (-self.time, tweetId)
        )

        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        valid_users = self.following[userId] | {userId}

        # put all latest tweets of all valid_users in a max heap

        heap = []

        for user_id in valid_users:

            if len(self.user_tweets[user_id]) == 0:
                continue

            # get their latest tweet obj

            c_time, c_tweetId = self.user_tweets[user_id][-1]

            next_latest_idx = len(self.user_tweets[user_id]) - 2

            tup = (c_time, c_tweetId, user_id, next_latest_idx)

            heapq.heappush(heap, tup)

        # now that heap is filled with latest tweets, we do the following:

        # pull latest tweet id by popping. store that in a result array
        # push the next latest tweet by that popped tweet's user
        # continue until result is full

        result = []

        while heap and len(result) != 10:

            c_time, c_tweetId, c_user_id, c_next_latest_idx = heapq.heappop(heap)
            
            result.append(c_tweetId)

            # ---------

            if c_next_latest_idx >= 0:

                n_time, n_tweetId = self.user_tweets[c_user_id][c_next_latest_idx]

                tup = (n_time, n_tweetId, c_user_id, c_next_latest_idx - 1)

                heapq.heappush(heap, tup)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:

        self.following[followerId].add(
            followeeId
        )

    def unfollow(self, followerId: int, followeeId: int) -> None:

        self.following[followerId].discard(
            followeeId
        )
        
