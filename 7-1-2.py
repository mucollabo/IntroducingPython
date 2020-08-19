actor = 'Richard Gere'
cat = 'Chester'
weight = 28

print("My wife's favorite actor is %s" %actor)
print("Our cat %s weight %s pounds" %(cat, weight))

n = 42
f = 7.03
s = 'string cheese'

d = {'n':42, 'f':7.03, 's':'string cheese'}
print('{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other'))

print('{0:d} {1:f} {2:s}'.format(n, f, s))

print('{n:d} {f:f} {s:s}'.format(n=42, f=7.03, s='string cheese'))

print('{0:10d} {1:10f} {2:10s}'.format(n, f, s))

print('{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s))

print('{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s))

print('{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s))

print('{0:>10d} {1:>10.4f} {2:>10.4s}'.format(n, f, s))

print('{0:!^20s}'.format('Big Sale'))