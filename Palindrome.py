def isPalindrome(x):
    def isPalindrome(self, x):

        #음수값은 펠린드롬 적용이 안됨
       if x < 0:
            return False
       
       else:
           nums2 = str(x)
           if nums2[:] == nums2[::-1]:
               return True
