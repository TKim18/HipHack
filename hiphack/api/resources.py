import json
from flask import request, abort
from flask.ext import restful
from flask.ext.restful import reqparse
from hiphack.api import api

#Inspirational Quotes: Up to page 7 on http://www.trans4mind.com/quotes/Words_of_Wisdom.pdf
#Python List:
import random
#quotes = list(("Let others lead small lives, but not you. Let others argue over small things, but not you. Let others cry over small hurts, but not you. Let others leave their future insomeone else's hands, but not you.", "Jim Rohn"))
quotes_raw = """
"Trust yourself, then you will know how to live." -Johann Wolfgang van Goethe
"You can never cross the ocean unless you have the courage to lose sight of the shore." -Christopher Columbus
"When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one that has opened for us." -Helen Keller
"Always do right. This will gratify some people and astonish the rest." -Mark Twain
"It is our choices that show what we truly are, far more than our abilities." -J.K.Rowling
"I'm not afraid... I was BORN for this!" -Joan of Arc
"Whatever you are willing to put up with is exactly what you will have." -Anonymous
"We are what we imagine. Our very existence consists in our imagination of ourselves. The greatest tragedy that can befall us is to go unimagined." -N. Scott Momaday
"There is a fire inside. Sit down beside it. Watch the flames, the ancient, flickering dance of yourself." -John MacEnulty
"Destiny is not a matter of chance, it is a matter of choice. It is not a thing to be waited for, it is a thing to be achieved." -William Jennings Bryan
"I have always known that at last I would take this road, but yesterday I did not know that it would be today." -Japanese Haiku
"There is no chance, no destiny, no fate that can circumvent or hinder or control the firm resolve of a determined soul." -Ella Wheeler Wilcox
"Life is not discovery of fate; it is continuous creation of future, through choices of thoughts, feelings and actions in the present." -Sanjay Sahay
"You were born an original. Don't die a copy." -John Mason
"Is life not a hundred times too short for us to stifle ourselves?" -Friedrich Nietzsche
"There is only one real failure in life that is possible, and that is not to be true to the best one knows." -John Farrar
"The pen that writes your life story must be held in your own hand." -Irene C. Kassorla
"Every choice before you represents the universe inviting you to remember who you are and what you want." -Alan Cohen
"Men weary as much of not doing the things they want to do as of doing the things they do not want to do." -Eric Hoffer
"Out of clutter, find simplicity. From discord, find harmony. In the middle of difficulty lies opportunity." -Albert Einstein
"Nothing truly valuable arises from ambition or from a mere sense of duty; it stems rather from love and devotion towards men and towards objective things." -Albert Einstein
"To serve is beautiful, but only if it is done with joy and a whole heart." -Pearl S. Buck
"How do we keep our inner fire alive? Two things, at minimum, are needed: an ability to appreciate the positives in our life - and a commitment to action." -Nathaniel Branden
"Let him who would enjoy a good future waste none of his present." -Roger Babson
"The path to our destination is not always a straight one. We go down the wrong road, we get lost, we turn back. Maybe it doesn't matter which road we embark on. Maybe what matters is that we embark." -Barbara Hall
"It takes great courage to faithfully follow what we know to be true." -Sara E. Anderson
"Our background and circumstances may have influenced who we are, but we are responsible for who we become." -Barbara Geraci
"Great thoughts speak only to the thoughtful mind, but great actions speak to all Mankind." -Emily P. Bissell
"There is a criterion by which you can judge whether the thoughts you are thinking and the things you are doing are right for you. The criterion is: Have they brought you inner peace?" -The Peace Pilgrim
"There is more in us than we know. If we can be made to see it, perhaps, for the rest of our lives, we will be unwilling to settle for less." -Kurt Hahn
"From long familiarity, we know what honor is. It is what enables the individual to do right in the face of complacency and cowardice. It is what enables the soldier to die alone, the political prisoner to resist, the singer to sing her song, hardly appreciated, on a side street." -Mark Helprin
"We all live under the same sky, but we don't all have the same horizon." -Konrad Adenauer
"If it doesn't feel right, don't do it. That is the lesson, and that lesson alone will save you a lot of grief." -Oprah Winfrey
"The time is always right to do what is right." -Martin Luther King, Jr.
"Time is the coin of your life. It is the only coin you have, and only you can determine how it will be spent. Be careful lest you let other people spend it for you." -Carl Sandburg
"The goal of childhood is to become an individual; the goal of adulthood is to give that individuality away. The task of childhood is to separate; the task of adulthood is to connect." -James W. Jones
"The best career advice to give the young is, find out what you like doing best and get someone else to pay you for doing it." -Katherine Whilehaen
"The gem cannot be polished without friction nor man without trials." -Confucius
"Hands that serve are holier than lips that pray." -Sai Baba
"To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment." -Ralph Waldo Emerson
"You will recognize your own path when you come upon it, because you will suddenly have all the energy and imagination you will ever need." -Jerry Gillies
"Destiny is not a matter of chance, it is a matter of choice. It is not a thing to be waited for, it is a thing to be achieved." -Jeremy Kitson
"The best way to find yourself is to lose yourself in the service of others." -Mohandas K. Gandhi
"The height of your accomplishments will equal the depth of your convictions." -William F. Scolavino
"I think the purpose of life is to be useful, to be responsible, to be honorable, to be compassionate. It is, after all, to matter: to count, to stand for something, to have made some difference that you lived at all." -Leo C. Rosten
"Toil and risk are the price of glory, but it is a lovely thing to live with courage and die leaving an everlasting fame." -Alexander the Great
"To give real service you must add something which cannot be bought or measured with money, and that is sincerity and integrity." -Donald A. Adams
"Dignity and respect has to do with ... your personal power to make a difference by being true to the best within you and letting that truth shine through your words and actions." -Gail Pursell Elliott
"When you are inspired by some great purpose, some extraordinary project, all your thoughts break their bonds: Your mind transcends limitations, your consciousness expands in every direction, and you find yourself in a new, great, and wonderful world. Dormant forces, faculties and talents become alive, and you discover yourself to be a greater person by far than you ever dreamed yourself to be." -Patanjali
"You will recognize your own path when you come upon it, because you will suddenly have all the energy and imagination you will ever need." -Jerry Gillies
"""

#some_list[::len(some_list)-1]
lines = quotes_raw.split('\n')[1:-1]
#quotes = lines[::len(lines)-1]
elem = random.choice(lines)

class Root(restful.Resource):
    def get(self):
        return {
            'result': 'OK'
        }

class HipChatInspiration(restful.Resource):
    def post(self):
        args = json.loads(request.data)

        print(args)
        quote = args['item']['message']['message'].replace('/inspire ', '')

        print(quote)

        message = "Something went wrong. Try again later."
        color = "green"
    
        print("formatting message")
        message = elem
        
        return {
            "color": color,
            "message": message,
            "notify": False,
            "message_format": "text"
        }

api.add_resource(Root, '/')
#api.add_resource(Inspiration, '/inspiration')
api.add_resource(HipChatInspiration, '/hipchat/inspiration')
