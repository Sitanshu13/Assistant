#pip install pyttsx3
#pip install wikipedia
#pip install googlesearch-python
#pip install GoogleNews

#Enter wiki to access wikipedia
#Enter google to access google
#Enter calc to access calculator
#Enter gnews to access Google News
#Enter calc to access calculator
#Enter link to access link_redirector and type in the the name of the website to open the link
#Enter link to access the date and time

import pyttsx3 #importing pyttsx3 
import wikipedia #importing wikipedia
from googlesearch import search #importing search from googlesearch
from GoogleNews import GoogleNews #importing GoogleNews from GoogleNews
import webbrowser #importing webbrowser (built in)
import datetime #importing datetime(built in)
googlenews = GoogleNews() #storing entire GoogleNews module in googlenews variable 

googlenews.setlang('en') #(optional)
googlenews.setperiod('d') #(optional)
googlenews.setTimeRange('10/06/2020','10/07/2020') #(optional)
googlenews.setencode('utf-8') #(optional)

startingMessage = 'Hello, I am your assistant, What can I do for you: ' #Intro message after the password verification
start = False # This variable is used to start the code after the password verification
Password = 'Python' #Remember to change the password

speaker = pyttsx3.init() #speaker initiation
speaker.say('Please enter the password') #speech of the speaker
speaker.runAndWait()

def searcherWiki(wikiSearch):
    speaker = pyttsx3.init() #speaker initiation
    print(' ')
    print(wikipedia.summary(questionWiki))
    speaker.say(wikipedia.summary(questionWiki))#speech of the speaker
    speaker.runAndWait()

def searcherGoogle(googleSearch):
    speaker = pyttsx3.init() #speaker initiation
    print(' ')
    speaker.say('These are the websites that came according to your search')#speech of the speaker
    print(search(questionGoogle))
    speaker.runAndWait()

def calculator(calclator1):
  if(calclator1 == '1'):
      speaker = pyttsx3.init() #speaker initiation
      add1 = int(input('Add this: '))
      add2 = int(input('To this: '))
      ans1 = add1 + add2
      print(ans1)
      speaker.say(ans1)#speech of the speaker
      speaker.runAndWait()
  elif (calclator1 == '2'):
      speaker = pyttsx3.init() #speaker initiation
      sub1 = int(input('Subtract this: '))
      sub2 = int(input('From this: '))
      ans2 = (sub1 - sub2)
      print(ans2)
      speaker.say(ans2)#speech of the speaker
      speaker.runAndWait()
  elif (calclator1 == '3'):
      speaker = pyttsx3.init() #speaker initiation
      mul1 = int(input('Multiply this: '))
      mul2 = int(input('Into this: '))
      ans3 = mul1 * mul2
      print(ans3)
      speaker.say(ans3)#speech of the speaker
      speaker.runAndWait()
  elif (calclator1 == '4'):
      speaker = pyttsx3.init() #speaker initiation
      div1 = int(input('Divide this: '))
      div2 = int(input('By this: '))
      ans4 = div1 / div2
      print(ans4)
      speaker.say(ans4)#speech of the speaker
      speaker.runAndWait()

speaker = pyttsx3.init() #speaker initiation
cPassword = input('Enter Password: ')
speaker.runAndWait()
if(cPassword == Password):
    speaker = pyttsx3.init() #speaker initiation
    speaker.say('Access accepted')#speech of the speaker
    speaker.runAndWait()
    start = True
    if (start == True):
        speaker = pyttsx3.init() #speaker initiation
        print(startingMessage)
        speaker.say(startingMessage)
        speaker.runAndWait()#speech of the speaker
        googleOrWiki = input(
            'Do you want to use Google, Wikipedia, Calculator or Google News or do you want to use the link redirector or know the time: ')
        if (googleOrWiki == 'wiki'):
            questionWiki = input('Wikipedia Search: ')
            searcherWiki(questionWiki)
            speaker = pyttsx3.init() #speaker initiation
        elif (googleOrWiki == 'google'):
            questionGoogle = input('Google Search: ')
            searcherGoogle(questionGoogle)
            speaker = pyttsx3.init() #speaker initiation
        elif (googleOrWiki == 'gnews'):
            googlenews.search('APPL')
            news = googlenews.gettext()
            print(news)
            speaker = pyttsx3.init() #speaker initiation
            speaker.say(news)#speech of the speaker
            speaker.runAndWait()
        elif (googleOrWiki == 'link'):
            speaker = pyttsx3.init() #speaker initiation
            speaker.say('What website would you like to open? ')
            linkSearch = input('Website name: ')
            webbrowser.open('https://' + linkSearch + '.com')
        elif (googleOrWiki == 'calc'):
            speaker = pyttsx3.init() #speaker initiation
            print(
                'Which operation would you like to perform, Press 1 to perform addition, 2 to perform subtraction, 3 to perform multiplication and 4 to perform division')
            operation = input('Operation: ')
            calculator(operation)
        elif (googleOrWiki == 'time'):
            speaker = pyttsx3.init() #speaker initiation
            ctime = datetime.datetime.now()
            time = str(ctime.strftime("%d-%m-%y %H:%M"))
            print(time)
            speaker.say('The current time is: ' + time)#speech of the speaker
            speaker.runAndWait()
else:
    speaker = pyttsx3.init() #speaker initiation
    speaker.say('Access denied')#speech of the speaker
    speaker.runAndWait()
