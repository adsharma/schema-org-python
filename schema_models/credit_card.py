from schema_models.loan_or_credit import LoanOrCredit


class CreditCard(LoanOrCredit):
    """
    A card payment method of a particular brand or name.  Used to mark up a particular payment method and/or the financial product/service that supplies the card account.

    Commonly used values:

    * http://purl.org/goodrelations/v1#AmericanExpress
    * http://purl.org/goodrelations/v1#DinersClub
    * http://purl.org/goodrelations/v1#Discover
    * http://purl.org/goodrelations/v1#JCB
    * http://purl.org/goodrelations/v1#MasterCard
    * http://purl.org/goodrelations/v1#VISA

    """
