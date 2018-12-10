dc0efb91cd8b

yum install python-devel libevent-devel openldap-devel gcc
tar -zxvf  python-ldap-2.4.25.tar.gz && cd python-ldap-2.4.25 && python setup.py install
pip install django-auth-ldap
