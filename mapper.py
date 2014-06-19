import os

with open('/dev/input') as fp:
    data = fp.read()

path_info = os.environ['PATH_INFO']
short_path = '/'.join(path_info.split('/')[2:])

with open('/dev/out/reducer', 'a') as fp:
    fp.write('%d %s' % (len(data.split()), short_path))
    fp.close()
