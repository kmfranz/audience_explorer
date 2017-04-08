from googleads import oauth2
from oauth2client import client


auth_code = "4/zdqc6DgHWcABsrG8-SJ3aPzQazmsIH2R9i8Hgiz1-H8#"

credentials = flow.step2_exchange(auth_code)

print credentials
