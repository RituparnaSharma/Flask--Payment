import datetime

"""
ValidateCard method helps to find the validity of credit card based on Luhn Algorithm.
Luhn a simple checksum formula used to validate a variety of identification numbers,
such as credit card numbers, IMEI numbers, Canadian Social Insurance Numbers etc.

https://en.wikipedia.org/wiki/Luhn_algorithm
"""


class verify:
    @staticmethod
    def __ValidateCard(CreditCardNumber):
        even_sum = 0
        odd_sum = 0
        try:
            for i in list(CreditCardNumber)[-2::-2]:
                val = str(int(i) * 2)
                if len(val) > 1:
                    even_sum += int(val[0]) + int(val[1])
                else:
                    even_sum += int(val)
            odd_sum += sum(list(map(int, list(CreditCardNumber)[-1::-2])))

        except:
            return False

        if (even_sum + odd_sum) % 10 == 0:
            return True
        return False

    """
    
    for any Premium Payment Gateway,
    check if the payment is true arr false (payment=?)
    if true,function will return (gateway and True)
    if False ,call itself recursively until the counter value will equal to zero.
    
    """

    @staticmethod
    def __PaymentGateway(counter=None, gateway=None, payment=None, flag=None):

        if gateway == 'PremiumPaymentGateway':
            if counter == 0:
                return "Error500"
            elif payment:
                flag = True
                return flag, gateway
                # fun(no-1,payment)
            else:
                return verify.__PaymentGateway(counter - 1, gateway='PremiumPaymentGateway')

        elif gateway == 'ExpensivePaymentGateway':

            if counter == 0:
                return "Error500"
            elif counter == 1 and payment:
                flag = True
                return flag, 'CheapPaymentGateway'
                # fun(no-1,gateway='ExpensivePaymentGateway')
            elif payment:
                flag = True
                return flag, gateway
                # fun(no-1,gateway='ExpensivePaymentGateway')
            else:
                return verify.__PaymentGateway(counter - 1, gateway='ExpensivePaymentGateway')

        else:
            if payment:
                flag = True
                return flag, 'CheapPaymentGateway'
            else:
                return "Error500"

    @staticmethod
    def ProcessPayment(CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount):
        # Check the possibility of bad input -->
        permission = False
        try:
            for i in [CreditCardNumber, CardHolder, ExpirationDate, SecurityCode]:
                assert len(str(i)) > 0
                assert type(i) == str
            today = datetime.datetime.strptime(datetime.date.today().strftime("%m/%y"), "%m/%y")  # current month/year
            exp_date = datetime.datetime.strptime(ExpirationDate, "%m/%y")  # provider  month/year
            assert verify.__ValidateCard(CreditCardNumber)
            assert (exp_date - today).days > 0
            assert len(str(SecurityCode)) == 3
            assert float(Amount) > 0
            permission = True
        except:
            return permission

        """
        if All inputs are correct ,Amount will be forwarded to the PaymentGateway method  
        value of variable payment will decide the success and failure of payment -->
        
        """
        if permission:
            try:
                if int(float(Amount)) in range(0, 21):
                    return verify.__PaymentGateway(gateway='CheapPaymentGateway', payment=True)
                elif int(float(Amount)) in range(21, 500):
                    return verify.__PaymentGateway(counter=2, gateway='ExpensivePaymentGateway', payment=True)
                else:
                    return verify.__PaymentGateway(counter=3, gateway='PremiumPaymentGateway', payment=True)
            except:
                return "Error500"
