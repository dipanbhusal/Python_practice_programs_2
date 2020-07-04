class ValidityChecker:
    
    def check(self, string):
        
        list_res = []
        opening_paranthesis = ['(','{', '[']
        for each_paranthesis in string:
            if each_paranthesis  in  opening_paranthesis:
                list_res.append(each_paranthesis)
            else:
                if not list_res:
                    return False #empty list 
                previous_paranthesis = list_res[-1]
                if each_paranthesis == ')':
                    if previous_paranthesis == '(':
                        list_res.pop()
                        
                if each_paranthesis == '}':
                    if previous_paranthesis == '{':
                        list_res.pop()
                if each_paranthesis == ']':
                    if previous_paranthesis == '[':
                        list_res.pop()
        if  list_res:
            return False
        return True

checker = ValidityChecker()
paranthesis = '[]()'
if checker.check(paranthesis):
    print('Valid')
else:
    print('Invalid')

