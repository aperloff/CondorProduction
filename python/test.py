from jobSubmitter import jobSubmitter
print '-'*10
print "Testing -c"
js = jobSubmitter(argv=["-c"])
js.run()
print '-'*10
print "Testing -p"
js = jobSubmitter(argv=["-p"])
js.run()
print '-'*10
print "Testing -s"
js = jobSubmitter(argv=["-s"])
js.run()
print '-'*10
print "Testing -m"
js = jobSubmitter(argv=["-m"])
js.run()
