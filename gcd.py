'''
>>> res=Eclide()
>>> res.gcd(1440,408)
24
'''

class Euclide:
    def gcd(self,p,q):
        if p==0:
            return q
        else:
            return self.gcd(q,p%q)
        