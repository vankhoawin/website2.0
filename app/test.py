__author__ = 'Van'


import flickrapi

api_key = 'aa97f39fc7ff944178ebd92711b9ab35'

flickr = flickrapi.FlickrAPI(api_key, cache=True)
flickr.cache = flickrapi.SimpleCache(timeout=300, max_entries=50)

sets = flickr.photosets_getList(user_id='126052905@N03')
#print flickr.photos_getRecent().__dict__

recent = flickr.photos_search(user_id='126052905@N03', per_page=5)

#for photo in recent.getchildren()[0]:
#    print '<img src="'+"http://farm%s.static.flickr.com/%s/%s_%s_m.jpg"\
#        % (photo.get('farm'), photo.get('server'), photo.get('id'), photo.get('secret')) +'" />'


for elm in sets.getchildren()[0]:
    print "new set"
    for photo in flickr.walk_set(elm.get('id')):
        print '<img src="'+"http://farm%s.static.flickr.com/%s/%s_%s_m.jpg"\
            % (photo.get('farm'), photo.get('server'), photo.get('id'), photo.get('secret')) +'" />'
