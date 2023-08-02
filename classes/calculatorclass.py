class calculator:
    """Class representing a person"""

    def basic_operation_sum(self,*list_of_numbers):
        result = 0
        for num in list_of_numbers:
            result+=num
        return result

    def basic_operation_sub(self,*list_of_numbers):
        result = 0
        for indx, num in enumerate(list_of_numbers):
            if indx == 0:
                result = num
                continue
            result-=num
        return result
    
    def basic_operation_mul(self,*list_of_numbers):
        result = 0
        for indx, num in enumerate(list_of_numbers):
            if indx == 0:
                result = num
                continue
            result*=num
        return result
    
    def basic_operation_dev(self,*list_of_numbers):
        result = 0
        for indx, num in enumerate(list_of_numbers):
            if indx == 0:
                result = num
                continue
            if num == 0:
                raise ZeroDivisionError("NOT possitble devide by 0")
            result/=num
                
        return result