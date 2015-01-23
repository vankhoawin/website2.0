from flask import render_template, request
from pyfb import Pyfb
from forms import ContactForm
from app import app

@app.route('/')
def cover():
    return render_template('cover.html')

@app.route('/photography')
def photography():

    album_names = ["murphy's ranch", 'yosemite', 'la jolla', 'london + scotland']


    return render_template('photography.html', album_names=album_names)


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


#@app.route('/test')
#def test():
#    return render_template('layouttest.html')

 
#if __name__ == '__main__':
#  app.run(debug=True)