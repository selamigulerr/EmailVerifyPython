from validate_email import validate_email
is_valid = validate_email(email_address='selami.gulerr@gmail.com',
                          check_regex=True,
                          check_mx=True,
                          smtp_timeout=10,
                          dns_timeout=10,
                          use_blacklist=True,
                          debug=False)

print(is_valid)
