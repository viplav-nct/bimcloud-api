import argparse
import sys
import lib

def start():
	parser = argparse.ArgumentParser()
	parser.add_argument('-m', '--manager', required=True, help='Url of BIMcloud Manager.')
	parser.add_argument('-c', '--clientid', required=True, help='3rd party client id (arbitrary unique string, your domain for example).')
	parser.add_argument('-d', '--debug', required=False, help='Debug exceptions.', action='store_true')
	args = parser.parse_args()

	wf = lib.Workflow(args.manager, args.clientid)
	try:
		wf.run()
	except Exception as err:
		print(getattr(err, 'message', str(err) or repr(err)), file=sys.stderr)
		if args.debug:
			raise err
		else:
			exit(1)

if __name__ == '__main__':
	start()
