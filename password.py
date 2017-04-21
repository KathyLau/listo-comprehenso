# list comprehension HW

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
nums = "1234567890"
symbols = ".?!&#,;:-_*"

def helper(pword):
     return [0.3 if char in lower else
            1 if char in upper else
            1.5 if char in nums else
            2 if char in symbols else
            0 for char in pword]
     
def threshold(pword):
     a = helper(pword)
     return 1 in a and 2 in a and 3 in a

def strength_rating(pword):
     a = helper(pword)
     return sum(a)
    
print strength_rating('3spr3sS0')
#print threshold('??5jpsdP')
