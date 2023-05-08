http_status = 200

match http_status:
  case 200 | 201: # |: or operator
    print('Success')
  case 400:
    print('Bad request')
  case 500 | 501:
    print('Internal Server Error')
  case _: # default condition
    print('Unknown')
