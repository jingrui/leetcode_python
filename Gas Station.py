class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        zero = 0
        i = 0
        startingStations = set(range(len(gas)))
        while True:
            if i in startingStations:
                startingStations.remove(i)
            else:
                break

            remain = 0
            station = i
            while True:
                remain += gas[station]
                remain -= cost[station]
                print "start = {}, station = {}, remain = {}"\
                    .format( i, station, remain)

                station += 1
                station %= len(gas)
                if remain < 0:
                    i = station
                    break

                if station == i:
                    return i

            
        return -1          
                
                
        
                    
                
                
a = Solution()
print a.canCompleteCircuit([2,4], [3,4])