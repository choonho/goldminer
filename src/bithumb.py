import httplib
import json
import time


class Bithumb:
    def __init__(self, public_url="api.bithumb.com", currency=["BTC","ETH","DASH","LTC","ETC","XRP"], interval=60):
        self.public_url = public_url
        self.private_url = None
        self.currency = currency
        self.histogram = {}
        self.delta= {}
        self.INTERVAL = interval
        for C in self.currency:
            self.histogram[C] = {}
            self.delta[C] = []

    def run(self, target="ETH"):
        count = 0
        while True:
            time.sleep(1)
            now = self.get_price(target)
            if now == None:
                continue
            self.histogram[target][count % self.INTERVAL] = int(now)
            self.calculate_delta(target, count)
            print self.histogram
            print self.delta
            count = (count + 1) % self.INTERVAL

    def calculate_delta(self, target, count):
        if len(self.histogram[target].keys()) < self.INTERVAL:
            print "Collecting period..."
            return
        # Calculate delta
        print count
        idx = count % self.INTERVAL
        prev = (idx - 1) % self.INTERVAL
        print "idx=%s, prev=%s, v1=%s, v2=%s" % (idx, prev, self.histogram[target][idx], self.histogram[target][prev])
        delta = self.histogram[target][idx] - self.histogram[target][prev]
        self.delta[target].append(delta)
        avg = 0
        if len(self.delta[target]) >= self.INTERVAL:
            # Too many list
            del self.delta[target][0]
            # Calculate Average
            sum = 0
            for i in range(self.INTERVAL-1):
                sum = sum + self.delta[target][i]
            avg = sum / (self.INTERVAL - 1)
        print "AVG:%s" % avg

    def get_price(self, coin):
        """
        get coin price
        """
        conn = httplib.HTTPSConnection(self.public_url)
        url = "/public/ticker/%s" % coin
        conn.request("GET",url)
        res = conn.getresponse()
        print res.status, res.reason
        if res.status == 200:
            data =json.loads(res.read())
            if data["status"] == "0000":
                # OK
                buy_price =  data["data"]["buy_price"]
                sell_price = data["data"]["sell_price"]

                print buy_price, sell_price
                return buy_price
        else:
            print "Error"
        return None


if __name__ == "__main__":
    inst = Bithumb(interval=10)
    inst.run("ETH")

