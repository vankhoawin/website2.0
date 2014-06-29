from flask import Flask, render_template
from pyfb import Pyfb

app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('layout.html')

@app.route('/photography')
def photography():
    FACEBOOK_APP_ID = '511339372322388'
    facebook = Pyfb(FACEBOOK_APP_ID)

    token = 'CAACEdEose0cBAK2js6ZALAE3QltVi6krtLJ3yDDeYgVUp0pr8dKTyc26eGlamH9IYFMAhZC6AXvsncs86kqpa3JKRz1yLMXWhFRX7BZASl1XSYMCfrUJ3HyI3pcocMmCeMlvXIFxEIZCKafbahVNkHOoPZAZCwanw2LLbANkRsm7z7Nopxl7duyBmhZCeqcrBUZD'
    facebook.set_access_token(token)

    #Gets info about myself
    me = facebook.get_myself()

    print "Name: %s" % me.name

    photos = facebook.get_photos()

    print me.id

    albums = facebook._client.get_list(me.id, 'albums')

    count = 0
    album_photos = 0
    album_name = ''
    for i in albums:
        album_photos = facebook.get_photos(i.id)
        album_name = i.name
        for j in album_photos:
            if count < 10:
                print j.picture
            else:
                break
        break
    #print albums.



    return render_template('photography.html', photos=photos, album_photos=album_photos, album_name=album_name)

#@app.route('/about')
#def about():
#  return render_template('about.html')
#

 
if __name__ == '__main__':
  app.run(debug=True)