from flask import Flask, render_template, request
from pyfb import Pyfb
from forms import ContactForm

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
    return render_template('resume.html', form=form)


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

@app.route('/contact', methods=['GET','POST'])
def contact():
    form = ContactForm(request.form)

    if request.method == 'POST' and form.validate():
        print 'yes'
        import smtplib

        to = 'vnguyen94@gmail.com'
        gmail_user = 'mhiwindpower@gmail.com'
        gmail_pass = '1P@ssword1'
        #omg H4x0r now you have access to all the questions about the website oh no pls dont steal ip

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pass)

        header = ('To: %s\n' +
                  'From: %s\n' +
                  'Subject: Website Contact\n\n') % (to, form.email.data)
        message = header + \
                  ('From: %s <%s>\n\n' +
                   'Subject: %s\n\n' +
                   'Message: %s') % (form.name.data, form.email.data, form.subject.data, form.message.data)

        server.sendmail(gmail_user, to, message)
        server.close()

    return render_template('contact.html', form=form)


@app.route('/test')
def test():
    return render_template('layouttest.html')

 
if __name__ == '__main__':
  app.run(debug=True)