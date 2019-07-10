from manimlib.imports import *

class TextScene(Scene):
    #Adding text on the screen
    def construct(self):
        self.domainandstuff()
    def pointsandstuff(self):
        #tk this needs done, explain what functions does to each point
    def domainandstuff(self):
        eng_objs = ["\\xrightarrow{function}","Domain","Range"]
        math_objs = ["f :","\\mathbb{R}","\\mathbb{R_{}}"]
        english_definition = TexMobject("Domain \\,\\, \\xrightarrow{function} Range",substrings_to_isolate = eng_objs)
        math_definition = TexMobject("f : \\mathbb{R} \\xrightarrow{} \\mathbb{R_{}}",substrings_to_isolate = math_objs) #objects needed for eng -> maths definitions
        
        arrow = math_definition.get_parts_by_tex("\\xrightarrow{}")
        
        #objects needed for turning X and Y into \mathbb{R}s
        R_1 = math_definition.get_parts_by_tex("\\mathbb{R}")
        X = TexMobject("X").next_to(R_1,RIGHT*0)
        R_2 = math_definition.get_parts_by_tex("\\mathbb{R_{}}")
        Y = TexMobject("Y").next_to(R_2,RIGHT*0)   
        
        #the english to maths animation
        self.play(FadeIn(english_definition))
        for eng, math in zip(eng_objs, math_objs):
            for eng_part, math_part in zip(english_definition.get_parts_by_tex(eng),math_definition.get_parts_by_tex(math)):
                self.play(ReplacementTransform(eng_part,math_part)) #this needs to be replacement so the Rs transform works as defined later
                
        #self.play(Transform())    #yes this is spaghetti but goddamn this has taken ages    
        self.play(FadeIn(arrow))
        self.wait()

        #transform Rs to X and Y
        self.play(ReplacementTransform(R_1,X))
        self.play(ReplacementTransform(R_2,Y))
        self.wait()
        #transform Xand Y back to Rs
        self.play(ReplacementTransform(X,TexMobject("\\mathbb{R}").next_to(X,RIGHT*0)))
        self.play(ReplacementTransform(Y,TexMobject("\\mathbb{R_{}}").next_to(Y,RIGHT*0)))
        self.wait()
        #X, firstR = "X",TexMobject("\\mathbb{R}")
        #X = math_definition.get_parts_by_tex(X)
        #self.play(Transform(X,firstR))
