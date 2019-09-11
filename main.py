#!/usr/bin/env python3

from Tori import *

if __name__ == '__main__':
    haku = Tori(location='Pohjois-Pohjanmaa', category='urheilu ja ulkoilu')
    print(haku.find_category_codes())
