import re

def group(string, pattern, group):
    p = re.compile(pattern)
    m = p.search(string)
    if m:
        return m.group(group)
    else:
        raise Exception()

class FilterModule(object):
    ''' A filter to return regex capture group. '''
    def filters(self):
        return {
            'group' : group
        }
