import logging, collections
from random import shuffle
from flask import Flask, url_for, render_template, make_response, redirect, request, session, escape
from flask_bootstrap import Bootstrap
from contextlib import closing
app = Flask(__name__)
Bootstrap(app)
app.debug = True

app.config.from_object(__name__)

animals = {'Imaginer': ["You may take a while to talk in class but when you do, you will come off to your professors and fellow students as thoughtful, deep, and reflective. You like to think over all your options and possibilities, and weigh the pros and cons. Sometimes you allow yourself to dream too long, and deadlines start to slip. At that point, it's helpful to get an outside nudge from your teammates or your professor, to bring you back to reality. You tend to space out during long meetings or discussions. You use this time to escape, and think about things that you've been waiting to process. In dealing with other students and professors, you prefer that they use clear and direct language, instead of using buzzy jargon or vague descriptors. In stressful situations, your tendency is to wait it out, to see if things will pass. If the tension doesn't break, sometimes you withdraw and just abandon what you've been working on. Your classmates love you for your easygoing nature, your calmness, even if the face of disaster, and your way of looking at things from several angles. They appreciate the fact that you are slow to judge others, and you tend to think on several levels, not just about the issue at hand, but about humanity at large.", "imaginer.jpg"],
           'Harmonizer': ["In class, you pay a vital role: relationship builder and peace maker. You can relate to all different types of people and you have a knack for being able to communicate a nurturing and accepting way. In turn, you expect your peers and professors to accept you and to and to acknowledge that you matter and you're an important part of the class. You like classroom environments that are sensory rich, and you thrive when collaboration and cooperation are a key part of learning. When things get stressful, you tend to become less assertive and certain about your opinion. You also tend to make mistakes when things get tense and laugh at yourself and be self-deprecating. You also are more likely than your other classmates to accept things that are unacceptable, being hopeful that they will change or become more acceptable to you over time.  Your peers and professors love how warm and understanding you are. They trust you with their deepest feelings and secrets, and know that you will never laugh at an idea or comment of theirs, no matter how simple or obvious it may seem. You have a naturally harmonious spirit, you learn through feeling and experiencing the world, rather than analyzing it from afar.", "harmonizer.gif"],
           'Rebel': ["We need more of you in academia. You think on your feet, and you're spontaneous, creative, and playful. You're not afraid to challenge authority, ask controversial questions, and engage in spirited debate. For you, learning comes from fun, excitement, and real involvement with the people around you. Your peers will respect you (although they may be overwhelmed by your intensity) and your professors will be thankful for your active presence. Discourse never falls flat when you're in the room. As a student, you REALLY don't like being told what to do and how to do it. You're motivated by freedom, and you are energized by setting your own course. You wake up and ask, \"What do I want to learn and do today?\" Then you charge ahead, determined to make it happen. When talking to your classmates, you have one piece of advice for them: Look alive. When under a great deal of stress, you tend to blame others or withdraw your responsibility for the issue at hand. Things in a crisis also seem overly complicated, and your tendency is to get frustrated and bored.  Your classmates and teachers appreciate how you always make them laugh. If there's something absurd to be said, you're saying it. You're also a creative thinker. Where others see problems, you see a game called \"finding a solution.\"", "rebel.gif"],
           'Persister': ["This will serve you well in school. You're dedicated to your work, observant of the requirements and the inner workings of the classroom, and you're conscientious about your responsibilities and others.  You're a natural leader, but you never get tired of others acknowledging your talents, or saying, \"I need your opinion on this,\" or \"I admire you; I could never do that.\" When you are stressed, you tend to get negative, focusing on what's going wrong, instead of what's going right. In these tense situations, your way feels like the only right way and you tend to push your beliefs or ideas on others. Your classmates depend on you for your strong leadership and vision. You've always got an opinion, and you're able to make sound snap decisions based on the information at hand. You have unquestionable morals and ethics and you hold others around you to the same high standard. You are passionate--your favorite baseball team, your political leanings--but you always manage to maintain your professionalism while still respecting your principles, values, and ideals.", "persister.gif"],
           'Thinker': ["As such, you're a natural fit for academic life. You like to plan ahead, organize your work, and pave a clear path for your success. If you're in a group, you're likely to take the lead and assume personal responsibility for the success of your group's project. You tend to ask a lot of questions, and when people propose an idea, you want real data that is logical and supportive. If you get overly stressed, you might go into perfectionist mode. You offer a number of details that aren't necessarily relevant. You also have the tendency to become controlling, getting stressed when you perceive your peers as being too lax about time, order, or output. You function best when chaos is contained, your path is structured, and your reasoning is logical. To feel good in class, you want your professor to acknowledge that you've done a great job and you've put in a lot of work. Your classmates like you because they know they can count on you, and you're always going to be welcoming, personable, and professional.", "thinker.gif"],
           'Promoter': ["You're a born charmer and politician, and a natural fit for academic life. Whatever life throws at you, you handle it. You move, you adapt, and you keep on moving. You're not much for routine, so you'll keep your professor on her feet, requiring her to be resourceful and provide a stimulating and constantly changing environment. When others talk to you, you want the to be direct and firm. You approach difficulties with the mindset, \"What's the problem? Now how do we solve it?\" You are pragmatic in this way, almost to a fault. When things get tense, you get impatient with others and you may even become manipulative to reach your goals--stepping over others, pushing limits, and breaking the rules. Your classmates and professor appreciate you because, well, you compliment them profusely. But you're also extremely resourceful. No matter the size of the problem, you're never down for long. Your energy is contagious. Even when people want to consider you tactless, they can't help but to like you, to look to you for your vision, and to count on you to take risks for the big win.", "promoter.gif"]}

questions = []
responses = []
responses.append(('A space cadet', 'Imaginer'))
responses.append(('A sap', 'Harmonizer'))
responses.append(('An outlaw', 'Rebel'))
responses.append(('A dictator', 'Persister'))
responses.append(('An egghead', 'Thinker'))
responses.append(('A politician', 'Promoter'))

questions.append(['What do your enemies call you?', responses])

responses = []
responses.append(('A cat', 'Imaginer'))
responses.append(('A hen', 'Harmonizer'))
responses.append(('A monkey', 'Rebel'))
responses.append(('A shark', 'Persister'))
responses.append(('An owl', 'Thinker'))
responses.append(('A chameleon', 'Promoter'))

questions.append(['Which is your spirit animal?', responses])

responses = []
responses.append(('Floating', 'Imaginer'))
responses.append(('Emoting', 'Harmonizer'))
responses.append(('Imploding', 'Rebel'))
responses.append(('Gloating', 'Persister'))
responses.append(('Noting', 'Thinker'))
responses.append(('Promoting', 'Promoter'))

questions.append(['Which activity is most appealing to you?', responses])

responses = []
responses.append(('Loss of creativity', 'Imaginer'))
responses.append(('Profound isolation', 'Harmonizer'))
responses.append(('Oppressive domesticity', 'Rebel'))
responses.append(('Unremitting chaos', 'Persister'))
responses.append(('Accidental lobotomy', 'Thinker'))
responses.append(('Loss of social influence', 'Promoter'))

questions.append(['Which is your greatest fear?', responses])

responses = []
responses.append(('"Enchanted"', 'Imaginer'))
responses.append(('"Love Story"', 'Harmonizer'))
responses.append(('"I Knew You Were Trouble"', 'Rebel'))
responses.append(('"Blank Space"', 'Persister'))
responses.append(('"We Are Never Getting Back Together"', 'Thinker'))
responses.append(('"Shake it Off"', 'Promoter'))

questions.append(['Which Taylor Swift song are you?', responses])

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/q/<int:question_id>', methods=['GET','POST'])
def display_question(question_id):
    if request.method == 'POST':
        session['question_' + str(question_id -1)] = request.form['r']
    if question_id > len(questions) - 1:
        return redirect(url_for('archetype'))
    shuffle(questions[question_id][1])
    resp = make_response(render_template('question.html', q=questions[question_id], r=questions[question_id][1], id=question_id))
    return resp

@app.route('/archetype')
def archetype():
    def calculate_animal():
        n = len(questions)
        qnames=map(lambda q: 'question_' + str(q), range(n))
        answers = []
        for q in qnames:
            answers.append(session[q])
        animal=collections.Counter(answers).most_common(1)
        app.logger.info(animal)
        return animal[0][0]
    return render_template('archetype.html', animal=calculate_animal(), animals=animals)


if __name__ == '__main__':
    app.run()

app.secret_key = 'SKLDJF804208sdklzklsjdf'
