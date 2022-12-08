class Number:
    def __init__(self,number):
        self.number=number
    def get_number(self):
        return self.number
    def is_even(self):
        return self.number%2==0
    def is_odd(self):
        return self.number%2==1
    def is_prime(self):
        number=self.number
        flag = True
        if number > 1:
           for i in range(2, number):
               if (number % i) == 0:
                    flag = False
                    break
        return flag
    def get_divisors(self):
        number=self.number
        flag = ''
        if number > 1:
           for i in range(2, number):
               if (number % i) == 0:
                    flag +=str(i)+','
                    
        return flag+str(number)
    def get_length(self):
        number=self.number
        digits=''
        for i in str(number):
            digits+=str(i)+','
        return digits[:-1]
    def get_sum(self):
        number=self.number
        sum=0
        for i in str(number):
            sum+=int(i)
        return sum
    def get_product(self):
        number=self.number
        sum=1
        for i in str(number):
            sum*=int(i)
        return sum
    def get_reverse(self):
        number=self.number
        reverse=''
        for i in str(number)[::-1]:
            reverse+=i
        return reverse
    def get_digits(self):
        number=self.number
        list1=[]
        for i in str(number):
            list1+=[int(i)]
        return list1
    def get_max(self):
        return max(str(self.number))
    def get_min(self):
        return min(str(self.number))
    def get_average(self):
        number=self.number
        sum=0
        for i in str(number):
            sum+=int(i)
        return sum/len(str(number))
    def get_median(self):
        number=self.number
        sum=1
        for i in str(number):
            sum*=int(i)
        return sum**(1/len(str(number)))
    def get_mode(self):
        pass
    def get_range(self):
        number=self.number
        range_=''
        for i in range(number):
            range_+=str(i)+','
        return range_+str(number)
    def get_frequency(self):
        pass
x=Number(number=12)
print(x.number)
print(x.get_number())
print(x.is_even())
print(x.is_odd())
print(x.is_prime())
print(x.get_divisors())
print(x.get_length())
print(x.get_sum())
print(x.get_product())
print(x.get_reverse())
print(x.get_digits())
print(x.get_max())
print(x.get_min())
print(x.get_average())
print(x.get_median())
print(x.get_range())