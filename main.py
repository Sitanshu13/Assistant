import pyttsx3
import wikipedia
from googlesearch import search
from GoogleNews import GoogleNews
import webbrowser
import datetime
googlenews = GoogleNews()

googlenews.setlang('en')
googlenews.setperiod('d')
googlenews.setTimeRange('10/06/2020','10/07/2020')
googlenews.setencode('utf-8')

startingMessage = 'Hello, I am your assistant, What can I do for you: '
start = False
Password = '8823'

speaker = pyttsx3.init()
speaker.say('Please enter the password')
speaker.runAndWait()

def password():
    speaker = pyttsx3.init()
    speaker.say('Please type in the password')
    cPassword = input('Enter Password: ')
    speaker.runAndWait()
    if(cPassword == 'Daffny'):
        speaker = pyttsx3.init()
        speaker.say('Access accepted')
        speaker.runAndWait()
    else:
        speaker = pyttsx3.init()
        speaker.say('Access denied')
        speaker.runAndWait()

def searcherWiki(wikiSearch):
    speaker = pyttsx3.init()
    print(' ')
    print(wikipedia.summary(questionWiki))
    speaker.say(wikipedia.summary(questionWiki))
    speaker.runAndWait()

def searcherGoogle(googleSearch):
    speaker = pyttsx3.init()
    print(' ')
    speaker.say('These are the websites that came according to your search')
    print(search(questionGoogle))
    speaker.runAndWait()

def calculator(calclator1):
  if(calclator1 == '1'):
      speaker = pyttsx3.init()
      add1 = int(input('Add this: '))
      add2 = int(input('To this: '))
      ans1 = add1 + add2
      print(ans1)
      speaker.say(ans1)
      speaker.runAndWait()
  elif (calclator1 == '2'):
      speaker = pyttsx3.init()
      sub1 = int(input('Subtract this: '))
      sub2 = int(input('From this: '))
      ans2 = (sub1 - sub2)
      print(ans2)
      speaker.say(ans2)
      speaker.runAndWait()
  elif (calclator1 == '3'):
      speaker = pyttsx3.init()
      mul1 = int(input('Multiply this: '))
      mul2 = int(input('Into this: '))
      ans3 = mul1 * mul2
      print(ans3)
      speaker.say(ans3)
      speaker.runAndWait()
  elif (calclator1 == '4'):
      speaker = pyttsx3.init()
      div1 = int(input('Divide this: '))
      div2 = int(input('By this: '))
      ans4 = div1 / div2
      print(ans4)
      speaker.say(ans4)
      speaker.runAndWait()

speaker = pyttsx3.init()
cPassword = input('Enter Password: ')
speaker.runAndWait()
if(cPassword == Password):
    speaker = pyttsx3.init()
    speaker.say('Access accepted')
    speaker.runAndWait()
    start = True
    if (start == True):
        speaker = pyttsx3.init()
        print(startingMessage)
        speaker.say(startingMessage)
        speaker.runAndWait()
        googleOrWiki = input(
            'Do you want to use Google, Wikipedia, Calculator or Google News or do you want to use the link redirector or know the time: ')
        if (googleOrWiki == 'wiki'):
            questionWiki = input('Wikipedia Search: ')
            searcherWiki(questionWiki)
            speaker = pyttsx3.init()
        elif (googleOrWiki == 'google'):
            questionGoogle = input('Google Search: ')
            searcherGoogle(questionGoogle)
            speaker = pyttsx3.init()
        elif (googleOrWiki == 'gnews'):
            googlenews.search('APPL')
            news = googlenews.gettext()
            print(news)
            speaker = pyttsx3.init()
            speaker.say(news)
            speaker.runAndWait()
        elif (googleOrWiki == 'link'):
            speaker = pyttsx3.init()
            speaker.say('What website would you like to open? ')
            linkSearch = input('Website name: ')
            webbrowser.open('https://' + linkSearch + '.com')
        elif (googleOrWiki == 'calc'):
            speaker = pyttsx3.init()
            print(
                'Which operation would you like to perform, Press 1 to perform addition, 2 to perform subtraction, 3 to perform multiplication and 4 to perform division')
            operation = input('Operation: ')
            calculator(operation)
        elif (googleOrWiki == 'time'):
            speaker = pyttsx3.init()
            ctime = datetime.datetime.now()
            time = str(ctime.strftime("%d-%m-%y %H:%M"))
            print(time)
            speaker.say('The current time is: ' + time)
            speaker.runAndWait()
else:
    speaker = pyttsx3.init()
    speaker.say('Access denied')
    speaker.runAndWait()