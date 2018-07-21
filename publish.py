import redis
import sys

def main():
  r = redis.client.StrictRedis()
  args = sys.argv
  if len(args) > 1 :
    for arg in args[1:] :
        print('Sending {0}'.format(arg))
        r.publish('jelly', arg)

if __name__ == '__main__':
  main()
