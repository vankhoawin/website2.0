from flask import Flask, render_template, request
from pyfb import Pyfb

app = Flask(__name__)      
 
@app.route('/')
def cover():
  return render_template('cover.html')

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
  albums = ['Radiohead', 'Tallest Man on Earth', 'Wilco', 'Elliot Smith',
            'Telefon Tel Aviv', 'Kettel', 'Fleet Foxes', 'Grizzly Bear',
            'Kanye West', 'Portishead', 'Purity Ring', 'Tame Impala']

  album_links = ['http://youtu.be/9wCJPm19XYQ', 'http://youtu.be/zG2ccH8jlCA',
                 'http://youtu.be/gm-MpLGfogA', 'http://youtu.be/elWEQzv5sXY',
                 'http://youtu.be/MQ2qEah8Fns', 'http://youtu.be/DS6ZIoV--6I',
                 'http://youtu.be/L5dUsZ4Djd0', 'http://youtu.be/11yTdWvH9f8',
                 'http://youtu.be/CPyKAmKxOAw', 'http://youtu.be/52bAsZI9xm8',
                 'http://youtu.be/PEQKwJred40', 'http://youtu.be/QfQCH-igyT4']



  return render_template('about.html', albums=albums, album_links=album_links)

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/test')
def test():
  return render_template('layouttest.html')

 
if __name__ == '__main__':
  app.run(debug=True)