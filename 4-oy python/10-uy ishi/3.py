    lst=list(range(1,10))
    class Juft_Kalkulyator:
        
        def sum(self,lst):
            sum=0
            for i in lst:
                if i%2==0:
                    sum+=i
            return sum
        def average(self,lst):
            sum=0
            soni=0
            for i in lst:
                if i%2==0:
                    sum+=i
                    soni+=1
            return sum/soni
        def multi(self,lst):
            sum=1
            for i in lst:
                if i%2==0:
                    sum*=i
            return sum
    a=Juft_Kalkulyator()
    print(a.sum(lst))
    print(a.average(lst))
    print(a.multi(lst))