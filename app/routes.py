from flask import Flask, render_template, request
from pyfb import Pyfb

app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('layout.html')

@app.route('/photography')
def photography():
    FACEBOOK_APP_ID = '511339372322388'
    facebook = Pyfb(FACEBOOK_APP_ID)

    token = 'CAACEdEose0cBADWohTjQVtZBt6MY1lSaJvJ6sHy7tcgmXrdhZCBI17wQTY5X4ZB83lqPB00z84KTzp3Go6lhL7DnnwtJn95ZAsbP9YrC6exMiMujxPCLiV3CeB2c32R9j9LHcz44lkOjEG3HZAFMDFPEnWBQKq0G3irSkj2K1dWtm7npAfbZByxmnXO7cnHm0ZD'
    facebook.set_access_token(token)

    #Gets info about myself
    me = facebook.get_myself()

    #print "Name: %s" % me.name

    photos = facebook.get_photos()

    #print me.id

    albums = facebook._client.get_list(me.id, 'albums')

    album_photos = []
    album_names = []
    for i in albums:
        photos = facebook.get_photos(i.id)
        album_names.append(i.name)

        temp_phot = []
        count = 0
        for j in photos:
            if count < 10:
                temp_phot.append(j.picture)
                #print j.picture
            else:
                break
        album_photos.append(temp_phot)
    #print albums.
    album_photos = zip(album_names,album_photos)


    return render_template('photography.html', photos=photos, album_photos=album_photos, album_names=album_names)


@app.route('/resume')
def resume():
  return render_template('resume.html')


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/test')
def test():
  return render_template('layouttest.html')

 
if __name__ == '__main__':
  app.run(debug=True)