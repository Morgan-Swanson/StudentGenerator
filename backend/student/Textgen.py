
#normie
import string
import random

name_intro_normie = ["My name is "," Welcmome to my bio, my name is ","Hope this helps you get to know me, my name is ",
                     "This bio belongs to "]

name_intro_normie_2 = ["If I had to decribe myself in one word id say im ","one word is not a lot, but id say Im ", "Me in just one word is ",
                       "I'd describe myself as "]

traits_normie = ["funny.","brave.","confident.","loyal.","kind.","clever.","outgoing.","encouraging.","optimistic.","reliable.","daring.","empathetic.",
                 "friendly.","hardworking.","painstaking.","principled."]

interest_normie = [" With my free time I enjoy "," I try to keep myself extra busy with "," The things I like to do for fun are ",
                   " some of my hobbies are "," When I'm not busy with homework I enjoy "]

Clubs_normie = ["On campus im involved with ","I try to explore my interest with ", "A lot of my time goes to ", "I'm a proud member of ",
                "I've met a lot of my freinfds at ","Many of my favorite experiences have been with "]

Clubs_normie2 = ["Being a active school student ", "Being involved on campus ", "All my participation ",
                 "Trying to participate in College life "]
Clubs_normie3 = ["made me lots of freinds.", "gave great experiences.", "taught me new skills.", "gave me new passions.", " filled my life with joy."
                 "taught me about myself."]

specialty = [" After some consideration I think id like to focus on ", " My experinces so far lead me to belive id like to learn ",
             " Ive become increasingly more interested in", " I really feel like id enjoy "]

#stoner
name_intro_stoner = [" What's up my name is ",[ "I made this bio last min, but my name is"]]



def getbio(student):
    # ["normie", "stoner", "brogrammer", "tryhard", "nerd", "alternative"]
    if student.personality != 'normie':
        s1 = random.choice(name_intro_normie) + student.name + ". "
        s2 = random.choice(name_intro_normie_2) + random.choice(traits_normie)
        s3 = random.choice(interest_normie)
        for i, a in enumerate(student.activities):
            if i == len(student.activities) - 1:
                if len(student.activities) == 1:
                    s3 = random.choice(interest_normie) + a + '. '
                else:
                    s3 = s3 + 'and ' + a + '. '
            else:
                s3 = s3 + a + ', '
        s4 = random.choice(Clubs_normie)
        for i, a in enumerate(student.clubs):
            if i == len(student.clubs) - 1:
                if len(student.clubs) == 1:
                    s4 = random.choice(Clubs_normie) + a + ". "
                else:
                    s4 = s4 + 'and ' + a + '. '
            else:
                s4 = s4 + a + ', '
        s5 = random.choice(Clubs_normie2) + random.choice(Clubs_normie3)
        s6 = random.choice(specialty)
        finalsentence = s1 + s2 + s3 + s4 + s5 + s6
        return finalsentence

    # if student.personality == "stoner":

    # if student.personality == "brogrammer":

    # if student.personality == "tryhard":

    # if student.personality == "nerd":

    # if student.personality == "alternative":

    else:
        s1 = (student.name +
              " is a " +
              string.capwords(student.race) + " " +
              student.gender +
              " from " + string.capwords(student.hometown) + ". ")
        s2 = (("He " if student.gender is "male" else "She ") +
              "went to " + student.highschool + ". ")
        s3 = ("He likes " if student.gender is "male" else "She likes ")
        for i, a in enumerate(student.activities):
            if i == len(student.activities) - 1:
                if len(student.activities) == 1:
                    s3 = a + '. '
                else:
                    s3 = s3 + 'and ' + a + '. '
            else:
                s3 = s3 + a + ', '
        if len(student.clubs) == 0:
            s5 = ""
        else:
            s5 = ("He is a part of " if student.gender is "male" else "She is a part of ")
            for i, a in enumerate(student.clubs):
                if i == len(student.clubs) - 1:
                    if len(student.clubs) == 1:
                        s5 = 'member of ' + a + ". "
                    else:
                        s5 = s5 + 'and ' + a + '. '
                else:
                    s5 = s5 + a + ', '

        s4 = (" Contact them at " +
              student.phone + " or " +
              student.email)

        finalsentecne = s1 + s2 + s3 + s5 + s4
        return finalsentecne
