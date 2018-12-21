
row = option_object.get_queryset_or_tuple(self.model_class,request,*args,**kwargs)

Option('gender').get_queryset_or_tuple(self.model_class,request,*args,**kwargs)
return
SearchGroupRow(verbose_name,field_object.rel.model.objects.filter(**db_condition),self,request.GET)


class PrimeNumbers(object):
    def __init__(self,start,end): 
        self.start=start
        self.end=end

    def isPrimeNumber(self,k):
        for i in xrange(2,k):
            if k%i==0:
                return False
        return True;

    def __iter__(self):
        for k in xrange(self.start,self.end+1):
            if self.isPrimeNumber(k):
                yield k    

for x in PrimeNumbers(1,10):
    print x
