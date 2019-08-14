import ldap

def authenticate(username, password):
	return {'status':'success', 'message':'successfully logged in'}
	#TODO remove testt success above
	server = 'ldap://10.87.20.53:389'
	conn = ldap.initialize(server)
	conn.protocol_version = 3
	conn.set_option(ldap.OPT_REFERRALS, 0)
	try:
		conn.simple_bind_s(username+'@corp.tstt.local', password)
		conn.unbind()
		return {'status':'success', 'message':'successfully logged in'}
	except ldap.INVALID_CREDENTIALS:
		return {'status':'failure', 'message':'wrong username/password'}
	except ldap.SERVER_DOWN:
		return {'status':'failure', 'message':'Server Down'}
	except Exception as e:
		print e
		return {'status':'failure', 'message':'unknown issues'}

if __name__ == '__main__':
	# test = 'baf3a6680ff0eafae59664bcf30ad18a'
	# user = 'test_ven'
	# raw = 'TestVen1'
	# print test==hash(user,raw)
	# print create_customer_password('admin','pass')
	authenticate('svc-dcrm', 'C@sino2018')
